from typing import cast, Iterable, Callable

from base_provider.clients.base_client import BaseClient
from base_provider.configuration.base_shared_configuration import BaseSharedConfiguration
from base_provider.extractors.base_extractor import BaseExtractor
from base_provider.models.base_shared_memory import BaseSharedMemory
from jumpcloud_provider.clients.jumpcloud_client import JumpcloudClient
from jumpcloud_provider.configuration.client_configuration import JumpcloudClientConfiguration
from jumpcloud_provider.configuration.shared_configuration import JumpcloudSharedConfiguration
from jumpcloud_provider.extractors import JumpcloudApiResult
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

    def extract_with_pagination(self, api: Callable[[int], JumpcloudApiResult]) -> Iterable[dict]:
        skip = 0
        limit = self.client_configuration.limit
        batch_count = self.client_configuration.limit  # for the first iteration

        while not limit > batch_count:
            batch_data_list = api(skip)
            list_results = getattr(batch_data_list, "results", batch_data_list)
            batch_count = len(list_results)
            skip += batch_count
            yield from list_results
