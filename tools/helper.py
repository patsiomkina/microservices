"""This module implements Helper that provides functions for code savings."""

import pathlib

import yaml

from tools.variables import Variables


class Singleton(type):
    """The class needed to implement the pattern Singleton."""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Implement a call to an instance of the class."""
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Helper(metaclass=Singleton):
    """Create a helper for code savings."""

    def __get_endpoint(self, path: pathlib, key: str) -> str:
        """Get access to the content of the configuration file."""
        with open(f'{path}{Variables.CONFIG_FILE_NAME.value}', 'r') as file:
            config_data = yaml.load(file, Loader=yaml.FullLoader)
            return config_data[key]

    def get_port(self, path: pathlib):
        """Get port number."""
        return self.__get_endpoint(path, 'port')

    def get_keeper_post_endpoint(self, path: pathlib) -> str:
        """Get keeper post endpoint."""
        return self.__get_endpoint(path, 'keeper_post_endpoint')

    def get_keeper_get_endpoint(self, path: pathlib) -> str:
        """Get keeper get endpoint."""
        return self.__get_endpoint(path, 'keeper_get_endpoint')

    def get_reaper_get_endpoint(self, path: pathlib) -> str:
        """Get reaper get endpoint."""
        return self.__get_endpoint(path, 'reaper_get_endpoint')
