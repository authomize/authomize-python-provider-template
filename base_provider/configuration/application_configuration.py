"""Configuration for exsiting authomize application"""
from pydantic import BaseModel


class ApplicationConfiguration(BaseModel):
    """
    Configuration for exsiting authomize application

    Should not be overwritten
    """
    app_id: str
