"""
    Secret Server Rest API

    REST API documentation for Secret Server. This document describes how to use the REST API. All requests require an authentication token; please see the <a href=\"../OAuth/\">authentication document</a> for more information. The <a href=\"swagger.json\">Swagger specification</a> for this API is also available.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 11.2.2
    Contact: info@authomize.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import plugins
from plugins.api.ip_address_restrictions_api import IpAddressRestrictionsApi  # noqa: E501


class TestIpAddressRestrictionsApi(unittest.TestCase):
    """IpAddressRestrictionsApi unit test stubs"""

    def setUp(self):
        self.api = IpAddressRestrictionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_ip_address_restrictions_service_create(self):
        """Test case for ip_address_restrictions_service_create

        Create IP Address restriction  # noqa: E501
        """
        pass

    def test_ip_address_restrictions_service_create_group_ip_restriction(self):
        """Test case for ip_address_restrictions_service_create_group_ip_restriction

        Create Group IP Address restriction  # noqa: E501
        """
        pass

    def test_ip_address_restrictions_service_create_user_ip_restriction(self):
        """Test case for ip_address_restrictions_service_create_user_ip_restriction

        Create User IP Address restriction  # noqa: E501
        """
        pass

    def test_ip_address_restrictions_service_delete(self):
        """Test case for ip_address_restrictions_service_delete

        Delete IP Address restriction  # noqa: E501
        """
        pass

    def test_ip_address_restrictions_service_delete_group_ip_restriction(self):
        """Test case for ip_address_restrictions_service_delete_group_ip_restriction

        Delete Group IP Address restriction  # noqa: E501
        """
        pass

    def test_ip_address_restrictions_service_delete_user_ip_restriction(self):
        """Test case for ip_address_restrictions_service_delete_user_ip_restriction

        Delete User IP Address restriction  # noqa: E501
        """
        pass

    def test_ip_address_restrictions_service_get(self):
        """Test case for ip_address_restrictions_service_get

        Get IP Address restriction  # noqa: E501
        """
        pass

    def test_ip_address_restrictions_service_get_all_by_group(self):
        """Test case for ip_address_restrictions_service_get_all_by_group

        Search IP Address restrictions assigned to a group  # noqa: E501
        """
        pass

    def test_ip_address_restrictions_service_get_all_by_user(self):
        """Test case for ip_address_restrictions_service_get_all_by_user

        Search IP Address restrictions assigned to a user  # noqa: E501
        """
        pass

    def test_ip_address_restrictions_service_get_group(self):
        """Test case for ip_address_restrictions_service_get_group

        Get Group IP Address restriction  # noqa: E501
        """
        pass

    def test_ip_address_restrictions_service_get_user_ip_restriction(self):
        """Test case for ip_address_restrictions_service_get_user_ip_restriction

        Get User IP Address restriction  # noqa: E501
        """
        pass

    def test_ip_address_restrictions_service_search(self):
        """Test case for ip_address_restrictions_service_search

        Search IP Address restrictions  # noqa: E501
        """
        pass

    def test_ip_address_restrictions_service_search_groups(self):
        """Test case for ip_address_restrictions_service_search_groups

        Search groups assigned to an IP Address restriction  # noqa: E501
        """
        pass

    def test_ip_address_restrictions_service_search_users(self):
        """Test case for ip_address_restrictions_service_search_users

        Search users assigned to an IP Address restriction  # noqa: E501
        """
        pass

    def test_ip_address_restrictions_service_update(self):
        """Test case for ip_address_restrictions_service_update

        Update IP Address restriction  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
