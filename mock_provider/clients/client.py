from base_provider.clients.base_data_provider_client import DataProviderClient


class MockProviderClient(DataProviderClient):
    def is_alive(self) -> bool:
        return True

    def me(self) -> dict:
        return {}
