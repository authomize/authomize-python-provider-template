from csv import field_size_limit
from typing import Iterable

from secret_server_openapiclient.apis import SecretsApi

from base_provider.extractors.base_extractor import BaseExtractor
from secret_server_provider.clients.secret_server_client import SecretServerClient
from secret_server_provider.normalize_id import normalize_id
from secret_server_provider.paginator import get_paginated_results


class SecretsLastAccessKeyExtractor(BaseExtractor):
    """
    Gets a history of the access-key field values through internal API
    For now the access-key and secret-key are assumed to exist in the
    secret's template which is not neccessary so
    The field name should be fetched from the secret template
    The returned dictionary contains records looking like this :
    {
            "attachmentId": 0,
            "secretItemHistoryId": 72,
            "date": "2022-08-29T12:35:50.707",
            "itemValueNew": "abc12345",
            "itemFileSize": null
    }
    """
    predefined_interesting_keys = ["access-key", "username"]
    def extract_raw(self) -> Iterable[tuple[str, dict, str]]:
        data_provider_client: SecretServerClient = self.data_provider_client
        api_instance = SecretsApi(data_provider_client.openapi_client)
        all_secrets = get_paginated_results(api_instance.secrets_service_search_v2)
        for secret in all_secrets:
            normalized_secret_id = normalize_id(secret.id)
            all_input_keys = []
            for field_key in data_provider_client.client_configuration.keys_to_fetch.split(','):
                all_input_keys.append(field_key)
                yield from self.get_records_by_slug(normalized_secret_id, field_key)
            for field_key in self.predefined_interesting_keys:
                if field_key not in all_input_keys:
                    yield from self.get_records_by_slug(normalized_secret_id, field_key)

    def get_records_by_slug(self, secret_id: str, slug: str) -> Iterable[tuple[str, dict, str]]:
        key_history = self.get_secret_access_key_history(secret_id, slug)
        key_records = key_history['records']
        for key_record in key_records:
            yield (secret_id, key_record, slug)

    def get_secret_access_key_history(self, secret_id: str, slug: str) -> dict:
        """Get secret access key history"""
        # TODO read slug from secret's template
        data_provider_client: SecretServerClient = self.data_provider_client
        response = data_provider_client.internal_api_client.post_internal_api(
            url_path=f'secret-audits/{secret_id}/fields/{slug}',
        )
        try:
            response.raise_for_status()
            return response.json()
        except Exception as e:
            if "API_SecretFieldNotFound" in str(e):
                self.logger.info("Secret {id} has no {slug}s", id=secret_id, slug=slug)
                return {"records": []}
            if "NoAccessKey" in str(e):
                self.logger.info("Secret {id} has no {slug}s", id=secret_id, slug=slug)
                return {"records": []}
            raise
