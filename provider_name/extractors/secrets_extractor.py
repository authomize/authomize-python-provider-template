from typing import Iterable

from provider_base.extractors.base_extactor import BaseExtractor


class SecretsExtactor(BaseExtractor):
    def extact_raw(self) -> Iterable[dict]:
        # for item in self.data_provider_client.list_secrets():
            # yield item
        pass
