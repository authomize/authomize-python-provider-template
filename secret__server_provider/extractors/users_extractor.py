from typing import Iterable

from plugins.apis import UsersApi
from plugins.model.user_model import UserModel

from base_provider.extractors.base_extractor import BaseExtractor
from secret__server_provider.clients.secret_server_client import SecretServerClient

class UsersExtactor(BaseExtractor):
    """
    Gets a list of User records.

    See docs/UsersApi.md#users_service_search_users
    """

    def extact_raw(self) -> Iterable[UserModel]:
        data_provider_client: SecretServerClient = self.data_provider_client 
        api_instance = UsersApi(data_provider_client)

        # TODO : errors handling
        api_response = api_instance.users_service_search_users()
        all_users = api_response.records()
        '''
        TODO:make skip work later
        while (api_response.hasNext) :
            api_response = api_instance.users_service_search_users(skip = 10)
            all_users.extend(api_response.records())
        '''
        # TODO : run for earch user GET v1/users/<id>/groups to add to the user info
        # this will extract the groupName - differs from v1/groups which is actually v1/roles...
        return all_users
