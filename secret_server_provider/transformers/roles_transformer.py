from authomize.rest_api_client.generated.schemas import (
    GroupingType,
    NewPermissionRequestSchema,
    NewGroupingRequestSchema,
    NewPrivilegeRequestSchema,
    PrivilegeType,
    RequestsBundleSchema,
    PermissionSourceType,
)
from secret_server_openapiclient.model.role_model import RoleModel

from base_provider.transformers.base_transformer import BaseTransformer
from secret_server_provider.normalize_id import normalize_id


class RolesTransformer(BaseTransformer):
    """
    Transform a list of Role resources.

    Creates a:
    * Role (Groupping)
    * Role -> App permission
    * User -> Role inhertiance
    # TODO - explain
    * Admin -> Role permission (in this context the role is an asset)

    See docs/RolesApi.md#roles_service_get_all
    """
    def validate_item_schema(self, raw_item: RoleModel) -> bool:
        return True

    def transform_model(self, raw_item: RoleModel) -> RequestsBundleSchema:
        bundle = self.create_bundle()
        role_id = normalize_id(raw_item.id)
        new_group = NewGroupingRequestSchema(
            uniqueId=role_id,
            name=raw_item.name,
            type=GroupingType.Group,
            isRole=True,
        )
        bundle.new_groupings.append(new_group)

        # Maybe duplicate?
        new_privilege = NewPrivilegeRequestSchema(
            uniqueId=role_id,
            type=self.get_privilege_type(raw_item.name),
            originPrivilegeName=raw_item.name,
        )
        permission = NewPermissionRequestSchema(
            sourceUniqueId=role_id,
            sourceType=PermissionSourceType.Grouping,
            privilegeId=role_id,
            assetId=None,
            isRole=True,
        )
        bundle.new_privileges.append(new_privilege)
        bundle.new_permissions.append(permission)

        return bundle

    def get_privilege_type(self, access_role_name: str) -> PrivilegeType:
        if 'owner' in access_role_name.lower():
            return PrivilegeType.Administrative
        if 'admin' in access_role_name.lower():
            return PrivilegeType.Administrative
        if 'write' in access_role_name.lower():
            return PrivilegeType.Write
        if 'read' in access_role_name.lower():
            return PrivilegeType.Read
        return PrivilegeType.Use
