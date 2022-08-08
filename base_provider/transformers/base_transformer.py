"""Base transformer with standard configuration"""
from logging import getLogger
from typing import Iterable

from authomize.rest_api_client.generated.schemas import (
    NewAccountsAssociationRequestSchema,
    NewAssetsInheritanceRequestSchema,
    NewAssetsRequestSchema,
    NewGroupingRequestSchema,
    NewGroupingsAssociationRequestSchema,
    NewIdentityRequestSchema,
    NewPermissionsRequestSchema,
    NewUserRequestSchema,
    RequestsBundleSchema,
    NewPrivilegesRequestSchema,
    NewPrivilegeGrantsRequestSchema,
)

from base_provider.configuration.base_shared_configuration import BaseSharedConfiguration
from base_provider.models.base_shared_memory import BaseSharedMemory

logger = getLogger(__name__)


class BaseTransformer:
    def __init__(
        self,
        shared_memory: BaseSharedMemory,
        shared_configuration: BaseSharedConfiguration,
    ) -> None:
        """Init with standard configuration"""
        self.shared_memory = shared_memory
        self.shared_configuration = shared_configuration

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
        logger.info(
            "Starting transformer: {transformer_name}",
            extra=dict(
                params=dict(
                    transformer_name=self.transformer_name,
                )
            ),
        )
        for idx, item in enumerate(self.transform_models(extracted_raw_data)):
            yield item
            if (idx + 1) % self.log_every_n_raw_items == 0:
                logger.info(
                    "Transforming in progess: {transformer_name} with {count} items so far",
                    extra=dict(
                        params=dict(
                            transformer_name=self.transformer_name,
                            count=(idx + 1),
                        )
                    ),
                )

        logger.info(
            "Transfomer done: {transformer_name} with {count} items",
            extra=dict(
                params=dict(
                    transformer_name=self.transformer_name,
                    count=idx,
                )
            ),
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
