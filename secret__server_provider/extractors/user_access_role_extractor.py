from typing import Iterable

from base_provider.extractors.base_extractor import BaseExtractor
from secret__server_provider.clients.secret_server_client import SecretServerClient
from secret__server_provider.normalize_id import normalize_id

from ..openapi_client.plugins.apis import SecretPermissionsApi, UsersApi
from ..openapi_client.plugins.model.secret_permission_summary import SecretPermissionSummary
from ..openapi_client.plugins.model.user_model import UserModel


class UserAccessRoleExtractor(BaseExtractor):
    """
    Gets a list of access role records.
    See docs/UsersApi.md#users_service_search_users
    """

    def extract_raw(self) -> Iterable[SecretPermissionSummary]:
        data_provider_client: SecretServerClient = self.data_provider_client
        api_instance = UsersApi(data_provider_client.client)
        secret_instance = SecretPermissionsApi(data_provider_client.client)
        # TODO : errors handling
        api_response = api_instance.users_service_search_users()
        all_users = api_response.records
        

        for user in all_users:
            user_access_roles = self._fetch_secret_permissions(secret_instance, user)
            yield from user_access_roles

    def _fetch_secret_permissions(self, api_instance: SecretPermissionsApi, user: UserModel) -> Iterable[SecretPermissionSummary]:
        return self.__get_paginated_results(api_instance, user)

    def __get_paginated_results(self, api_instance:SecretPermissionsApi, user: UserModel) -> Iterable[SecretPermissionSummary]:
        cur_skip = 0
        has_next = True
        while (has_next) :
            api_response = api_instance.secret_permissions_service_search_secret_permissions(filter_user_id=normalize_id(user.id),skip = normalize_id(cur_skip))
            has_next = api_response.has_next
            cur_skip += int(api_response.next_skip)
            yield from api_response.records
