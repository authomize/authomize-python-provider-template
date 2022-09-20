from typing import Iterator, Dict

from base_provider.extractors.base_extractor import BaseExtractor
from teams_provider.clients.microsoft_client import MicrosoftClient
from teams_provider.models.shared_memory import TeamsProviderSharedMemory


class TeamsExtractor(BaseExtractor):
    """
    Gets a list of Teams in the organization.
    See https://learn.microsoft.com/en-us/graph/teams-list-all-teams
    """

    def extract_raw(self) -> Iterator[Dict]:
        data_provider_client: MicrosoftClient = self.data_provider_client  # type: ignore
        shared_memory: TeamsProviderSharedMemory = self.shared_memory  # type: ignore

        teams = data_provider_client.client.get_all_items(
            'groups',
            params={'filter': "resourceProvisioningOptions/Any(x:x eq 'Team')"}
        )
        for team in teams:
            shared_memory.team_ids.append(team['id'])
            yield team
