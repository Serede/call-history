#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
import requests
import pandas
from bs4 import BeautifulSoup
from sqlalchemy import create_engine, MetaData, Table, Column, String

# Constants

_DBG_ = False

IP = '192.168.1.1'
LOGIN_URL = 'http://{ip}/login-login.cgi'.format(**{'ip': IP})
CHO_URL = 'http://{ip}/voip/CallHistoryOutgoing.html'.format(**{'ip': IP})
CHI_URL = 'http://{ip}/voip/CallHistoryIncoming.html'.format(**{'ip': IP})
USER = '1234'
PASSWD_FILE = '.passwd'
DB_FILE = 'call_history.db'
TABLE_INDEX = -1
TABLE_TIME_COLNAME = 'time'
TABLE_OUT_NAME = 'outgoing'
TABLE_IN_NAME = 'incoming'

# Fetch tables

with open(PASSWD_FILE) as file:
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


def read_table(session, url):
    response = session.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    if _DBG_:
        print(soup.prettify())
    table = soup.find_all('table')[TABLE_INDEX]
    df = pandas.read_html(str(table), header=0, index_col=0)[0]
    df.columns = df.columns.str.replace(' ', '_')
    return df


cho = read_table(session, CHO_URL)
chi = read_table(session, CHI_URL)

if _DBG_:
    print(cho)
    print(chi)

# Database

engine = create_engine('sqlite:///' + DB_FILE, echo=_DBG_)

metadata = MetaData()

outgoing = Table(TABLE_OUT_NAME, metadata,
                 *[Column(name, String, nullable=False) for name in list(cho)])
incoming = Table(TABLE_IN_NAME, metadata,
                 *[Column(name, String, nullable=False) for name in list(chi)])

metadata.create_all(engine)

cho.apply(lambda x: engine.execute(
    outgoing.insert().prefix_with('OR IGNORE').values(x)), axis=1)
chi.apply(lambda x: engine.execute(
    incoming.insert().prefix_with('OR IGNORE').values(x)), axis=1)
