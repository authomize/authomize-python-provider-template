"""
    Secret Server Rest API

    REST API documentation for Secret Server. This document describes how to use the REST API. All requests require an authentication token; please see the <a href=\"../OAuth/\">authentication document</a> for more information. The <a href=\"swagger.json\">Swagger specification</a> for this API is also available.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 11.2.2
    Contact: info@authomize.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import secret_server_openapiclient
from secret_server_openapiclient.api.categorized_lists_api import CategorizedListsApi  # noqa: E501


class TestCategorizedListsApi(unittest.TestCase):
    """CategorizedListsApi unit test stubs"""

    def setUp(self):
        self.api = CategorizedListsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_categorized_lists_service_add_item_to_list(self):
        """Test case for categorized_lists_service_add_item_to_list

        Adds an option to a list  # noqa: E501
        """
        pass

    def test_categorized_lists_service_add_items_to_list(self):
        """Test case for categorized_lists_service_add_items_to_list

        Adds options to a list  # noqa: E501
        """
        pass

    def test_categorized_lists_service_add_items_to_list_from_file(self):
        """Test case for categorized_lists_service_add_items_to_list_from_file

        Upload a file of list options  # noqa: E501
        """
        pass

    def test_categorized_lists_service_add_items_to_list_with_category(self):
        """Test case for categorized_lists_service_add_items_to_list_with_category

        Adds options to the list with the specified category  # noqa: E501
        """
        pass

    def test_categorized_lists_service_create_list(self):
        """Test case for categorized_lists_service_create_list

        Create a list  # noqa: E501
        """
        pass

    def test_categorized_lists_service_delete_list(self):
        """Test case for categorized_lists_service_delete_list

        Delete List  # noqa: E501
        """
        pass

    def test_categorized_lists_service_get_all_lists_user_may_see(self):
        """Test case for categorized_lists_service_get_all_lists_user_may_see

        Get a list of lists available to current user  # noqa: E501
        """
        pass

    def test_categorized_lists_service_get_categories_for_list(self):
        """Test case for categorized_lists_service_get_categories_for_list

        Get a list's current categories  # noqa: E501
        """
        pass

    def test_categorized_lists_service_get_list(self):
        """Test case for categorized_lists_service_get_list

        Get a list  # noqa: E501
        """
        pass

    def test_categorized_lists_service_get_list_items(self):
        """Test case for categorized_lists_service_get_list_items

        Get a list's items  # noqa: E501
        """
        pass

    def test_categorized_lists_service_remove_item_from_list(self):
        """Test case for categorized_lists_service_remove_item_from_list

        Delete a list option from a list  # noqa: E501
        """
        pass

    def test_categorized_lists_service_remove_items_from_list(self):
        """Test case for categorized_lists_service_remove_items_from_list

        Delete all list options from a list  # noqa: E501
        """
        pass

    def test_categorized_lists_service_replace_items_in_list(self):
        """Test case for categorized_lists_service_replace_items_in_list

        Replaces options in a list  # noqa: E501
        """
        pass

    def test_categorized_lists_service_search(self):
        """Test case for categorized_lists_service_search

        Search Lists  # noqa: E501
        """
        pass

    def test_categorized_lists_service_search_list_audit(self):
        """Test case for categorized_lists_service_search_list_audit

        Get Audits for List  # noqa: E501
        """
        pass

    def test_categorized_lists_service_update_item_in_list(self):
        """Test case for categorized_lists_service_update_item_in_list

        Updates an option in a list  # noqa: E501
        """
        pass

    def test_categorized_lists_service_update_items_in_list(self):
        """Test case for categorized_lists_service_update_items_in_list

        Updates options in a list  # noqa: E501
        """
        pass

    def test_categorized_lists_service_update_list(self):
        """Test case for categorized_lists_service_update_list

        Update a list  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
