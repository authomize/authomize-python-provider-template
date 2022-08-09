"""Configuration for connecting to authomize api"""
from pydantic import BaseSettings, Field


class AuthomizeApiConfiguration(BaseSettings):
    """
    Configuration for connecting to authomize api

    Should not be overwritten
    """
    auth_token: str = Field(..., env="AUTHOMIZE_API_TOKEN")
    api_url: str = Field(..., env="AUTHOMIZE_API_URL")
