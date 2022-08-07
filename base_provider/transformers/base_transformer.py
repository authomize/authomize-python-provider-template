from typing import Iterable

from authomize.rest_api_client.generated.schemas import RequestsBundleSchema

from base_provider.models.base_shared_memory import BaseProviderSharedMemory


class BaseTransformer:
    def __init__(self, shared_memory: BaseProviderSharedMemory) -> None:
        self.shared_memory = shared_memory

    def __call__(
        self,
        extracted_raw_data: Iterable[dict],
    ) -> Iterable[RequestsBundleSchema]:
        for item in self.transform_models(extracted_raw_data):
            return item

    def transform_models(
        self,
        extracted_raw_data: Iterable[dict],
    ) -> Iterable[RequestsBundleSchema]:
        for raw_item in extracted_raw_data:
            if not self.validate_item_schema(raw_item):
                # Can continue as well if we prefer to ignore "damaged data"
                raise ValueError("Item not validated")
            yield self.transform_model(raw_item)

    def validate_item_schema(self, raw_item: dict) -> bool:
        raise NotImplementedError()

    def transform_model(self, raw_item: dict) -> RequestsBundleSchema:
        bundle = self.create_bundle()
        # todo
        return bundle

    @staticmethod
    def create_bundle(
        new_users=None,
        new_groupings=None,
        new_assets=None,
        new_accounts_association=None,
        new_permissions=None,
        new_groupings_association=None,
    ) -> RequestsBundleSchema:
        return RequestsBundleSchema(
            new_users=new_users or [],
            new_groupings=new_groupings or [],
            new_assets=new_assets or [],
            new_accounts_association=new_accounts_association or [],
            new_permissions=new_permissions or [],
            new_groupings_association=new_groupings_association or [],
        )
