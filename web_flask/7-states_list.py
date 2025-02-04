#!/usr/bin/python3
"""
script that starts a Flask web application
"""

from flask import Flask, render_template
from models.state import State
from models import storage
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """display a HTML page: (inside the tag BODY)"""
    states = sorted(
            list(storage.all(State).values()), key=lambda val: val.name
            )
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exception):
    """closes storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
