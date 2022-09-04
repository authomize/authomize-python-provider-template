from typing import Iterable, List, Tuple

from onelogin.api.models.privilege import Privilege

from base_provider.extractors.base_extractor import BaseExtractor
from onelogin_provider.clients.onelogin_client import OneloginClient


class PrivilegesExtractor(BaseExtractor):
    """
    Gets a list of privilege resources.
    Note: Is not working and shouldn't be used now (Because the API is not working)
    For every privilege, get roles ids that are assigned to it
    And also get users ids that are assigned to it

    See https://developers.onelogin.com/api-docs/1/privileges/list-privileges
        https://developers.onelogin.com/api-docs/1/privileges/get-roles
        https://developers.onelogin.com/api-docs/1/privileges/get-users
    """

    def extract_raw(self) -> Iterable[Tuple[Privilege, List[int], List[int]]]:
        data_provider_client: OneloginClient = self.data_provider_client  # type: ignore
        privileges: Iterable[Privilege] = data_provider_client.client.get_privileges()
        for privilege in privileges:
            assigned_role_ids: List[int] = list(
                data_provider_client.client.get_roles_assigned_to_privilege(privilege_id=privilege.id),
            )
            assigned_user_ids: List[int] = list(
                data_provider_client.client.get_users_assigned_to_privilege(privilege_id=privilege.id),
            )
            yield (privilege, assigned_role_ids, assigned_user_ids)
