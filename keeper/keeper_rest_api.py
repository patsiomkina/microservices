"""This module implements Keeper API."""

import pathlib

from flask import Flask

from tools.helper import Helper
from keeper_controller import KeeperController

app = Flask(__name__)


@app.route('/keeper/api/db_news', methods=['GET'])
def get_all_news_from_db():
    """Retrieve news from the database."""
    response = KeeperController.get_all_news_from_db()
    return response


@app.route('/keeper/api/db_news/add_news', methods=['POST'])
def store_news_in_db():
    """Save news in the database."""
    response = KeeperController.store_news_in_db()
    return response


@app.route('/')
def main():
    """Check API availability."""
    return 'Welcome to the Keeper API!'


if __name__ == '__main__':
    path = pathlib.Path(__file__).parent.absolute()
    app.run(port=Helper().get_port(path))
