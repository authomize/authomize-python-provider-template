from pydantic import Field

from base_provider.configuration.base_client_configuration import BaseClientConfiguration


class BamboohrClientConfiguration(BaseClientConfiguration):
    domain: str = Field(..., env="BAMBOOHR_DOMAIN")
    access_token: str = Field(..., env="BAMBOOHR_ACCESS_TOKEN")
