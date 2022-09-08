from secret_server_openapiclient import ApiClient, Configuration
import requests
from base_provider.clients.base_client import BaseClient
from secret_server_provider.clients.simple_http_client import SimpleHttpClient
from secret_server_provider.configuration.client_configuration import SecretServerConfiguration


class SecretServerClient(BaseClient):
    def __init__(
        self,
        client_configuration: SecretServerConfiguration,
    ) -> None:
        super().__init__(client_configuration=client_configuration)
        self.generate_authentication_token_and_update_configuration()
        configuration = Configuration(host=client_configuration.api_host)
        configuration.api_key['BearerToken'] = client_configuration.api_key
        # openapi client needs this
        self.configuration = configuration
        self.openapi_client = ApiClient(configuration=configuration)
        self.internal_api_client = SimpleHttpClient(client_configuration)

    def generate_authentication_token_and_update_configuration(self):
        if (self.client_configuration.api_key == ""):
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
            data = {"username": "AuthomizeUser",
                    "grant_type": "password",
                    "password": "Authomize123!",
                    }
            url = f'{self.client_configuration.api_host}/oauth2/token'
            response = requests.post(url, headers=headers, data=data)
            response.raise_for_status()
            bearer_token = response.json()['access_token']
            # shared with http_simple_client for internal api and external api querying
            self.client_configuration.set_new_host(f'{self.client_configuration.api_host}/api')
            self.client_configuration.set_api_key(f'bearer {bearer_token}')