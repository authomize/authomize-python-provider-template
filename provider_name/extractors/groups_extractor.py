from typing import Iterable
from provider_name.extractors.base_extactor import BaseExtractor


class GroupsExtactor(BaseExtractor):
    def extact_raw(self) -> Iterable[dict]:
        # for item in self.data_provider_client.list_groups():
            # yield item
        pass
