import structlog
from typing import Iterable

from base_provider.extractors.base_extractor import BaseExtractor
from secret_server_provider.clients.secret_server_client import SecretServerClient
from secret_server_provider.normalize_id import normalize_id

from secret_server_openapiclient.apis import SecretPermissionsApi, UsersApi
from secret_server_openapiclient.model.secret_permission_model import SecretPermissionModel
from secret_server_openapiclient.model.user_model import UserModel
logger = structlog.get_logger()

class UserAccessRoleExtractor(BaseExtractor):
    """
    Gets a list of access role records.
    See docs/UsersApi.md#users_service_search_users
    """
    logger = logger.bind(loader_name="UserAccessRoleExtractor")
    def extract_raw(self) -> Iterable[SecretPermissionModel]:
        data_provider_client: SecretServerClient = self.data_provider_client
        api_instance = UsersApi(data_provider_client.client)
        secret_instance = SecretPermissionsApi(data_provider_client.client)
        # TODO : errors handling
        api_response = api_instance.users_service_search_users()
        all_users = api_response.records
        
        for user in all_users:
            try:
                response = self._fetch_secret_permissions(secret_instance, user)
            except Exception as e:
                if "API_AccessDenied" in str(e):
                    self.logger.info("Got API_AccessDenied in secret_permissions_service_get for id {user_id}", user_id=user.id)
                else:
                    if "API_SecretPermissionDoesNotExist" in str(e):
                        self.logger.info("Got API_SecretPermissionDoesNotExist in secret_permissions_service_get for id {user_id}", user_id=user.id)
                    else:
                        self.logger.error("Got exception : {exception}", exception=str(e))
            else:
                yield response

    def _fetch_secret_permissions(self, api_instance: SecretPermissionsApi, user: UserModel) -> Iterable[SecretPermissionModel]:
        return api_instance.secret_permissions_service_get(id=normalize_id(user.id))
        
