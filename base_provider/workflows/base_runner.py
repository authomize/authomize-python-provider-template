import logging
import sys
from datetime import datetime
from typing import Iterable

from authomize.rest_api_client.generated.schemas import RequestsBundleSchema
from pythonjsonlogger import jsonlogger

from base_provider.configuration.application_configuration import ApplicationConfiguration
from base_provider.configuration.authomize_api_configuration import AuthomizeApiConfiguration
from base_provider.configuration.base_client_configuration import BaseClientConfiguration
from base_provider.configuration.base_shared_configuration import BaseSharedConfiguration
from base_provider.loaders.basic_loader import BasicLoader

DEFAULT_FORMAT = '%(asctime)s [%(levelname)s] %(name)s - %(message)s'
DEFAULT_JSON_FORMAT = '%(timestamp)s %(level)s %(name)s %(message)s'
DEFAULT_DATE_FORMAT = '%Y-%m-%dT%H:%M:%S%z'

logger = logging.getLogger(__name__)


class JsonFormatter(jsonlogger.JsonFormatter):
    """Default json formatter"""

    def add_fields(self, log_record, record, message_dict):
        """Add default fields to each log record"""
        if hasattr(record, 'params'):
            record.message = record.message.format(**record.params)
        super().add_fields(log_record, record, message_dict)
        timestamp = datetime.fromtimestamp(record.created)
        log_record['timestamp'] = timestamp.strftime(DEFAULT_DATE_FORMAT)
        log_record['level'] = record.levelname


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
        logger.info(
            "Starting provider",
            extra=dict(params=dict()),
        )
        loader = BasicLoader(
            authomize_api_configuration=self.authomize_api_configuration,
            application_configuration=self.application_configuration,
            shared_configuration=self.shared_configuration,
        )
        transformed_data = self.get_transformed_data()
        loader(transformed_data)
        logger.info(
            "Provider done",
            extra=dict(params=dict()),
        )

    def get_transformed_data(self) -> Iterable[RequestsBundleSchema]:
        pass

    def _init_logger(
        self,
        level=logging.INFO,
        json: bool = True,
        log_format=DEFAULT_FORMAT,
        date_format=DEFAULT_DATE_FORMAT,
    ):
        console_handler = logging.StreamHandler(sys.stdout)
        if json:
            console_handler.setFormatter(JsonFormatter(DEFAULT_JSON_FORMAT))
        else:
            console_handler.setFormatter(logging.Formatter(log_format, date_format))
        logging.root.handlers = [console_handler]

        logging.root.setLevel(level)
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
