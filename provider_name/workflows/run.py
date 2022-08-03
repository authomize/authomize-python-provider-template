from itertools import chain
from typing import Iterable
from authomize.rest_api_client.generated.schemas import ItemsBundleSchema
from provider_name.clients.data_provider_client import DataProviderClient
from provider_name.configuration.authomize_api_configuration import AuthomizeApiConfiguration
from provider_name.configuration.data_provider_configuration import DataProviderConfiguration
from provider_name.configuration.application_configuration import ApplicationConfiguration
from provider_name.extractors.files_extractor import FilesExtactor

from provider_name.loaders.united_loader import UnitedLoader
from provider_name.models.shared_memory import SharedMemory
from provider_name.transformers.files_transformer import FilesTransformer

class RunWorkflow:
    def __init__(
        self,
        authomize_api_configuration: AuthomizeApiConfiguration,
        data_provider_configuration: DataProviderConfiguration,
        application_configuration: ApplicationConfiguration
    ) -> None:
        self.authomize_api_configuration = authomize_api_configuration
        self.data_provider_configuration = data_provider_configuration
        self.application_configuration = application_configuration

    def run(self):
        loader = UnitedLoader(
            authomize_api_configuration=self.authomize_api_configuration,
            application_configuration=self.application_configuration,
        )
        transfomed_data = self.get_transformed_data()
        loader.load_all(transfomed_data)

    def get_transformed_data(self) -> Iterable[ItemsBundleSchema]:
        client = DataProviderClient(
            data_provider_configuration=self.data_provider_configuration,
        )
        shared_memory = SharedMemory()
        return chain([
            FilesTransformer(shared_memory).transform_models(FilesExtactor(client).extact_raw()),
        ])