from typing import Dict, List

from base_provider.models.base_shared_memory import BaseSharedMemory


class TeamsProviderSharedMemory(BaseSharedMemory):
    def __init__(self) -> None:
        super().__init__()
        self.team_ids: List[str] = []
        self.team_id_to_channel_ids: Dict[str, str] = {}
