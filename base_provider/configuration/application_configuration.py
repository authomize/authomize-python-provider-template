"""Configuration for exsiting authomize application"""
from pydantic import BaseSettings, Field


class ApplicationConfiguration(BaseSettings):
    """
    Configuration for exsiting authomize application

    Should not be overwritten
    """
    app_id: str = Field(..., env="AUTHOMIZE_API_APP_ID")
