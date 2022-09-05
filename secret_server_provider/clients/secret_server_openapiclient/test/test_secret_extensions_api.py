"""
    Secret Server Rest API

    REST API documentation for Secret Server. This document describes how to use the REST API. All requests require an authentication token; please see the <a href=\"../OAuth/\">authentication document</a> for more information. The <a href=\"swagger.json\">Swagger specification</a> for this API is also available.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 11.2.2
    Contact: info@authomize.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import secret_server_openapiclient
from secret_server_openapiclient.api.secret_extensions_api import SecretExtensionsApi  # noqa: E501


class TestSecretExtensionsApi(unittest.TestCase):
    """SecretExtensionsApi unit test stubs"""

    def setUp(self):
        self.api = SecretExtensionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_secret_extensions_service_get_auto_fill_values(self):
        """Test case for secret_extensions_service_get_auto_fill_values

        Get AutoFill values for Url by SecretId  # noqa: E501
        """
        pass

    def test_secret_extensions_service_get_web_secret_templates(self):
        """Test case for secret_extensions_service_get_web_secret_templates

        Get Secret Templates  # noqa: E501
        """
        pass

    def test_secret_extensions_service_search(self):
        """Test case for secret_extensions_service_search

        Search Secrets by Url  # noqa: E501
        """
        pass

    def test_secret_extensions_service_search_active_directory_secrets(self):
        """Test case for secret_extensions_service_search_active_directory_secrets

        Search Secrets by Domain  # noqa: E501
        """
        pass

    def test_secret_extensions_service_search_windows_account_secrets(self):
        """Test case for secret_extensions_service_search_windows_account_secrets

        Search Secrets by Computer Name  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()