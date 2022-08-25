from typing import Tuple, Type

from base_provider.extractors.base_extractor import BaseExtractor
from base_provider.transformers.base_transformer import BaseTransformer
from base_provider.workflows.base_auto_runner import BaseAutoProviderRunner
from secret__server_provider.clients.secret_server_client import SecretServerClient
from secret__server_provider.configuration.client_configuration import SecretServerConfiguration
from secret__server_provider.extractors.groups_extractor import GroupsExtractor
from secret__server_provider.extractors.roles_extractor import RolesExtractor
from secret__server_provider.extractors.folders_extractor import FoldersExtractor
from secret__server_provider.extractors.user_access_role_extractor import UserAccessRoleExtractor
from secret__server_provider.extractors.user_member_of_group_extractor import (
    UserMemberOfGroupExtractor,
)
from secret__server_provider.extractors.users_extractor import UsersExtractor
from secret__server_provider.models.shared_memory import SecretServerProviderSharedMemory
from secret__server_provider.transformers.groups_transformer import GroupsTransformer
from secret__server_provider.transformers.roles_transformer import RolesTransformer
from secret__server_provider.transformers.folders_transformer import FoldersTransformer
from secret__server_provider.transformers.user_access_role_transformer import (
    UserAccessRoleTransformer,
)
from secret__server_provider.transformers.user_member_of_group_transformer import (
    UserMemberOfGroupTransformer,
)
from secret__server_provider.transformers.users_transformer import UsersTransformer


class SecretServerRunner(BaseAutoProviderRunner):
    ExtractorTransformersList = [
        (GroupsExtractor, GroupsTransformer),
        (UsersExtractor, UsersTransformer),
        (UserMemberOfGroupExtractor, UserMemberOfGroupTransformer),
        (RolesExtractor, RolesTransformer),
        (UserAccessRoleExtractor, UserAccessRoleTransformer),
        (FoldersExtractor, FoldersTransformer),
    ]

    def get_extractor_and_transformer_type_list(
        self,
    ) -> list[Tuple[Type[BaseExtractor], Type[BaseTransformer]]]:
        return self.ExtractorTransformersList

    def create_client(self) -> SecretServerClient:
        client_configuration: SecretServerConfiguration = self.client_configuration  # type: ignore
        return SecretServerClient(
            client_configuration=client_configuration,
        )

    def create_shared_memory(self) -> SecretServerProviderSharedMemory:
        return SecretServerProviderSharedMemory()


# '''
# - How to run all
# - Skip doesn’t work
# - Tests
# - Errors handling
# - Visualization
# - Integration with Authomize
# '''
