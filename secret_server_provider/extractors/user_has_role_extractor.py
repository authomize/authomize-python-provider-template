from typing import Iterable

from secret_server_openapiclient.apis import UsersApi
from secret_server_openapiclient.model.role_summary import RoleSummary
from secret_server_openapiclient.model.user_model import UserModel

from base_provider.extractors.base_extractor import BaseExtractor
from secret_server_provider.clients.secret_server_client import SecretServerClient
from secret_server_provider.paginator import get_paginated_results, get_paginated_results_by_id


class UserHasRoleExtractor(BaseExtractor):
    """
    Gets a list of Role records.
    """

    def extract_raw(self) -> Iterable[tuple[UserModel, RoleSummary]]:
        data_provider_client: SecretServerClient = self.data_provider_client
        api_instance = UsersApi(data_provider_client.openapi_client)

        all_users = get_paginated_results(api_instance.users_service_search_users)
        return self._get_all_user_roles(api_instance, all_users)

    def _get_all_user_roles(self, api_instance: UsersApi,
                            all_users: Iterable[UserModel]) -> Iterable[tuple[UserModel, RoleSummary]]:
        for user in all_users:
            user_roles = get_paginated_results_by_id(user.id, api_instance.users_service_get_roles)
            for role_record in user_roles:
                yield (user, role_record)
