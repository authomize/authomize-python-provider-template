from provider_base.configuration.base_data_provider_configuration import \
    BaseDataProviderConfiguration


class DataProviderConfiguration(BaseDataProviderConfiguration):
    base_url: str

    domain: str
    # tenant_id: str

    token: str
    # oauth_token: str
    # user_name: str
    # user_password: str
