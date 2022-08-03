

from provider_name.configuration.data_provider_configuration import DataProviderConfiguration


class DataProviderClient:
    def __init__(
        self,
        data_provider_configuration: DataProviderConfiguration,
    ) -> None:
        self.data_provider_configuration = data_provider_configuration
