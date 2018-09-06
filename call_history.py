#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
import requests
import pandas
from bs4 import BeautifulSoup
from sqlalchemy import create_engine, MetaData, Table, Column, String, UniqueConstraint

# Constants

_DBG_ = False

IP = '192.168.1.1'
LOGIN_URL = 'http://{ip}/login-login.cgi'.format(**{'ip': IP})
OUTGOING_URL = 'http://{ip}/voip/CallHistoryOutgoing.html'.format(**{'ip': IP})
INCOMING_URL = 'http://{ip}/voip/CallHistoryIncoming.html'.format(**{'ip': IP})
USER = '1234'
PW_FILE = '.passwd'
DB_FILE = 'call_history.db'
TABLE_INDEX = -1
OUTGOING_TABLE = 'outgoing'
INCOMING_TABLE = 'incoming'
TIME_COLUMN = 'time'


def _read_table(session, url):
    response = session.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    if _DBG_:
        print(soup.prettify())
    table = soup.find_all('table')[TABLE_INDEX]
    df = pandas.read_html(str(table), header=0, index_col=0)[0]
    df.columns = df.columns.str.replace(' ', '_')
    df[TIME_COLUMN] = pandas.to_datetime(df[TIME_COLUMN]).astype(str)
    return df


def _get_tables():
    with open(PW_FILE) as file:
        sessionKey = base64.b64encode(
            '{user}:{pass}'.format(**{
                'user': USER,
                'pass': file.readline().rstrip('\n')
            }).encode()
        )

    data = {
        'sessionKey': sessionKey,
        'pass': ''
    }

    session = requests.Session()

    login_response = session.post(LOGIN_URL, data=data)

    if _DBG_:
        print(login_response.headers)
        print(session.cookies.get_dict())

    och = _read_table(session, OUTGOING_URL)
    ich = _read_table(session, INCOMING_URL)

    if _DBG_:
        print(och)
        print(ich)

    return (och, ich)


def _update_database(och, ich):
    engine = create_engine('sqlite:///' + DB_FILE, echo=_DBG_)

    metadata = MetaData()

    outgoing = Table(OUTGOING_TABLE, metadata,
                     *[Column(name, String, nullable=False)
                       for name in list(och)],
                     UniqueConstraint(*list(och), name='uix'))
    incoming = Table(INCOMING_TABLE, metadata,
                     *[Column(name, String, nullable=False)
                       for name in list(ich)],
                     UniqueConstraint(*list(och), name='uix'))

    metadata.create_all(engine)

    och.apply(lambda x: engine.execute(
        outgoing.insert().prefix_with('OR IGNORE').values(x)), axis=1)
    ich.apply(lambda x: engine.execute(
        incoming.insert().prefix_with('OR IGNORE').values(x)), axis=1)


def update_call_history():
    tables = _get_tables()
    _update_database(*tables)
