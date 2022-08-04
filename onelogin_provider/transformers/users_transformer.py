from authomize.rest_api_client.generated.schemas import NewUserRequestSchema, RequestsBundleSchema
from onelogin.api.models.user import User

from provider_base.transformers.base_transformer import BaseTransformer


class UsersTransformer(BaseTransformer):
    """
    Transform a list of User resources.

    See https://developers.onelogin.com/api-docs/1/users/get-users Get Users documentation
        https://developers.onelogin.com/api-docs/2/users/list-users
    """

    def validate_item_schema(self, raw_item: User) -> bool:
        return True

    def transform_model(self, raw_item: User) -> RequestsBundleSchema:
        bundle = self.create_empty_bundle()
        new_user = NewUserRequestSchema(
            id=raw_item.id,
            name=raw_item.distinguished_name,
            firstName=raw_item.firstname,
            lastName=raw_item.lastname,
        )
        bundle.new_users.append(new_user)
        return bundle
