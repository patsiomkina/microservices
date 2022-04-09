"""This module implements Reaper API."""

import pathlib

from flask import Flask

from tools.helper import Helper
from reaper_controller import ReaperController

app = Flask(__name__)


@app.route('/reaper/api/sites', methods=['GET'])
def get_from_url():
    """Retrieve and process the news feed of a given website."""
    response = ReaperController.get_from_url()
    return response


@app.route('/')
def main():
    """Check API availability."""
    return 'Welcome to the Reaper API!'


if __name__ == '__main__':
    path = pathlib.Path(__file__).parent.absolute()
    app.run(port=Helper().get_port(path))
