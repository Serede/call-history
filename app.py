#!/usr/bin/env python3

import sqlite3
import sys

import bottle
from bottle import route, run, static_file, template

from call_history import (
    DB_FILE,
    INCOMING_TABLE,
    OUTGOING_TABLE,
    TIME_COLUMN,
    update_call_history,
)

bottle.TEMPLATE_PATH.insert(0, "template")


@route("/")
def call_history():
    update_call_history()
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM " + OUTGOING_TABLE + " ORDER BY " + TIME_COLUMN)
    outgoing_hdr = list(map(lambda x: x[0].replace("_", " "), c.description))
    outgoing = c.fetchall()[::-1]
    c.execute("SELECT * FROM " + INCOMING_TABLE + " ORDER BY " + TIME_COLUMN)
    incoming_hdr = list(map(lambda x: x[0].replace("_", " "), c.description))
    incoming = c.fetchall()[::-1]
    c.close()
    template_dict = {
        "outgoing_hdr": outgoing_hdr,
        "outgoing": outgoing,
        "incoming_hdr": incoming_hdr,
        "incoming": incoming,
    }
    output = template("table", **template_dict)
    return output


# Static Routes
@route("/<filepath:path>")
def server_static(filepath):
    return static_file(filepath, root="template")


def main() -> int:
    run(host="0.0.0.0", port=8008, debug=True, reloader=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
