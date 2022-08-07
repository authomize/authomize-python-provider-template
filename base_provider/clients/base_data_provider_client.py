from base_provider.configuration.base_client_configuration import ClientConfiguration


class DataProviderClient:
    def __init__(
        self,
        data_provider_client_configuration: ClientConfiguration,
    ) -> None:
        self.data_provider_client_configuration = data_provider_client_configuration
