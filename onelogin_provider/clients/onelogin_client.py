from onelogin.api.client import OneLoginClient as OneLoginApiClient

from base_provider import DataProviderClient
from onelogin_provider.configuration.client_configuration import OneloginClientConfiguration


class OneloginClient(DataProviderClient):
    def __init__(
        self,
        data_provider_client_configuration: OneloginClientConfiguration,
    ) -> None:
        super().__init__(data_provider_client_configuration=data_provider_client_configuration)
        self.client = OneLoginApiClient(
            client_id=data_provider_client_configuration.client_id,
            client_secret=data_provider_client_configuration.client_secret,
            region=data_provider_client_configuration.region,
        )
