from typing import Iterable

from onelogin.api.models.user import User

from base_provider.extractors.base_extactor import BaseExtractor
from onelogin_provider.clients.onelogin_client import OneloginClient


class UsersExtractor(BaseExtractor):
    """
    Gets a list of User resources.

    See https://developers.onelogin.com/api-docs/1/users/get-users Get Users documentation
        https://developers.onelogin.com/api-docs/2/users/list-users
    """

    def extract_raw(self) -> Iterable[User]:
        data_provider_client: OneloginClient = self.data_provider_client  # type: ignore
        return data_provider_client.client.get_users()
