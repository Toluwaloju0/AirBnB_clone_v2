#!/usr/bin/python3
"""A mmodule to serve a website"""

from flask import Flask, abort


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def Ctext(text):
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route("/number/<n>", strict_slashes=False)
def is_num(n):
    try:
        n = int(n)
        return f"{n} is a number"
    except ValueError:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
