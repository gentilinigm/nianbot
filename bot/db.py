import psycopg2


class DB:
    """Abstraction for a connection to the main nian database."""

    def __init__(self, connection: psycopg2):
        self.cursor = connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.cursor.close()
