from pydantic import Field

from base_provider.configuration.base_client_configuration import BaseClientConfiguration


class SecretServerConfiguration(BaseClientConfiguration):
    host: str = Field(..., env="SECRET_SERVER_HOST", default="https://integrations.secretservercloud.com/api")
    api_key: str = Field(..., env="SECRET_SERVER_API_KEY")
