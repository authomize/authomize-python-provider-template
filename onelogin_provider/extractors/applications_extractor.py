from typing import Iterable

from onelogin.api.models.app import App

from base_provider import BaseExtractor
from onelogin_provider.clients.onelogin_client import OneloginClient


class ApplicationsExtactor(BaseExtractor):
    """
    Gets a list of all Apps in a OneLogin account.

    See https://developers.onelogin.com/api-docs/1/apps/get-apps Get Apps documentation
        https://developers.onelogin.com/api-docs/2/apps/list-apps
    """

    def extact_raw(self) -> Iterable[App]:
        data_provider_client: OneloginClient = self.data_provider_client  # type: ignore
        return data_provider_client.client.get_apps()
