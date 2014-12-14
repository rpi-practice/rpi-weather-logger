from query_weather_data import QueryWeatherData as qwd
from db_connect import DBConnect
import os

class WebDataLogger(object):
    def __init__(self):
        #Initialize db if not found.
        self.table = "web_data"
        self.db = "weather_data.db"
        with DBConnect(self.db) as cur:
            cur.execute("""CREATE TABLE IF NOT EXISTS {0} 
                        (timestamp NUMERIC,
                         loc_id NUMERIC,
                         temp NUMERIC,
                         humidity NUMERIC,
                         pres NUMERIC,
                         wind NUMERIC,
                         clouds NUMERIC)""".format(self.table))

    def commit_data(self, data):
        with DBConnect(self.db) as cur: 
            cur.execute("""INSERT INTO {0}(timestamp,
                     loc_id, temp, humidity,
                     pres, wind, clouds) VALUES 
                     ( ?, ?, ?, ?, ?, ?, ?)""".format(self.table), (
                     data['timestamp'], data['loc_id'],
                     data['temp'], data['humidity'],
                     data['pres'], data['wind'],
                     data['clouds'])
                     )

if __name__=="__main__":
    tl = WebDataLogger()
    tl.commit_data(qwd().decorated_data())

