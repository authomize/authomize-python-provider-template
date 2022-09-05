from secret_server_openapiclient.api.users_api import UsersApi

from base_provider.workflows.base_health_checker import BaseProviderHealthChecker
from secret_server_provider.clients.secret_server_client import SecretServerClient
from secret_server_provider.configuration.client_configuration import SecretServerConfiguration


class SecretServerHealthChecker(BaseProviderHealthChecker):
    def can_connect_to_data_provider(self) -> bool:
        return self.can_read_from_data_provider()

    def can_read_from_data_provider(self) -> bool:
        client_configuration: SecretServerConfiguration = self.client_configuration  # type: ignore
        client = SecretServerClient(
            client_configuration=client_configuration,
        )

        users = UsersApi(client.openapi_client).users_service_search_users().records
        return bool(users)
