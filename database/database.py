import mysql.connector
from config.database_config import DB_CONFIG


class Database:
    """Small wrapper around the MySQL connection and cursor operations."""

    def __init__(self):
        self.connection = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.connection.cursor(dictionary=True)

    def execute(self, query, params=None, fetch=False):
        self.cursor.execute(query, params or ())
        if fetch:
            return self.cursor.fetchall()
        self.connection.commit()
        return self.cursor.lastrowid

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection and self.connection.is_connected():
            self.connection.close()
