from typing import Tuple, Type

from base_provider.extractors.base_extractor import BaseExtractor
from base_provider.transformers.base_transformer import BaseTransformer
from base_provider.workflows.base_auto_runner import BaseAutoProviderRunner
from jumpcloud_provider.clients.jumpcloud_client import JumpcloudClient
from jumpcloud_provider.configuration.client_configuration import JumpcloudClientConfiguration
from jumpcloud_provider.extractors.applications_extractor import ApplicationsExtractor
from jumpcloud_provider.extractors.groups_extractor import GroupsExtractor
from jumpcloud_provider.extractors.roles_extractor import RolesExtractor
from jumpcloud_provider.extractors.users_extractor import UsersExtractor
from jumpcloud_provider.models.shared_memory import JumpcloudProviderSharedMemory
from jumpcloud_provider.transformers.applications_transformer import ApplicationsTransformer
from jumpcloud_provider.transformers.groups_transformer import GroupsTransformer
from jumpcloud_provider.transformers.roles_transformer import RolesTransformer
from jumpcloud_provider.transformers.users_transformer import UsersTransformer


class JumpcloudRunner(BaseAutoProviderRunner):
    def get_extractor_and_transformer_type_list(
        self,
    ) -> list[Tuple[Type[BaseExtractor], Type[BaseTransformer]]]:
        return [
            (GroupsExtractor, GroupsTransformer),
            (UsersExtractor, UsersTransformer),
            (ApplicationsExtractor, ApplicationsTransformer),
            (RolesExtractor, RolesTransformer),
        ]

    def create_client(self) -> JumpcloudClient:
        client_configuration: JumpcloudClientConfiguration = self.client_configuration  # type: ignore
        return JumpcloudClient(client_configuration=client_configuration)

    def create_shared_memory(self) -> JumpcloudProviderSharedMemory:
        return JumpcloudProviderSharedMemory()
