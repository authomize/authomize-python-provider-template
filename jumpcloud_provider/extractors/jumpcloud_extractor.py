from itertools import chain
from typing import cast, Iterable, Callable

from base_provider.clients.base_client import BaseClient
from base_provider.configuration.base_shared_configuration import BaseSharedConfiguration
from base_provider.extractors.base_extractor import BaseExtractor
from base_provider.models.base_shared_memory import BaseSharedMemory
from jumpcloud_provider.clients.jumpcloud_client import JumpcloudClient
from jumpcloud_provider.configuration.client_configuration import JumpcloudClientConfiguration
from jumpcloud_provider.configuration.shared_configuration import JumpcloudSharedConfiguration
from jumpcloud_provider.extractors.jumpcloud_pagination import JumpcloudPagination
from jumpcloud_provider.models.shared_memory import JumpcloudProviderSharedMemory


class JumpcloudExtractor(BaseExtractor):
    jumpcloud_client: JumpcloudClient
    client_configuration: JumpcloudClientConfiguration
    jumpcloud_shared_memory: JumpcloudProviderSharedMemory

    def __init__(
            self,
            data_provider_client: BaseClient,
            shared_memory: BaseSharedMemory,
            shared_configuration: BaseSharedConfiguration,
    ) -> None:
        super(JumpcloudExtractor, self).__init__(
            shared_memory=shared_memory,
            data_provider_client=data_provider_client,
            shared_configuration=shared_configuration
        )
        shared_configuration = cast(JumpcloudSharedConfiguration, self.shared_configuration)
        self.client_configuration = shared_configuration.client_configuration
        self.jumpcloud_client = cast(JumpcloudClient, self.data_provider_client)
        self.jumpcloud_shared_memory = cast(JumpcloudProviderSharedMemory, shared_memory)

    def extract_raw(self) -> Iterable[dict]:
        pass

    def extract_with_pagination(self, api: Callable[[int], JumpcloudPagination]) -> chain:
        list_of_data: JumpcloudPagination = api(0)

        return self._extract_tail_data(list_of_data, api)

    def _extract_tail_data(self, list_of_data: JumpcloudPagination, api: Callable[[int], JumpcloudPagination]) -> chain:
        total_count = list_of_data.total_count
        list_results = list_of_data.results
        count = len(list_results)
        yield from list_results

        while count < total_count:
            batch_data_list = api(count)
            list_results = batch_data_list.results
            count += len(list_results)
            yield from list_results
