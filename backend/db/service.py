import sqlite3

from models import User


class DB:
    # Must be checked manually
    msg_logger: list[tuple]

    def __init__(self, db="rumpulinks.db"):
        # Init DB
        self.db_name = db

    def open_conn(self):
        self.connection = sqlite3.connect(self.db_name)

        # Creating dict like accessible rows for myself
        self.connection.row_factory = sqlite3.Row

        # Enable foreign keys for this connection:
        with self.connection:
            self.connection.execute("PRAGMA foreign_keys = ON;")
        return self

    def create_new_user(self, user: User):
        if self.is_redundant("Users", "username", user.username):
            raise ValueError("This already exists")
        keys = tuple(dict(user).keys())
        values = tuple(dict(user).values())

        # Logging
        print(f"Columns {keys} are being saved respectively as {values}")

        # Create Query Strings
        cols = ", ".join(keys)
        placeholder = ", ".join(["?"] * len(keys))

        with self.connection:
            cursor = self.connection.cursor()
            query = f"INSERT INTO Users ({cols}) Value({placeholder})"
            cursor.execute(query, values)

        return self

    def close_conn(self):
        if self.connection:
            self.connection.close()
        return self
    
    def __enter__(self):
        return self.open_conn()

    def __exit__(self, *args):
        self.close_conn()

    # --------------------- Helpers ---------------------
    def is_redundant(self, table: str, col: str, to_compare):
        with self.connection:
            query = f"SELECT 1 FROM {table} WHERE {col} = ? LIMIT 1"
            cursor = self.connection.cursor()
            cursor.execute(query, (to_compare,))
            return cursor.fetchone() is not None
