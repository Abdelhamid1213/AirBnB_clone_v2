from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """
    This is the index route of the Flask application.
    It returns a string "Hello HBNB!" when accessed.
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    """
    This is the main entry point of the application.
    It runs the Flask application on the local server.
    """
    app.run()
