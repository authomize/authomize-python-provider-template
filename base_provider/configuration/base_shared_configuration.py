"""Configuration for running the connector"""
from pydantic import BaseModel


class BaseSharedConfiguration(BaseModel):
    """
    Configuration for running the connector

    Should be overwritten, but existing configures should not get replaced

    Can include any flags for code-flow mgmt
    """

    loader_batch_size: int = 100
    extractor_logs_every_n_raw_items: int = 100
    transformer_logs_every_n_raw_items: int = 100
