from authomize.rest_api_client.generated.schemas import (
    NewPermissionRequestSchema,
    NewPrivilegeRequestSchema,
    PermissionSourceType,
    PrivilegeType,
    RequestsBundleSchema,
)

from base_provider.transformers.base_transformer import BaseTransformer
from secret_server_provider.normalize_id import normalize_id

from secret_server_openapiclient.model.secret_permission_summary import SecretPermissionSummary


class UserAccessRoleToSecretTransformer(BaseTransformer):
    """
    Transform a SecretPermissionModel relevant to users and secrets (not groups / folder).

    See docs/UsersApi.md#xxx
    """

    def validate_item_schema(self, raw_item: SecretPermissionSummary) -> bool:
        return True

    def transform_model(self, raw_item: SecretPermissionSummary) -> RequestsBundleSchema:
        bundle = self.create_bundle()
        privilege_id = normalize_id(raw_item.secret_access_role_id)
        permission = NewPermissionRequestSchema(
            sourceUniqueId=normalize_id(raw_item.user_id),
            sourceType=PermissionSourceType.Account,
            privilegeId=privilege_id,
            assetId=normalize_id(raw_item.secret_id),
            isRole=False,
        )
        # check if AccessRole has already been handled
        if privilege_id not in self.shared_memory.existing_priveleges_set:
            privilege_type = self.get_privilege_type(raw_item.secret_access_role_name)
            privilege = NewPrivilegeRequestSchema(
                uniqueId=privilege_id,
                type=privilege_type,
                originName=raw_item.secret_access_role_name,
            )
            bundle.new_privileges.append(privilege)
            self.shared_memory.existing_priveleges_set.add(privilege_id)
        bundle.new_permissions.append(permission)
        return bundle

    def get_privilege_type(self, access_role_name: str) -> PrivilegeType:
        if access_role_name == "Owner":
            return PrivilegeType.Administrative
        if access_role_name == "View":
            return PrivilegeType.Read
        self.logger.warning(
            "Unknown `secretAccessRoleName` - using `Uses` instead",
            secretAccessRoleName=access_role_name,
        )
        return PrivilegeType.Use
