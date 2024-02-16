#!/usr/bin/python3
"""A simple Flask web application."""
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Route function to display 'Hello HBNB!' message."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Route function to display 'HBNB' message."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Route function to display '/c/<text>' message."""
    return "C " + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Route function to display 'python/<text>' message."""
    return "Python " + text.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Route function to display '/number/<n>' message."""
    return f'{n} is a number'


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Route function to display '/number_template/<n>' message."""
    return render_template("5-number.html", number=n)


if __name__ == "__main__":
    """Starts the Flask web application."""
    app.run(host='0.0.0.0', port=5000)
