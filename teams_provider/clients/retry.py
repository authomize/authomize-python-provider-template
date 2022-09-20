import logging
from json import JSONDecodeError
from random import random
from time import sleep

from requests.exceptions import ConnectionError
from urllib3.exceptions import ProtocolError

logger = logging.getLogger(__name__)


SHOULD_RETRY = {'should-retry': True, 'headers': []}
SHOULD_RETRY_BATCH = [SHOULD_RETRY]


class Retry:
    MAX_RETRIES = 6

    def __init__(self):
        self.attempt = 0

    def __call__(self, function, *args, **kwargs):
        fail_without_retry = False
        error = None
        try:
            response = function(*args, **kwargs)
        except (ProtocolError, ConnectionError) as e:
            response = SHOULD_RETRY
            fail_without_retry = True
            error = e
        if self._should_retry(response):
            self.attempt += 1
            delay = self._get_delay(response)
            logging.info(f'Sleeping {delay}s for the {self.attempt}st time for non batch request')
            sleep(delay)
            logging.info(f'Done sleeping {delay}s for the {self.attempt}st time for non batch request')
            return self.__call__(function, *args, **kwargs)
        elif fail_without_retry:
            logging.error('Failed retrying for non batch request')
            raise error
        return response

    def call_batch(self, function, *args, **kwargs):
        fail_without_retry = False
        error = None
        try:
            responses = function(*args, **kwargs)
        except ProtocolError as e:
            responses = SHOULD_RETRY_BATCH
            fail_without_retry = True
            error = e
        if self._should_retry_batch(responses):
            self.attempt += 1
            delay = self._get_delay_batch(responses)
            logging.info(f'Sleeping {delay}s for the {self.attempt}st time for batch request')
            sleep(delay)
            logging.info(f'Done sleeping {delay}s for the {self.attempt}st time for batch request')
            return self.call_batch(function, *args, **kwargs)
        elif fail_without_retry:
            logging.error('Failed retrying for batch request')
            raise error
        return responses

    def _should_retry(self, response) -> bool:
        if self.attempt >= Retry.MAX_RETRIES:
            return False
        if response is SHOULD_RETRY:
            return True
        status = getattr(response, 'status_code', None) or response['status']

        response_json = {}
        if isinstance(response, dict):
            response_json = response
        else:
            try:
                response_json = response.json()
            except JSONDecodeError as e:
                # Note: this point is reached when we get a csv data in response.text
                logger.warning(f'Could not jsonify the response: ({e})', extra={'response': response.text})

        if status == 500 and response_json.get("error", {}).get("code") == "AF50005":
            return True
        return status in (429, 503, 401)

    def _get_delay(self, response):
        headers = getattr(response, 'headers', None) or response.get('headers')
        if headers and 'Retry-After' in headers:
            return int(headers['Retry-After']) + random()

        return round(0.5 * (2 ** self.attempt - 1)) + random()

    def _should_retry_batch(self, responses):
        if self.attempt >= Retry.MAX_RETRIES:
            return False
        if responses is SHOULD_RETRY_BATCH:
            return True
        return any(self._should_retry(response) for response in responses)

    def _get_delay_batch(self, responses):
        return max(
            self._get_delay(response) if self._should_retry(response) else 0
            for response
            in responses
        )
