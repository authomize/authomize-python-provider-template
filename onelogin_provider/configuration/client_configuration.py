from pydantic import Field

from base_provider.configuration.base_client_configuration import BaseClientConfiguration


class OneloginClientConfiguration(BaseClientConfiguration):
    client_id: str = Field(..., env="ONELOGIN_CLIENT_ID")
    client_secret: str = Field(..., env="ONELOGIN_CLIENT_SECRET")
    region: str = 'us'
