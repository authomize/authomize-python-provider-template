from base_provider.workflows.base_provider_health_checker import ProviderHealthChecker
from onelogin_provider.clients.onelogin_client import OneloginClient
from onelogin_provider.configuration.onelogin_configuration import OneloginConfiguration


class OneloginHealthChecker(ProviderHealthChecker):
    def can_connect_to_data_provider(self) -> bool:
        return self.can_read_from_data_provider()

    def can_read_from_data_provider(self) -> bool:
        data_provider_configuration: OneloginConfiguration = self.data_provider_configuration  # type: ignore
        client = OneloginClient(
            data_provider_configuration=data_provider_configuration,
        )
        client.client.get_users(limit=1)
        return True
