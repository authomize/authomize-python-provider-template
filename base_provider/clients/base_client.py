"""Base client with standard configuration"""

from base_provider.configuration.base_client_configuration import BaseClientConfiguration


class BaseClient:
    """
    Wrapper for a third-party client

    Should be overwritten

    Sub classes should include:
    * Auth methods
    * Calls / Wrapped calls to relevant APIs used by extractors
    """
    def __init__(
        self,
        client_configuration: BaseClientConfiguration,
    ) -> None:
        """Init with standard configuration"""
        self.client_configuration = client_configuration
