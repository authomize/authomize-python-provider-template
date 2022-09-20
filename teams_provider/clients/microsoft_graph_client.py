import logging
from typing import Dict, Generator, Optional

from teams_provider.clients.base_client import BaseMicrosoftHttpClient
from teams_provider.clients.data_link_model import DataLink

logger = logging.getLogger(__name__)


class MicrosoftGraphClient(BaseMicrosoftHttpClient):
    """
    Microsoft Graph API client
    Read about it: https://docs.microsoft.com/en-us/graph/overview

    """

    @property
    def _url_prefix(self) -> str:
        return 'https://graph.microsoft.com/v1.0/'

    def _get_token(self):
        url = f"https://login.microsoftonline.com/{self.tenant_id}/oauth2/v2.0/token"
        payload = {
            "client_id": self.client_id,
            "scope": "https://graph.microsoft.com/.default",
            "client_secret": self.client_secret,
            "grant_type": "client_credentials",
        }

        token = self._ask_for_token(url=url, payload=payload)
        if not token:
            raise Exception('Failed to get MicrosoftGraphClient token')
        return token.decode('utf-8')

    def get_all_items(
            self,
            sub_uri: str = None,
            complete_url: str = None,
            headers: dict = None,
            params: dict = None,
    ) -> Generator[Dict, bool, Optional[DataLink]]:
        """
        Method for handling lists requests - including pagination

        Method for handling delta API GET requests and response. Use only for delta compatible
        resources, with the relevant sub_uri.
        See: https://docs.microsoft.com/en-us/graph/delta-query-overview

        Params:
            sub_uri: the uri to query under the graph API endpoint https://graph.microsoft.com/v1.0/
                Each result is also tagged with the sub_uri so it can be identified by the caller.
            headers: additional request headers
            params: query parameters, converted to the $param=value& format
            complete_url: allows to override endpoint URL
            tag: a tag to add to the results for the caller's convenience

        Yields: a generator of results (dict)
        Returns: (as StopIteration) the deltaLink
        """

        response = self.get(
            sub_uri=sub_uri,
            headers=headers,
            params=params,
            complete_url=complete_url,
        )
        # To help identify the result
        for result in response['value']:
            result['sub_uri'] = sub_uri
            yield result
        while '@odata.nextLink' in response:
            data_link = DataLink(
                url=response['@odata.nextLink'],
                has_new_data=True,
            )
            response = self.get(
                complete_url=data_link.url,
                headers=headers,
            )
            yield from response['value']

    def get_one_item(
            self,
            sub_uri: str = None,
            headers: dict = None,
            params: dict = None,
            complete_url: str = None,
    ):
        response = self.get(
            sub_uri=sub_uri,
            headers=headers,
            params=params,
            complete_url=complete_url
        )
        return response


class MicrosoftBetaGraphClient(MicrosoftGraphClient):
    @property
    def _url_prefix(self) -> str:
        return 'https://graph.microsoft.com/beta/'
