from base_provider import BaseClient


class MockProviderClient(BaseClient):
    def is_alive(self) -> bool:
        return True

    def me(self) -> dict:
        return {}
