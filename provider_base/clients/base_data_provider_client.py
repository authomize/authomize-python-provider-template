from provider_base.configuration.base_data_provider_configuration import (
    BaseDataProviderConfiguration,
)


class BaseDataProviderClient:
    def __init__(
        self,
        data_provider_configuration: BaseDataProviderConfiguration,
    ) -> None:
        self.data_provider_configuration = data_provider_configuration
