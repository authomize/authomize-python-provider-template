from typing import Dict

from base_provider.models.base_shared_memory import BaseSharedMemory


class JumpcloudProviderSharedMemory(BaseSharedMemory):
    groups_members: Dict[str, object]

    def __init__(self) -> None:
        super().__init__()
        self.groups_members = {}

