__author__ = 'mFoxRU'

from time import sleep, time

from checker import check
from saver import write_data

db_file = 'kongonline.sqlite'


def routine():
    timestamp = int(time())
    online, games = check()
    if online is not None:
        write_data(timestamp, online, games, db_file)
        print timestamp, online, games


def main():
    while 1:
        routine()
        sleep(100)

if __name__ == '__main__':
    main()