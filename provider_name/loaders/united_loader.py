from authomize.rest_api_client.generated.schemas import ItemsBundleSchema
from authomize.rest_api_client.client import Client

from typing import Iterable
from provider_name.configuration.authomize_api_configuration import AuthomizeApiConfiguration


class UnitedLoader:
    def __init__(
        self,
        authomize_api_configuration: AuthomizeApiConfiguration,
    ) -> None:
        self.authomize_api_client = Client(
            auth_token=authomize_api_configuration.auth_token,
            base_url=authomize_api_configuration.api_url,
        )

    def load_all(self, items: Iterable[ItemsBundleSchema]):
        pass

    def load_batch(self, items: list[ItemsBundleSchema]):
        pass
