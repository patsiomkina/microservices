"""This module implements parser for RSS."""

import feedparser

from typing import List, Dict
from tools.variables import Variables


class RSSParser:
    """Create a parser for extracting news from RSS."""

    @staticmethod
    def parse_news(response: str) -> List[Dict]:
        """Parse the received data and creates list of news."""
        rss_news = feedparser.parse(response)
        default_value = '---'

        news_list = []
        for entry in rss_news[Variables.ENTRIES_FIELD.value]:
            title = entry.get(Variables.TITLE_FIELD.value, default_value)
            link = entry.get(Variables.LINK_FIELD.value, default_value)
            published = entry.get(Variables.PUBLISHED_FIELD.value, default_value)
            source = entry.get(Variables.SOURCE_FIELD.value, default_value)
            description = entry.get(Variables.DESCRIPTION_FIELD.value, default_value)

            source_title = default_value
            if source != default_value:
                source_title = source[Variables.TITLE_FIELD.value]

            article = {
                Variables.TITLE_FIELD.name: title,
                Variables.LINK_FIELD.name: link,
                Variables.PUBLISHED_FIELD.name: published,
                Variables.SOURCE_FIELD.name: source_title,
                Variables.DESCRIPTION_FIELD.name: description,
            }
            news_list.append(article)

        return news_list
