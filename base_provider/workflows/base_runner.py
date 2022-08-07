from logging import getLogger
from typing import Iterable

from authomize.rest_api_client.generated.schemas import RequestsBundleSchema

from base_provider.configuration.application_configuration import ApplicationConfiguration
from base_provider.configuration.authomize_api_configuration import AuthomizeApiConfiguration
from base_provider.configuration.base_client_configuration import BaseClientConfiguration
from base_provider.configuration.base_shared_configuration import BaseSharedConfiguration
from base_provider.loaders.basic_loader import BasicLoader

logger = getLogger(__name__)


class BaseProviderRunner:
    def __init__(
        self,
        authomize_api_configuration: AuthomizeApiConfiguration,
        client_configuration: BaseClientConfiguration,
        application_configuration: ApplicationConfiguration,
        shared_configuration: BaseSharedConfiguration,
    ) -> None:
        self.authomize_api_configuration = authomize_api_configuration
        self.client_configuration = client_configuration
        self.application_configuration = application_configuration
        self.shared_configuration = shared_configuration

    def run(self):
        logger.info(
            "Starting provider",
            extra=dict(params=dict()),
        )
        loader = BasicLoader(
            authomize_api_configuration=self.authomize_api_configuration,
            application_configuration=self.application_configuration,
            shared_configuration=self.shared_configuration,
        )
        transfomed_data = self.get_transformed_data()
        loader(transfomed_data)
        logger.info(
            "Provider done",
            extra=dict(params=dict()),
        )

    def get_transformed_data(self) -> Iterable[RequestsBundleSchema]:
        pass
