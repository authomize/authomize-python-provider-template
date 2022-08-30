from asyncio.log import logger
from pydantic import Field
from typing import Iterable

from base_provider.extractors.base_extractor import BaseExtractor
from secret_server_provider.clients.secret_server_client import SecretServerClient

from secret_server_openapiclient.apis import SecretsApi
from secret_server_openapiclient.model.secret_model_v2 import SecretModelV2

from secret_server_provider.normalize_id import normalize_id
import requests

URL_PREFIX = "https://integrations.secretservercloud.com/internals/secret-audits"

class SecretsLastAccessKeyExtractor(BaseExtractor):
    """
    Gets a list of Secrets records.
    """
    api_key: str = Field(..., env="SECRET_SERVER_API_KEY")
    #TODO bearer from env 
    @property
    def headers(self) -> dict:
        """Get/Create bearer headers"""
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
    @property
    def body(self) -> dict:
        """Get/Create bearer headers"""
        return {}
    def extract_raw(self) -> Iterable[tuple[str, dict]]:
        data_provider_client: SecretServerClient = self.data_provider_client
        api_instance = SecretsApi(data_provider_client.client)
        all_secrets = self.__get_paginated_results(api_instance)
        for secret in all_secrets:
            try:
                for result in self.get_secret_access_key_history(normalize_id(secret.id))['records']:
                    yield (normalize_id(secret.id), result)
            except Exception as e:
                if "API_SecretFieldNotFound"  in str(e) :
                    self.logger.info("Secret {secret} has no access-keys", secret=secret.id)
                else:
                    self.logger.info(str(e))
    
    def __get_paginated_results(self, api_instance:SecretsApi) -> Iterable[SecretModelV2]:
        cur_skip = 0
        has_next = True
        while (has_next) :
            api_response = api_instance.secrets_service_search_v2(skip = normalize_id(cur_skip))
            has_next = api_response.has_next
            cur_skip += int(api_response.next_skip)
            yield from api_response.records
    
    def get_secret_access_key_history(self, secret_id : str) -> dict:
        """Get secret access key history"""
        #TODO read slug from secret's template
        slug = "access-key"
        url = f"{URL_PREFIX}/{secret_id}/fields/{slug}"  # noqa: E501
        response = requests.post(url, headers=self.headers, json=self.body)
        response.raise_for_status()
        return response.json()



