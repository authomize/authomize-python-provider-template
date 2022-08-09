"""Base transformer with standard configuration"""
from typing import Iterable

import structlog
from authomize.rest_api_client.generated.schemas import (
    NewAccountsAssociationRequestSchema,
    NewAssetsInheritanceRequestSchema,
    NewAssetsRequestSchema,
    NewGroupingRequestSchema,
    NewGroupingsAssociationRequestSchema,
    NewIdentityRequestSchema,
    NewPermissionsRequestSchema,
    NewPrivilegeGrantsRequestSchema,
    NewPrivilegesRequestSchema,
    NewUserRequestSchema,
    RequestsBundleSchema,
)

from base_provider.configuration.base_shared_configuration import BaseSharedConfiguration
from base_provider.models.base_shared_memory import BaseSharedMemory

logger = structlog.get_logger()


class BaseTransformer:
    def __init__(
        self,
        shared_memory: BaseSharedMemory,
        shared_configuration: BaseSharedConfiguration,
    ) -> None:
        """Init with standard configuration"""
        self.shared_memory = shared_memory
        self.shared_configuration = shared_configuration
        self.logger = logger.bind(transformer_name=self.transformer_name)

    @property
    def transformer_name(self):
        """
        Transformer name.

        Used in logs
        """
        return type(self).__name__

    def validate_item_schema(self, raw_item: dict) -> bool:
        """ """
        raise NotImplementedError()

    def transform_model(self, raw_item: dict) -> RequestsBundleSchema:
        raise NotImplementedError()

    def __call__(
        self,
        extracted_raw_data: Iterable[dict],
    ) -> Iterable[RequestsBundleSchema]:
        self.logger.info(
            "Starting transformer",
            transformer_name=self.transformer_name,
        )
        idx = -1
        for idx, item in enumerate(self.transform_models(extracted_raw_data)):
            yield item
            item_count = idx + 1
            if item_count % self.log_every_n_raw_items == 0:
                self.logger.info(
                    f"Transforming in progess with {item_count} items so far",
                    count=item_count,
                )

        item_count = idx + 1
        self.logger.info(
            f"Transfomer done with {item_count} items",
            count=item_count,
        )

    def transform_models(
        self,
        extracted_raw_data: Iterable[dict],
    ) -> Iterable[RequestsBundleSchema]:
        for raw_item in extracted_raw_data:
            if not self.validate_item_schema(raw_item):
                # Can continue as well if we prefer to ignore "damaged data"
                raise ValueError("Item not validated")
            yield self.transform_model(raw_item)

    @staticmethod
    def create_bundle(
        new_users: list[NewUserRequestSchema] = None,
        new_groupings: list[NewGroupingRequestSchema] = None,
        new_permissions: list[NewPermissionsRequestSchema] = None,
        new_privileges: list[NewPrivilegesRequestSchema] = None,
        new_privileges_grants: list[NewPrivilegeGrantsRequestSchema] = None,
        new_accounts_association: list[NewAccountsAssociationRequestSchema] = None,
        new_groupings_association: list[NewGroupingsAssociationRequestSchema] = None,
        new_assets: list[NewAssetsRequestSchema] = None,
        new_assets_inheritance: list[NewAssetsInheritanceRequestSchema] = None,
        new_identities: list[NewIdentityRequestSchema] = None,
    ) -> RequestsBundleSchema:
        """Create bundle with everything by default set as empty list"""
        return RequestsBundleSchema(
            new_users=new_users or [],
            new_groupings=new_groupings or [],
            new_permissions=new_permissions or [],
            new_privileges=new_privileges or [],
            new_privileges_grants=new_privileges_grants or [],
            new_accounts_association=new_accounts_association or [],
            new_groupings_association=new_groupings_association or [],
            new_assets=new_assets or [],
            new_assets_inheritance=new_assets_inheritance or [],
            new_identities=new_identities or [],
        )

    @property
    def log_every_n_raw_items(self):
        """Every how many items should we log the progress"""
        return self.shared_configuration.transformer_logs_every_n_raw_items
