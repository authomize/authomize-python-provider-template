from base_provider.models.base_shared_memory import BaseProviderSharedMemory


class MockProviderSharedMemory(BaseProviderSharedMemory):
    def __init__(self, domain: str) -> None:
        self.domain = domain
