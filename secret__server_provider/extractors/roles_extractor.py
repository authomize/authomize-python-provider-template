from typing import Iterable

from ..openapi_client.plugins.apis import RolesApi
from ..openapi_client.plugins.model.role_model import RoleModel

from base_provider.extractors.base_extractor import BaseExtractor
from secret__server_provider.clients.secret_server_client import SecretServerClient

class RolesExtactor(BaseExtractor):
    """
    Gets a list of Roles records.

    See docs/RolesApi.md#roles_service_get_all
    """

    def extact_raw(self) -> Iterable[RoleModel]:
        data_provider_client: SecretServerClient = self.data_provider_client 
        api_instance = RolesApi(data_provider_client)

        # TODO : errors handling
        api_response = api_instance.roles_service_get_all()
        all_roles = api_response.records()
        '''
        TODO:make skip work later
        while (api_response.hasNext) :
            api_response = api_instance.roles_service_get_all(skip = 10)
            all_roles.extend(api_response.records())        
        '''
        return all_roles
