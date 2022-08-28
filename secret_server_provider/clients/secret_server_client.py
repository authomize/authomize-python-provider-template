from base_provider.clients.base_client import BaseClient
from secret_server_provider.configuration.client_configuration import SecretServerConfiguration
from secret_server_openapiclient import Configuration
from secret_server_openapiclient import ApiClient


class SecretServerClient(BaseClient):
    def __init__(
        self,
        client_configuration: SecretServerConfiguration,
    ) -> None:
        super().__init__(client_configuration=client_configuration)
        configuration = Configuration(host=client_configuration.host)
        configuration.api_key['BearerToken'] = f'bearer {client_configuration.api_key}'
        self.client = ApiClient(configuration=configuration)
        self.configuration = configuration

    @staticmethod
    def iter_all(callable, *args, **kwargs):
        return callable(*args, **kwargs)
