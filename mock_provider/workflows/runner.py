from typing import Tuple, Type

from base_provider.extractors.base_extractor import BaseExtractor
from base_provider.transformers.base_transformer import BaseTransformer
from base_provider.workflows.base_auto_runner import BaseAutoProviderRunner
from mock_provider.clients.client import MockProviderClient
from mock_provider.configuration.client_configuration import MockProviderClientConfiguration
from mock_provider.extractors.files_extractor import FilesExtractor
from mock_provider.models.shared_memory import MockProviderSharedMemory
from mock_provider.transformers.files_transformer import FilesTransformer


class MockProviderRunner(BaseAutoProviderRunner):
    def get_extractor_and_transformer_type_list(
        self,
    ) -> list[Tuple[Type[BaseExtractor], Type[BaseTransformer]]]:
        return [
            (FilesExtractor, FilesTransformer),
        ]

    def create_client(self) -> MockProviderClient:
        client_configuration: MockProviderClientConfiguration = self.client_configuration  # type: ignore
        return MockProviderClient(
            client_configuration=client_configuration,
        )

    def create_shared_memory(self) -> MockProviderSharedMemory:
        client_configuration: MockProviderClientConfiguration = self.client_configuration  # type: ignore
        return MockProviderSharedMemory(
            domain=client_configuration.domain,
        )
