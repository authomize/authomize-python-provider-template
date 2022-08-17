from typing import List

from pydantic import BaseModel

from jumpcloud_provider.models.member_association import MemberAssociation


class GroupMembersAssociation(BaseModel):
    id: str
    name: str
    members: List[MemberAssociation]
