from typing import Iterable

from secret_server_openapiclient.apis import SecretsApi
from secret_server_openapiclient.model.secret_model_v2 import SecretModelV2

from base_provider.extractors.base_extractor import BaseExtractor
from secret_server_provider.clients.secret_server_client import SecretServerClient
from secret_server_provider.normalize_id import normalize_id


class SecretsExtractor(BaseExtractor):
    """
    Gets a list of Secrets records.
    """

    def extract_raw(self) -> Iterable[SecretModelV2]:
        data_provider_client: SecretServerClient = self.data_provider_client
        api_instance = SecretsApi(data_provider_client.openapi_client)

        return self.__get_paginated_results(api_instance)

    def __get_paginated_results(self, api_instance: SecretsApi) -> Iterable[SecretModelV2]:
        cur_skip = 0
        has_next = True
        while (has_next):
            api_response = api_instance.secrets_service_search_v2(skip=cur_skip)
            has_next = api_response.has_next
            cur_skip += int(api_response.next_skip)
            yield from api_response.records
