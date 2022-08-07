"""Configuration for connecting to third party api"""
from pydantic import BaseModel


class BaseClientConfiguration(BaseModel):
    """
    Configuration for connecting to authomize api

    Should be overwritten

    Should include auth details
    """
    pass
