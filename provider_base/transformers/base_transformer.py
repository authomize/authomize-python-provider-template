from typing import Iterable

from authomize.rest_api_client.generated.schemas import RequestsBundleSchema
from pydantic import ValidationError

from provider_base.models.base_shared_memory import BaseSharedMemory


class BaseTransformer:
    def __init__(self, shared_memory: BaseSharedMemory) -> None:
        self.shared_memory = shared_memory

    def transform_models(
        self,
        extracted_raw_data: Iterable[dict],
    ) -> Iterable[RequestsBundleSchema]:
        for raw_item in extracted_raw_data:
            if not self.validate_item_schema(raw_item):
                # Can continue as well if we prefer to ignore "damaged data"
                raise ValidationError("Item not validated")
            yield self.transform_model(raw_item)

    def validate_item_schema(self, raw_item: dict) -> bool:
        raise NotImplementedError()

    def transform_model(self, raw_item: dict) -> RequestsBundleSchema:
        bundle = self.create_empty_bundle()
        # todo
        return bundle

    @staticmethod
    def create_empty_bundle() -> RequestsBundleSchema:
        return RequestsBundleSchema(
            new_users=[],
            new_groupings=[],
            new_assets=[],
            new_accounts_association=[],
        )
