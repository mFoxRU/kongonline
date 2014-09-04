__author__ = 'mFoxRU'

import sqlite3

table_create = 'CREATE TABLE IF NOT EXISTS stats (id INTEGER PRIMARY KEY NOT NULL, time_t INTEGER, online INTEGER, games INTEGER);'
table_write = 'INSERT INTO stats (time_t, online, games) VALUES (?, ?, ?);'


def write_data(time, online, games, filename):
    connection = None
    try:
        connection = sqlite3.connect(filename)
        connection.execute(table_create)
        connection.execute(table_write, (time, online, games))

    except sqlite3.Error as e:
        if connection:
            connection.rollback()
        print e
    else:
        connection.commit()
    finally:
        if connection:
            connection.close()