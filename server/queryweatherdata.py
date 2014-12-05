import httplib

class QueryWeatherData:
    def __init__(self):
        self.url = "api.openweathermap.org"
        self.path = "/data/2.5/weather"
        self.query = "?q=pune,in"#&units=metric"

    def make_request(self):
        try:
            conn = httplib.HTTPConnection(self.url)
            conn.request("GET", self.path+self.query)
            resp = conn.getresponse()

            if resp.status == 200:
                msg = resp.read()
        except Exception as e:
            print(e)
        finally:
            conn.close()
        return msg

if __name__ == "__main__":
    q = QueryWeatherData()
    msg = q.make_request()
    print(msg)

