from base_provider.workflows.base_health_checker import BaseProviderHealthChecker
from mock_provider.clients.client import MockProviderClient


class MockProviderHelathChecker(BaseProviderHealthChecker):
    def can_connect_to_data_provider(self) -> bool:
        client = MockProviderClient(
            client_configuration=self.client_configuration,
        )
        return client.is_alive()

    def can_read_from_data_provider(self) -> bool:
        client = MockProviderClient(
            client_configuration=self.client_configuration,
        )
        client.me()
        return True
