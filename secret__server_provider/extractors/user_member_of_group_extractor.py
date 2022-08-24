from typing import Iterable

from base_provider.extractors.base_extractor import BaseExtractor
from secret__server_provider.clients.secret_server_client import SecretServerClient
from secret__server_provider.normalize_id import normalize_id

from ..openapi_client.plugins.apis import UsersApi
from ..openapi_client.plugins.model.group_user_summary import GroupUserSummary
from ..openapi_client.plugins.model.user_model import UserModel


class UserMemberOfGroupExtractor(BaseExtractor):
    """
    Gets a list of User records.

    See docs/UsersApi.md#users_service_search_users
    """

    def extract_raw(self) -> Iterable[GroupUserSummary]:
        data_provider_client: SecretServerClient = self.data_provider_client
        api_instance = UsersApi(data_provider_client.client)

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
            user_groups = self._fetch_user_groups(api_instance, user)
            yield from user_groups

    def _fetch_user_groups(self, api_instance: UsersApi, user: UserModel) -> Iterable[GroupUserSummary]:
        return api_instance.users_service_get_user_groups(id=normalize_id(user.id)).records
