"""
We create (self_made) a context manager for connecting to a database.
exc - exception
exc_type: exception type, exc_val: value exception, exc_tb: exception traceback
"""

import sqlite3

class DatabaseConnection:
    def __init__(self, host):
        self.connection = None
        self.host = host

    def __enter__(self):
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()