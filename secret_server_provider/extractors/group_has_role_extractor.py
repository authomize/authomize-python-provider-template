from typing import Iterable

from secret_server_openapiclient.apis import GroupsApi
from secret_server_openapiclient.model.group_model import GroupModel
from secret_server_openapiclient.model.role_summary import RoleSummary
from secret_server_openapiclient.model.user_model import UserModel

from base_provider.extractors.base_extractor import BaseExtractor
from secret_server_provider.clients.secret_server_client import SecretServerClient
from secret_server_provider.paginator import get_paginated_results, get_paginated_results_by_id


class GroupHasRoleExtractor(BaseExtractor):
    """
    Gets a list of Role records.
    """

    def extract_raw(self) -> Iterable[tuple[UserModel, RoleSummary]]:
        data_provider_client: SecretServerClient = self.data_provider_client
        api_instance = GroupsApi(data_provider_client.openapi_client)

        all_groups = get_paginated_results(api_instance.groups_service_search)
        return self._get_all_group_roles(api_instance, all_groups)

    def _get_all_group_roles(self, api_instance: GroupsApi,
                             all_groups: Iterable[GroupModel]) -> Iterable[tuple[GroupModel, RoleSummary]]:
        for group in all_groups:
            group_roles = get_paginated_results_by_id(group.id, api_instance.groups_service_get_roles)
            for role_record in group_roles:
                yield (group, role_record)
