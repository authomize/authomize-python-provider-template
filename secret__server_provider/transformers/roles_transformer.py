from authomize.rest_api_client.generated.schemas import (
    GroupingType,
    NewAccountsAssociationRequestSchema,
    NewGroupingRequestSchema,
    NewPermissionsRequestSchema,
    RequestsBundleSchema,
)
from plugins.model.role_model import RoleModel

from base_provider.transformers.base_transformer import BaseTransformer


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
        role_id = raw_item.id
        new_group = NewGroupingRequestSchema(
            id=role_id,
            name=raw_item.name,
            # todo - make role
            type=GroupingType.Group,
            role=raw_item.name,
        )
        bundle.new_groupings.append(new_group)

        return bundle
