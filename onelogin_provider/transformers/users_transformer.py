from authomize.rest_api_client.generated.schemas import NewUserRequestSchema, RequestsBundleSchema, NewAccountsAssociationRequestSchema
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
        user_id = raw_item.id
        # TODO! this should be an account! not User!
        new_user = NewUserRequestSchema(
            id=user_id,
            name=f'{raw_item.firstname} {raw_item.lastname}',
            firstName=raw_item.firstname,
            lastName=raw_item.lastname,
            **(dict(email=raw_item.email) if raw_item.email else dict()),
        )
        # Every user can be member of 0/1 group (but not many groups!)
        if raw_item.group_id:
            association = NewAccountsAssociationRequestSchema(
                sourceId=user_id,
                targetId=raw_item.group_id,
            )
            bundle.new_accounts_association.append(association)
        bundle.new_users.append(new_user)
        return bundle
