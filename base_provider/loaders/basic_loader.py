from typing import Iterable

import structlog
from authomize.rest_api_client.client import Client
from authomize.rest_api_client.generated.schemas import (
    NewAccountsAssociationResponseSchema,
    NewPrivilegesGrantsListRequestSchema,
    NewGroupingsListRequestSchema,
    NewGroupingsAssociationsListRequestSchema,
    NewPermissionsListRequestSchema,
    NewIdentitiesListRequestSchema,
    NewUsersListRequestSchema,
    RequestsBundleSchema,
)

from base_provider.configuration.application_configuration import ApplicationConfiguration
from base_provider.configuration.authomize_api_configuration import AuthomizeApiConfiguration
from base_provider.configuration.base_shared_configuration import BaseSharedConfiguration
from base_provider.transformers.base_transformer import BaseTransformer

logger = structlog.get_logger()


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
        self.logger = logger.bind(loader_name=self.loader_name)

    @property
    def loader_name(self):
        return type(self).__name__

    def __call__(self, items: Iterable[RequestsBundleSchema]):
        self.logger.info("Starting loader")
        self.load_all(items)
        self.logger.info("Loading done")

    def load_all(self, items: Iterable[RequestsBundleSchema]):
        app_id = self.application_configuration.app_id
        self.logger.info(
            f"Loading progress: Delete old data: {app_id}",
            app_id=app_id,
        )

        self.authomize_api_client.delete_app_data(
            app_id=self.application_configuration.app_id,
        )
        merged_bundle = BaseTransformer.create_bundle()
        for item in items:
            merged_bundle = self.merge_bundle_schemas(items=[merged_bundle, item])
            self.load_bundle(bundle=merged_bundle)
        self.load_bundle(bundle=merged_bundle, load_all=True)

    def load_bundle(self, bundle: RequestsBundleSchema, load_all: bool = False):
        if bundle.new_users and (
            load_all or len(bundle.new_users) >= self.shared_configuration.loader_batch_size
        ):
            self.authomize_api_client.create_users(
                app_id=self.application_configuration.app_id,
                body=NewUsersListRequestSchema(data=bundle.new_users),
            )
        if bundle.new_groupings and (
            load_all or len(bundle.new_groupings) >= self.shared_configuration.loader_batch_size
        ):
            self.authomize_api_client.create_groupings(
                app_id=self.application_configuration.app_id,
                body=NewGroupingsListRequestSchema(data=bundle.new_groupings),
            )
        if bundle.new_privileges and (
            load_all or len(bundle.new_privileges) >= self.shared_configuration.loader_batch_size
        ):
            self.authomize_api_client.create_privileges(
                app_id=self.application_configuration.app_id,
                body=bundle.new_privileges,
            )
        if bundle.new_assets and (
            load_all or len(bundle.new_assets) >= self.shared_configuration.loader_batch_size
        ):
            self.authomize_api_client.create_assets(
                app_id=self.application_configuration.app_id,
                body=bundle.new_assets,
            )
        if bundle.new_identities and (
            load_all or len(bundle.new_identities) >= self.shared_configuration.loader_batch_size
        ):
            self.authomize_api_client.create_identities(
                app_id=self.application_configuration.app_id,
                body=NewIdentitiesListRequestSchema(data=bundle.new_identities),
            )
        if bundle.new_permissions and (
            load_all or len(bundle.new_permissions) >= self.shared_configuration.loader_batch_size
        ):
            self.authomize_api_client.create_permissions(
                app_id=self.application_configuration.app_id,
                body=NewPermissionsListRequestSchema(data=bundle.new_permissions),
            )
        if bundle.new_privileges_grants and (
            load_all
            or len(bundle.new_privileges_grants) >= self.shared_configuration.loader_batch_size
        ):
            self.authomize_api_client.create_privileges_grants(
                app_id=self.application_configuration.app_id,
                body=NewPrivilegesGrantsListRequestSchema(data=bundle.new_privileges_grants),
            )
        if bundle.new_accounts_association and (
            load_all
            or len(bundle.new_accounts_association) >= self.shared_configuration.loader_batch_size
        ):
            self.authomize_api_client.create_accounts_association(
                app_id=self.application_configuration.app_id,
                body=NewAccountsAssociationResponseSchema(data=bundle.new_accounts_association),
            )
        if bundle.new_groupings_association and (
            load_all
            or len(bundle.new_groupings_association) >= self.shared_configuration.loader_batch_size
        ):
            self.authomize_api_client.create_groupings_association(
                app_id=self.application_configuration.app_id,
                body=NewGroupingsAssociationsListRequestSchema(data=bundle.new_groupings_association),
            )
        if bundle.new_assets_inheritance and (
            load_all
            or len(bundle.new_assets_inheritance) >= self.shared_configuration.loader_batch_size
        ):
            self.authomize_api_client.create_assets_inheritance(
                app_id=self.application_configuration.app_id,
                body=bundle.new_assets_inheritance,
            )

    @staticmethod
    def merge_bundle_schemas(items: list[RequestsBundleSchema]) -> RequestsBundleSchema:
        new_users = []
        new_groupings = []
        new_permissions = []
        new_privileges = []
        new_privileges_grants = []
        new_accounts_association = []
        new_groupings_association = []
        new_assets = []
        new_assets_inheritance = []
        new_identities = []
        for item in items:
            if item.new_users:
                new_users.extend(item.new_users)
            if item.new_groupings:
                new_groupings.extend(item.new_groupings)
            if item.new_permissions:
                new_permissions.extend(item.new_permissions)
            if item.new_privileges:
                new_privileges.extend(item.new_privileges)
            if item.new_privileges_grants:
                new_privileges_grants.extend(item.new_privileges_grants)
            if item.new_accounts_association:
                new_accounts_association.extend(item.new_accounts_association)
            if item.new_groupings_association:
                new_groupings_association.extend(item.new_groupings_association)
            if item.new_assets:
                new_assets.extend(item.new_assets)
            if item.new_assets_inheritance:
                new_assets_inheritance.extend(item.new_assets_inheritance)
            if item.new_identities:
                new_identities.extend(item.new_identities)
        return RequestsBundleSchema(
            new_users=new_users,
            new_groupings=new_groupings,
            new_permissions=new_permissions,
            new_privileges=new_privileges,
            new_privileges_grants=new_privileges_grants,
            new_accounts_association=new_accounts_association,
            new_groupings_association=new_groupings_association,
            new_assets=new_assets,
            new_assets_inheritance=new_assets_inheritance,
            new_identities=new_identities,
        )
