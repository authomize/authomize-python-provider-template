from typing import Iterable

from secret_server_openapiclient.apis import SecretsApi
from secret_server_openapiclient.model.secret_model_v2 import SecretModelV2

from base_provider.extractors.base_extractor import BaseExtractor
from secret_server_provider.clients.secret_server_client import SecretServerClient
from secret_server_provider.normalize_id import normalize_id


class SecretsLastAccessKeyExtractor(BaseExtractor):
    """
    Gets a list of Secrets records.
    """

    def extract_raw(self) -> Iterable[tuple[str, dict]]:
        data_provider_client: SecretServerClient = self.data_provider_client
        api_instance = SecretsApi(data_provider_client.openapi_client)
        all_secrets = self.__get_paginated_results(api_instance)
        for secret in all_secrets:
            for result in self.get_secret_access_key_history(normalize_id(secret.id))['records']:
                yield (normalize_id(secret.id), result)

    def __get_paginated_results(self, api_instance: SecretsApi) -> Iterable[SecretModelV2]:
        cur_skip = 0
        has_next = True
        while (has_next):
            api_response = api_instance.secrets_service_search_v2(skip=cur_skip)
            has_next = api_response.has_next
            cur_skip += int(api_response.next_skip)
            yield from api_response.records

    def get_secret_access_key_history(self, secret_id: str) -> dict:
        """Get secret access key history"""
        # TODO read slug from secret's template
        data_provider_client: SecretServerClient = self.data_provider_client
        slug = "access-key"
        response = data_provider_client.internal_api_client.post_internal_api(f'{secret_id}/fields/{slug}', {})
        try:
            response.raise_for_status()
            return response.json()
        except Exception as e:
            if "API_SecretFieldNotFound" in str(e):
                self.logger.info("Secret {secret} has no access-keys", secret=secret_id)
            else:
                self.logger.info(str(e))
            return {"records": []}
