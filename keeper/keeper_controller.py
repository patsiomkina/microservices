"""This module implements class KeeperController that provides functions for API endpoints."""

from flask import Response, jsonify, request, make_response

from tools.news_database import NewsDB
from tools.variables import Variables


class KeeperController:
    """Create KeeperController that provides functions for API endpoints."""

    @staticmethod
    def get_all_news_from_db() -> Response:
        """Retrieve news from the database according to the specified parameters.

        Parameter 'date' should be entered in the format: %d/%m/%Y

        """
        try:
            date = request.args.get(Variables.DATE_FIELD.value)
            url = request.args.get(Variables.URL_FIELD.value)
            if date is not None and url is not None:
                result = NewsDB().retrieve_news_from_db(url=url, date=date)
            elif date is not None:
                result = NewsDB().retrieve_news_from_db(date=date)
            elif url is not None:
                result = NewsDB().retrieve_news_from_db(url=url)
            else:
                result = NewsDB().retrieve_news_from_db()
            return jsonify({Variables.ARTICLES_FIELD.value: result})
        except Exception as e:
            message = jsonify({Variables.STATUS_FIELD.value: 404, Variables.MESSAGE_FIELD.value: e})
            return make_response(message, 404)

    @staticmethod
    def store_news_in_db() -> Response:
        """Save news in the database."""
        try:
            url = request.json[Variables.URL_FIELD.value]
            news = request.json[Variables.ARTICLES_FIELD.value]
            NewsDB().upload_news_to_db(url=url, list_of_news=news)
            return jsonify({Variables.STATUS_FIELD.value: 200,
                            Variables.MESSAGE_FIELD.value.title(): 'All data are successfully inserted'})
        except Exception as e:
            message = jsonify({Variables.STATUS_FIELD.value: 404, Variables.MESSAGE_FIELD.value: e})
            return make_response(message, 404)
