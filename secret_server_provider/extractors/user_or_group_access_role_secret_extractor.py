from typing import Iterable

import structlog
from secret_server_openapiclient.apis import GroupsApi, SecretPermissionsApi, UsersApi
from secret_server_openapiclient.model.group_model import GroupModel
from secret_server_openapiclient.model.secret_permission_summary import SecretPermissionSummary
from secret_server_openapiclient.model.user_model import UserModel
from secret_server_openapiclient.model.user_summary import UserSummary

from base_provider.extractors.base_extractor import BaseExtractor
from secret_server_provider.clients.secret_server_client import SecretServerClient

logger = structlog.get_logger()


class UserOrGroupAccessRoleToSecretExtractor(BaseExtractor):
    """
    Gets a list of access role records.
    See docs/UsersApi.md#users_service_search_users
    """
    logger = logger.bind(loader_name="UserOrGroupAccessRoleToSecretExtractor")

    def extract_raw(self) -> Iterable[SecretPermissionSummary]:
        data_provider_client: SecretServerClient = self.data_provider_client
        api_users_instance = UsersApi(data_provider_client.openapi_client)
        api_groups_instance = GroupsApi(data_provider_client.openapi_client)
        secret_instance = SecretPermissionsApi(data_provider_client.openapi_client)
        for user in self.__get_paginated_users_results(api_users_instance):
            yield from self.__get_paginated_permissions_results_user_or_group(secret_instance, user)
        for group in self.__get_paginated_groups_results(api_groups_instance):
            yield from self.__get_paginated_permissions_results_user_or_group(secret_instance, group)

    def __get_paginated_permissions_results_user_or_group(
            self, api_instance: UsersApi,
            user: UserModel | GroupModel) -> Iterable[SecretPermissionSummary]:
        cur_skip = 0
        has_next = True
        while (has_next):
            if isinstance(user, UserModel):
                api_response = api_instance.secret_permissions_service_search_secret_permissions(
                                            filter_user_id=user.id,
                                            skip=cur_skip)
            else:
                api_response = api_instance.secret_permissions_service_search_secret_permissions(
                                            filter_group_id=user.id,
                                            skip=cur_skip)
            has_next = api_response.has_next
            cur_skip += int(api_response.next_skip)
            yield from api_response.records

    def __get_paginated_users_results(self, api_instance: UsersApi) -> Iterable[UserSummary]:
        cur_skip = 0
        has_next = True
        while (has_next):
            api_response = api_instance.users_service_search_users(skip=cur_skip)
            has_next = api_response.has_next
            cur_skip += int(api_response.next_skip)
            yield from api_response.records

    def __get_paginated_groups_results(self, api_instance: GroupsApi) -> Iterable[GroupModel]:
        cur_skip = 0
        has_next = True
        while (has_next):
            api_response = api_instance.groups_service_search(skip=cur_skip)
            has_next = api_response.has_next
            cur_skip += int(api_response.next_skip)
            yield from api_response.records
