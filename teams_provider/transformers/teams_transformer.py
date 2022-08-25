from typing import Dict

from authomize.rest_api_client.generated.schemas import (
    GroupingType,
    NewGroupingRequestSchema,
    RequestsBundleSchema, NewAssetsRequestSchema, AssetType,
)

from base_provider.transformers.base_transformer import BaseTransformer


class TeamsTransformer(BaseTransformer):
    """
    Transform a list of Team resources
    """

    def validate_item_schema(self, raw_item: Dict) -> bool:
        return True

    def transform_model(self, raw_item: Dict) -> RequestsBundleSchema:
        bundle = self.create_bundle()
        if raw_item['deletedDateTime'] is not None:
            return bundle
        new_group = NewGroupingRequestSchema(
            id=raw_item['id'],
            name=raw_item['displayName'],
            type=GroupingType.Group,
            anyoneCanJoinOrLeave=raw_item['visibility'] == 'Public',
            isRole=False,
        )
        new_owners_group = NewGroupingRequestSchema(
            id='owners:' + raw_item['id'],
            name=raw_item['displayName'] + ' owners',
            type=GroupingType.VirtualGroup,
            anyoneCanJoinOrLeave=False,
            isRole=True,
        )
        bundle.new_groupings.extend([new_group, new_owners_group])

        # Do I need to create a group asset or is it created automatically?
        new_team = NewAssetsRequestSchema(
            id=raw_item['id'],
            name=raw_item['displayName'],
            type=AssetType.Other
        )
        team_all_public_channels = NewAssetsRequestSchema(
            id='pubchannels:' + raw_item['id'],
            name=raw_item['displayName'] + ' all public channels',
            type=AssetType.Other
        )
        team_all_private_channels = NewAssetsRequestSchema(
            id='privchannels:' + raw_item['id'],
            name=raw_item['displayName'] + ' all private channels',
            type=AssetType.Other
        )

        bundle.new_assets.extend([new_team, team_all_public_channels, team_all_private_channels])

        return bundle
