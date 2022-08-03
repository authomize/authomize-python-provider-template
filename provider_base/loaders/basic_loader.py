from typing import Iterable

from authomize.rest_api_client.client import Client
from authomize.rest_api_client.generated.schemas import ItemsBundleSchema

from provider_base.configuration.application_configuration import \
    ApplicationConfiguration
from provider_base.configuration.authomize_api_configuration import \
    AuthomizeApiConfiguration


class BasicLoader:
    def __init__(
        self,
        authomize_api_configuration: AuthomizeApiConfiguration,
        application_configuration: ApplicationConfiguration,
    ) -> None:
        self.authomize_api_client = Client(
            auth_token=authomize_api_configuration.auth_token,
            base_url=authomize_api_configuration.api_url,
        )

    def load_all(self, items: Iterable[ItemsBundleSchema]):
        pass

    def load_batch(self, items: list[ItemsBundleSchema]):
        pass
