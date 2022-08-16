from typing import Dict, Iterator

from base_provider.extractors.base_extractor import BaseExtractor
from teams_provider.clients.microsoft_client import MicrosoftClient
from teams_provider.models.shared_memory import TeamsProviderSharedMemory


class ChannelsExtractor(BaseExtractor):
    """
    Gets a list of channels
    See
    """

    def extract_raw(self) -> Iterator[Dict]:
        data_provider_client: MicrosoftClient = self.data_provider_client  # type: ignore
        shared_memory: TeamsProviderSharedMemory = self.shared_memory  # type: ignore
        teams = shared_memory.teams
        team_to_channels = shared_memory.team_to_channels

        for team in teams:
            for channel in data_provider_client.client.get_all_items(
                'teams/{}/channels'.format(team),
            ):
                team_to_channels[team] = team_to_channels.get(team, []) + [channel['id']]
                yield channel
