"""This module implements class Variables that provides variables for microservices."""

from enum import Enum


class Variables(Enum):
    """Create variables for microservices."""

    ENTRIES_FIELD = 'entries'
    TITLE_FIELD = 'title'
    LINK_FIELD = 'link'
    PUBLISHED_FIELD = 'published'
    SOURCE_FIELD = 'source'
    DESCRIPTION_FIELD = 'description'
    URL_FIELD = 'url'
    DATE_FIELD = 'date'
    DATE_FORMAT = '%d/%m/%Y'
    ARTICLES_FIELD = 'articles'
    STATUS_FIELD = 'status'
    MESSAGE_FIELD = 'message'
    CONFIG_FILE_NAME = '/config.yaml'
