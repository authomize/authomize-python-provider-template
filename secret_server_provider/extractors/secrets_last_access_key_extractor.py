from asyncio.log import logger
from urllib import response
from pydantic import Field
from typing import Iterable

from base_provider.extractors.base_extractor import BaseExtractor
from base_provider.extractors.base_internal_and_external_extractor import BaseInternalAndExternalExtractor
from secret_server_provider.clients.secret_server_client import SecretServerClient

from secret_server_openapiclient.apis import SecretsApi
from secret_server_openapiclient.model.secret_model_v2 import SecretModelV2
from secret_server_provider.clients.simple_http_client import SimpleHttpClient

from secret_server_provider.normalize_id import normalize_id


class SecretsLastAccessKeyExtractor(BaseInternalAndExternalExtractor):
    """
    Gets a list of Secrets records.
    """

    def extract_raw(self) -> Iterable[tuple[str, dict]]:
        data_provider_client: SecretServerClient = self.data_provider_client
        api_instance = SecretsApi(data_provider_client.client)
        all_secrets = self.__get_paginated_results(api_instance)
        for secret in all_secrets:
            for result in self.get_secret_access_key_history(normalize_id(secret.id))['records']:
                yield (normalize_id(secret.id), result)
            
    
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
        response = self.http_client._post_internal_api(f'{secret_id}/fields/access-key',{})
        try:
            response.raise_for_status()
            return response.json()
        except Exception as e:
            if "API_SecretFieldNotFound"  in str(e) :
                self.logger.info("Secret {secret} has no access-keys", secret=secret_id)
            else:
                self.logger.info(str(e))
            return {"records": []}



