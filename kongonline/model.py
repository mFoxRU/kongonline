__author__ = 'mFoxRU'

from peewee import SqliteDatabase, Model, Proxy, IntegerField

database = SqliteDatabase('kongonline.sqlite')
database.connect()


class Stats(Model):
    time_t = IntegerField(null=True)
    online = IntegerField(null=True)
    games = IntegerField(null=True)

    class Meta:
        database = database
        db_table = 'stats'


def write_info(time, online, games):
    Stats.create(time_t=time, online=online, games=games)


database.create_tables((Stats,), safe=True)