from typing import Iterable

from onelogin.api.models.role import Role

from base_provider.extractors.base_extractor import BaseExtractor
from onelogin_provider.clients.onelogin_client import OneloginClient


class RolesExtractor(BaseExtractor):
    """
    Gets a list of Role resources.

    See https://developers.onelogin.com/api-docs/1/roles/get-roles Get Roles documentation
        https://developers.onelogin.com/api-docs/2/roles/list-roles
    """

    def extract_raw(self) -> Iterable[Role]:
        data_provider_client: OneloginClient = self.data_provider_client  # type: ignore
        return data_provider_client.client.get_roles()
