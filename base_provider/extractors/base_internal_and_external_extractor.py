"""Base extractor with standard configuration"""

import structlog

from base_provider.clients.base_client import BaseClient
from base_provider.configuration.base_shared_configuration import BaseSharedConfiguration
from base_provider.extractors.base_extractor import BaseExtractor
from base_provider.models.base_shared_memory import BaseSharedMemory
from secret_server_provider.clients.simple_http_client import SimpleHttpClient

logger = structlog.get_logger()


class BaseInternalAndExternalExtractor(BaseExtractor):
    """
    Wrapper for a simple extractor with http_client
    """

    def __init__(
        self,
        data_provider_client: BaseClient,
        shared_memory: BaseSharedMemory,
        shared_configuration: BaseSharedConfiguration,
    ) -> None:
        super().__init__(data_provider_client, shared_memory, shared_configuration)
        self.http_client = SimpleHttpClient(data_provider_client.client_configuration)

