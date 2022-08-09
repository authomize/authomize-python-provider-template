from base_provider.clients.base_client import BaseClient


class MockProviderClient(BaseClient):
    def is_alive(self) -> bool:
        return True

    def me(self) -> dict:
        return {}
