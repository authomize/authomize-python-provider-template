from typing import Iterable

from authomize.rest_api_client.client import Client
from authomize.rest_api_client.generated.schemas import RequestsBundleSchema

from provider_base.configuration.application_configuration import ApplicationConfiguration
from provider_base.configuration.authomize_api_configuration import AuthomizeApiConfiguration
from provider_base.configuration.general_configuration import GeneralConfiguration


class BasicLoader:
    def __init__(
        self,
        authomize_api_configuration: AuthomizeApiConfiguration,
        application_configuration: ApplicationConfiguration,
        general_configuration: GeneralConfiguration,
    ) -> None:
        self.authomize_api_client = Client(
            auth_token=authomize_api_configuration.auth_token,
            base_url=authomize_api_configuration.api_url,
        )
        self.application_configuration = application_configuration
        self.general_configuration = general_configuration

    def load_all(self, items: Iterable[RequestsBundleSchema]):
        self.authomize_api_client.delete_app_data(
            app_id=self.application_configuration.app_id,
        )
        batch = []
        for item in items:
            batch.append(item)
            if len(items) == self.general_configuration:
                self.load_batch(batch)
                batch = []
        if batch:
            self.load_batch(batch)

    def load_batch(self, items: list[RequestsBundleSchema]):
        merged = self.merge_buntle_schemas(items)
        if merged.new_users:
            self.authomize_api_client.create_users(
                app_id=self.application_configuration.app_id,
                body=merged.new_users,
            )
        if merged.new_groupings:
            self.authomize_api_client.create_groupings(
                app_id=self.application_configuration.app_id,
                body=merged.new_groupings,
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
