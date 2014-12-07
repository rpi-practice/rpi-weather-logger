import httplib
import json

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

    def decorated_data(self):
        data = self.make_request()
        json_data = json.loads(data)
        #timestamp, loc_id, temp, humid, pres, wind, cloud
        return {'timestamp':json_data['dt'],
                'loc_id':json_data['id'],
                'temp':json_data['main']['temp'],
                'humidity':json_data['main']['humidity'],
                'pres':json_data['main']['pres'],
                'wind':json_data['main']['wind'],
                'cloud':json_data['main']['cloud'],
               }

if __name__ == "__main__":
    q = QueryWeatherData()
    print(q.make_request())
    #q.decorated_data()

