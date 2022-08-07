from base_provider import DataProviderClient


class MockProviderClient(DataProviderClient):
    def is_alive(self) -> bool:
        return True

    def me(self) -> dict:
        return {}
