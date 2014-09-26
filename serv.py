__author__ = 'mFoxRU'

from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime as dt

from online import routine, get_last, count_entries

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


@app.route("/last/")
@app.route("/last/<int:num>")
def last(num=10):
    data = ['Showing {0} of {1} entries'.format(num, count_entries())]
    for entry in get_last(num):
        data.append('[{0}] Games: {1}, Online: {2}'.format(*entry))
    reply = '<br>'.join(data)
    return reply

if __name__ == "__main__":
    initialize()
    app.run(debug=True)