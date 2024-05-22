from peewee import *
import config


db = SqliteDatabase(config.db_path)


class BaseModel(Model):
    class Meta:
        database = db


class Group(BaseModel):
    name = CharField(unique=True)


class Student(BaseModel):
    full_name = CharField()
    email = CharField(unique=True)
    group = ForeignKeyField(Group, backref='students')
    age = IntegerField()


db.connect()
db.create_tables([Group, Student])
