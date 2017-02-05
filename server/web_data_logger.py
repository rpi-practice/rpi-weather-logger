#!/usr/bin/env python
"""Log web data"""

# Standard imports
import os
# Local imports
from query_weather_data import QueryWeatherData as qwd
from db_connect import DBConnect


class WebDataLogger(object):
    def __init__(self):
        #Initialize db if not found.
        self._table = "web_data"
        self._db = "weather_data.db"
        with DBConnect(self._db) as cur:
            cur.execute("""CREATE TABLE IF NOT EXISTS {0} 
                        (timestamp NUMERIC,
                         loc_id NUMERIC,
                         temp NUMERIC,
                         humidity NUMERIC,
                         pres NUMERIC,
                         wind NUMERIC,
                         clouds NUMERIC)""".format(self._table))

    def commit_data(self, data):
        with DBConnect(self._db) as cur: 
            cur.execute("""INSERT INTO {0}(timestamp,
                     loc_id, temp, humidity,
                     pres, wind, clouds) VALUES 
                     ( ?, ?, ?, ?, ?, ?, ?)""".format(self._table), (
                     data['timestamp']*1000, data['loc_id'],
                     data['temp'], data['humidity'],
                     data['pres'], data['wind'],
                     data['clouds'])
                     )

if __name__=="__main__":
    tl = WebDataLogger()
    tl.commit_data(qwd().decorated_data())

