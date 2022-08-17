from typing import Iterable

from jcapiv2 import PoliciesApi
from onelogin.api.models.role import Role

from jumpcloud_provider.extractors.jumpcloud_extractor import JumpcloudExtractor


class RolesExtractor(JumpcloudExtractor):
    """
    Gets a list of Role resources.

    See https://developers.onelogin.com/api-docs/1/roles/get-roles Get Roles documentation
        https://developers.onelogin.com/api-docs/2/roles/list-roles
    """

    def extract_raw(self) -> Iterable[Role]:
        client_v2 = self.jumpcloud_client.client_v2
        policy_apy = PoliciesApi(client_v2)
        return policy_apy.policyresults_list("", content_type="", accept="")
