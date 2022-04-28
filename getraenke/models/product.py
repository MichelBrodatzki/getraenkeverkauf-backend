from peewee import *

from getraenke.models.base import BaseModel

class Product(BaseModel):
    ean = CharField(unique=True)
    name = CharField()
    price = DoubleField()
