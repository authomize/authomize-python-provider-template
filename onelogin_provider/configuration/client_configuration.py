from base_provider.configuration.base_client_configuration import BaseClientConfiguration


class OneloginClientConfiguration(BaseClientConfiguration):
    client_id: str
    client_secret: str
    region: str = 'us'
