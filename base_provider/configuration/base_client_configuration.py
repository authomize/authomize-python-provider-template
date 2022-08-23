"""Configuration for connecting to third party api"""
from pydantic import BaseSettings


class BaseClientConfiguration(BaseSettings):
    """
    Configuration for connecting to authomize api

    Should be overwritten

    Should include auth details
    """

    pass
