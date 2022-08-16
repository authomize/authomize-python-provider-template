import json
import logging
from abc import abstractmethod
from typing import Dict, Optional
from urllib.parse import quote, urljoin

import requests

from teams_provider.clients.errors import (
    AccessDeniedError,
    GatewayTimeoutException,
    ResourceNotFoundError,
    SyncErrorException,
    UnsupportedRequestError,
)
from teams_provider.clients.retry import Retry

logger = logging.getLogger(__name__)


class BaseMicrosoftHttpClient:
    """
    An HTTP base class for various Microsoft APIs.
    Handles throttling and result pagination.

    """

    def __init__(
            self,
            tenant_id: str,
            client_id: str,
            client_secret: str,
    ):
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret
        self._token: bytes = None

    # Using an impractically large number, just to ensure we aren't stuck waiting forever
    DEFAULT_TIMEOUT = 3600  # 1 hour in seconds

    @property
    def token(self) -> bytes:
        if not self._token:
            self._set_token()
        return self._token

    def _set_token(self):
        self._token = self._get_token()

    @abstractmethod
    def _get_token(self) -> bytes:
        """
        Performs the authentication processes and returns an access token

        """
        pass

    @staticmethod
    def _ask_for_token(url: str, payload: dict) -> bytes:
        """
        Util function, used by _get_token
        Performs the authentication processes and returns an access token

        """
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.post(
            url=url,
            headers=headers,
            data=payload,
            timeout=BaseMicrosoftHttpClient.DEFAULT_TIMEOUT
        )
        response_json = json.loads(response.text)
        if 'error' in response_json:
            raise ValueError(f'Token creation issue - {str(response_json["error"])}')
        return response_json['access_token'].encode('utf-8')

    @staticmethod
    def _dict_to_query_params(params: dict) -> str:
        """
        Builds and returns a query parameters string from a dict.
        E.g, `dict(top=2, count=true) -> $top=2&$count=true`

        """
        if params:
            return "&".join(f"${k}={quote(str(v))}" for k, v in params.items()).rstrip(':')
        else:
            return ''

    @property
    def _url_prefix(self) -> Optional[str]:
        """
        Returns the endpoint url of the API. E.g, `https://graph.microsoft.com/v1.0/`

        """
        return None

    def _build_url(
            self,
            url: str = None,
            complete_url: str = None,
    ) -> str:
        if complete_url:
            return complete_url
        if self._url_prefix:
            return urljoin(self._url_prefix, url)
        return url

    def _auth_header(self) -> Dict:
        """
        Builds a header with the token data

        """
        return {"Authorization": f"Bearer {self.token}"}

    @staticmethod
    def _default_headers() -> Dict:
        return {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }

    def _process_headers(self, headers) -> Dict:
        headers_ = self._default_headers()
        headers_.update(self._auth_header())
        if headers:
            headers_.update(headers)
        return headers_

    def get(
            self,
            sub_uri: str = None,
            headers: dict = None,
            params: dict = None,
            complete_url: str = None,
            to_json: bool = True,
    ) -> Dict:
        """
        A GET request to the class endpoint with the sub_uri.
        Params:
            sub_uri: appended after the class endpoint.
            e.g.  `/drive/items/01OXYKUGV6Y2GOVW7725BZO354PWSELRRZ/permissions`
            complete_url: there in case the called wishes not to use the default class' endpoint

        """
        url = self._build_url(sub_uri, complete_url)
        params_string = self._dict_to_query_params(params)
        return self._get_with_auth(
            headers=headers,
            url=url,
            params=params_string,
            to_json=to_json,
        )

    def post(
            self,
            sub_uri: str,
            headers: dict = None,
            params: dict = None,
            complete_url: str = None,
            body: dict = None,
    ) -> Dict:
        """
        Perform POST request.

        """
        url = self._build_url(sub_uri, complete_url)
        params_string = self._dict_to_query_params(params)
        body = body or {}
        return self._post_with_auth(
            headers=headers,
            url=url,
            params=params_string,
            json=body,
        )

    @staticmethod
    def _handle_success(response, to_json: bool = True):
        if not to_json:
            return response
        return response.json()

    @staticmethod
    def _check_error_code(response_json, code: str) -> bool:
        return bool(
            (isinstance(response_json, str) and code in response_json)
            or (isinstance(response_json, Dict) and response_json["error"]["code"] == code)
        )

    @staticmethod
    def _handle_client_errors(response, response_json, message):
        """Handle client errors, that we are catching, if we find anything new, base Exception will be raised."""
        if response.status_code == 404:
            raise ResourceNotFoundError(message)
        if response.status_code == 400 and BaseMicrosoftHttpClient._check_error_code(response_json,
                                                                                     "Request_UnsupportedQuery"):
            raise UnsupportedRequestError()
        if response.status_code == 403:
            raise AccessDeniedError(message)
        if response.status_code == 410 and BaseMicrosoftHttpClient._check_error_code(response_json, "resyncRequired"):
            raise SyncErrorException()
        raise Exception(message)

    @staticmethod
    def _handle_server_errors(response, create_empty_list_on_internal_error, message):
        """Handle server errors, that we are catching, if we find anything new, base Exception will be raised."""
        if response.status_code == 504:
            raise GatewayTimeoutException()
        if response.status_code in [500] and create_empty_list_on_internal_error:
            logger.warning(f'Replacing internal error with empty list for status {response.status_code}')
            return dict(value=[])
        raise Exception(message)

    @staticmethod
    def _handle_base_response(
            response: requests.Response,
            to_json: bool = True,
            **kwargs,
    ):
        """Handle API response, if we find unhandled errors, base Exception will be raised."""
        if 200 <= response.status_code < 300:
            return BaseMicrosoftHttpClient._handle_success(response, to_json)
        try:
            response_json = response.json()
        except json.decoder.JSONDecodeError:
            response_json = str(response)

        message = f"{response.status_code}: {response.url}: {response_json}"
        if 400 <= response.status_code < 500:
            return BaseMicrosoftHttpClient._handle_client_errors(response,
                                                                 response_json,
                                                                 message)
        if response.status_code >= 500:
            return BaseMicrosoftHttpClient._handle_server_errors(response, message)

        raise Exception(message)

    def _get_with_auth(
            self,
            headers=None,
            to_json: bool = True,
            **kwargs,
    ) -> dict:
        return self._get_or_post_with_auth(
            request_function=requests.get,
            headers=headers,
            to_json=to_json,
            **kwargs,
        )

    def _post_with_auth(
            self,
            headers=None,
            **kwargs,
    ) -> dict:
        return self._get_or_post_with_auth(
            request_function=requests.post,
            headers=headers,
            **kwargs,
        )

    def _get_or_post_with_auth(
            self,
            request_function,
            headers=None,
            to_json: bool = True,
            **kwargs,
    ) -> dict:
        headers_with_auth = self._process_headers(headers)
        response = Retry()(
            request_function,
            headers=headers_with_auth,
            timeout=BaseMicrosoftHttpClient.DEFAULT_TIMEOUT,
            **kwargs
        )
        if response.status_code == 401:
            self._set_token()
            headers_with_new_auth = self._process_headers(headers)
            response = Retry()(
                request_function,
                headers=headers_with_new_auth,
                timeout=BaseMicrosoftHttpClient.DEFAULT_TIMEOUT,
                **kwargs
            )
        return self._handle_base_response(
            response,
            to_json=to_json,
        )
