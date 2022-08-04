from itertools import chain
from typing import Iterable

from authomize.rest_api_client.generated.schemas import RequestsBundleSchema

from onelogin_provider.clients.onelogin_client import OneloginClient
from onelogin_provider.extractors.users_extractor import UsersExtactor
from onelogin_provider.models.shared_memory import SharedMemory
from onelogin_provider.transformers.users_transformer import UsersTransformer
from provider_base.workflows.base_run import BaseRunWorkflow


class OneloginRunWorkflow(BaseRunWorkflow):

    def get_transformed_data(self) -> Iterable[RequestsBundleSchema]:
        client = OneloginClient(
            data_provider_configuration=self.data_provider_configuration,
        )
        shared_memory = SharedMemory()
        return chain([
            list(UsersTransformer(shared_memory).transform_models(
                list(UsersExtactor(client).extact_raw()),
            )),
        ])
