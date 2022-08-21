from typing import Tuple, Type

from bamboohr_provider.clients.bamboohr_client import BamboohrClient
from bamboohr_provider.configuration.client_configuration import BamboohrClientConfiguration
from bamboohr_provider.extractors.users_extractor import UsersExtractor
from bamboohr_provider.models.shared_memory import BamboohrProviderSharedMemory
from bamboohr_provider.transformers.users_transformer import UsersTransformer
from base_provider.extractors.base_extractor import BaseExtractor
from base_provider.transformers.base_transformer import BaseTransformer
from base_provider.workflows.base_auto_runner import BaseAutoProviderRunner


class BamboohrRunner(BaseAutoProviderRunner):
    def get_extractor_and_transformer_type_list(
        self,
    ) -> list[Tuple[Type[BaseExtractor], Type[BaseTransformer]]]:
        return [
            (UsersExtractor, UsersTransformer),
        ]

    def create_client(self) -> BamboohrClient:
        client_configuration: BamboohrClientConfiguration = self.client_configuration  # type: ignore
        return BamboohrClient(
            client_configuration=client_configuration,
        )

    def create_shared_memory(self) -> BamboohrProviderSharedMemory:
        return BamboohrProviderSharedMemory()
