from peewee import *

database = SqliteDatabase('../data/database.db', **{})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Users(BaseModel):
    age = IntegerField(null=True)
    email = TextField()
    username = TextField()

    class Meta:
        db_table = 'Users'
