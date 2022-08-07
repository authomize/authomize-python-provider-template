from base_provider import ProviderHealthChecker
from onelogin_provider.clients.onelogin_client import OneloginClient
from onelogin_provider.configuration.client_configuration import OneloginClientConfiguration


class OneloginHealthChecker(ProviderHealthChecker):
    def can_connect_to_data_provider(self) -> bool:
        return self.can_read_from_data_provider()

    def can_read_from_data_provider(self) -> bool:
        data_provider_client_configuration: OneloginClientConfiguration = self.data_provider_client_configuration  # type: ignore
        client = OneloginClient(
            data_provider_client_configuration=data_provider_client_configuration,
        )
        client.client.get_users(limit=1)
        return True
