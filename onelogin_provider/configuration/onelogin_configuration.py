from base_provider.configuration.base_data_provider_configuration import (
    DataProviderConfiguration,
)


class OneloginConfiguration(DataProviderConfiguration):
    client_id: str
    client_secret: str
    region: str = 'us'
