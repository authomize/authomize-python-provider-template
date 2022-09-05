from typing import Iterable, List, Tuple

from onelogin.api.models.otp_device import OTP_Device
from onelogin.api.models.user import User

from base_provider.extractors.base_extractor import BaseExtractor
from onelogin_provider.clients.onelogin_client import OneloginClient


class UsersExtractor(BaseExtractor):
    """
    Gets a list of User resources.
    For every user, get enrolled devices (MFA)

    See https://developers.onelogin.com/api-docs/1/users/get-users
        https://developers.onelogin.com/api-docs/2/users/list-users
        https://developers.onelogin.com/api-docs/1/multi-factor-authentication/enrolled-factors
        https://developers.onelogin.com/api-docs/2/multi-factor-authentication/enrolled-factors
    """

    def extract_raw(self) -> Iterable[Tuple[User, List[OTP_Device]]]:
        data_provider_client: OneloginClient = self.data_provider_client  # type: ignore
        users: Iterable[User] = data_provider_client.client.get_users()
        for user in users:
            enrolled_factors: List[OTP_Device] = list(
                data_provider_client.client.get_enrolled_factors(user_id=user.id),
            )
            yield (user, enrolled_factors)
