from base_provider import BaseProviderHealthChecker
from onelogin_provider.clients.onelogin_client import OneloginClient
from onelogin_provider.configuration.client_configuration import OneloginClientConfiguration


class OneloginHealthChecker(BaseProviderHealthChecker):
    def can_connect_to_data_provider(self) -> bool:
        return self.can_read_from_data_provider()

    def can_read_from_data_provider(self) -> bool:
        client_configuration: OneloginClientConfiguration = self.client_configuration  # type: ignore
        client = OneloginClient(
            client_configuration=client_configuration,
        )
        client.client.get_users(limit=1)
        return True
