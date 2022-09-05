from typing import Iterable

from secret_server_openapiclient.apis import FoldersApi
from secret_server_openapiclient.model.folder_model import FolderModel

from base_provider.extractors.base_extractor import BaseExtractor
from secret_server_provider.clients.secret_server_client import SecretServerClient
from secret_server_provider.paginator import get_paginated_results


class FoldersExtractor(BaseExtractor):
    """
    Gets a list of Folders records.
    """

    def extract_raw(self) -> Iterable[FolderModel]:
        data_provider_client: SecretServerClient = self.data_provider_client
        api_instance = FoldersApi(data_provider_client.openapi_client)

        return get_paginated_results(api_instance.folders_service_search)
