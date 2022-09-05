from authomize.rest_api_client.generated.schemas import (
    GroupingType,
    NewGroupingRequestSchema,
    RequestsBundleSchema,
)
from secret_server_openapiclient.model.group_model import GroupModel

from base_provider.transformers.base_transformer import BaseTransformer
from secret_server_provider.normalize_id import normalize_id


class GroupsTransformer(BaseTransformer):
    """
    Transorm a list of Group resources
    """

    def validate_item_schema(self, raw_item: GroupModel) -> bool:
        return True

    def transform_model(self, raw_item: GroupModel) -> RequestsBundleSchema:
        bundle = self.create_bundle()
        new_group = NewGroupingRequestSchema(
            uniqueId=normalize_id(raw_item.id),
            name=raw_item.name,
            type=GroupingType.Group,
            isRole=False,
        )
        bundle.new_groupings.append(new_group)
        return bundle
