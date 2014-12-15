from db_connect import DBConnect

class GetData:
    def __init__(self):
        self.db = "weather_data.db"
        self.table = "web_data"

    @property
    def temp(self):
        with DBConnect(self.db) as cur:
            cur.execute("SELECT timestamp, temp from {0}".format(self.table))
            return cur.fetchall()

    @property
    def humidity(self):
        with DBConnect(self.db) as cur:
            cur.execute("SELECT timestamp, humidity from {0}".format(self.table))
            return cur.fetchall()

    @property
    def pres(self):
        with DBConnect(self.db) as cur:
            cur.execute("SELECT timestamp, pres from {0}".format(self.table))
            return cur.fetchall()

    @property
    def wind(self):
        with DBConnect(self.db) as cur:
            cur.execute("SELECT timestamp, wind from {0}".format(self.table))
            return cur.fetchall()

    @property
    def clouds(self):
        with DBConnect(self.db) as cur:
            cur.execute("SELECT timestamp, clouds from {0}".format(self.table))
            return cur.fetchall()

if __name__=="__main__":
    print(GetData().temp)

