"""
    Secret Server Rest API

    REST API documentation for Secret Server. This document describes how to use the REST API. All requests require an authentication token; please see the <a href=\"../OAuth/\">authentication document</a> for more information. The <a href=\"swagger.json\">Swagger specification</a> for this API is also available.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 11.2.2
    Contact: info@authomize.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import secret_server_openapiclient
from secret_server_openapiclient.api.secret_template_permissions_api import SecretTemplatePermissionsApi  # noqa: E501


class TestSecretTemplatePermissionsApi(unittest.TestCase):
    """SecretTemplatePermissionsApi unit test stubs"""

    def setUp(self):
        self.api = SecretTemplatePermissionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_secret_template_permissions_service_get_template_permission_roles(self):
        """Test case for secret_template_permissions_service_get_template_permission_roles

        Get Secret Template Permission Roles  # noqa: E501
        """
        pass

    def test_secret_template_permissions_service_search(self):
        """Test case for secret_template_permissions_service_search

        Search Secret Template Permissions  # noqa: E501
        """
        pass

    def test_secret_template_permissions_service_search_template_permissions(self):
        """Test case for secret_template_permissions_service_search_template_permissions

        Get Secret Template Permissions  # noqa: E501
        """
        pass

    def test_secret_template_permissions_service_update(self):
        """Test case for secret_template_permissions_service_update

        Update Secret Templates Permissions  # noqa: E501
        """
        pass

    def test_secret_template_permissions_service_update_template_permissions(self):
        """Test case for secret_template_permissions_service_update_template_permissions

        Update Secret Template Type Permissions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
