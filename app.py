#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import bottle
from bottle import route, run, template, static_file

bottle.TEMPLATE_PATH.insert(0, 'template')


@route('/')
def call_history():
    conn = sqlite3.connect('call_history.db')
    c = conn.cursor()
    c.execute("SELECT * FROM outgoing")
    outgoing_hdr = list(map(lambda x: x[0], c.description))
    outgoing = c.fetchall()
    c.execute("SELECT * FROM incoming")
    incoming_hdr = list(map(lambda x: x[0], c.description))
    incoming = c.fetchall()
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
