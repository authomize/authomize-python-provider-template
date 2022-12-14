from authomize.rest_api_client.generated.schemas import (
    AssetType,
    GroupingType,
    NewAccountsAssociationRequestSchema,
    NewAssetRequestSchema,
    NewGroupingRequestSchema,
    NewPermissionRequestSchema,
    PermissionSourceType,
    RequestsBundleSchema,
)
from onelogin.api.models.role import Role

from base_provider.transformers.base_transformer import BaseTransformer
from onelogin_provider.models.const_models import ROLE_ADMIN_PRIVILEGE, USE_APP_PRIVILEGE
from onelogin_provider.models.shared_memory import OneloginProviderSharedMemory


class RolesTransformer(BaseTransformer):
    """
    Transform a list of Role resources.
    Creates a:
    * Role (Groupping)
    * Role -> App permission
    * User -> Role inhertiance
    * Admin -> Role permission (in this context the role is an asset)

    See https://developers.onelogin.com/api-docs/1/roles/get-roles Get Roles documentation
        https://developers.onelogin.com/api-docs/2/roles/list-roles
    """

    def validate_item_schema(self, raw_item: Role) -> bool:
        return True

    def transform_model(self, raw_item: Role) -> RequestsBundleSchema:
        shared_memory: OneloginProviderSharedMemory = self.shared_memory
        bundle = self.create_bundle()

        if USE_APP_PRIVILEGE.uniqueId not in shared_memory.saved_const_models_ids:
            shared_memory.saved_const_models_ids.add(USE_APP_PRIVILEGE.uniqueId)
            bundle.new_privileges.append(USE_APP_PRIVILEGE)

        if ROLE_ADMIN_PRIVILEGE.uniqueId not in shared_memory.saved_const_models_ids:
            shared_memory.saved_const_models_ids.add(ROLE_ADMIN_PRIVILEGE.uniqueId)
            bundle.new_privileges.append(ROLE_ADMIN_PRIVILEGE)

        role_id = raw_item.id
        new_role_group = NewGroupingRequestSchema(
            uniqueId=role_id,
            name=raw_item.name,
            originType="Role",
            type=GroupingType.Group,
            isRole=True,
        )
        bundle.new_groupings.append(new_role_group)

        new_role_asset = NewAssetRequestSchema(
            uniqueId=role_id,
            name=raw_item.name,
            originType="Role",
            type=AssetType.Other,
        )
        bundle.new_assets.append(new_role_asset)

        if raw_item.apps:
            for app_id in raw_item.apps:
                app_permission = NewPermissionRequestSchema(
                    sourceUniqueId=role_id,
                    sourceType=PermissionSourceType.Grouping,
                    assetId=app_id,
                    privilegeId=USE_APP_PRIVILEGE.uniqueId,
                )
                bundle.new_permissions.append(app_permission)

        if raw_item.users:
            for user_id in raw_item.users:
                association = NewAccountsAssociationRequestSchema(
                    sourceId=user_id,
                    targetId=role_id,
                )
                bundle.new_accounts_association.append(association)
        if raw_item.admins:
            for admin_user_id in raw_item.admins:
                role_admin_permission = NewPermissionRequestSchema(
                    sourceUniqueId=admin_user_id,
                    sourceType=PermissionSourceType.Account,
                    assetId=role_id,
                    privilegeId=ROLE_ADMIN_PRIVILEGE.uniqueId,
                    isRole=False,
                )
                bundle.new_permissions.append(role_admin_permission)

        return bundle
