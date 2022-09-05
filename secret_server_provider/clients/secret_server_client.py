from secret_server_openapiclient import ApiClient, Configuration

from base_provider.clients.base_client import BaseClient
from secret_server_provider.configuration.client_configuration import SecretServerConfiguration
from secret_server_provider.clients.simple_http_client import SimpleHttpClient


class SecretServerClient(BaseClient):
    def __init__(
        self,
        client_configuration: SecretServerConfiguration,
    ) -> None:
        super().__init__(client_configuration=client_configuration)
        configuration = Configuration(host=client_configuration.host)
        configuration.api_key['BearerToken'] = f'bearer {client_configuration.api_key}'
        # openapi client needs this
        self.configuration = configuration
        self.openapi_client = ApiClient(configuration=configuration)
        self.internal_api_client = SimpleHttpClient(client_configuration)
