""" libraries/app_library.py """
import requests


class AppLibrary:
    def __init__(self):
        self._base_url = "http://localhost:5001"

    def send_ping(self):
        requests.get(f"{self._base_url}/ping")
