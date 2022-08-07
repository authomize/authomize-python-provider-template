"""Configuration for connecting to authomize api"""
from pydantic import BaseModel


class AuthomizeApiConfiguration(BaseModel):
    """
    Configuration for connecting to authomize api

    Should not be overwritten
    """
    auth_token: str
    api_url: str
