from query_weather_data import QueryWeatherData as qwd
import sqlite3
import os

class WebDataLogger(object):
    def __init__(self):
        pass

    def commit_data(self, data):
        db_dir = os.path.dirname(os.path.realpath(__file__))
        db = os.path.join(db_dir, "weather_data.db")
        table = "web_data"
        print(data)

        conn = sqlite3.connect(db)
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
                     table,
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

