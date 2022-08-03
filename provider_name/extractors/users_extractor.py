from typing import Iterable
from provider_name.extractors.base_extactor import BaseExtractor


class UsersExtactor(BaseExtractor):
    def extact_raw(self) -> Iterable[dict]:
        # for item in self.data_provider_client.list_users():
            # yield item
        pass
