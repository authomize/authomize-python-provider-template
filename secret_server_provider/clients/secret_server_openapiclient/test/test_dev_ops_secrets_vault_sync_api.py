"""
    Secret Server Rest API

    REST API documentation for Secret Server. This document describes how to use the REST API. All requests require an authentication token; please see the <a href=\"../OAuth/\">authentication document</a> for more information. The <a href=\"swagger.json\">Swagger specification</a> for this API is also available.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 11.2.2
    Contact: info@authomize.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import secret_server_openapiclient
from secret_server_openapiclient.api.dev_ops_secrets_vault_sync_api import DevOpsSecretsVaultSyncApi  # noqa: E501


class TestDevOpsSecretsVaultSyncApi(unittest.TestCase):
    """DevOpsSecretsVaultSyncApi unit test stubs"""

    def setUp(self):
        self.api = DevOpsSecretsVaultSyncApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_dev_ops_secrets_vault_sync_service_create_sync(self):
        """Test case for dev_ops_secrets_vault_sync_service_create_sync

        Create a DevOps sync for a secret.  # noqa: E501
        """
        pass

    def test_dev_ops_secrets_vault_sync_service_get_sync_status(self):
        """Test case for dev_ops_secrets_vault_sync_service_get_sync_status

        Information about secret syncing.  # noqa: E501
        """
        pass

    def test_dev_ops_secrets_vault_sync_service_get_sync_statuses(self):
        """Test case for dev_ops_secrets_vault_sync_service_get_sync_statuses

        Information about secrets syncing.  # noqa: E501
        """
        pass

    def test_dev_ops_secrets_vault_sync_service_sync_secret(self):
        """Test case for dev_ops_secrets_vault_sync_service_sync_secret

        Sync a secret.  # noqa: E501
        """
        pass

    def test_dev_ops_secrets_vault_sync_service_update_sync(self):
        """Test case for dev_ops_secrets_vault_sync_service_update_sync

        Update a secret sync.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
