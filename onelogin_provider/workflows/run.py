from itertools import chain
from typing import Iterable

from authomize.rest_api_client.generated.schemas import RequestsBundleSchema

from onelogin_provider.clients.onelogin_client import OneloginClient
from onelogin_provider.extractors.groups_extactor import GroupsExtactor
from onelogin_provider.extractors.users_extractor import UsersExtactor
from onelogin_provider.models.shared_memory import SharedMemory
from onelogin_provider.transformers.groups_transformer import GroupsTransformer
from onelogin_provider.transformers.users_transformer import UsersTransformer
from provider_base.workflows.base_run import BaseRunWorkflow


class OneloginRunWorkflow(BaseRunWorkflow):

    def get_transformed_data(self) -> Iterable[RequestsBundleSchema]:
        client = OneloginClient(
            data_provider_configuration=self.data_provider_configuration,
        )
        shared_memory = SharedMemory()
        return chain.from_iterable([
            UsersTransformer(shared_memory).transform_models(
                UsersExtactor(client).extact_raw(),
            ),
            GroupsTransformer(shared_memory).transform_models(
                GroupsExtactor(client).extact_raw(),
            ),
        ])
