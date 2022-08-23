from authomize.rest_api_client.generated.schemas import NewAssetRequestSchema, RequestsBundleSchema

from base_provider.transformers.base_transformer import BaseTransformer

from ..openapi_client.plugins.model.secret_model_v2 import SecretModelV2 

class SecretsTransformer(BaseTransformer):
    """
    Tramsform a list of all Apps in a OneLogin account.

    See https://developers.onelogin.com/api-docs/1/apps/get-apps Get Apps documentation
        https://developers.onelogin.com/api-docs/2/apps/list-apps
    """

    def validate_item_schema(self, raw_item: SecretModelV2) -> bool:
        return True

    def transform_model(self, raw_item: SecretModelV2) -> RequestsBundleSchema:
        bundle = self.create_bundle()
        breakpoint()
        asset = NewAssetRequestSchema(
            uniqueId=raw_item.id,
            name=raw_item.name,
        )
        bundle.new_assets.append(asset)
        return bundle
