import sqlite3


class DB:
    def __init__(self, db="rumpulinks.db"):
        # Init DB
        self.db_name = db
        self.connection = sqlite3.connect(self.db_name)

        # Enable foreign keys for this connection:
        self.connection.execute("PRAGMA foreign_keys = ON;")

    def exists(value):
        return 
