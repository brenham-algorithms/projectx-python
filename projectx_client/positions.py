import json
import logging

import requests

logger = logging.getLogger(__name__)


class Positions:
    def __init__(self, base_url, jwt_token):
        self.base_url = base_url
        self.jwt_token = jwt_token

    def search_open(self, **payload):
        url = f"{self.base_url}/api/Position/searchOpen"

        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json",
        }

        logger.debug(json.dumps({"event": "search_open_request", "args": payload}))

        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()

        positions = response.json()["positions"]

        return positions

    def close_contract(self, **payload):
        url = f"{self.base_url}/api/Position/closeContract"

        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json",
        }

        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()

        return response.json()
