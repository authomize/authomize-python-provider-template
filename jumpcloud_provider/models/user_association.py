from pydantic import BaseModel


class UserAssociation(BaseModel):
    user_id: str
