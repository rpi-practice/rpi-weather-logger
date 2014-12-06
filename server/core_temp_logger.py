import sqlite3
import subprocess
import time

class CoreTempLogger:
    def log_temp(self):
        """Logs core temperature to sqlite DB."""
        core_temp = self.get_core_temp()
        timestamp = int(time.time())

        #open db connection
        conn = sqlite3.connect("weather_data.db")
        #get cursor
        cur = conn.cursor()
        try:
            #execute query
            cur.execute("INSERT INTO ltemps VALUES (timestamp, core_temp)")
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
