from typing import Tuple

from authomize.rest_api_client.client import Client

from base_provider.configuration.authomize_api_configuration import AuthomizeApiConfiguration
from base_provider.configuration.base_data_provider_configuration import (
    BaseDataProviderConfiguration,
)


class BaseProviderHealthChecker:
    def __init__(
        self,
        authomize_api_configuration: AuthomizeApiConfiguration,
        data_provider_configuration: BaseDataProviderConfiguration,
    ) -> None:
        self.authomize_api_client = Client(
            auth_token=authomize_api_configuration.auth_token,
            base_url=authomize_api_configuration.api_url,
        )
        self.data_provider_configuration = data_provider_configuration

    def is_configuration_defined(self) -> bool:
        return True

    def can_connect_to_authomize(self) -> bool:
        return self.authomize_api_client.is_alive().isAlive

    def can_write_to_authomize(self) -> bool:
        return self.authomize_api_client.me()

    def can_connect_to_data_provider(self) -> bool:
        raise NotImplementedError()

    def can_read_from_data_provider(self) -> bool:
        raise NotImplementedError()

    def is_healthy(self) -> bool:
        health, explanation = self._is_healthy()
        return health

    def raise_unhealthy(self):
        health, explanation = self._is_healthy()
        if not health:
            raise ValueError(explanation)

    def _is_healthy(self) -> Tuple[bool, str]:
        if not self.is_configuration_defined():
            return False, "Configuration is courrupted"
        if not self.can_connect_to_authomize():
            return False, "Cannot access Authomize"
        if not self.can_write_to_authomize():
            return False, "Cannot update authomize"
        if not self.can_connect_to_data_provider():
            return False, "Cannot access data provider"
        if not self.can_read_from_data_provider():
            return False, "Cannot read from data provider"
        return True, "Ready!"
