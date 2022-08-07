from itertools import chain
from typing import Iterable

from authomize.rest_api_client.generated.schemas import RequestsBundleSchema

from base_provider import ProviderRunner
from mock_provider.clients.client import MockProviderClient
from mock_provider.configuration.configuration import MockProviderClientConfiguration
from mock_provider.extractors.files_extractor import FilesExtactor
from mock_provider.models.shared_memory import MockProviderSharedMemory
from mock_provider.transformers.files_transformer import FilesTransformer


class MockProviderRunner(ProviderRunner):

    def get_transformed_data(self) -> Iterable[RequestsBundleSchema]:
        general_configuration: MockProviderClientConfiguration = self.general_configuration  # type: ignore
        client = MockProviderClient(
            data_provider_client_configuration=self.data_provider_client_configuration,
        )
        shared_memory = MockProviderSharedMemory(
            domain=general_configuration.domain,
        )
        return chain([
            FilesTransformer(shared_memory)(
                FilesExtactor(client)(),
            ),
        ])
