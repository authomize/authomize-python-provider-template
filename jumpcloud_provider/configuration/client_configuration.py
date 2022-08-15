from pydantic import Field

from base_provider.configuration.base_client_configuration import BaseClientConfiguration


class JumpcloudClientConfiguration(BaseClientConfiguration):
    api_key: str = Field(..., env="JUMPCLOUD_API_KEY")
    limit: int = Field(..., env="JUMPCLOUD_REQUEST_LIMIT")
    content_type = "application/json"
    accept = "application/json"
