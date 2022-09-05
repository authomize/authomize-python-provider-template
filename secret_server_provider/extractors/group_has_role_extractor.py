from tokenize import group
from typing import Iterable

from secret_server_openapiclient.apis import GroupsApi
from secret_server_openapiclient.model.group_model import GroupModel
from secret_server_openapiclient.model.role_summary import RoleSummary
from secret_server_openapiclient.model.user_model import UserModel

from base_provider.extractors.base_extractor import BaseExtractor
from secret_server_provider.clients.secret_server_client import SecretServerClient
from secret_server_provider.normalize_id import normalize_id


class GroupHasRoleExtractor(BaseExtractor):
    """
    Gets a list of Role records.
    """

    def extract_raw(self) -> Iterable[tuple[UserModel, RoleSummary]]:
        data_provider_client: SecretServerClient = self.data_provider_client
        api_instance = GroupsApi(data_provider_client.openapi_client)

        all_groups = self.__get_paginated_groups_results(api_instance)
        return self._get_all_group_roles(api_instance, all_groups)

    def _get_all_group_roles(self, api_instance: GroupsApi,
                            all_groups: Iterable[GroupModel]) -> Iterable[tuple[GroupModel, RoleSummary]]:
        for group in all_groups:
            for role_record in self._fetch_group_roles(api_instance, group):
                yield (group, role_record)

    def _fetch_group_roles(self, api_instance: GroupsApi, user: GroupModel) -> Iterable[RoleSummary]:
        return self.__get_paginated_results_for_roles(api_instance, group)

    def __get_paginated_results_for_roles(self, api_instance: GroupsApi, user: GroupModel) -> Iterable[RoleSummary]:
        cur_skip = 0
        has_next = True
        while (has_next):
            api_response = api_instance.group_service_get_roles(id=user.id,
                                                                skip=cur_skip)
            has_next = api_response.has_next
            cur_skip += int(api_response.next_skip)
            yield from api_response.records

    def __get_paginated_groups_results(self, api_instance: GroupsApi) -> Iterable[GroupModel]:
        cur_skip = 0
        has_next = True
        while (has_next):
            api_response = api_instance.groups_service_search_users(skip=cur_skip)
            has_next = api_response.has_next
            cur_skip += int(api_response.next_skip)
            yield from api_response.records