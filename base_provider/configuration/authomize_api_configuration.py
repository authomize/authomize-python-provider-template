from pydantic import BaseModel


class AuthomizeApiConfiguration(BaseModel):
    auth_token: str
    api_url: str
