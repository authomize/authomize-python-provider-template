from ..openapi_client.plugins import ApiClient    
from base_provider import BaseClient
from secret__server_provider.configuration.client_configuration import SecretServerConfiguration


class SecretServerClient(BaseClient):
    def __init__(
        self,
        client_configuration: SecretServerConfiguration,
    ) -> None:
        super().__init__(client_configuration=client_configuration)
        self.client = ApiClient(client_configuration.configuration)