from authomize.rest_api_client.generated.schemas import (
    AssetType,
    NewAssetInheritanceRequestSchema,
    NewAssetRequestSchema,
    RequestsBundleSchema,
)

from base_provider.transformers.base_transformer import BaseTransformer


class SecretsLastAccessKeyTransformer(BaseTransformer):
    """
    Transformer for history of a found access keys
    """

    def validate_item_schema(self, raw_item: tuple[str, dict, str]) -> bool:
        return True

    def transform_model(self, raw_item: tuple[str, dict, str]) -> RequestsBundleSchema:
        bundle = self.create_bundle()
        (normalized_secret_id, access_key_records, field_name) = raw_item
        asset = NewAssetRequestSchema(
            uniqueId=access_key_records['secretItemHistoryId'],
            name=f"{field_name}: {access_key_records['itemValueNew']}",
            description=access_key_records['itemValueNew'],
            # TODO need new type 'access_key" and "secret_key"
            type=AssetType.Other,
        )
        bundle.new_assets.append(asset)
        inheritance = NewAssetInheritanceRequestSchema(
            sourceId=normalized_secret_id,
            targetId=access_key_records['secretItemHistoryId'],
        )
        bundle.new_assets_inheritance.append(inheritance)
        return bundle
