from authomize.rest_api_client.generated.schemas import (
    NewAccountsAssociationRequestSchema,
    RequestsBundleSchema,
)

from base_provider.transformers.base_transformer import BaseTransformer
from secret__server_provider.normalize_id import normalize_id

from ..openapi_client.plugins.model.group_user_summary import GroupUserSummary


class UserMemberOfGroupTransformer(BaseTransformer):
    """
    Transform a list of (User, Group) tuples.

    See docs/UsersApi.md#xxx
    """

    def validate_item_schema(self, raw_item: GroupUserSummary) -> bool:
        return True

    def transform_model(self, raw_item: GroupUserSummary) -> RequestsBundleSchema:
        bundle = self.create_bundle()
        group_info = raw_item
        user_id = normalize_id(group_info.user_id)
        group_id = normalize_id(group_info.group_id)
        association = NewAccountsAssociationRequestSchema(
            sourceId=user_id,
            targetId=group_id,
        )
        bundle.new_accounts_association.append(association)
        return bundle
