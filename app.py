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
    outgoing = c.fetchall()
    c.execute("SELECT * FROM incoming")
    incoming = c.fetchall()
    c.close()
    output = template('table', outgoing=outgoing, incoming=incoming)
    return output


# Static Routes
@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='template')


run(host='0.0.0.0', port=8008, debug=True, reloader=True)
