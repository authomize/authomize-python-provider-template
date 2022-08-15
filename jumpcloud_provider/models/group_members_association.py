from typing import List

from jcapiv2 import GraphConnection
from pydantic import BaseModel


class GroupMembersAssociation(BaseModel):
    id: str
    name: str
    members: List[GraphConnection]
