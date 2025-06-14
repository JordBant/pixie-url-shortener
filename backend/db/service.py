import os
import sqlite3

from models import User


class DB:
    def __init__(self, db="rumpulinks.db"):
        # Init DB
        self.db_name = db
        self._init_schemas().close_conn()

    def _init_schemas(self, schemas: tuple[str, ...] = ("tables/init.sql",)):
        path = os.path
        cursor = self.open_conn().connection.cursor()
        for file in schemas:
            script_path = path.join(path.dirname(__file__), file)
            with open(script_path, "r") as f:
                cursor.executescript(f.read())
        return self

    def _is_connected(self):
        if hasattr(self, "connection"):
            try:
                self.connection.execute("SELECT 1")
                return True
            except Exception:
                return False
        else:
            return False

    def open_conn(self):
        if not self._is_connected():
            self.connection = sqlite3.connect(self.db_name)

            # Enable foreign keys for this connection:
            with self.connection:
                self.connection.execute("PRAGMA foreign_keys = ON;")
            self.is_open = True
            return self
        else:
            raise Exception("An already established connection exists")

    def create_new_user(self, user: User):
        if self.is_redundant("Users", "username", user["username"]):
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
            query = f"INSERT INTO Users ({cols}) VALUES ({placeholder})"
            cursor.execute(query, values)

        return self

    def close_conn(self):
        if self._is_connected():
            self.connection.close()
            self.is_open = False
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
