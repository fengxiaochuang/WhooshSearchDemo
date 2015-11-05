#!python
# -*- coding: utf-8 -*-
import MySQLdb.cursors


db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'passwd': 'root',
    'db': 'spider',
    'charset': "utf8",
    'cursorclass': MySQLdb.cursors.DictCursor
}
