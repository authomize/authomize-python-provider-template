from collections import defaultdict
from typing import Dict, Iterator

from base_provider.extractors.base_extractor import BaseExtractor
from teams_provider.clients.microsoft_client import MicrosoftClient
from teams_provider.models.shared_memory import TeamsProviderSharedMemory


class ChannelsExtractor(BaseExtractor):
    """
    Gets a list of channels
    See https://docs.microsoft.com/en-us/graph/api/channel-list?view=graph-rest-1.0&tabs=http
    TODO - potentially replace with listAllChannels
        (https://docs.microsoft.com/en-us/graph/api/team-list-allchannels?view=graph-rest-1.0&tabs=http)
        To also get channels shared with team (needs an additional permission).
    """

    def extract_raw(self) -> Iterator[Dict]:
        data_provider_client: MicrosoftClient = self.data_provider_client  # type: ignore
        shared_memory: TeamsProviderSharedMemory = self.shared_memory  # type: ignore
        team_id_to_channel_ids = defaultdict(list)

        for team in shared_memory.team_ids:
            for channel in data_provider_client.client.get_all_items(
                'teams/{}/channels'.format(team),
            ):
                team_id_to_channel_ids[team].append(channel['id'])
                yield channel

        shared_memory.team_id_to_channel_ids = dict(team_id_to_channel_ids)
