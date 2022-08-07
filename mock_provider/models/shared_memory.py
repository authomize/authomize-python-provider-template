from base_provider.models.base_shared_memory import ProviderSharedMemory


class MockProviderSharedMemory(ProviderSharedMemory):
    def __init__(self, domain: str) -> None:
        self.domain = domain
