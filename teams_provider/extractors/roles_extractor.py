from typing import Iterator, Dict

from authomize.core.concurrent import ConcurrentTaskRunner

from base_provider.extractors.base_extractor import BaseExtractor


class RolesExtractor(BaseExtractor):
    """
    Gets a list of Role resources.

    See
    """

    def extract_raw(self) -> Iterator[Dict]:
        data_provider_client: MicrosoftClient = self.data_provider_client  # type: ignore
        shared_memory: TeamsProviderSharedMemory = self.shared_memory  # type: ignore
        teams = shared_memory.teams
        team_to_channels = shared_memory.team_to_channels

        task_runner = ConcurrentTaskRunner(max_workers=10)
        team_task_results = task_runner.task_map(
            data_provider_client.client.get_all_items,
            ['teams/{}/members'.format(team) for team in teams]
        )
        channel_task_results = task_runner.task_map(
            data_provider_client.client.get_all_items,
            ['teams/{}/channels/{}/members'.format(team, channel)
             for team in teams for channel in team_to_channels[team]]
        )
        for result in team_task_results:
            yield from result
        for result in channel_task_results:
            yield from result
