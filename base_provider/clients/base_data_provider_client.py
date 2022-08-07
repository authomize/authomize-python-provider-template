from base_provider.configuration.base_client_configuration import BaseClientConfiguration


class BaseDataProviderClient:
    def __init__(
        self,
        data_provider_client_configuration: BaseClientConfiguration,
    ) -> None:
        self.data_provider_client_configuration = data_provider_client_configuration
