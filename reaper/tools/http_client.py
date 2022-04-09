"""This module implements the REST API."""

from typing import Optional
import requests
from requests import Response


class HTTPClient:
    """Send requests and returns the results of execution."""

    def get(self, url: str, headers: Optional[dict] = None, params: Optional[dict] = None) -> Response:
        """Send a GET request."""
        return requests.get(url, headers=headers, params=params)

    def post(self, url: str, data: Optional[dict] = None, json: Optional[str] = None, headers: Optional[dict] = None,
             params: Optional[dict] = None) -> Response:
        """Send a POST request."""
        return requests.post(url, data=data, json=json, headers=headers, params=params)

    def delete(self, url: str, headers: Optional[dict] = None, params: Optional[dict] = None,
               data: Optional[dict] = None) -> Response:
        """Send a DELETE request."""
        return requests.delete(url, headers=headers, params=params, data=data)

    def put(self, url: str, headers: Optional[dict] = None, params: Optional[dict] = None,
            data: Optional[dict] = None) -> Response:
        """Send a PUT request."""
        return requests.put(url, headers=headers, params=params, data=data)
