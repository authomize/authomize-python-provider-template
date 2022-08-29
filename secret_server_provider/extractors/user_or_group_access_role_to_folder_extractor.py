from locale import normalize
import structlog
from typing import Iterable

from base_provider.extractors.base_extractor import BaseExtractor
from secret_server_provider.clients.secret_server_client import SecretServerClient
from secret_server_provider.normalize_id import normalize_id

from secret_server_openapiclient.apis import FolderPermissionsApi, UsersApi
from secret_server_openapiclient.model.folder_permission_summary import FolderPermissionSummary
from secret_server_openapiclient.model.user_model import UserModel
logger = structlog.get_logger()

class UserOrGroupAccessRoleToFolderExtractor(BaseExtractor):
    """
    Gets a list of folder permissions.
    """
    logger = logger.bind(loader_name="UserOrGroupAccessRoleToFolderExtractor")
    def extract_raw(self) -> Iterable[FolderPermissionSummary]:
        data_provider_client: SecretServerClient = self.data_provider_client
        api_instance = UsersApi(data_provider_client.client)
        secret_instance = FolderPermissionsApi(data_provider_client.client)
        api_response = api_instance.users_service_search_users()
        all_users = api_response.records
        for user in all_users:
            yield from self._fetch_secret_permissions(secret_instance, user)

    def _fetch_secret_permissions(self, api_instance: FolderPermissionsApi, user: UserModel) -> Iterable[FolderPermissionSummary]:
        return self.__get_paginated_results(api_instance, user)
        
    def __get_paginated_results(self, api_instance:UsersApi, user: UserModel) -> Iterable[FolderPermissionSummary]:
        cur_skip = 0
        has_next = True
        while (has_next) :
            api_response = api_instance.folder_permissions_service_search(filter_user_id=normalize_id(user.id) , skip=normalize_id(cur_skip))
            has_next = api_response.has_next
            cur_skip += int(api_response.next_skip)
            yield from api_response.records