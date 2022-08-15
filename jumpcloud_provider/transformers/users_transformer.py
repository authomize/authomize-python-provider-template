from authomize.rest_api_client.generated.schemas import (
    NewIdentityRequestSchema,
    NewUserRequestSchema,
    RequestsBundleSchema,
)
from jcapiv1 import Systemuserreturn

from base_provider.transformers.base_transformer import BaseTransformer


class UsersTransformer(BaseTransformer):
    """
    Transform a list of User resources.
    See https://github.com/TheJumpCloud/jcapi-python/blob/master/jcapiv1/docs/SystemusersApi.md
        https://github.com/TheJumpCloud/jcapi-python/blob/master/jcapiv1/jcapiv1/api/systemusers_api.py
    """

    def validate_item_schema(self, raw_item: Systemuserreturn) -> bool:
        return True

    def transform_model(self, raw_item: Systemuserreturn) -> RequestsBundleSchema:
        bundle = self.create_bundle()
        user_id = raw_item.id
        new_user = NewUserRequestSchema(
            id=user_id,
            name=f'{raw_item.firstname} {raw_item.lastname}',
            firstName=raw_item.firstname,
            lastName=raw_item.lastname,
            **(dict(email=raw_item.email) if raw_item.email else dict()),
        )
        new_identity = NewIdentityRequestSchema(
            id=user_id,
            name=f'{raw_item.firstname} {raw_item.lastname}',
            firstName=raw_item.firstname,
            lastName=raw_item.lastname,
            **(dict(email=raw_item.email) if raw_item.email else dict()),
        )
        bundle.new_users.append(new_user)
        bundle.new_identities.append(new_identity)
        return bundle
