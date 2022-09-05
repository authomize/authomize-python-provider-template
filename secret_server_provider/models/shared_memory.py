from base_provider.models.base_shared_memory import BaseSharedMemory


class SecretServerProviderSharedMemory(BaseSharedMemory):

    def __init__(self) -> None:
        self.existing_privileges_ids_set = set()
        self.non_system_role_ids_set = set()
