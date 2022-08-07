from base_provider.configuration.base_data_provider_configuration import (
    DataProviderConfiguration,
)


class MockProviderConfiguration(DataProviderConfiguration):
    base_url: str

    domain: str
    # tenant_id: str

    token: str
    # oauth_token: str
    # user_name: str
    # user_password: str
