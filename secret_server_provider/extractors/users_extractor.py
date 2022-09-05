from encodings import search_function
from typing import Iterable

from secret_server_openapiclient.apis import UsersApi
from secret_server_openapiclient.model.user_summary import UserSummary

from base_provider.extractors.base_extractor import BaseExtractor
from secret_server_provider.clients.secret_server_client import SecretServerClient
from secret_server_provider.paginator import get_paginated_results


class UsersExtractor(BaseExtractor):
    """
    Gets a list of User records.

    See docs/UsersApi.md#users_service_search_users
    """

    def extract_raw(self) -> Iterable[UserSummary]:
        data_provider_client: SecretServerClient = self.data_provider_client
        api_instance = UsersApi(data_provider_client.openapi_client)
        # paginated results
        # return self.__get_paginated_results(api_instance)
        return get_paginated_results(api_instance.users_service_search_users)

