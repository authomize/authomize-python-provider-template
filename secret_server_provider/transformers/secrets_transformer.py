from authomize.rest_api_client.generated.schemas import (
    AssetType,
    NewAssetRequestSchema,
    RequestsBundleSchema,
)
from secret_server_openapiclient.model.secret_summary import SecretSummary

from base_provider.transformers.base_transformer import BaseTransformer
from secret_server_provider.normalize_id import normalize_id


class SecretsTransformer(BaseTransformer):
    """
    Tramsform a list secrets
    """

    def validate_item_schema(self, raw_item: SecretSummary) -> bool:
        return True

    def transform_model(self, raw_item: SecretSummary) -> RequestsBundleSchema:
        bundle = self.create_bundle()
        asset = NewAssetRequestSchema(
            uniqueId=normalize_id(raw_item.id),
            name=raw_item.name,
            createdAt=raw_item.create_date,
            lastUsedAt=raw_item.last_accessed,
            # storing the template name as description
            description=raw_item.secret_template_name,
            type=AssetType.File,
            originType="Secret",

        )
        bundle.new_assets.append(asset)
        return bundle
