__author__ = 'mFoxRU'

from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler

from online import routine

app = Flask(__name__)
cron = BackgroundScheduler()


def initialize():
    import os
    # Defence against apscheduler double start in Flask debug mode
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        cron.add_job(routine, 'interval', seconds=100, max_instances=1)
        cron.start()


@app.route("/")
def last_stats():
    return 'Kongonline is up and running...'


if __name__ == "__main__":
    initialize()
    app.run(debug=True)