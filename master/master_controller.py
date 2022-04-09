"""This module implements class MasterController that provides functions for API endpoints."""
import pathlib

import requests

from flask import request, Response, make_response, jsonify

from tools.helper import Helper
from tools.variables import Variables


class MasterController:
    """Create MasterController that provides functions for API endpoints."""

    @staticmethod
    def get_news_from_reaper() -> Response:
        """Retrieve news feed data using Reaper and Keeper and upload it to the database."""
        path = pathlib.Path(__file__).parent.absolute()
        url = request.args.get(Variables.URL_FIELD.value)
        params = {Variables.URL_FIELD.value: url}
        response = requests.get(url=Helper().get_reaper_get_endpoint(path), params=params)
        if response.ok:
            resp = response.json()
            resp[Variables.URL_FIELD.value] = url
            response = requests.post(url=Helper().get_keeper_post_endpoint(path), json=resp)
            if response.ok:
                return response.json()
            else:
                return make_response(jsonify({Variables.STATUS_FIELD.value: response.status_code})
                                     , response.status_code)
        else:
            return make_response(jsonify({Variables.STATUS_FIELD.value: response.status_code})
                                 , response.status_code)

    @staticmethod
    def get_news_from_keeper() -> Response:
        """Retrieve data from database using Keeper."""
        path = pathlib.Path(__file__).parent.absolute()
        date = request.args.get(Variables.DATE_FIELD.value)
        url = request.args.get(Variables.URL_FIELD.value)
        params = {Variables.DATE_FIELD.value: date, Variables.URL_FIELD.value: url}
        response = requests.get(url=Helper().get_keeper_get_endpoint(path), params=params)
        if response.ok:
            return response.json()
        else:
            return make_response(jsonify({Variables.STATUS_FIELD.value: response.status_code})
                                 , response.status_code)
