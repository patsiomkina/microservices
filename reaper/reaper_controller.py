"""This module implements class ReaperController that provides functions for API endpoints."""

from flask import jsonify, Response, request, make_response

from tools.rss_parser import RSSParser
from tools.http_client import HTTPClient
from tools.variables import Variables


class ReaperController:
    """Create ReaperController that provides functions for API endpoints."""

    @staticmethod
    def get_from_url() -> Response:
        """Retrieve and process the news feed of a given website."""
        try:
            url = request.args.get(Variables.URL_FIELD.value)
            http_client = HTTPClient()
            response = http_client.get(url)
            if response.ok:
                result = RSSParser.parse_news(response.text)
                return jsonify({Variables.ARTICLES_FIELD.value: result})
            else:
                return make_response(jsonify({Variables.STATUS_FIELD.value: response.status_code})
                                     , response.status_code)
        except Exception as e:
            message = jsonify({Variables.STATUS_FIELD.value: 404, Variables.MESSAGE_FIELD.value: e})
            return make_response(message, 404)
