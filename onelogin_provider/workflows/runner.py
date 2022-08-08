from typing import Tuple, Type

from base_provider.extractors.base_extactor import BaseExtractor
from base_provider.transformers.base_transformer import BaseTransformer
from base_provider.workflows.base_auto_runner import BaseAutoProviderRunner
from onelogin_provider.clients.onelogin_client import OneloginClient
from onelogin_provider.configuration.client_configuration import OneloginClientConfiguration
from onelogin_provider.extractors.applications_extractor import ApplicationsExtractor
from onelogin_provider.extractors.groups_extactor import GroupsExtractor
from onelogin_provider.extractors.roles_extractor import RolesExtractor
from onelogin_provider.extractors.users_extractor import UsersExtractor
from onelogin_provider.models.shared_memory import OneloginProviderSharedMemory
from onelogin_provider.transformers.applications_transformer import ApplicationsTransformer
from onelogin_provider.transformers.groups_transformer import GroupsTransformer
from onelogin_provider.transformers.roles_transformer import RolesTransformer
from onelogin_provider.transformers.users_transformer import UsersTransformer


class OneloginRunner(BaseAutoProviderRunner):
    def get_extractor_and_transformer_type_list(
        self,
    ) -> list[Tuple[Type[BaseExtractor], Type[BaseTransformer]]]:
        return [
            (GroupsExtractor, GroupsTransformer),
            (UsersExtractor, UsersTransformer),
            (ApplicationsExtractor, ApplicationsTransformer),
            (RolesExtractor, RolesTransformer),
        ]

    def create_client(self) -> OneloginClient:
        client_configuration: OneloginClientConfiguration = self.client_configuration  # type: ignore
        return OneloginClient(
            client_configuration=client_configuration,
        )

    def create_shared_memory(self) -> OneloginProviderSharedMemory:
        return OneloginProviderSharedMemory()
