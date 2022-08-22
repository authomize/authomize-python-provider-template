from ..openapi_client.plugins import ApiClient    
from base_provider.clients.base_client import BaseClient
from secret__server_provider.configuration.client_configuration import SecretServerConfiguration
from secret__server_provider.openapi_client.plugins import Configuration


class SecretServerClient(BaseClient):
    def __init__(
        self,
        client_configuration: SecretServerConfiguration,
    ) -> None:
        super().__init__(client_configuration=client_configuration)
        configuration = Configuration(host=client_configuration.host)
        configuration.api_key['BearerToken'] = f'bearer {client_configuration.api_key}'
        self.client = ApiClient(configuration=configuration)
