from pydantic import Field
import requests

from base_provider.configuration.base_client_configuration import BaseClientConfiguration


class SecretServerConfiguration(BaseClientConfiguration):
    # TODO : add default like host: str = Field(..., env="SECRET_SERVER_HOST",
    #        default="https://integrations.secretservercloud.com/api")
 
    api_host: str = Field(..., env="SECRET_SERVER_HOST")
    user_name: str = Field(..., env="SECRET_SERVER_USERNAME")
    password: str = Field(..., env="SECRET_SERVER_PASSWORD")
    keys_to_fetch: str = Field(..., env="KEY_FIELD_NAMES")
    api_key: str = ""

    def generate_authentication_token(self):
        if (self.api_key == ""):
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
            data = {"username": "AuthomizeUser","grant_type": "password","password":"Authomize123!"}
            url = f'{self.api_host}/oauth2/token'
            self.api_host = f'{self.api_host}/api'
            response = requests.post(url, headers=headers, data=data)
            response.raise_for_status()
            bearer_token = response.json()['access_token']
            self.api_key = f'bearer {bearer_token}'
