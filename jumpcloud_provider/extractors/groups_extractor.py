from typing import Iterable, cast

from jcapiv2 import GraphConnection, GroupsApi, UserGroupsApi, Group, ApiClient

from jumpcloud_provider.extractors import JumpcloudApiResult
from jumpcloud_provider.extractors.jumpcloud_extractor import JumpcloudExtractor
from jumpcloud_provider.models.group_members_association import GroupMembersAssociation
from jumpcloud_provider.models.member_association import MemberAssociation


class GroupsExtractor(JumpcloudExtractor):
    """
    Gets a list of Group resources
    See https://github.com/TheJumpCloud/jcapi-python/blob/master/jcapiv2/jcapiv2/api/groups_api.py
        https://github.com/TheJumpCloud/jcapi-python/blob/master/jcapiv2/jcapiv2/api/system_groups_api.py
    """

    def extract_raw(self) -> Iterable[GroupMembersAssociation]:
        client_v2 = self.jumpcloud_client.client_v2
        groups = self._get_groups(client_v2)
        return self._associate_members_to_group(groups, client_v2)

    def _get_groups(self, jumpcloud_client: ApiClient) -> Iterable[Group]:
        groups_api = GroupsApi(jumpcloud_client)
        groups = self.extract_with_pagination(self._call_groups_api(groups_api))
        return cast(Iterable[Group], groups)

    def _call_groups_api(self, groups_api: GroupsApi) -> JumpcloudApiResult:
        client_configuration = self.client_configuration
        return lambda skip: groups_api.groups_list(
            skip=skip,
            limit=client_configuration.limit,
            accept=client_configuration.accept,
            content_type=client_configuration.content_type
        )

    def _call_user_groups_api(self, group_id: str, users_groups_api: UserGroupsApi) -> JumpcloudApiResult:
        client_configuration = self.client_configuration
        return lambda skip: users_groups_api.graph_user_group_members_list(
            skip=skip,
            group_id=group_id,
            limit=client_configuration.limit,
            accept=client_configuration.accept,
            content_type=client_configuration.content_type
        )

    def _associate_members_to_group(
            self,
            groups: Iterable[Group],
            jumpcloud_client: ApiClient
    ) -> Iterable[GroupMembersAssociation]:
        users_groups_api = UserGroupsApi(jumpcloud_client)
        for group in groups:
            api = self._call_user_groups_api(group.id, users_groups_api)
            members = cast(Iterable[GraphConnection], self.extract_with_pagination(api))
            members_association = [MemberAssociation(member_id=member.to.id) for member in members]
            yield GroupMembersAssociation(
                id=group.id,
                name=group.name,
                members=members_association
            )
