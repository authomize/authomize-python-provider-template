from base_provider import ClientConfiguration


class MockProviderClientConfiguration(ClientConfiguration):
    base_url: str

    domain: str
    # tenant_id: str

    token: str
    # oauth_token: str
    # user_name: str
    # user_password: str
