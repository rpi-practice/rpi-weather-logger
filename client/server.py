import cherrypy
import json
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'server'))
from get_data import GetData

class Server(object):
    #@cherrypy.expose
    #def index(self):
        #return open(os.path.join(os.path.dirname(__file__), 'html', 'chart.html'))

    @cherrypy.expose
    def temp(self):
        return json.dumps(GetData().temp)

sconf = os.path.join(os.path.dirname(__file__), 'server.conf')

if __name__ == '__main__':
       cherrypy.quickstart(Server(), config=sconf)

