from base_provider.workflows.base_health_checker import BaseProviderHealthChecker


class SecretServerHealthChecker(BaseProviderHealthChecker):
    def can_connect_to_data_provider(self) -> bool:
        return self.can_read_from_data_provider()

    def can_read_from_data_provider(self) -> bool:
        # client_configuration: SecretServerConfiguration = self.client_configuration  # type: ignore
        # client = SecretServerClient(
        #     client_configuration=client_configuration,
        # )
        # client.client.get_users(limit=1)
        return True
