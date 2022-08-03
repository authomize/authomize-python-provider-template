from typing import Iterable
from provider_name.clients.data_provider_client import DataProviderClient


class BaseExtractor:
    def __init__(
        self,
        data_provider_client: DataProviderClient
    ) -> None:
        self.data_provider_client = data_provider_client
    
    def extact_raw(self) -> Iterable[dict]:
        pass
