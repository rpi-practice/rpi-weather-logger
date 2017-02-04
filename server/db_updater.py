from db_connect import DBConnect

db = "weather_data.db"
table = "web_data"

with DBConnect(db) as cur:
	cur.execute("SELECT timestamp from {0}".format(table))
	l = cur.fetchall()
	for x in l:
		if x[0]:
			print("Changing {0}".format(x[0]))
			cur.execute("UPDATE {0} SET timestamp = {1} WHERE timestamp = {2}".format(table, x[0]/1000, x[0]))

