import requests
from secret_server_openapiclient import ApiClient, Configuration

from base_provider.clients.base_client import BaseClient
from secret_server_provider.clients.simple_http_client import SimpleHttpClient
from secret_server_provider.configuration.client_configuration import SecretServerConfiguration


class SecretServerClient(BaseClient):
    def __init__(
        self,
        client_configuration: SecretServerConfiguration,
    ) -> None:
        super().__init__(client_configuration=client_configuration)
        (api_key, api_host) = self.generate_authentication_token()
        configuration = Configuration(host=api_host)
        configuration.api_key['BearerToken'] = api_key
        # openapi client needs this
        self.configuration = configuration
        self.openapi_client = ApiClient(configuration=configuration)
        self.internal_api_client = SimpleHttpClient(client_configuration, api_key)

    def generate_authentication_token(self) -> tuple[str, str]:
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {
            "grant_type": "password",
            "username": self.client_configuration.user_name,
            "password": self.client_configuration.password,
        }
        url = f'{self.client_configuration.api_host}/oauth2/token'
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()
        bearer_token = response.json()['access_token']
        # shared with http_simple_client for internal api and external api querying
        return (f'bearer {bearer_token}', f'{self.client_configuration.api_host}/api')
