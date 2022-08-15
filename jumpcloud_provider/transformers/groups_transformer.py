from typing import cast, List

from authomize.rest_api_client.generated.schemas import (
    GroupingType,
    NewGroupingRequestSchema,
    RequestsBundleSchema, NewAccountsAssociationRequestSchema,
)
from jcapiv2 import GraphConnection
from onelogin.api.models.group import Group

from base_provider.transformers.base_transformer import BaseTransformer
from jumpcloud_provider.models.group_members_association import GroupMembersAssociation


class GroupsTransformer(BaseTransformer):
    def validate_item_schema(self, raw_item: Group) -> bool:
        return True

    def transform_model(self, raw_item: GroupMembersAssociation) -> RequestsBundleSchema:
        group_id = raw_item.id
        bundle = self.create_bundle()
        group_members: List[GraphConnection] = raw_item.members
        new_group = NewGroupingRequestSchema(
            id=group_id,
            name=raw_item.name,
            type=GroupingType.Group,
        )

        for member in group_members:
            association = NewAccountsAssociationRequestSchema(
                targetId=group_id,
                sourceId=member.to.id
            )
            bundle.new_accounts_association.append(association)

        bundle.new_groupings.append(new_group)
        return bundle
