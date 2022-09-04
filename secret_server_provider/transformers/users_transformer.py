from authomize.rest_api_client.generated.schemas import (
    NewUserRequestSchema,
    RequestsBundleSchema,
    UserStatus,
)
from secret_server_openapiclient.model.user_summary import UserSummary

from base_provider.transformers.base_transformer import BaseTransformer
from secret_server_provider.normalize_id import normalize_id


class UsersTransformer(BaseTransformer):
    """
    Transform a list of User resources.

    See docs/UsersApi.md#users_service_search_users
    """

    def validate_item_schema(self, raw_item: UserSummary) -> bool:
        return True

    def transform_model(self, raw_item: UserSummary) -> RequestsBundleSchema:
        bundle = self.create_bundle()
        user = raw_item
        user_id = normalize_id(user.id)

        new_user = NewUserRequestSchema(
            uniqueId=user_id,
            name=user.user_name,
            lastLoginAt=user.last_login,
            display_name=user.display_name,
            status=UserStatus.Enabled if user.enabled is True else UserStatus.Disabled,
            hasMFA=bool(user.two_factor_method),
            **(dict(email=user.email_address) if user.email_address else dict()),
        )
        bundle.new_users.append(new_user)
        return bundle
