__author__ = 'mFoxRU'

from peewee import SqliteDatabase, Model, IntegerField

database = SqliteDatabase('kongonline.sqlite')


class Stats(Model):
    time_t = IntegerField(null=True)
    online = IntegerField(null=True)
    games = IntegerField(null=True)

    class Meta:
        database = database
        db_table = 'stats'






