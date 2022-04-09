"""This module implements class NewsDB."""

import pathlib
import sqlite3

import dateparser

from typing import List, Optional, Dict
from tools.variables import Variables


class Singleton(type):
    """The class needed to implement the pattern Singleton."""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Implement a call to an instance of the class."""
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class NewsDB(metaclass=Singleton):
    """Creates a data base for storing news."""

    def __init__(self):
        """Initialize class attributes."""
        db_name = '/news.db'
        db_path = pathlib.Path(__file__).parent.absolute()
        db = f'{db_path}{db_name}'
        self.connection = sqlite3.connect(db)
        self.__init_database()

    def __init_database(self):
        """Create required table."""
        cursor = self.connection.cursor()
        sql = 'CREATE TABLE IF NOT EXISTS news (title text, link text UNIQUE, full_date text, date text, ' \
              'source text, description text, url text)'
        cursor.execute(sql)
        self.connection.commit()

    def upload_news_to_db(self, list_of_news: List[Dict], url: str):
        """Store news in a local storage."""
        cursor = self.connection.cursor()
        for item in list_of_news:
            title = item[Variables.TITLE_FIELD.name]
            link = item[Variables.LINK_FIELD.name]
            date = item[Variables.PUBLISHED_FIELD.name]
            new_date = dateparser.parse(item[Variables.PUBLISHED_FIELD.name]).strftime(Variables.DATE_FORMAT.value)
            source = item[Variables.SOURCE_FIELD.name]
            description = item[Variables.DESCRIPTION_FIELD.name]

            sql = "INSERT OR REPLACE INTO news VALUES (?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(sql, (title, link, date, new_date, source, description, url))
        self.connection.commit()

    def retrieve_news_from_db(self, url: Optional[str] = None, date: Optional[str] = None) -> \
            List[Dict]:
        """Retrieve news for the selected date and (or) from selected url."""
        cursor = self.connection.cursor()
        if url and date:
            cursor.execute('SELECT title, link, date, source, description, url FROM news WHERE date=:date '
                           'and url=:url', {'date': date, 'url': url})
        elif date and url is None:
            cursor.execute('SELECT title, link, date, source, description, url FROM news WHERE date=:date',
                           {'date': date})
        elif url and date is None:
            cursor.execute('SELECT title, link, date, source, description, url FROM news WHERE url=:url',
                           {'url': url})
        else:
            cursor.execute('SELECT title, link, date, source, description, url FROM news')

        records = cursor.fetchall()
        articles = []
        for title, link, date, source, description, url in records:
            articles.append({
                Variables.TITLE_FIELD.value.title(): title,
                Variables.LINK_FIELD.value.title(): link,
                Variables.PUBLISHED_FIELD.value.title(): date,
                Variables.SOURCE_FIELD.value.title(): source,
                Variables.DESCRIPTION_FIELD.value.title(): description,
                Variables.URL_FIELD.value: url,
            })
        return articles
