from typing import Iterable

import jcapiv2
from jcapiv2 import PolicyResult
from onelogin.api.models.role import Role

from jumpcloud_provider.extractors.jumpcloud_extractor import JumpcloudExtractor
from onelogin_provider.clients.onelogin_client import OneloginClient


class RolesExtractor(JumpcloudExtractor):
    """
    Gets a list of Role resources.

    See https://developers.onelogin.com/api-docs/1/roles/get-roles Get Roles documentation
        https://developers.onelogin.com/api-docs/2/roles/list-roles
    """

    def extract_raw(self) -> Iterable[Role]:
        client_v2 = self.jumpcloud_client.client_v2
        jcapiv2.PoliciesApi(client_v2).policyresults_list()
        data_provider_client: OneloginClient = self.data_provider_client  # type: ignore
        return data_provider_client.client.get_roles()
