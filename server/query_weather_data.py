#!/usr/bin/env python
"""Module to query weather data"""

# Standar imports
import httplib
import json

class QueryWeatherData(object):
  def __init__(self):
    self.url = "api.openweathermap.org"
    self.path = "/data/2.5/weather"
    #self.query = "?q=pune,in&units=metric"
    self.query = "?q=khadki,in&units=metric"
    self.appid = "&appid=2b198757fd4f56ce9b1e8677b4cbe120"

  
  def make_request(self):
    msg = None
  
    try:
      conn = httplib.HTTPConnection(self.url)
      conn.request("GET", self.path+self.query+self.appid)
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
    if data:
      json_data = json.loads(data)
      
      #timestamp, loc_id, temp, humidity, pres, wind, cloud
      data = {'timestamp':json_data['dt'],
        'loc_id':json_data['id'],
        'temp':json_data['main']['temp'],
        'humidity':json_data['main']['humidity'],
        'pres':json_data['main']['pressure'],
        'wind':json_data['wind']['speed'],
        'clouds':json_data['clouds']['all'],
      }
    
    return data


if __name__ == "__main__":
  q = QueryWeatherData()
  #print(q.make_request())
  print(q.decorated_data())

