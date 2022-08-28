from typing import Iterable

from base_provider.extractors.base_extractor import BaseExtractor
from secret__server_provider.clients.secret_server_client import SecretServerClient
from secret__server_provider.normalize_id import normalize_id

from ..openapi_client.plugins.apis import FoldersApi
from ..openapi_client.plugins.model.folder_model import FolderModel


class FoldersExtractor(BaseExtractor):
    """
    Gets a list of Folders records.
    """

    def extract_raw(self) -> Iterable[FolderModel]:
        data_provider_client: SecretServerClient = self.data_provider_client
        api_instance = FoldersApi(data_provider_client.client)

        return self.__get_paginated_results(api_instance)

    def __get_paginated_results(self, api_instance:FoldersApi) -> Iterable[FolderModel]:
        cur_skip = 0
        has_next = True
        while (has_next) :
            api_response = api_instance.folders_service_lookup(skip = normalize_id(cur_skip))
            has_next = api_response.has_next
            cur_skip += int(api_response.next_skip)
            yield from api_response.records
