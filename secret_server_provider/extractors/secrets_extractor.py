from typing import Iterable

from base_provider.extractors.base_extractor import BaseExtractor
from secret_server_provider.clients.secret_server_client import SecretServerClient

from secret_server_openapiclient.apis import SecretsApi
from secret_server_openapiclient.model.secret_model_v2 import SecretModelV2


class SecretsExtractor(BaseExtractor):
    """
    Gets a list of Secrets records.

    See docs/SecretsApi.md#secrets_service_search_v2)
    """

    def extract_raw(self) -> Iterable[SecretModelV2]:
        data_provider_client: SecretServerClient = self.data_provider_client
        api_instance = SecretsApi(data_provider_client.client)

        # TODO : errors handling
        # response codes return None Type - swagger.json problem
        api_response = api_instance.secrets_service_search_v2()

        all_secrets = api_response.records

        '''
        TODO:make skip work later
        while (api_response.hasNext) :
            api_response = api_instance.secrets_service_search_v2(skip = 10)
            all_secrets.extend(api_response.records())
        '''
        return all_secrets
