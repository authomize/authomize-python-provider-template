from typing import Iterable

from onelogin.api.models.group import Group

from base_provider.extractors.base_extractor import BaseExtractor
from onelogin_provider.clients.onelogin_client import OneloginClient


class GroupsExtractor(BaseExtractor):
    """
    Gets a list of Group resources
    See https://developers.onelogin.com/api-docs/1/groups/get-groups Get Groups documentation
    """

    def extract_raw(self) -> Iterable[Group]:
        data_provider_client: OneloginClient = self.data_provider_client  # type: ignore
        return data_provider_client.client.get_groups()
