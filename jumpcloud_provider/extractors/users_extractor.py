from typing import Iterable, cast

from jcapiv1 import SystemusersApi, Systemuserreturn

from jumpcloud_provider.extractors import JumpcloudApiResult
from jumpcloud_provider.extractors.jumpcloud_extractor import JumpcloudExtractor


class UsersExtractor(JumpcloudExtractor):
    """
    Gets a list of User resources.

    See https://docs.jumpcloud.com/api/1.0/index.html#tag/Systemusers Get Users documentation
        https://github.com/TheJumpCloud/jcapi-python/blob/master/jcapiv1/jcapiv1/api/systemusers_api.py
    """

    def extract_raw(self) -> Iterable[Systemuserreturn]:
        users_client = SystemusersApi(self.jumpcloud_client.client_v1)
        pagination_api = self._call_users_api(users_client)
        system_users = self.extract_with_pagination(pagination_api)
        return cast(Iterable[Systemuserreturn], system_users)

    def _call_users_api(self, users_client: SystemusersApi) -> JumpcloudApiResult:
        client_configuration = self.client_configuration
        return lambda skip: users_client.systemusers_list(
            skip=skip,
            limit=client_configuration.limit,
            accept=client_configuration.accept,
            content_type=client_configuration.content_type
        )

