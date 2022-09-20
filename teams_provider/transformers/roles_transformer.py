from typing import Dict

from authomize.rest_api_client.generated.schemas import (
    NewAccountsAssociationRequestSchema,
    RequestsBundleSchema,
)

from base_provider.transformers.base_transformer import BaseTransformer
from teams_provider.constants import OWNERS_ID_PREFIX


class RolesTransformer(BaseTransformer):
    """
    Transform a list of Role resources.
    If a user is a team or a channel owner, creates an association between it and the team/channel
    owners virtual group.
    TODO: create rest of associations.
    """

    def validate_item_schema(self, raw_item: Dict) -> bool:
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
                target = OWNERS_ID_PREFIX + channel
            else:
                target = OWNERS_ID_PREFIX + team

            association = NewAccountsAssociationRequestSchema(
                sourceId=user_id,
                targetId=target,
            )
            bundle.new_accounts_association.append(association)

        return bundle
