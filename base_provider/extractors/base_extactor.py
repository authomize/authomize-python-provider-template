from typing import Iterable

from base_provider.clients.base_data_provider_client import DataProviderClient


class Extractor:
    def __init__(
        self,
        data_provider_client: DataProviderClient,
    ) -> None:
        self.data_provider_client = data_provider_client

    def __call__(self) -> Iterable[dict]:
        for result in self.extact_raw():
            return result

    def extact_raw(self) -> Iterable[dict]:
        raise NotImplementedError()
