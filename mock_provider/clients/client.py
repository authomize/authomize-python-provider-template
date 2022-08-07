from base_provider import BaseDataProviderClient


class MockProviderClient(BaseDataProviderClient):
    def is_alive(self) -> bool:
        return True

    def me(self) -> dict:
        return {}
