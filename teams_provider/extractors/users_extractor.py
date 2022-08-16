from typing import Iterator, Dict

from base_provider.extractors.base_extractor import BaseExtractor
from teams_provider.clients.microsoft_client import MicrosoftClient


class UsersExtractor(BaseExtractor):
    """
    Gets a list of User resources.

    See https://developers.onelogin.com/api-docs/1/users/get-users Get Users documentation
        https://developers.onelogin.com/api-docs/2/users/list-users
    """

    def extract_raw(self) -> Iterator[Dict]:
        data_provider_client: MicrosoftClient = self.data_provider_client  # type: ignore
        users = data_provider_client.client.get_all_items(
            'users',
            params={'select': 'userType,displayName,mail,externalUserState'}
        )
        for user in users:
            if user['externalUserState'] == 'PendingAcceptance':
                # User is not actually "in" yet - e.g. "PendingAcceptance"
                continue
            elif user['externalUserState'] == 'Accepted':
                user['userType'] = 'External'
            user.pop('externalUserState')
            yield user
