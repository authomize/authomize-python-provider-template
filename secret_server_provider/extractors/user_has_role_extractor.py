from typing import Iterable

from secret_server_openapiclient.apis import UsersApi
from secret_server_openapiclient.model.role_summary import RoleSummary
from secret_server_openapiclient.model.user_model import UserModel

from base_provider.extractors.base_extractor import BaseExtractor
from secret_server_provider.clients.secret_server_client import SecretServerClient
from secret_server_provider.normalize_id import normalize_id


class UserHasRoleExtractor(BaseExtractor):
    """
    Gets a list of Role records.
    """

    def extract_raw(self) -> Iterable[tuple[UserModel,RoleSummary]]:
        data_provider_client: SecretServerClient = self.data_provider_client
        api_instance = UsersApi(data_provider_client.client)

        api_response = api_instance.users_service_search_users()
        all_users = api_response.records
        return self._get_all_user_roles(api_instance, all_users)
    
    def _get_all_user_roles (self, api_instance: UsersApi, all_users: Iterable[UserModel]) -> Iterable[tuple[UserModel,RoleSummary]]:
        for user in all_users:
            for roleRecord in self._fetch_user_roles(api_instance, user):
                yield (user,roleRecord) 
            
    def _fetch_user_roles(self, api_instance: UsersApi, user: UserModel) -> Iterable[RoleSummary]:
        return self.__get_paginated_results(api_instance, user)
        
    def __get_paginated_results(self, api_instance:UsersApi, user: UserModel) -> Iterable[RoleSummary]:
        cur_skip = 0
        has_next = True
        while (has_next) :
            api_response = api_instance.users_service_get_roles(id=normalize_id(user.id),skip = normalize_id(cur_skip))
            has_next = api_response.has_next
            cur_skip += int(api_response.next_skip)
            yield from api_response.records

