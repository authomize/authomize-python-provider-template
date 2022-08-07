"""Base extractor with standard configuration"""
from logging import getLogger
from typing import Iterable

from base_provider.clients.base_client import BaseClient
from base_provider.configuration.base_shared_configuration import BaseSharedConfiguration
from base_provider.models.base_shared_memory import BaseSharedMemory

logger = getLogger(__name__)


class BaseExtractor:
    """
    Wrapper for a simple extractor

    The extractor should be very simple and should not try to shape the data, only
    call relevant api routes

    `extact_raw` function should be overwritten
    the default data that returns is dict, but can be anything as long it is shared
    between the extractor and the relevant transformer

    Should be independent from other extractors - an extractor cannot call another extractor.
    In rare cases, this can be ignored be passing small amount of data with `shared_memory`.
    """
    def __init__(
        self,
        data_provider_client: BaseClient,
        shared_memory: BaseSharedMemory,
        shared_configuration: BaseSharedConfiguration,
    ) -> None:
        """Init with standard configuration"""
        self.data_provider_client = data_provider_client
        self.shared_memory = shared_memory
        self.shared_configuration = shared_configuration

    def extact_raw(self) -> Iterable[dict]:
        """
        Extract all items from source system

        Should be overwritten

        Should handle:
        * pagination
        * rate-limit
        Should prefer to use generators (yield) over lists
        """
        raise NotImplementedError()

    @property
    def extractor_name(self):
        """Extractor name. Used in logs"""
        return type(self).__name__

    def __call__(self) -> Iterable[dict]:
        """
        Extract all items from source system

        This function wraps `extact_raw` with logs
        """
        logger.info(
            "Starting extraction: {extractor_name}",
            extra=dict(params=dict(
                extractor_name=self.extractor_name,
            )),
        )
        total = 0
        for idx, result in enumerate(self.extact_raw()):
            yield result
            total += 1
            if (idx + 1) % self.log_every_n_raw_items == 0:
                self._log_progress(idx + 1)

        logger.info(
            "Extraction done: {extractor_name} with {count} items",
            extra=dict(params=dict(
                extractor_name=self.extractor_name,
                count=total,
            )),
        )

    @property
    def log_every_n_raw_items(self) -> int:
        """After how many items should we log progress"""
        return self.shared_configuration.extactor_logs_every_n_raw_items

    def _log_progress(self, count: int):
        logger.info(
            "Extraction in progess: {extractor_name} with {count} items so far",
            extra=dict(params=dict(
                extractor_name=self.extractor_name,
                count=count,
            )),
        )
