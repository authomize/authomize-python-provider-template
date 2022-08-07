from json import loads
from logging import getLogger
from typing import Iterable

from authomize.rest_api_client.client import Client
from authomize.rest_api_client.generated.schemas import RequestsBundleSchema

from base_provider.configuration.application_configuration import ApplicationConfiguration
from base_provider.configuration.authomize_api_configuration import AuthomizeApiConfiguration
from base_provider.configuration.base_shared_configuration import BaseSharedConfiguration

logger = getLogger(__name__)


class BasicLoader:
    def __init__(
        self,
        authomize_api_configuration: AuthomizeApiConfiguration,
        application_configuration: ApplicationConfiguration,
        shared_configuration: BaseSharedConfiguration,
    ) -> None:
        """Init with standard configuration"""
        self.authomize_api_client = Client(
            auth_token=authomize_api_configuration.auth_token,
            base_url=authomize_api_configuration.api_url,
        )
        self.application_configuration = application_configuration
        self.shared_configuration = shared_configuration

    @property
    def loader_name(self):
        return type(self).__name__

    def __call__(self, items: Iterable[RequestsBundleSchema]):
        logger.info(
            "Starting loader: {loader_name}",
            extra=dict(params=dict(
                loader_name=self.loader_name,
            )),
        )
        self.load_all(items)
        logger.info(
            "Loading done: {loader_name}",
            extra=dict(params=dict(
                loader_name=self.loader_name,
            )),
        )

    def load_all(self, items: Iterable[RequestsBundleSchema]):
        logger.info(
            "Loading progress: Delete old data: {app_id}",
            extra=dict(params=dict(
                app_id=self.application_configuration.app_id,
            )),
        )
        self.authomize_api_client.delete_app_data(
            app_id=self.application_configuration.app_id,
        )
        batch = []
        for item in items:
            batch.append(item)
            if len(batch) == self.shared_configuration.loader_batch_size:
                self.load_batch(batch)
                batch = []
        if batch:
            self.load_batch(batch)

    def load_batch(self, items: list[RequestsBundleSchema]):
        merged = self.merge_buntle_schemas(items)
        if merged.new_users:
            self.authomize_api_client.create_users(
                app_id=self.application_configuration.app_id,
                body=[loads(item.json()) for item in merged.new_users],
            )
        if merged.new_groupings:
            self.authomize_api_client.create_groupings(
                app_id=self.application_configuration.app_id,
                body=[loads(item.json()) for item in merged.new_groupings],
            )
        logger.info(
            "Loading progress: Saving items to Authomize with {loader_name} on {app_id}",
            extra=dict(params=dict(
                loader_name=self.loader_name,
                app_id=self.application_configuration.app_id,
                new_users=len(merged.new_users or []),
                new_groupings=len(merged.new_groupings or []),
            )),
        )

    @staticmethod
    def merge_buntle_schemas(items: list[RequestsBundleSchema]) -> RequestsBundleSchema:
        new_users = []
        new_groupings = []
        for item in items:
            if item.new_users:
                new_users.extend(item.new_users)
            if item.new_groupings:
                new_groupings.extend(item.new_groupings)
        return RequestsBundleSchema(
            new_users=new_users,
            new_groupings=new_groupings,
        )
