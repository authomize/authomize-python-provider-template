from authomize.rest_api_client.generated.schemas import ItemsBundleSchema, AssetDescription, AccessDescription, AccessTypes
from provider_name.transformers.base_transformer import BaseTransfomer


class FilesTransformer(BaseTransfomer):
    def validate_item_schema(self, raw_item: dict) -> bool:
        if 'id' not in raw_item:
            raise ValueError("File without an id")
        return True

    def transform_model(self, raw_item: dict) -> ItemsBundleSchema:
        bundle = self.create_empty_bundle()
        item_id = raw_item['id']
        # access = [
        #     AccessDescription(
        #         fromIdentityId=
        #         toAssetId=
        #         accessType=AccessTypes.
        #         accessName="Owner",
        #     )

        # ]
        bundle.assets.append(
            AssetDescription(
                id=item_id,
            ),

        )
        return bundle

