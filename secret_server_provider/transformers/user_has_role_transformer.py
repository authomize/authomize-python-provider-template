from authomize.rest_api_client.generated.schemas import (
    NewAccountsAssociationRequestSchema,
    RequestsBundleSchema,
)
from secret_server_openapiclient.model.role_summary import RoleSummary
from secret_server_openapiclient.model.user_model import UserModel

from base_provider.transformers.base_transformer import BaseTransformer
from secret_server_provider.normalize_id import normalize_id


class UserHasRoleTransformer(BaseTransformer):
    """
    Transform a list of (User, Role) tuples.
    """

    def validate_item_schema(self, raw_item: tuple[UserModel,RoleSummary]) -> bool:
        return True

    def transform_model(self, raw_item: tuple[UserModel,RoleSummary]) -> RequestsBundleSchema:
        bundle = self.create_bundle()
        (user,role_info) = raw_item
        user_id = normalize_id(user.id)
        role_id = normalize_id(role_info.role_id)
        association = NewAccountsAssociationRequestSchema(
            sourceId=user_id,
            targetId=role_id,
        )
        bundle.new_accounts_association.append(association)
        return bundle
