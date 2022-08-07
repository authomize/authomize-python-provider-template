from authomize.rest_api_client.generated.schemas import NewAssetsRequestSchema, RequestsBundleSchema
from onelogin.api.models.app import App

from base_provider import Transformer


class ApplicationsTransformer(Transformer):
    """
    Tramsform a list of all Apps in a OneLogin account.

    See https://developers.onelogin.com/api-docs/1/apps/get-apps Get Apps documentation
        https://developers.onelogin.com/api-docs/2/apps/list-apps
    """

    def validate_item_schema(self, raw_item: App) -> bool:
        return True

    def transform_model(self, raw_item: App) -> RequestsBundleSchema:
        bundle = self.create_bundle()
        asset = NewAssetsRequestSchema(
            id=raw_item.id,
            name=raw_item.name,
        )
        bundle.new_assets.append(asset)
        return bundle
