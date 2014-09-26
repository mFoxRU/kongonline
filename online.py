__author__ = 'mFoxRU'

from time import sleep, time

from kongonline.checker import check
from kongonline.model import *


def routine():
    timestamp = int(time())
    online, games = check()
    if online is not None:
        write_info(timestamp, online, games)
        return timestamp, online, games
    return None


def main():
    while 1:
        print routine()
        sleep(100)

if __name__ == '__main__':
    main()