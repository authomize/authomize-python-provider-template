from typing import Dict

from authomize.rest_api_client.generated.schemas import (
    NewAccountsAssociationRequestSchema,
    RequestsBundleSchema,
)
from onelogin.api.models.role import Role

from base_provider.transformers.base_transformer import BaseTransformer


class RolesTransformer(BaseTransformer):
    """
    Transform a list of Role resources.
    If a user is a team or a channel owner, creates an association between it and the team/channel owners virtual group.
    """

    def validate_item_schema(self, raw_item: Role) -> bool:
        return True

    def transform_model(self, raw_item: Dict) -> RequestsBundleSchema:
        bundle = self.create_bundle()

        uri_parts = raw_item['sub_uri'].split('/')
        team, channel = uri_parts[1], None
        if len(uri_parts) > 3:
            channel = uri_parts[3]

        if 'owner' in raw_item['roles']:
            user_id = raw_item['userId']
            if channel:
                target = 'owners:' + channel
            else:
                target = 'owners:' + team

            association = NewAccountsAssociationRequestSchema(
                sourceId=user_id,
                targetId=target,
            )
            bundle.new_accounts_association.append(association)

        return bundle
