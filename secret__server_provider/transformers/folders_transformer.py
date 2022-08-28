from typing_extensions import assert_type
from authomize.rest_api_client.generated.schemas import NewAssetRequestSchema, RequestsBundleSchema, AssetType

from base_provider.transformers.base_transformer import BaseTransformer
from secret__server_provider.normalize_id import normalize_id

from ..openapi_client.plugins.model.folder_model import FolderModel


class FoldersTransformer(BaseTransformer):
    """
    Tramsform a list of all Apps in a OneLogin account.

    See https://developers.onelogin.com/api-docs/1/apps/get-apps Get Apps documentation
        https://developers.onelogin.com/api-docs/2/apps/list-apps
    """

    def validate_item_schema(self, raw_item: FolderModel) -> bool:
        return True

    def transform_model(self, raw_item: FolderModel) -> RequestsBundleSchema:
        bundle = self.create_bundle()
        asset = NewAssetRequestSchema(
            uniqueId=normalize_id(raw_item.id),
            name=raw_item.value,
            type = AssetType.Folder
        )
        bundle.new_assets.append(asset)
        return bundle