from itertools import chain
from typing import Iterable

from authomize.rest_api_client.generated.schemas import RequestsBundleSchema

from provider_base.workflows.base_run import BaseRunWorkflow
from provider_name.clients.data_provider_client import DataProviderClient
from provider_name.extractors.files_extractor import FilesExtactor
from provider_name.models.shared_memory import SharedMemory
from provider_name.transformers.files_transformer import FilesTransformer


class RunWorkflow(BaseRunWorkflow):

    def get_transformed_data(self) -> Iterable[RequestsBundleSchema]:
        client = DataProviderClient(
            data_provider_configuration=self.data_provider_configuration,
        )
        shared_memory = SharedMemory()
        return chain([
            UsersTransformer(shared_memory).transform_models(
                UsersExtactor(client).extact_raw(),
            ),
            FilesTransformer(shared_memory).transform_models(
                chain([
                    FilesExtactor(client).extact_raw(),
                    FoldersExtactor(client).extact_raw(),
                ])
            ),
        ])
