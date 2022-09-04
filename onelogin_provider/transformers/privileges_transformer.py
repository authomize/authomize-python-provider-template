from typing import List, Tuple

from authomize.rest_api_client.generated.schemas import (
    NewPermissionRequestSchema,
    NewPrivilegeRequestSchema,
    PermissionSourceType,
    PrivilegeType,
    RequestsBundleSchema,
)
from onelogin.api.models.privilege import Privilege

from base_provider.transformers.base_transformer import BaseTransformer


class PrivilegesTransformer(BaseTransformer):
    """
    Transform a list of privilege resources and roles + users assigned to it

    See https://developers.onelogin.com/api-docs/1/privileges/list-privileges
        https://developers.onelogin.com/api-docs/1/privileges/get-roles
        https://developers.onelogin.com/api-docs/1/privileges/get-users
    """

    def validate_item_schema(self, raw_item: Tuple[Privilege, List[int], List[int]]) -> bool:
        return True

    def transform_model(self, raw_item: Tuple[Privilege, List[int], List[int]]) -> RequestsBundleSchema:
        bundle = self.create_bundle()
        privilege_raw, role_ids, user_ids = raw_item

        new_privilege = NewPrivilegeRequestSchema(
            uniqueId=privilege_raw.id,
            type=PrivilegeType.Use,
            originPrivilegeName=privilege_raw.name,
        )
        bundle.new_permissions.append(new_privilege)

        for role_id in role_ids:
            role_permission = NewPermissionRequestSchema(
                sourceUniqueId=str(role_id),
                sourceType=PermissionSourceType.Grouping,
                # None - as its on the whole "Onelogin base application"
                assetId=None,
                privilegeId=privilege_raw.id,
                isRole=True,
            )
            bundle.new_permissions.append(role_permission)

        for user_id in user_ids:
            role_permission = NewPermissionRequestSchema(
                sourceUniqueId=str(user_id),
                sourceType=PermissionSourceType.Account,
                # None - as its on the whole "Onelogin base application"
                assetId=None,
                privilegeId=privilege_raw.id,
                isRole=True,
            )
            bundle.new_permissions.append(role_permission)

        return bundle
