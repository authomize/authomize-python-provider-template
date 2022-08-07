from logging import getLogger
from typing import Iterable

from base_provider.clients.base_client import BaseClient
from base_provider.configuration.base_shared_configuration import BaseSharedConfiguration

logger = getLogger(__name__)


class BaseExtractor:
    def __init__(
        self,
        data_provider_client: BaseClient,
        shared_configuration: BaseSharedConfiguration,
    ) -> None:
        self.data_provider_client = data_provider_client
        self.shared_configuration = shared_configuration

    @property
    def extractor_name(self):
        return type(self).__name__

    def extact_raw(self) -> Iterable[dict]:
        raise NotImplementedError()

    def __call__(self) -> Iterable[dict]:
        logger.info(
            "Starting extraction: {extractor_name}",
            extra=dict(params=dict(
                extractor_name=self.extractor_name,
            )),
        )
        for idx, result in enumerate(self.extact_raw()):
            yield result
            if idx % self.log_every_n_raw_items == 0:
                logger.info(
                    "Extraction in progess: {extractor_name} with {count} items so far",
                    extra=dict(params=dict(
                        extractor_name=self.extractor_name,
                        count=idx,
                    )),
                )

        logger.info(
            "Extraction done: {extractor_name} with {count} items",
            extra=dict(params=dict(
                extractor_name=self.extractor_name,
                count=idx,
            )),
        )

    @property
    def log_every_n_raw_items(self):
        return self.shared_configuration.log_extactor_every_n_raw_items
