from typing import Iterable

import structlog
from secret_server_openapiclient.apis import GroupsApi, SecretPermissionsApi, UsersApi
from secret_server_openapiclient.model.group_model import GroupModel
from secret_server_openapiclient.model.secret_permission_summary import SecretPermissionSummary
from secret_server_openapiclient.model.user_model import UserModel

from base_provider.extractors.base_extractor import BaseExtractor
from secret_server_provider.clients.secret_server_client import SecretServerClient
from secret_server_provider.normalize_id import normalize_id

logger = structlog.get_logger()


class UserOrGroupAccessRoleToSecretExtractor(BaseExtractor):
    """
    Gets a list of access role records.
    See docs/UsersApi.md#users_service_search_users
    """
    logger = logger.bind(loader_name="UserOrGroupAccessRoleToSecretExtractor")

    def extract_raw(self) -> Iterable[SecretPermissionSummary]:
        data_provider_client: SecretServerClient = self.data_provider_client
        api_users_instance = UsersApi(data_provider_client.client)
        api_groups_instance = GroupsApi(data_provider_client.client)
        secret_instance = SecretPermissionsApi(data_provider_client.client)
        for user in api_users_instance.users_service_search_users().records:
            yield from self.__get_paginated_results_user_or_group(secret_instance, user)
        for group in api_groups_instance.groups_service_search().records:
            yield from self.__get_paginated_results_user_or_group(secret_instance, group)

    def __get_paginated_results_user_or_group(
            self, api_instance: UsersApi,
            user: UserModel | GroupModel) -> Iterable[SecretPermissionSummary]:
        cur_skip = 0
        has_next = True
        while (has_next):
            if type(user) == UserModel:
                api_response = api_instance.secret_permissions_service_search_secret_permissions(
                                            filter_user_id=normalize_id(user.id),
                                            skip=normalize_id(cur_skip))
            else:
                api_response = api_instance.secret_permissions_service_search_secret_permissions(
                                            filter_group_id=normalize_id(user.id),
                                            skip=normalize_id(cur_skip))
            has_next = api_response.has_next
            cur_skip += int(api_response.next_skip)
            yield from api_response.records
