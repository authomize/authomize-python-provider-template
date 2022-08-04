from authomize.rest_api_client.generated.schemas import NewAssetsRequestSchema, RequestsBundleSchema

from provider_base.transformers.base_transformer import BaseTransformer


class FilesTransformer(BaseTransformer):
    def validate_item_schema(self, raw_item: dict) -> bool:
        if 'id' not in raw_item:
            raise ValueError("File without an id")
        return True

    def transform_model(self, raw_item: dict) -> RequestsBundleSchema:
        bundle = self.create_empty_bundle()
        item_id = raw_item['id']
        asset = NewAssetsRequestSchema(
            id=item_id,
        )
        bundle.new_assets.append(asset)
        return bundle
