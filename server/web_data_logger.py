from query_weather_data import QueryWeatherData as qwd
import sqlite3
import os

class WebDataLogger(object):
    def __init__(self):
        #Initialize db if not found.
        self.db_dir = os.path.dirname(os.path.realpath(__file__))
        self.db = os.path.join(db_dir, "weather_data.db")
        self.table = "web_data"

        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        try:
            cur.execute("""CREATE TABLE {0} 
                        (timestamp NUMERIC,
                         loc_id NUMERIC,
                         temp NUMERIC,
                         humidity NUMERIC,
                         pres NUMERIC,
                         wind NUMERIC,
                         clouds NUMERIC)""".format(self.table))
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)
        finally:
            conn.close()



    def commit_data(self, data):
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        try:
            cur.execute("""INSERT INTO {0} VALUES 
                     (
                     {1},
                     {2},
                     {3},
                     {4},
                     {5},
                     {6},
                     {7})""".format(
                     self.table,
                     data['timestamp'],
                     data['loc_id'],
                     data['temp'],
                     data['humidity'],
                     data['pres'],
                     data['wind'],
                     data['clouds']
                     ))
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)
        finally:
            conn.close()

if __name__=="__main__":
    tl = WebDataLogger()
    tl.commit_data(qwd().decorated_data())

