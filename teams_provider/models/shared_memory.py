from base_provider.models.base_shared_memory import BaseSharedMemory


class TeamsProviderSharedMemory(BaseSharedMemory):
    def __init__(self) -> None:
        super().__init__()
        self.teams = []
        self.team_to_channels = {}
