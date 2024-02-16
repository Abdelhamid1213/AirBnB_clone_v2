#!/usr/bin/python3
"""A simple Flask web application."""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Route function to display 'Hello HBNB!' message."""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Route function to display 'HBNB' message."""
    return "HBNB"


if __name__ == "__main__":
    """Starts the Flask web application."""
    app.run(host='0.0.0.0', port=5000)
