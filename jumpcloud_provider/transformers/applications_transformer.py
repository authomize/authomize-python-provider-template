from authomize.rest_api_client.generated.schemas import NewAssetsRequestSchema, RequestsBundleSchema
from jcapiv1 import Application

from base_provider.transformers.base_transformer import BaseTransformer


class ApplicationsTransformer(BaseTransformer):
    """
    Tramsform a list of all Apps in a JumpCloud account.

    See https://github.com/TheJumpCloud/jcapi-python/blob/master/jcapiv1/jcapiv1/api/applications_api.py
        https://docs.jumpcloud.com/api/1.0/index.html#operation/applications_list
    """

    def validate_item_schema(self, raw_item: Application) -> bool:
        return True

    def transform_model(self, raw_item: Application) -> RequestsBundleSchema:
        bundle = self.create_bundle()
        asset = NewAssetsRequestSchema(
            id=raw_item.id,
            name=raw_item.name,
        )
        bundle.new_assets.append(asset)
        return bundle
