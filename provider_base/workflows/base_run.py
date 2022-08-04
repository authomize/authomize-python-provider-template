from typing import Iterable

from authomize.rest_api_client.generated.schemas import RequestsBundleSchema

from provider_base.configuration.application_configuration import ApplicationConfiguration
from provider_base.configuration.authomize_api_configuration import AuthomizeApiConfiguration
from provider_base.configuration.base_data_provider_configuration import (
    BaseDataProviderConfiguration,
)
from provider_base.configuration.general_configuration import GeneralConfiguration
from provider_base.loaders.basic_loader import BasicLoader


class BaseRunWorkflow:
    def __init__(
        self,
        authomize_api_configuration: AuthomizeApiConfiguration,
        data_provider_configuration: BaseDataProviderConfiguration,
        application_configuration: ApplicationConfiguration,
        general_configuration: GeneralConfiguration,
    ) -> None:
        self.authomize_api_configuration = authomize_api_configuration
        self.data_provider_configuration = data_provider_configuration
        self.application_configuration = application_configuration
        self.general_configuration = general_configuration

    def run(self):
        loader = BasicLoader(
            authomize_api_configuration=self.authomize_api_configuration,
            application_configuration=self.application_configuration,
            general_configuration=self.general_configuration,
        )
        transfomed_data = self.get_transformed_data()
        loader.load_all(transfomed_data)

    def get_transformed_data(self) -> Iterable[RequestsBundleSchema]:
        pass
