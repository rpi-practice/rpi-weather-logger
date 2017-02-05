#!/usr/bin/env python
"""Core temperature logger module"""

# Standard imports
import os
import time
import subprocess

# Local imports
from db_connect import DBConnect


class CoreTempLogger(object):
    """Logs core temperature to SQLite DB"""
    def __init__(self):
        self._table = "ltemps"
        self._db = "weather_data.db"
        with DBConnect(self._db) as cur:
            cur.execute("CREATE TABLE IF NOT EXISTS {0} (timestamp NUMERIC, core_temp NUMERIC)".format(self._table))

    def log_temp(self):
        """Logs core temperature to sqlite DB."""
        core_temp = self._get_core_temp()
        timestamp = int(time.time())

        with DBConnect(self._db) as cur:
            #execute query
            cur.execute("INSERT INTO {0} VALUES (?, ?)".format(self.table),(timestamp, core_temp))

    def _get_core_temp(self):
        """Get CPU temperature"""
        core_temp = subprocess.check_output(["/opt/vc/bin/vcgencmd",
                                            "measure_temp"]).strip()
        #core_temp value is in format temp=XX.X'C.
        #Fixing core_temp to required format.
        core_temp = core_temp.split("=")[1].split("\'")[0]
        return float(core_temp)

if __name__=="__main__":
    #print(CoreTempLogger().get_core_temp())
    CoreTempLogger().log_temp()

