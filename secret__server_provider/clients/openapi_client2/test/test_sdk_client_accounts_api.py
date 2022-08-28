"""
    Secret Server Rest API

    REST API documentation for Secret Server. This document describes how to use the REST API. All requests require an authentication token; please see the <a href=\"../OAuth/\">authentication document</a> for more information. The <a href=\"swagger.json\">Swagger specification</a> for this API is also available.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 11.2.2
    Contact: info@authomize.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import plugins
from plugins.api.sdk_client_accounts_api import SdkClientAccountsApi  # noqa: E501


class TestSdkClientAccountsApi(unittest.TestCase):
    """SdkClientAccountsApi unit test stubs"""

    def setUp(self):
        self.api = SdkClientAccountsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sdk_client_accounts_service_create_client_account(self):
        """Test case for sdk_client_accounts_service_create_client_account

        Create SDK Client Account  # noqa: E501
        """
        pass

    def test_sdk_client_accounts_service_get(self):
        """Test case for sdk_client_accounts_service_get

        Get SDK Client Account  # noqa: E501
        """
        pass

    def test_sdk_client_accounts_service_get_enabled(self):
        """Test case for sdk_client_accounts_service_get_enabled

        Get Current State  # noqa: E501
        """
        pass

    def test_sdk_client_accounts_service_revoke(self):
        """Test case for sdk_client_accounts_service_revoke

        Revoke SDK Client Account  # noqa: E501
        """
        pass

    def test_sdk_client_accounts_service_search_client_accounts(self):
        """Test case for sdk_client_accounts_service_search_client_accounts

        Search SDK Client Accounts  # noqa: E501
        """
        pass

    def test_sdk_client_accounts_service_toggle_enabled(self):
        """Test case for sdk_client_accounts_service_toggle_enabled

        Toggle Current State  # noqa: E501
        """
        pass

    def test_sdk_client_accounts_service_update_client_account(self):
        """Test case for sdk_client_accounts_service_update_client_account

        Update SDK Client Account  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
