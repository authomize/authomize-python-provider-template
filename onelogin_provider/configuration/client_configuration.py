from base_provider import BaseClientConfiguration


class OneloginClientConfiguration(BaseClientConfiguration):
    client_id: str
    client_secret: str
    region: str = 'us'
