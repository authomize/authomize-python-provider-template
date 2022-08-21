from bamboohr_provider.clients.bamboohr_client import BamboohrClient
from bamboohr_provider.configuration.client_configuration import BamboohrClientConfiguration
from base_provider.workflows.base_health_checker import BaseProviderHealthChecker


class BamboohrHealthChecker(BaseProviderHealthChecker):
    def can_connect_to_data_provider(self) -> bool:
        return self.can_read_from_data_provider()

    def can_read_from_data_provider(self) -> bool:
        client_configuration: BamboohrClientConfiguration = self.client_configuration  # type: ignore
        client = BamboohrClient(
            client_configuration=client_configuration,
        )
        return len(list(client.get_users())) > 0
