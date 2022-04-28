from flask import g
from os import getenv

from playhouse.db_url import connect

def get_database():
    """
    Returns existing database object, if it exists, else it connects to database and returns new database object.
    """
    if 'database' not in g:
        # Open new database connection, if it doesn't exist yet
        database_url = getenv("DATABASE_URL", None)

        if database_url is None:
            print ("No database url set! Defaulting to SQLite database")

        print ("Opening database")
        g.database = connect(database_url or 'sqlite:///database.sqlite')

    # Return existing database connection
    return g.database
