__author__ = 'mFoxRU'

from flask import Flask

app = Flask(__name__)


@app.route("/")
def last_stats():
    return 'Kongonline is up and running'


if __name__ == "__main__":
    app.run(debug=False)