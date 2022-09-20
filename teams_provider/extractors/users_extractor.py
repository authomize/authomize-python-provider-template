from typing import Iterator, Dict

from base_provider.extractors.base_extractor import BaseExtractor
from teams_provider.clients.microsoft_client import MicrosoftClient
from teams_provider.constants import USER_ATTRIBUTES


class UsersExtractor(BaseExtractor):
    """
    Gets a list of User resources.
    """

    def extract_raw(self) -> Iterator[Dict]:
        data_provider_client: MicrosoftClient = self.data_provider_client  # type: ignore
        users = data_provider_client.client.get_all_items(
            'users',
            params={'select': USER_ATTRIBUTES}
        )
        yield from users
