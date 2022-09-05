from typing import Tuple, Type

from base_provider.extractors.base_extractor import BaseExtractor
from base_provider.transformers.base_transformer import BaseTransformer
from base_provider.workflows.base_auto_runner import BaseAutoProviderRunner
from secret_server_provider.clients.secret_server_client import SecretServerClient
from secret_server_provider.configuration.client_configuration import SecretServerConfiguration
from secret_server_provider.extractors.folder_to_secrets_extractor import FolderToSecretsExtractor
from secret_server_provider.extractors.folders_extractor import FoldersExtractor
from secret_server_provider.extractors.group_has_role_extractor import GroupHasRoleExtractor
from secret_server_provider.extractors.groups_extractor import GroupsExtractor
from secret_server_provider.extractors.roles_extractor import RolesExtractor
from secret_server_provider.extractors.secrets_extractor import SecretsExtractor
from secret_server_provider.extractors.secrets_last_access_key_extractor import (
    SecretsLastAccessKeyExtractor,
)
from secret_server_provider.extractors.user_has_role_extractor import UserHasRoleExtractor
from secret_server_provider.extractors.user_member_of_group_extractor import (
    UserMemberOfGroupExtractor,
)
from secret_server_provider.extractors.user_or_group_access_role_secret_extractor import (
    UserOrGroupAccessRoleToSecretExtractor,
)
from secret_server_provider.extractors.user_or_group_access_role_to_folder_extractor import (
    UserOrGroupAccessRoleToFolderExtractor,
)
from secret_server_provider.extractors.users_extractor import UsersExtractor
from secret_server_provider.models.shared_memory import SecretServerProviderSharedMemory
from secret_server_provider.transformers.folder_to_secrets_transformer import (
    FoldersToSecretsTransformer,
)
from secret_server_provider.transformers.folders_transformer import FoldersTransformer
from secret_server_provider.transformers.group_has_role_transformer import GroupHasRoleTransformer
from secret_server_provider.transformers.groups_transformer import GroupsTransformer
from secret_server_provider.transformers.roles_transformer import RolesTransformer
from secret_server_provider.transformers.secrets_last_access_key_transformer import (
    SecretsLastAccessKeyTransformer,
)
from secret_server_provider.transformers.secrets_transformer import SecretsTransformer
from secret_server_provider.transformers.user_has_role_transformer import UserHasRoleTransformer
from secret_server_provider.transformers.user_member_of_group_transformer import (
    UserMemberOfGroupTransformer,
)
from secret_server_provider.transformers.user_or_group_access_role_secret_transformer import (
    UserOrGroupAccessRoleToSecretTransformer,
)
from secret_server_provider.transformers.user_or_group_access_role_to_folder_transformer import (
    UserOrGroupAccessRoleToFolderTransformer,
)
from secret_server_provider.transformers.users_transformer import UsersTransformer


class SecretServerRunner(BaseAutoProviderRunner):
    ExtractorTransformersList = [
        (UsersExtractor, UsersTransformer),
        (GroupsExtractor, GroupsTransformer),
        (RolesExtractor, RolesTransformer),
        (SecretsExtractor, SecretsTransformer),
        (FoldersExtractor, FoldersTransformer),
        (UserMemberOfGroupExtractor, UserMemberOfGroupTransformer),
        (UserHasRoleExtractor, UserHasRoleTransformer),
        (GroupHasRoleExtractor, GroupHasRoleTransformer),
        (UserOrGroupAccessRoleToSecretExtractor, UserOrGroupAccessRoleToSecretTransformer),
        (UserOrGroupAccessRoleToFolderExtractor, UserOrGroupAccessRoleToFolderTransformer),
        (FolderToSecretsExtractor, FoldersToSecretsTransformer),
        (SecretsLastAccessKeyExtractor, SecretsLastAccessKeyTransformer),
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
