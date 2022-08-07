from typing import Iterable

from onelogin.api.models.role import Role

from base_provider.extractors.base_extactor import Extractor
from onelogin_provider.clients.onelogin_client import OneloginClient


class RolesExtactor(Extractor):
    """
    Gets a list of Role resources.

    See https://developers.onelogin.com/api-docs/1/roles/get-roles Get Roles documentation
        https://developers.onelogin.com/api-docs/2/roles/list-roles
    """

    def extact_raw(self) -> Iterable[Role]:
        data_provider_client: OneloginClient = self.data_provider_client  # type: ignore
        return data_provider_client.client.get_roles()
