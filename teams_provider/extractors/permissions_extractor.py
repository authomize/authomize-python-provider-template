from typing import Iterator, Dict

from authomize.core.concurrent import ConcurrentTaskRunner

from base_provider.extractors.base_extractor import BaseExtractor


class PermissionsExtractor(BaseExtractor):
    """
    Gets a list of Role resources.

    See
    """

    def extract_raw(self) -> Iterator[Dict]:
        data_provider_client: MicrosoftClient = self.data_provider_client  # type: ignore
        shared_memory: TeamsProviderSharedMemory = self.shared_memory  # type: ignore
        teams = shared_memory.teams

        task_runner = ConcurrentTaskRunner(max_workers=10)
        task_results = task_runner.task_map(
            data_provider_client.client.get_one_item,
            ['teams/{}'.format(team) for team in teams]
        )
        for result in task_results:
            yield from result
