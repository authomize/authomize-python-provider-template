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
        '''
        TODO:make skip work later
        while (api_response.hasNext) :
            api_response = api_instance.users_service_search_users(skip = 10)
            all_users.extend(api_response.records())
        '''
        # TODO : run for earch user GET v1/users/<id>/groups to add to the user info
        # this will extract the groupName - differs from v1/groups which is actually v1/roles...
        # TODO : support pagination for groups too!
        for user in all_users:
            user_secret_permissions = self._fetch_secret_permissions(secret_instance, user)
            yield from user_secret_permissions

    def _fetch_secret_permissions(
        self,
        api_instance: SecretPermissionsApi,
        user: UserModel,
    ) -> Iterable[SecretPermissionSummary]:
        return api_instance.secret_permissions_service_search_secret_permissions(
            filter_user_id=normalize_id(user.id),
        ).records
