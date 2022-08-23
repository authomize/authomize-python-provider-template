from authomize.rest_api_client.generated.schemas import (
    NewIdentityRequestSchema,
    NewUserRequestSchema,
    RequestsBundleSchema,
)

from base_provider.transformers.base_transformer import BaseTransformer
from secret__server_provider.openapi_client.plugins.model.user_model import UserModel


class UsersTransformer(BaseTransformer):
    """
    Transform a list of User resources.

    See docs/UsersApi.md#users_service_search_users
    """

    def validate_item_schema(self, raw_item: UserModel) -> bool:
        return True

    def transform_model(self, raw_item: UserModel) -> RequestsBundleSchema:
        bundle = self.create_bundle()
        user_id = raw_item.id
        new_user = NewUserRequestSchema(
            uniqueId=user_id,
            name=raw_item.user_name,
            **(dict(email=raw_item.email_address) if raw_item.email_address else dict()),
        )
        new_identity = NewIdentityRequestSchema(
            uniqueId=user_id,
            name=raw_item.user_name,
            **(dict(email=raw_item.email_address) if raw_item.email_address else dict()),
        )
        '''
        TODO : support group info by id from users extractor

        # Every user can be member of 0/1 group (but not many groups!)
        if raw_item.group_id:
            association = NewAccountsAssociationRequestSchema(
                sourceId=user_id,
                targetId=raw_item.group_id,
            )
            bundle.new_accounts_association.append(association)
        '''
        bundle.new_users.append(new_user)
        bundle.new_identities.append(new_identity)
        return bundle
