from base_provider import BaseProviderSharedMemory


class MockProviderSharedMemory(BaseProviderSharedMemory):
    def __init__(self, domain: str) -> None:
        self.domain = domain
