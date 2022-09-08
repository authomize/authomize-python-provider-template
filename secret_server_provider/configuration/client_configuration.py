from typing import Optional

from pydantic import Field

from base_provider.configuration.base_client_configuration import BaseClientConfiguration


class SecretServerConfiguration(BaseClientConfiguration):
    api_host: str = Field(..., env="SECRET_SERVER_HOST")
    user_name: str = Field(..., env="SECRET_SERVER_USERNAME")
    password: str = Field(..., env="SECRET_SERVER_PASSWORD")
    # access-key and username are by default fetched
    keys_to_fetch: Optional[str] = Field(default="access-key,username", env="KEY_FIELD_NAMES")
