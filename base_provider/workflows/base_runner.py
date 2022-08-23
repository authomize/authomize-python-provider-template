from typing import Iterable

import structlog
from authomize.rest_api_client.generated.schemas import RequestsBundleSchema

from base_provider.configuration.application_configuration import ApplicationConfiguration
from base_provider.configuration.authomize_api_configuration import AuthomizeApiConfiguration
from base_provider.configuration.base_client_configuration import BaseClientConfiguration
from base_provider.configuration.base_shared_configuration import BaseSharedConfiguration
from base_provider.loaders.basic_loader import BasicLoader

DEFAULT_FORMAT = '%(asctime)s [%(levelname)s] %(name)s - %(message)s'

logger = structlog.get_logger()


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
        self.logger = logger.bind(loader_name=self.loader_name)

    @property
    def loader_name(self):
        return type(self).__name__

    def run(self):
        self.logger.info("Starting provider")
        loader = BasicLoader(
            authomize_api_configuration=self.authomize_api_configuration,
            application_configuration=self.application_configuration,
            shared_configuration=self.shared_configuration,
        )
        transformed_data = self.get_transformed_data()
        loader(transformed_data)
        self.logger.info("Provider done")

    def get_transformed_data(self) -> Iterable[RequestsBundleSchema]:
        pass
