from authomize.rest_api_client.generated.schemas import (
    GroupingType,
    NewGroupingRequestSchema,
    RequestsBundleSchema,
)
from onelogin.api.models.group import Group

from base_provider.transformers.base_transformer import BaseTransformer


class GroupsTransformer(BaseTransformer):
    """
    Transorm a list of Group resources
    See https://developers.onelogin.com/api-docs/1/groups/get-groups Get Groups documentation
    """

    def validate_item_schema(self, raw_item: Group) -> bool:
        return True

    def transform_model(self, raw_item: Group) -> RequestsBundleSchema:
        bundle = self.create_bundle()
        new_group = NewGroupingRequestSchema(
            id=raw_item.id,
            name=raw_item.name,
            type=GroupingType.Group,
        )
        bundle.new_groupings.append(new_group)
        return bundle
