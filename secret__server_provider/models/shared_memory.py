from base_provider.models.base_shared_memory import BaseSharedMemory


class SecretServerProviderSharedMemory(BaseSharedMemory):

    def __init__(self) -> None:
        self.existing_priveleges_set = set()
