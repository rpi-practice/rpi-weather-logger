#!/usr/bin/env python
"""Database connector module"""
# Standard imports
import os
import sqlite3


class DBConnect(object):
    """Database connector"""
    def __init__(self, name):
        self._name = name 

    def __enter__(self):
        db_dir = os.path.dirname(os.path.realpath(__file__))
        self.db = os.path.join(db_dir, self._name)
        self.conn = sqlite3.connect(self.db)
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(exc_value)
            self.conn.rollback()
        self.conn.commit()
        self.conn.close()

