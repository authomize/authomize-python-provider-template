import requests

from base_provider.clients.base_client import BaseClient
from secret_server_provider.configuration.client_configuration import SecretServerConfiguration


class SimpleHttpClient(BaseClient):
    def __init__(
        self,
        client_configuration: SecretServerConfiguration,
    ) -> None:
        super().__init__(client_configuration=client_configuration)
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": client_configuration.api_key,
        }
        self.url = "https://integrations.secretservercloud.com/internals"

    def post_internal_api(self, url_path, json_body=None):
        json_body = json_body or {}
        url = f'{self.url}/{url_path}'
        return requests.post(url, headers=self.headers, json=json_body)
