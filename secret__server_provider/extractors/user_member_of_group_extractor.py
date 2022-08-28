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
        return self._get_all_user_groups(api_instance, all_users)
    
    def _get_all_user_groups (self, api_instance: UsersApi, all_users: Iterable[UserModel]) -> Iterable[GroupUserSummary]:
        for user in all_users:
            yield from self._fetch_user_groups(api_instance, user)
    def _fetch_user_groups(self, api_instance: UsersApi, user: UserModel) -> Iterable[GroupUserSummary]:
        return self.__get_paginated_results(api_instance, user)
        
    def __get_paginated_results(self, api_instance:UsersApi, user: UserModel) -> Iterable[UserModel]:
        cur_skip = 0
        has_next = True
        while (has_next) :
            api_response = api_instance.users_service_get_user_groups(id=normalize_id(user.id),skip = normalize_id(cur_skip))
            has_next = api_response.has_next
            cur_skip += int(api_response.next_skip)
            yield from api_response.records

