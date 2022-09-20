from typing import Dict

from authomize.rest_api_client.generated.schemas import (
    GroupingType,
    NewGroupingRequestSchema,
    RequestsBundleSchema, NewAssetsRequestSchema, AssetType,
)

from base_provider.transformers.base_transformer import BaseTransformer
from teams_provider.constants import TEAM_PUBLIC_CHANNELS_ID_PREFIX, \
    TEAM_PUBLIC_CHANNELS_NAME_POSTFIX, TEAM_PRIVATE_CHANNELS_ID_PREFIX, \
    TEAM_PRIVATE_CHANNELS_NAME_POSTFIX, OWNERS_ID_PREFIX, OWNERS_NAME_POSTFIX


class TeamsTransformer(BaseTransformer):
    """
    Transform a list of Team resources. For each team:
    - Identities:
      - Grouping of the team, which is equal to the AD Group.
      - Virtual grouping of the team owners.
    - Assets:
      - Team asset. Team members can, for example, join or view the team, while the owners can do
          also invite new members, delete etc.
      - Team "all public channels" asset. Team members permissions on it are inherited to all the
          public channels in the team.
      - Team "all private channels" asset. Owners can list the channels, but not read channels
          which they aren't members of.
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
            id=OWNERS_ID_PREFIX + raw_item['id'],
            name=raw_item['displayName'] + OWNERS_NAME_POSTFIX,
            type=GroupingType.VirtualGroup,
            anyoneCanJoinOrLeave=False,
            isRole=True,
        )
        bundle.new_groupings.extend([new_group, new_owners_group])

        new_team = NewAssetsRequestSchema(
            id=raw_item['id'],
            name=raw_item['displayName'],
            type=AssetType.Other
        )
        team_all_public_channels = NewAssetsRequestSchema(
            id=TEAM_PUBLIC_CHANNELS_ID_PREFIX + raw_item['id'],
            name=raw_item['displayName'] + TEAM_PUBLIC_CHANNELS_NAME_POSTFIX,
            type=AssetType.Other
        )
        team_all_private_channels = NewAssetsRequestSchema(
            id=TEAM_PRIVATE_CHANNELS_ID_PREFIX + raw_item['id'],
            name=raw_item['displayName'] + TEAM_PRIVATE_CHANNELS_NAME_POSTFIX,
            type=AssetType.Other
        )

        bundle.new_assets.extend([new_team, team_all_public_channels, team_all_private_channels])

        return bundle
