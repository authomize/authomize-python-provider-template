import logging
import sys
from typing import Any, Iterable, List

import structlog
from authomize.rest_api_client.generated.schemas import RequestsBundleSchema

from base_provider.configuration.application_configuration import ApplicationConfiguration
from base_provider.configuration.authomize_api_configuration import AuthomizeApiConfiguration
from base_provider.configuration.base_client_configuration import BaseClientConfiguration
from base_provider.configuration.base_shared_configuration import BaseSharedConfiguration
from base_provider.loaders.basic_loader import BasicLoader

DEFAULT_FORMAT = '%(asctime)s [%(levelname)s] %(name)s - %(message)s'

logger = structlog.get_logger()


class BaseProviderRunner:
    def __init__(
        self,
        authomize_api_configuration: AuthomizeApiConfiguration,
        client_configuration: BaseClientConfiguration,
        application_configuration: ApplicationConfiguration,
        shared_configuration: BaseSharedConfiguration,
    ) -> None:
        self.authomize_api_configuration = authomize_api_configuration
        self.client_configuration = client_configuration
        self.application_configuration = application_configuration
        self.shared_configuration = shared_configuration
        self._init_logger()

    def run(self):
        logger.info("Starting provider")
        loader = BasicLoader(
            authomize_api_configuration=self.authomize_api_configuration,
            application_configuration=self.application_configuration,
            shared_configuration=self.shared_configuration,
        )
        transformed_data = self.get_transformed_data()
        loader(transformed_data)
        logger.info("Provider done")

    def get_transformed_data(self) -> Iterable[RequestsBundleSchema]:
        pass

    def _init_logger(
        self,
        level=logging.INFO,
        json: bool = False,
        log_format=DEFAULT_FORMAT,
    ):
        timestamper = structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S")
        shared_processors: List[Any] = [
            structlog.stdlib.add_log_level,
            structlog.stdlib.add_logger_name,
            # Add extra attributes of LogRecord objects to the event dictionary
            # so that values passed in the extra parameter of log methods pass
            # through to log output.
            structlog.stdlib.ExtraAdder(),
            structlog.processors.format_exc_info,
            timestamper,
        ]

        structlog.configure(
            processors=shared_processors + [
                # Prepare event dict for `ProcessorFormatter`.
                structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
            ],
            logger_factory=structlog.stdlib.LoggerFactory(),
        )

        renderer: Any = structlog.processors.JSONRenderer() if json else structlog.dev.ConsoleRenderer()
        formatter = structlog.stdlib.ProcessorFormatter(
            # These run ONLY on `logging` entries that do NOT originate within
            # structlog.
            foreign_pre_chain=shared_processors,
            # These run on ALL entries after the pre_chain is done.
            processors=[
                # Remove _record & _from_structlog.
                structlog.stdlib.ProcessorFormatter.remove_processors_meta,
                renderer,
            ],
        )

        handler = logging.StreamHandler()
        # Use OUR `ProcessorFormatter` to format all `logging` entries.
        handler.setFormatter(formatter)
        root_logger = logging.getLogger()
        root_logger.addHandler(handler)
        root_logger.setLevel(level)

        sys.excepthook = self.handle_exception
        logging.captureWarnings(capture=True)
        self.configure_common_loggers()

    @staticmethod
    def configure_common_loggers():
        # charset_normalizer is noisy when using requests (directly and indirectly)
        logging.getLogger('charset_normalizer').setLevel('WARNING')

    @staticmethod
    def handle_exception(exc_type, exc_value, exc_traceback):
        """Handle all exceptions"""
        # Handle Ctrl-C as usual in terminal
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return

        logger.critical("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))
