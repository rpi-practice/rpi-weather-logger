from query_weather_data import QueryWeatherData as qwd
import sqlite3

class TempLogger(object):
    def __init__(self):
        pass

    def commit_data(self, data):
        db = "weather_data.db"
        table = "web_data"

        conn = sqlite3.connect(db)
        cur = conn.cursor()
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
                     data['cloud'],
                     ))

if __name__=="__main__":
    tl = TempLogger()
    tl.commit_data(qwd().decorated_data())

