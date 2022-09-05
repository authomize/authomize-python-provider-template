from typing import Iterable

from secret_server_openapiclient.apis import GroupsApi
from secret_server_openapiclient.model.group_model import GroupModel

from base_provider.extractors.base_extractor import BaseExtractor
from secret_server_provider.clients.secret_server_client import SecretServerClient
from secret_server_provider.paginator import get_paginated_results


class GroupsExtractor(BaseExtractor):
    """
    Gets a list of Group records.

    See docs/GroupsApi.md#groups_service_search
    """

    def extract_raw(self) -> Iterable[GroupModel]:
        data_provider_client: SecretServerClient = self.data_provider_client
        api_instance = GroupsApi(data_provider_client.openapi_client)

        return get_paginated_results(api_instance.groups_service_search)
