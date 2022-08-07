from base_provider import ClientConfiguration


class OneloginClientConfiguration(ClientConfiguration):
    client_id: str
    client_secret: str
    region: str = 'us'
