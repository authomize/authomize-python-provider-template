from base_provider.workflows.base_health_checker import BaseProviderHealthChecker
from teams_provider.clients.microsoft_client import MicrosoftClient


class MicrosoftHealthChecker(BaseProviderHealthChecker):
    def can_connect_to_data_provider(self) -> bool:
        return self.can_read_from_data_provider()

    def can_read_from_data_provider(self) -> bool:
        client_configuration: MicrosoftClientConfiguration = self.client_configuration  # type: ignore
        client = MicrosoftClient(
            client_configuration=client_configuration,
        )
        client.client.get_all_items(
            'users',
        )
        return True
