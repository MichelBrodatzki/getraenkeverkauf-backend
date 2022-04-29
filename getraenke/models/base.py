from peewee import *

from getraenke.database import get_database

class BaseModel(Model):
    class Meta:
        database = get_database()
