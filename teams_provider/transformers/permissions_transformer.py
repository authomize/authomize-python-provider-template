from typing import Dict

from authomize.rest_api_client.generated.schemas import (
    RequestsBundleSchema,
)

from base_provider.transformers.base_transformer import BaseTransformer


class RolesTransformer(BaseTransformer):
    """
    Todo.
    """

    def validate_item_schema(self, raw_item: Dict) -> bool:
        return True

    def transform_model(self, raw_item: Dict) -> RequestsBundleSchema:
        bundle = self.create_bundle()

        return bundle
