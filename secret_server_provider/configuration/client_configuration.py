from typing import Optional

from pydantic import Field

from base_provider.configuration.base_client_configuration import BaseClientConfiguration


class SecretServerConfiguration(BaseClientConfiguration):
    api_host: str = Field(..., env="SECRET_SERVER_HOST")
    user_name: str = Field(..., env="SECRET_SERVER_USERNAME")
    password: str = Field(..., env="SECRET_SERVER_PASSWORD")
    # access-key and username are by default fetched
    keys_to_fetch: Optional[str] = Field(default="access-key,username", env="KEY_FIELD_NAMES")
    api_key: str = ""

    # shared cofiguration api_key needs to be updated after token generation
    # for a sake of the http_simple_client who uses token for internal api queries
    def set_api_key(self, new_key):
        self.api_key = new_key

    def set_new_host(self, new_host):
        self.api_host = new_host
