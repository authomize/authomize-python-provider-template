"""Client for banboo hr using basic auth"""
from base64 import b64encode
from typing import Optional

import requests

from bamboohr_provider.configuration.client_configuration import BamboohrClientConfiguration
from base_provider.clients.base_client import BaseClient


class BamboohrClient(BaseClient):
    """Client for Bamboo using basic auth"""

    # password is allways x
    PASSWORD = 'x'

    def __init__(
        self,
        client_configuration: BamboohrClientConfiguration,
    ) -> None:
        """Init client with doamin and token"""
        super().__init__(client_configuration=client_configuration)
        self.domain = client_configuration.domain
        self.basic = b64encode(
            bytes(client_configuration.access_token + ':' + self.PASSWORD, "utf-8"),
        ).decode("ascii")

    def get_users(self, fields_to_fetch: Optional[list[str]] = None, only_current=True) -> dict:
        """
        Get users list using custom report api, as suggested by bamboohr

        XXX - Notice that we set onlyCurrent=true, we might want to change it to false

        API: https://documentation.bamboohr.com/reference/request-custom-report-1
        Fields: https://documentation.bamboohr.com/docs/list-of-field-names

        Efficiency Tip: If you're trying to get employee data in bulk (for all employees),
        we recommend using the request a custom report API.

        """
        if not fields_to_fetch:
            fields_to_fetch = ['id']
        only_current_str = 'true' if only_current else 'false'
        url = f"https://api.bamboohr.com/api/gateway.php/{self.domain}/v1/reports/custom?format=json&onlyCurrent={only_current_str}"  # noqa E501
        payload = {"fields": fields_to_fetch}
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {self.basic}",
        }

        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
