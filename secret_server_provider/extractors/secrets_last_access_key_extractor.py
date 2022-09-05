from typing import Iterable

from secret_server_openapiclient.apis import SecretsApi

from base_provider.extractors.base_extractor import BaseExtractor
from secret_server_provider.clients.secret_server_client import SecretServerClient
from secret_server_provider.normalize_id import normalize_id
from secret_server_provider.paginator import get_paginated_results


class SecretsLastAccessKeyExtractor(BaseExtractor):
    """
    Gets a history of the access-key field values through internal API
    For now the access-key is assumed to exist in the secret's template which is not neccessary so
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

    def extract_raw(self) -> Iterable[tuple[str, dict]]:
        data_provider_client: SecretServerClient = self.data_provider_client
        api_instance = SecretsApi(data_provider_client.openapi_client)
        all_secrets = get_paginated_results(api_instance.secrets_service_search_v2)
        for secret in all_secrets:
            normalized_secret_id = normalize_id(secret.id)
            access_key_history = self.get_secret_access_key_history(normalized_secret_id)
            access_key_records = access_key_history['records']
            for access_key_record in access_key_records:
                yield (normalized_secret_id, access_key_record)

    def get_secret_access_key_history(self, secret_id: str) -> dict:
        """Get secret access key history"""
        # TODO read slug from secret's template
        data_provider_client: SecretServerClient = self.data_provider_client
        slug = "access-key"
        response = data_provider_client.internal_api_client.post_internal_api(
            url_path=f'/secret-audits/{secret_id}/fields/{slug}',
        )
        try:
            response.raise_for_status()
            return response.json()
        except Exception as e:
            if "API_SecretFieldNotFound" in str(e):
                self.logger.info("Secret {secret} has no access-keys", secret=secret_id)
                return {"records": []}
            if "NoAccessKey" in str(e):
                self.logger.info("Secret {secret} has no access-keys", secret=secret_id)
                return {"records": []}
            raise
