__author__ = 'mFoxRU'

import json
import urllib2


def check(tries=3):
    for _ in xrange(tries):
        try:
            resp = urllib2.urlopen('http://www.kongregate.com/site_stats.json')
        except Exception as e:
            print e
        else:
            params = json.load(resp)
            if 'users_online_count' in params and 'games_count' in params:
                return params['users_online_count'], params['games_count']
            else:
                print KeyError
    return None, None


if __name__ == '__main__':
    print check()