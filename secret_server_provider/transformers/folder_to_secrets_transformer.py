from asyncio.log import logger
from authomize.rest_api_client.generated.schemas import NewAssetInheritanceRequestSchema, RequestsBundleSchema

from base_provider.transformers.base_transformer import BaseTransformer
from secret_server_provider.normalize_id import normalize_id

from secret_server_openapiclient.model.secret_model_v2 import SecretModelV2


class FoldersToSecretsTransformer(BaseTransformer):
    """
    Gets all secrets with its parent folder
    """

    def validate_item_schema(self, raw_item: SecretModelV2) -> bool:
        return True

    def transform_model(self, raw_item: SecretModelV2) -> RequestsBundleSchema:
        bundle = self.create_bundle()
        
        inheritance = NewAssetInheritanceRequestSchema(
            sourceId=normalize_id(raw_item.folder_id),
            targetId=normalize_id(raw_item.id)
        )
        
        if raw_item.inherits_permissions == True:
            bundle.new_assets_inheritance.append(inheritance)
        return bundle
