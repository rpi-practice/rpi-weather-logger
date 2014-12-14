import os
import sqlite3
import subprocess
import time

class CoreTempLogger:
    def __init__(self):
        db_dir = os.path.dirname(os.path.realpath(__file__))
        self.db = os.path.join(db_dir, "weather_data.db")
        self.table = "ltemps"
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()

        try:
            cur.execute("CREATE TABLE {0} (timestamp NUMERIC, core_temp NUMERIC))".format(self.table))
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)
        finally:
            conn.close()


    def log_temp(self):
        """Logs core temperature to sqlite DB."""
        core_temp = self.get_core_temp()
        timestamp = int(time.time())

        #open db connection
        db_dir = os.path.dirname(os.path.realpath(__file__))
        conn = sqlite3.connect(self.db)
        #get cursor
        cur = conn.cursor()
        try:
            #execute query
            cur.execute("INSERT INTO {0} VALUES ({1}, {2})".format(self.table, timestamp, core_temp))
            #commit db
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)
        finally:
            #close connection
            conn.close()


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
