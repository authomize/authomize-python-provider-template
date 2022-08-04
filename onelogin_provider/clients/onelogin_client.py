from onelogin.api.client import OneLoginClient as OneLoginApiClient

from onelogin_provider.configuration.onelogin_configuration import OneloginConfiguration
from provider_base.clients.base_data_provider_client import BaseDataProviderClient


class OneloginClient(BaseDataProviderClient):
    def __init__(
        self,
        data_provider_configuration: OneloginConfiguration,
    ) -> None:
        super().__init__(data_provider_configuration=data_provider_configuration)
        self.client = OneLoginApiClient(
            client_id=data_provider_configuration.client_id,
            client_secret=data_provider_configuration.client_secret,
            region=data_provider_configuration.region,
        )