"""Base extractor with standard configuration"""
from typing import Iterable

import structlog

from base_provider.clients.base_client import BaseClient
from base_provider.configuration.base_shared_configuration import BaseSharedConfiguration
from base_provider.models.base_shared_memory import BaseSharedMemory

logger = structlog.get_logger()


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
        self.logger = logger.bind(extractor_name=self.extractor_name)

    def extract_raw(self) -> Iterable[dict]:
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
        """
        Extractor name.

        Used in logs
        """
        return type(self).__name__

    def __call__(self) -> Iterable[dict]:
        """
        Extract all items from source system

        This function wraps `extact_raw` with logs
        """
        self.logger.info("Starting extraction")
        total = 0
        for result in self.extract_raw():
            yield result
            total += 1
            if total % self.log_every_n_raw_items == 0:
                self._log_progress(total)

        self.logger.info(f"Extraction done with {total} items", count=total)

    @property
    def log_every_n_raw_items(self) -> int:
        """Every how many items should we log the progress"""
        return self.shared_configuration.extractor_logs_every_n_raw_items

    def _log_progress(self, count: int):
        self.logger.info(
            f"Extraction in progess with {count} items so far",
            count=count,
        )
