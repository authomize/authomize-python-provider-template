from base_provider.models.base_shared_memory import BaseSharedMemory


class MockProviderSharedMemory(BaseSharedMemory):
    def __init__(self, domain: str) -> None:
        self.domain = domain
