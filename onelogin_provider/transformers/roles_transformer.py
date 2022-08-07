from authomize.rest_api_client.generated.schemas import (
    GroupingType,
    NewAccountsAssociationRequestSchema,
    NewGroupingRequestSchema,
    NewPermissionsRequestSchema,
    RequestsBundleSchema,
)
from onelogin.api.models.role import Role

from base_provider import BaseTransformer


class RolesTransformer(BaseTransformer):
    """
    Transform a list of Role resources.
    Creates a:
    * Role (Groupping)
    * Role -> App permission
    * User -> Role inhertiance
    # TODO - explain
    * Admin -> Role permission (in this context the role is an asset)

    See https://developers.onelogin.com/api-docs/1/roles/get-roles Get Roles documentation
        https://developers.onelogin.com/api-docs/2/roles/list-roles
    """

    def validate_item_schema(self, raw_item: Role) -> bool:
        return True

    def transform_model(self, raw_item: Role) -> RequestsBundleSchema:
        bundle = self.create_bundle()
        role_id = raw_item.id
        new_group = NewGroupingRequestSchema(
            id=role_id,
            name=raw_item.name,
            # todo - make role
            type=GroupingType.Group,
            role=raw_item.name,
        )
        bundle.new_groupings.append(new_group)
        if raw_item.apps:
            for app_id in raw_item.apps:
                permission = NewPermissionsRequestSchema(
                    formId=role_id,
                    targetAssets=[app_id],
                )
                bundle.new_permissions.append(permission)
        if raw_item.users:
            for user_id in raw_item.users:
                association = NewAccountsAssociationRequestSchema(
                    sourceId=user_id,
                    targetId=role_id,
                )
                bundle.new_accounts_association.append(association)
        if raw_item.admins:
            for admin_user_id in raw_item.admins:
                permission = NewPermissionsRequestSchema(
                    formId=admin_user_id,
                    targetAssets=[role_id],
                )
                bundle.new_permissions.append(permission)

        return bundle
