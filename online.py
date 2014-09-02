__author__ = 'mFoxRU'

from time import sleep

from checker import check


def main():
    while 1:
        print check()
        sleep(100)

if __name__ == '__main__':
    main()