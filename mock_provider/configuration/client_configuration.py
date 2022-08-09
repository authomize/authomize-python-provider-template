from base_provider.configuration.base_client_configuration import BaseClientConfiguration


class MockProviderClientConfiguration(BaseClientConfiguration):
    base_url: str

    domain: str
    # tenant_id: str

    token: str
    # oauth_token: str
    # user_name: str
    # user_password: str
