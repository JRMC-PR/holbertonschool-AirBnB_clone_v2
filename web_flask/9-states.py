#!/usr/bin/python3
""" This module starts a Flask web application """""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
""" Flask class and render_template method"""""
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(self):
    storage.close()


@app.route('/states')
def states():
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>')
def states_id(id):
    states = storage.all(id)
    return render_template('9-states.html', id=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
