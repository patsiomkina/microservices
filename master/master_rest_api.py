"""This module implements Master API."""

import pathlib

from flask import Flask

from tools.helper import Helper
from master_controller import MasterController

app = Flask(__name__)


@app.route('/master/api/url', methods=['POST'])
def get_news_from_reaper():
    """Retrieve news feed data using Reaper and Keeper and upload it to the database."""
    response = MasterController.get_news_from_reaper()
    return response


@app.route('/master/api/db', methods=['GET'])
def get_news_from_keeper():
    """Retrieve data from database using Keeper."""
    response = MasterController.get_news_from_keeper()
    return response


@app.route('/')
def main():
    """Check API availability."""
    return 'Welcome to the Master API!'


if __name__ == '__main__':
    path = pathlib.Path(__file__).parent.absolute()
    app.run(port=Helper().get_port(path))
