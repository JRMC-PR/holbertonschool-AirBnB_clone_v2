#!/usr/bin/python3
""" This module starts a Flask web application """""
from flask import Flask
from flask import render_template
""" Flask class and render_template method"""""
app = Flask(__name__)
app.url_map.strict_slashes = False

""" App route section
    Add a second route /hbnb:
    display “HBNB”

    Add a third route /c/<text>:
    display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space ) "

    Add a fourth route /python/(<text>):
    display “Python ”, followed by the value of the text variable"""""


@app.route('/')
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    return f"C {text.replace('_', ' ')}"


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python(text='is cool'):
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>')
def number(n):
    return f"{n} is a number"


@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_even(n):
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
