from typing import Iterable

from provider_base.extractors.base_extactor import BaseExtractor


class GroupsExtactor(BaseExtractor):
    def extact_raw(self) -> Iterable[dict]:
        # yield from [
        #     {
        #         "name": "Admin",
        #     },
        #     {
        #         "name": "Reader",
        #     }
        # ]
        pass
