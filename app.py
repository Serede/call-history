#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import bottle
from bottle import route, run, template, static_file

from call_history import update_call_history
from call_history import DB_FILE, OUTGOING_TABLE, INCOMING_TABLE, TIME_COLUMN


bottle.TEMPLATE_PATH.insert(0, 'template')


@route('/')
def call_history():
    update_call_history()
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT * FROM ' + OUTGOING_TABLE + ' ORDER BY ' + TIME_COLUMN)
    outgoing_hdr = list(map(lambda x: x[0].replace('_', ' '), c.description))
    outgoing = c.fetchall()[::-1]
    c.execute('SELECT * FROM ' + INCOMING_TABLE + ' ORDER BY ' + TIME_COLUMN)
    incoming_hdr = list(map(lambda x: x[0].replace('_', ' '), c.description))
    incoming = c.fetchall()[::-1]
    c.close()
    template_dict = {
        'outgoing_hdr': outgoing_hdr,
        'outgoing': outgoing,
        'incoming_hdr': incoming_hdr,
        'incoming': incoming
    }
    output = template('table', **template_dict)
    return output


# Static Routes
@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='template')


run(host='0.0.0.0', port=8008, debug=True, reloader=True)
