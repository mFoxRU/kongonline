__author__ = 'mFoxRU'

from time import sleep, time

from checker import check
from saver import write_data

db_file = 'kongonline.sqlite'


def main():
    while 1:
        online, games = check()
        timestamp = int(time())
        write_data(timestamp, online, games, db_file)
        sleep(5)

if __name__ == '__main__':
    main()