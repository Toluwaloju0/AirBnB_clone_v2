#!/usr/bin/python3
"""A mmodule to serve a website"""

from flask import abort, Flask, render_template


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


@app.route("/number_template/<n>", strict_slashes=False)
def render_temp(n):
    try:
        n = int(n)
        return render_template('5-number.html', n=n)
    except ValueError:
        abort(404)


@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def odd_or_even(n):
    try:
        n = int(n)
        if (n % 2) == 0:
            num_type = 'even'
        else:
            num_type = 'odd'
        temp = "6-number_odd_or_even.html"
        return render_template(temp, n=n, num_type=num_type)
    except ValueError:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
