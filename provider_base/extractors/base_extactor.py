from typing import Iterable

from provider_base.clients.base_data_provider_client import BaseDataProviderClient


class BaseExtractor:
    def __init__(
        self,
        data_provider_client: BaseDataProviderClient
    ) -> None:
        self.data_provider_client = data_provider_client

    def extact_raw(self) -> Iterable[dict]:
        raise NotImplementedError()
