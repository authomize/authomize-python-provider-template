from typing import List

from pydantic import BaseModel

from jumpcloud_provider.models.user_association import UserAssociation
from jumpcloud_provider.models.user_group_association import UserGroupAssociation


class ApplicationAssociations(BaseModel):
    id: str
    name: str
    user_associations: List[UserAssociation]
    user_group_associations: List[UserGroupAssociation]
