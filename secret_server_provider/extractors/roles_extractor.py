from typing import Iterable

from secret_server_openapiclient.apis import RolesApi
from secret_server_openapiclient.model.role_model import RoleModel

from base_provider.extractors.base_extractor import BaseExtractor
from secret_server_provider.clients.secret_server_client import SecretServerClient
from secret_server_provider.paginator import get_paginated_results


class RolesExtractor(BaseExtractor):
    """
    Gets a list of Roles records.

    See docs/RolesApi.md#roles_service_get_all
    """

    def extract_raw(self) -> Iterable[RoleModel]:
        data_provider_client: SecretServerClient = self.data_provider_client
        api_instance = RolesApi(data_provider_client.openapi_client)

        return get_paginated_results(api_instance.roles_service_get_all)
