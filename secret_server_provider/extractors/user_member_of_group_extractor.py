from typing import Iterable

from secret_server_openapiclient.apis import UsersApi
from secret_server_openapiclient.model.group_user_summary import GroupUserSummary
from secret_server_openapiclient.model.user_model import UserModel

from base_provider.extractors.base_extractor import BaseExtractor
from secret_server_provider.clients.secret_server_client import SecretServerClient
from secret_server_provider.paginator import get_paginated_results, get_paginated_results_by_id

class UserMemberOfGroupExtractor(BaseExtractor):
    """
    Gets a list of User records.

    See docs/UsersApi.md#users_service_search_users
    """

    def extract_raw(self) -> Iterable[GroupUserSummary]:
        data_provider_client: SecretServerClient = self.data_provider_client
        api_instance = UsersApi(data_provider_client.openapi_client)

        all_users = get_paginated_results(api_instance.users_service_search_users)
        return self._get_all_user_groups(api_instance, all_users)

    def _get_all_user_groups(self,
                             api_instance: UsersApi,
                             all_users: Iterable[UserModel]) -> Iterable[GroupUserSummary]:
        for user in all_users:
            yield from self._fetch_user_groups(api_instance, user)

    def _fetch_user_groups(self, api_instance: UsersApi, user: UserModel) -> Iterable[GroupUserSummary]:
        return get_paginated_results_by_id(user.id, api_instance.users_service_get_user_groups)

