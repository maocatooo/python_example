from flask import Flask
from flask import Blueprint

app = Flask(__name__)


@app.route('/')
def index():
    pass


if __name__ == "__main__":
    app.run()