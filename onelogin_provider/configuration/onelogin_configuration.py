from base_provider.configuration.base_data_provider_configuration import (
    BaseDataProviderConfiguration,
)


class OneloginConfiguration(BaseDataProviderConfiguration):
    client_id: str
    client_secret: str
    region: str = 'us'
