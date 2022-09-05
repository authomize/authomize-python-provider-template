from onelogin.api.client import OneLoginClient as OneLoginApiClient

from base_provider.clients.base_client import BaseClient
from onelogin_provider.configuration.client_configuration import OneloginClientConfiguration


class OneloginClient(BaseClient):
    def __init__(
        self,
        client_configuration: OneloginClientConfiguration,
    ) -> None:
        super().__init__(client_configuration=client_configuration)
        self.client = OneLoginApiClient(
            client_id=client_configuration.client_id,
            client_secret=client_configuration.client_secret,
            region=client_configuration.region,
        )
