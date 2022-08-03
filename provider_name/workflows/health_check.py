from provider_base.workflows.base_health_check import BaseHelathChecker
from provider_name.clients.data_provider_client import DataProviderClient


class ProviderNameHelathChecker(BaseHelathChecker):
    def can_connect_to_data_provider(self) -> bool:
        client = DataProviderClient(
            data_provider_configuration=self.data_provider_configuration,
        )
        return True

    def can_read_from_data_provider(self) -> bool:
        client = DataProviderClient(
            data_provider_configuration=self.data_provider_configuration,
        )
        return True
