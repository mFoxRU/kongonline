__author__ = 'mFoxRU'

from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
import sqlite3
from datetime import datetime as dt

from online import routine, db_file

app = Flask(__name__)
cron = BackgroundScheduler()


def initialize():
    from os import environ
    # Defence against apscheduler double start in Flask debug mode
    if environ.get('WERKZEUG_RUN_MAIN') == 'true':
        cron.start()
        cron.add_job(routine, 'interval', seconds=100, max_instances=1,
                     next_run_time=dt.now())


@app.route("/")
def status():
    return 'Kongonline is up and running...'

@app.route("/last")
def last_10():
    connection = None
    reply = ''
    try:
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM stats ORDER BY ROWID DESC LIMIT 10')
        data = []
        for line in cursor.fetchall():
            time = dt.fromtimestamp(line[1])
            data.append('[%s] Games: %i, Online: %i' %
                        (time.strftime('%y-%m-%d|%H:%M:%S'), line[2], line[3]))
            reply = '<br>'.join(data)
    except sqlite3.Error as e:
        reply = e
    finally:
        if connection:
            connection.close()
    return reply

if __name__ == "__main__":
    initialize()
    app.run(debug=True)