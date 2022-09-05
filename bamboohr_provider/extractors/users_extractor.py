from typing import Iterable

from bamboohr_provider.clients.bamboohr_client import BamboohrClient
from bamboohr_provider.models.users import USER_MODEL_FIELDS
from base_provider.extractors.base_extractor import BaseExtractor


class UsersExtractor(BaseExtractor):
    """
    Gets a list of User resources.

    See https://developers.bamboohr.com/api-docs/1/users/get-users Get Users documentation
        https://developers.bamboohr.com/api-docs/2/users/list-users
    """

    def extract_raw(self) -> Iterable[dict]:
        """Fetch BambooHR users

        Get users list using custom report api, as suggested by bamboohr

        API: https://documentation.bamboohr.com/reference/request-custom-report-1
        Fields: https://documentation.bamboohr.com/docs/list-of-field-names

        @param client: BasicClient REST API session
        @return: Iterable[Dict]
        """
        data_provider_client: BamboohrClient = self.data_provider_client  # type: ignore
        result = openapi_client.get_users(fields_to_fetch=USER_MODEL_FIELDS)
        return result["employees"]
