from pydantic import BaseModel


class MemberAssociation(BaseModel):
    member_id: str
