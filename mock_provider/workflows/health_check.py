from base_provider.workflows.base_provider_health_checker import BaseProviderHealthChecker
from mock_provider.clients.client import MockProviderClient


class MockProviderHelathChecker(BaseProviderHealthChecker):
    def can_connect_to_data_provider(self) -> bool:
        client = MockProviderClient(
            data_provider_configuration=self.data_provider_configuration,
        )
        return client.is_alive()

    def can_read_from_data_provider(self) -> bool:
        client = MockProviderClient(
            data_provider_configuration=self.data_provider_configuration,
        )
        client.me()
        return True
