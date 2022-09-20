from base_provider.clients.base_client import BaseClient
from teams_provider.clients.microsoft_graph_client import MicrosoftGraphClient
from teams_provider.configuration.client_configuration import MicrosoftClientConfiguration


class MicrosoftClient(BaseClient):
    def __init__(
            self,
            client_configuration: MicrosoftClientConfiguration,
    ) -> None:
        super().__init__(client_configuration=MicrosoftClientConfiguration())
        self.client = MicrosoftGraphClient(client_configuration.tenant_id,
                                           client_configuration.client_id,
                                           client_configuration.client_secret)
