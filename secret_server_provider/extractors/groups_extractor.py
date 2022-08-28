from typing import Iterable

from base_provider.extractors.base_extractor import BaseExtractor
from secret_server_provider.clients.secret_server_client import SecretServerClient
from secret_server_provider.normalize_id import normalize_id

from secret_server_openapiclient.apis import GroupsApi
from secret_server_openapiclient.model.group_model import GroupModel


class GroupsExtractor(BaseExtractor):
    """
    Gets a list of Group records.

    See docs/GroupsApi.md#groups_service_search
    """

    def extract_raw(self) -> Iterable[GroupModel]:
        data_provider_client: SecretServerClient = self.data_provider_client
        api_instance = GroupsApi(data_provider_client.client)

        return self.__get_paginated_results(api_instance)

    def __get_paginated_results(self, api_instance:GroupsApi) -> Iterable[GroupModel]:
        cur_skip = 0
        has_next = True
        while (has_next) :
            api_response = api_instance.groups_service_search(skip = normalize_id(cur_skip))
            has_next = api_response.has_next
            cur_skip += int(api_response.next_skip)
            yield from api_response.records
