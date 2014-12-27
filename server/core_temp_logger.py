import os
from db_connect import DBConnect
import subprocess
import time

class CoreTempLogger:
    def __init__(self):
        self.table = "ltemps"
        self.db = "weather_data.db"
        with DBConnect(self.db) as cur:
            cur.execute("CREATE TABLE IF NOT EXISTS {0} (timestamp NUMERIC, core_temp NUMERIC)".format(self.table))

    def log_temp(self):
        """Logs core temperature to sqlite DB."""
        core_temp = self.get_core_temp()
        timestamp = int(time.time())

        with DBConnect(self.db) as cur:
            #execute query
            cur.execute("INSERT INTO {0} VALUES (?, ?)".format(self.table),(timestamp, core_temp))

    def get_core_temp(self):
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

