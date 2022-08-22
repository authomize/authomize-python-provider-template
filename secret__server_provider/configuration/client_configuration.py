from base_provider.configuration.base_client_configuration import BaseClientConfiguration
from pydantic import Field


class SecretServerConfiguration(BaseClientConfiguration):
    host: str = Field(..., env="SECRET_SERVER_HOST")
    api_key: str = Field(..., env="SECRET_SERVER_API_KEY")
