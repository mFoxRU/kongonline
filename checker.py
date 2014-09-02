__author__ = 'mFoxRU'

import json
import urllib2


def check():
    try:
        resp = urllib2.urlopen('http://www.kongregate.com/site_stats.json')
    except Exception as e:
        return e
    else:
        params = json.load(resp)
        return params['users_online_count'], params['games_count']


if __name__ == '__main__':
    print check()