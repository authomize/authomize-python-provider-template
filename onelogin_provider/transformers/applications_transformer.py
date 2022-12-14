from authomize.rest_api_client.generated.schemas import (
    AssetType,
    NewAssetRequestSchema,
    RequestsBundleSchema,
)
from onelogin.api.models.app import App

from base_provider.transformers.base_transformer import BaseTransformer


class ApplicationsTransformer(BaseTransformer):
    """
    Tramsform a list of all Apps in a OneLogin account.

    See https://developers.onelogin.com/api-docs/1/apps/get-apps Get Apps documentation
        https://developers.onelogin.com/api-docs/2/apps/list-apps
    """

    def validate_item_schema(self, raw_item: App) -> bool:
        return True

    def transform_model(self, raw_item: App) -> RequestsBundleSchema:
        bundle = self.create_bundle()
        asset = NewAssetRequestSchema(
            type=AssetType.Application,
            uniqueId=raw_item.id,
            name=raw_item.name,
            href=raw_item.icon_url,
        )
        bundle.new_assets.append(asset)
        return bundle
