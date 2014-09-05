__author__ = 'mFoxRU'

from time import sleep, time

from kongonline.checker import check
from kongonline.saver import write_data

db_file = 'kongonline.sqlite'


def routine():
    timestamp = int(time())
    online, games = check()
    if online is not None:
        write_data(timestamp, online, games, db_file)
        return timestamp, online, games
    return None


def main():
    while 1:
        print routine()
        sleep(100)

if __name__ == '__main__':
    main()