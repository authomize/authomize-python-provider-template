from typing import Dict

from authomize.rest_api_client.generated.schemas import (
    GroupingType,
    NewGroupingRequestSchema,
    RequestsBundleSchema,
)

from base_provider.transformers.base_transformer import BaseTransformer


class ChannelsTransformer(BaseTransformer):
    """
    Transform a list of Channel resources. For each channel:
    - Identities:
      - Virtual grouping of the channel members.
      - For private channels, a virtual grouping of the channel owners. For public channels,
        only a members virtual group is created. Owners are the same as the team's.
        Ditto for members, but the members group is useful because its entitlements may vary.
      - For public moderated channels, a virtual grouping of the channel moderators -
        maybe todo in the future.
    - Assets:
      - An asset representing the channel.
    """

    def validate_item_schema(self, raw_item: Dict) -> bool:
        return True

    def transform_model(self, raw_item: Dict) -> RequestsBundleSchema:
        bundle = self.create_bundle()
        if raw_item['deletedDateTime'] is not None:
            return bundle
        new_channel = NewGroupingRequestSchema(
            id=raw_item['id'],
            name=raw_item['displayName'],
            type=GroupingType.Group,
            anyoneCanJoinOrLeave=raw_item['membershipType'] != 'private',
            isRole=False,
        )
        bundle.new_groupings.append(new_channel)

        # TODO: add remaining channel groupings and assets.
        return bundle
