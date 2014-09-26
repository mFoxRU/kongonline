__author__ = 'mFoxRU'

from datetime import datetime as dt

from peewee import SqliteDatabase, Model, IntegerField

database = SqliteDatabase('kongonline.sqlite', check_same_thread=False)
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


def get_last(num=10):
    ret = []
    for item in Stats.select().order_by(Stats.time_t.desc()).limit(num):
        time = dt.fromtimestamp(item.time_t).strftime('%y-%m-%d|%H:%M:%S')
        ret.append((time, item.online, item.games))
    return ret


def count_entries():
    return Stats.select().count()

database.create_tables((Stats,), safe=True)