from base_provider.configuration.base_client_configuration import BaseClientConfiguration


class BaseClient:
    def __init__(
        self,
        client_configuration: BaseClientConfiguration,
    ) -> None:
        self.client_configuration = client_configuration
