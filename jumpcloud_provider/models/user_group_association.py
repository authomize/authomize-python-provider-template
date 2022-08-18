from pydantic import BaseModel


class UserGroupAssociation(BaseModel):
    group_id: str
