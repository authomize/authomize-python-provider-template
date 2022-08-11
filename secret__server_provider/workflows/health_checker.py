from base_provider import BaseProviderHealthChecker
from secret__server_provider.clients.secret_server_client import SecretServerClient
from secret__server_provider.configuration.client_configuration import SecretServerConfiguration


class SecretServerHealthChecker(BaseProviderHealthChecker):
    def can_connect_to_data_provider(self) -> bool:
        return self.can_read_from_data_provider()

    def can_read_from_data_provider(self) -> bool:
        client_configuration: OneloginClientConfiguration = self.client_configuration  # type: ignore
        client = SecretServerClient(
            client_configuration=client_configuration,
        )
        client.client.get_users(limit=1)
        return True
