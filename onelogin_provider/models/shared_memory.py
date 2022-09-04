from typing import Set

from base_provider.models.base_shared_memory import BaseSharedMemory


class OneloginProviderSharedMemory(BaseSharedMemory):
    def __init__(self) -> None:
        super().__init__()
        self.saved_const_models_ids: Set[str] = set()
