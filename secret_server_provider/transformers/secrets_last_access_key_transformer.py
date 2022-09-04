from authomize.rest_api_client.generated.schemas import (
    AssetType,
    NewAssetInheritanceRequestSchema,
    NewAssetRequestSchema,
    RequestsBundleSchema,
)

from base_provider.transformers.base_transformer import BaseTransformer


class SecretsLastAccessKeyTransformer(BaseTransformer):
    """
    Tramsform a list of all Apps in a OneLogin account.

    See https://developers.onelogin.com/api-docs/1/apps/get-apps Get Apps documentation
        https://developers.onelogin.com/api-docs/2/apps/list-apps
    """

    def validate_item_schema(self, raw_item: tuple[str, dict]) -> bool:
        return True

    def transform_model(self, raw_item: tuple[str, dict]) -> RequestsBundleSchema:
        bundle = self.create_bundle()
        (normalized_secret_id, access_key_records) = raw_item
        asset = NewAssetRequestSchema(
            uniqueId=access_key_records['secretItemHistoryId'],
            name=access_key_records['itemValueNew'],
            # TODO need new type 'access_key"
            type=AssetType.Other,
        )
        bundle.new_assets.append(asset)
        inheritance = NewAssetInheritanceRequestSchema(
            sourceId=normalized_secret_id,
            targetId=access_key_records['secretItemHistoryId'],
        )
        bundle.new_assets_inheritance.append(inheritance)
        return bundle
