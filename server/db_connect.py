import os
import sqlite3

class DBConnect:
    def __init__(self, name):
        self.name = name 

    def __enter__(self):
        db_dir = os.path.dirname(os.path.realpath(__file__))
        self.db = os.path.join(db_dir, self.name)
        self.conn = sqlite3.connect(self.db)
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(exc_value)
            self.conn.rollback()
        self.conn.commit()
        self.conn.close()

