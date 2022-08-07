from itertools import chain
from typing import Iterable

from authomize.rest_api_client.generated.schemas import RequestsBundleSchema

from base_provider import ProviderRunner
from onelogin_provider.clients.onelogin_client import OneloginClient
from onelogin_provider.configuration.client_configuration import OneloginClientConfiguration
from onelogin_provider.extractors.applications_extractor import ApplicationsExtactor
from onelogin_provider.extractors.groups_extactor import GroupsExtactor
from onelogin_provider.extractors.roles_extractor import RolesExtactor
from onelogin_provider.extractors.users_extractor import UsersExtactor
from onelogin_provider.models.shared_memory import OneloginProviderSharedMemory
from onelogin_provider.transformers.applications_transformer import ApplicationsTransformer
from onelogin_provider.transformers.groups_transformer import GroupsTransformer
from onelogin_provider.transformers.roles_transformer import RolesTransformer
from onelogin_provider.transformers.users_transformer import UsersTransformer


class OneloginRunWorkflow(ProviderRunner):

    def get_transformed_data(self) -> Iterable[RequestsBundleSchema]:
        data_provider_client_configuration: OneloginClientConfiguration = self.data_provider_client_configuration  # type: ignore
        client = OneloginClient(
            data_provider_client_configuration=data_provider_client_configuration,
        )
        shared_memory = OneloginProviderSharedMemory()
        return chain.from_iterable([
            GroupsTransformer(shared_memory)(
                GroupsExtactor(client)(),
            ),
            UsersTransformer(shared_memory)(
                UsersExtactor(client)(),
            ),
            ApplicationsTransformer(shared_memory)(
                ApplicationsExtactor(client)(),
            ),
            RolesTransformer(shared_memory)(
                RolesExtactor(client)(),
            ),
        ])
