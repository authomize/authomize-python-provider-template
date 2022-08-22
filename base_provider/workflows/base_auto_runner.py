from typing import Iterable, Tuple, Type

from authomize.rest_api_client.generated.schemas import RequestsBundleSchema

from base_provider.clients.base_client import BaseClient
from base_provider.extractors.base_extractor import BaseExtractor
from base_provider.models.base_shared_memory import BaseSharedMemory
from base_provider.transformers.base_transformer import BaseTransformer
from base_provider.workflows.base_runner import BaseProviderRunner


class BaseAutoProviderRunner(BaseProviderRunner):
    def get_extractor_and_transformer_type_list(
        self,
    ) -> list[Tuple[Type[BaseExtractor], Type[BaseTransformer]]]:
        raise NotImplementedError()

    def create_client(self) -> BaseClient:
        raise NotImplementedError()

    def create_shared_memory(self) -> BaseSharedMemory:
        return BaseSharedMemory()

    def get_transformed_data(self) -> Iterable[RequestsBundleSchema]:
        print ("moooooo!!!\n")
        data_provider_client = self.create_client()
        shared_memory = self.create_shared_memory()
        print ("=====moooooo 2 =====!!!\n")
        print (self.get_extractor_and_transformer_type_list())
        for extractor_type, transformer_type in self.get_extractor_and_transformer_type_list():
            print ("=====moooooo 3 =====!!!\n")
            transfomr = transformer_type(
                shared_memory=shared_memory,
                shared_configuration=self.shared_configuration,
            )
            print ("=====moooooo 4 =====!!!\n")
            extractor = extractor_type(
                data_provider_client=data_provider_client,
                shared_memory=shared_memory,
                shared_configuration=self.shared_configuration,
            )
            print ("=====moooooo 5 =====!!!\n")
            yield from transfomr(extractor())
