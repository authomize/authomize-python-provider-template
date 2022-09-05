from typing import Iterable

from secret_server_openapiclient.apis import SecretsApi
from secret_server_openapiclient.model.secret_model_v2 import SecretModelV2

from base_provider.extractors.base_extractor import BaseExtractor
from secret_server_provider.clients.secret_server_client import SecretServerClient
from secret_server_provider.paginator import get_paginated_results


class SecretsExtractor(BaseExtractor):
    """
    Gets a list of Secrets records.
    """

    def extract_raw(self) -> Iterable[SecretModelV2]:
        data_provider_client: SecretServerClient = self.data_provider_client
        api_instance = SecretsApi(data_provider_client.openapi_client)

        return get_paginated_results(api_instance.secrets_service_search_v2)

