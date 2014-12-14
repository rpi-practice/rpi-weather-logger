import sqlite3

class DBConnect:
    def __enter__(self, name):
        self.db_dir = os.path.dirname(os.path.realpath(__file__))
        self.db = os.path.join(db_dir, name)
        self.conn = sqlite3.connect(self.db)
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type not None:
            conn.rollback()
        self.conn.close()

