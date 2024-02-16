from flask import Flask

app = Flask(__name__)


class HelloWorld:
    """A simple class representing the Hello World application."""

    @staticmethod
    @app.route('/', strict_slashes=False)
    def hello():
        """
        Route function to display 'Hello HBNB!'.

        Returns:
            str: The message 'Hello HBNB!'.
        """
        return 'Hello HBNB!'


if __name__ == '__main__':
    app.run()
