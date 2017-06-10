#!/usr/bin/env python
"""Module containing class to get data"""

# Local imports
from db_connect import DBConnect


class GetData(object):
    """Get data from database"""
    def __init__(self):
        self._db = "weather_data.db"
        self._table = "web_data"

    @property
    def temp(self):
        with DBConnect(self._db) as cur:
            cur.execute("SELECT timestamp, temp from {0}".format(self._table))
            return cur.fetchall()

    @property
    def humidity(self):
        with DBConnect(self._db) as cur:
            cur.execute("SELECT timestamp, humidity from {0}".format(self._table))
            return cur.fetchall()

    @property
    def pres(self):
        with DBConnect(self._db) as cur:
            cur.execute("SELECT timestamp, pres from {0}".format(self._table))
            return cur.fetchall()

    @property
    def wind(self):
        with DBConnect(self._db) as cur:
            cur.execute("SELECT timestamp, wind from {0}".format(self._table))
            return cur.fetchall()

    @property
    def clouds(self):
        with DBConnect(self._db) as cur:
            cur.execute("SELECT timestamp, clouds from {0}".format(self._table))
            return cur.fetchall()

if __name__=="__main__":
    print(GetData().temp)

