from base_provider import BaseSharedMemory


class MockProviderSharedMemory(BaseSharedMemory):
    def __init__(self, domain: str) -> None:
        self.domain = domain
