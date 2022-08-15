from typing import Iterable

import jcapiv2

from jumpcloud_provider.extractors.jumpcloud_extractor import JumpcloudExtractor
from jumpcloud_provider.models.group_members_association import GroupMembersAssociation


class GroupsExtractor(JumpcloudExtractor):
    """
    Gets a list of Group resources
    See https://github.com/TheJumpCloud/jcapi-python/blob/master/jcapiv2/jcapiv2/api/groups_api.py
        https://github.com/TheJumpCloud/jcapi-python/blob/master/jcapiv2/jcapiv2/api/system_groups_api.py
    """

    def extract_raw(self) -> Iterable[GroupMembersAssociation]:
        client_configuration = self.client_configuration
        client_v2 = self.jumpcloud_client.client_v2
        groups_client = jcapiv2.GroupsApi(client_v2)
        system_groups_client = jcapiv2.UserGroupsApi(client_v2)
        groups = groups_client.groups_list(
            accept=client_configuration.accept,
            content_type=client_configuration.content_type
        )

        results = []

        for group in groups:
            members = system_groups_client.graph_user_group_members_list(
                group_id=group.id,
                accept=client_configuration.accept,
                content_type=client_configuration.content_type
            )
            group_members_assoc = GroupMembersAssociation(
                id=group.id,
                name=group.name,
                members=members
            )
            results.append(group_members_assoc)

        return results
