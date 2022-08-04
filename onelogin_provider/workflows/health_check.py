from onelogin_provider.clients.onelogin_client import OneloginClient
from provider_base.workflows.base_health_check import BaseHelathChecker


class OneloginHealthChecker(BaseHelathChecker):
    def can_connect_to_data_provider(self) -> bool:
        return self.can_read_from_data_provider()

    def can_read_from_data_provider(self) -> bool:
        client = OneloginClient(
            data_provider_configuration=self.data_provider_configuration,
        )
        client.client.get_users(limit=1)
        return True
