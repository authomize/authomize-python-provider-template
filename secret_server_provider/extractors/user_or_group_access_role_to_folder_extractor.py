from typing import Iterable

import structlog
from secret_server_openapiclient.apis import FolderPermissionsApi, GroupsApi, UsersApi
from secret_server_openapiclient.model.folder_permission_summary import FolderPermissionSummary
from secret_server_openapiclient.model.group_model import GroupModel
from secret_server_openapiclient.model.user_model import UserModel
from secret_server_openapiclient.model.user_summary import UserSummary

from base_provider.extractors.base_extractor import BaseExtractor
from secret_server_provider.clients.secret_server_client import SecretServerClient

logger = structlog.get_logger()


class UserOrGroupAccessRoleToFolderExtractor(BaseExtractor):
    """
    Gets a list of folder permissions.
    """
    logger = logger.bind(loader_name="UserOrGroupAccessRoleToFolderExtractor")

    def extract_raw(self) -> Iterable[FolderPermissionSummary]:
        data_provider_client: SecretServerClient = self.data_provider_client
        api_users_instance = UsersApi(data_provider_client.openapi_client)
        api_groups_instance = GroupsApi(data_provider_client.openapi_client)
        secret_instance = FolderPermissionsApi(data_provider_client.openapi_client)
        for user in self.__get_paginated_users_results(api_users_instance):
            yield from self.__get_paginated_results_user_or_group(secret_instance, user)
        for group in self.__get_paginated_groups_results(api_groups_instance):
            yield from self.__get_paginated_results_user_or_group(secret_instance, group)

    def __get_paginated_results_user_or_group(self, api_instance: UsersApi, user:
                                              UserModel | GroupModel) -> Iterable[FolderPermissionSummary]:
        cur_skip = 0
        has_next = True
        while (has_next):
            if type(user) == UserModel:
                api_response = api_instance.folder_permissions_service_search(
                                            filter_user_id=user.id,
                                            skip=cur_skip)
            else:
                api_response = api_instance.folder_permissions_service_search(
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
