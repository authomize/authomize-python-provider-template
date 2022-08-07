from authomize.rest_api_client.generated.schemas import NewAssetsRequestSchema, RequestsBundleSchema

from base_provider.transformers.base_transformer import Transformer
from mock_provider.models.shared_memory import MockProviderSharedMemory


class FilesTransformer(Transformer):
    def validate_item_schema(self, raw_item: dict) -> bool:
        assert 'id' in raw_item, "File without id"
        assert 'name' in raw_item, "File without name"
        return True

    def transform_model(self, raw_item: dict) -> RequestsBundleSchema:
        shared_memory: MockProviderSharedMemory = self.shared_memory  # type: ignore
        domain = shared_memory.domain
        bundle = self.create_bundle(
            new_assets=[
                NewAssetsRequestSchema(
                    id=f"{domain}:{raw_item['id']}",
                    name=raw_item['name'],
                ),
            ],
        )
        return bundle
