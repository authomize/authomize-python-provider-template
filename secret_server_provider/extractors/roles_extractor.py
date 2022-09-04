from typing import Iterable

from secret_server_openapiclient.apis import RolesApi
from secret_server_openapiclient.model.role_model import RoleModel

from base_provider.extractors.base_extractor import BaseExtractor
from secret_server_provider.clients.secret_server_client import SecretServerClient
from secret_server_provider.normalize_id import normalize_id


class RolesExtractor(BaseExtractor):
    """
    Gets a list of Roles records.

    See docs/RolesApi.md#roles_service_get_all
    """

    def extract_raw(self) -> Iterable[RoleModel]:
        data_provider_client: SecretServerClient = self.data_provider_client
        api_instance = RolesApi(data_provider_client.openapi_client)

        return self.__get_paginated_results(api_instance)

    def __get_paginated_results(self, api_instance: RolesApi) -> Iterable[RoleModel]:
        cur_skip = 0
        has_next = True
        while (has_next):
            api_response = api_instance.roles_service_get_all(skip=cur_skip)
            has_next = api_response.has_next
            cur_skip += int(api_response.next_skip)
            yield from api_response.records
