from base_provider import ProviderSharedMemory


class MockProviderSharedMemory(ProviderSharedMemory):
    def __init__(self, domain: str) -> None:
        self.domain = domain
