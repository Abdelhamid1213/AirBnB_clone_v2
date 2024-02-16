#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Route function to display 'Hello HBNB!' message."""
    return "Hello HBNB!"


if __name__ == "__main__":
    """Starts the Flask web application."""
    app.run()
