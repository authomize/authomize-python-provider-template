from typing import Iterable

from onelogin.api.models.group import Group

from onelogin_provider.clients.onelogin_client import OneloginClient
from provider_base.extractors.base_extactor import BaseExtractor


class GroupsExtactor(BaseExtractor):
    """
    Gets a list of Group resources
    See https://developers.onelogin.com/api-docs/1/groups/get-groups Get Groups documentation
    """

    def extact_raw(self) -> Iterable[Group]:
        data_provider_client: OneloginClient = self.data_provider_client
        return data_provider_client.client.get_groups()
