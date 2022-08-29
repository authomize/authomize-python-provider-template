from typing_extensions import assert_type
from authomize.rest_api_client.generated.schemas import NewAssetRequestSchema, RequestsBundleSchema, AssetType, NewAssetInheritanceRequestSchema

from base_provider.transformers.base_transformer import BaseTransformer
from secret_server_provider.normalize_id import normalize_id

from secret_server_openapiclient.model.folder_model import FolderModel


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
            name=raw_item.folder_name,
            type = AssetType.Folder
        )
        bundle.new_assets.append(asset)
        inheritance = NewAssetInheritanceRequestSchema(
            sourceId=normalize_id(raw_item.parent_folder_id),
            targetId=normalize_id(raw_item.id)
        )
        
        if raw_item.inherit_permissions == True:
            bundle.new_assets_inheritance.append(inheritance)
        return bundle
