"""
    Secret Server Rest API

    REST API documentation for Secret Server. This document describes how to use the REST API. All requests require an authentication token; please see the <a href=\"../OAuth/\">authentication document</a> for more information. The <a href=\"swagger.json\">Swagger specification</a> for this API is also available.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 11.2.2
    Contact: info@authomize.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import secret_server_openapiclient
from secret_server_openapiclient.api.inbox_rules_api import InboxRulesApi  # noqa: E501


class TestInboxRulesApi(unittest.TestCase):
    """InboxRulesApi unit test stubs"""

    def setUp(self):
        self.api = InboxRulesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_inbox_rules_service_copy_inbox_rule(self):
        """Test case for inbox_rules_service_copy_inbox_rule

        Copy Inbox Rule  # noqa: E501
        """
        pass

    def test_inbox_rules_service_create_inbox_rule(self):
        """Test case for inbox_rules_service_create_inbox_rule

        Create Inbox Rule  # noqa: E501
        """
        pass

    def test_inbox_rules_service_create_inbox_rule_condition(self):
        """Test case for inbox_rules_service_create_inbox_rule_condition

        Create Inbox Rule Condition  # noqa: E501
        """
        pass

    def test_inbox_rules_service_get_inbox_rule(self):
        """Test case for inbox_rules_service_get_inbox_rule

        Get Inbox Rule  # noqa: E501
        """
        pass

    def test_inbox_rules_service_get_inbox_rule_condition(self):
        """Test case for inbox_rules_service_get_inbox_rule_condition

        Get Inbox Rule Condition  # noqa: E501
        """
        pass

    def test_inbox_rules_service_get_inbox_rule_stub(self):
        """Test case for inbox_rules_service_get_inbox_rule_stub

        Get Inbox Rule Stub  # noqa: E501
        """
        pass

    def test_inbox_rules_service_patch_inbox_rule(self):
        """Test case for inbox_rules_service_patch_inbox_rule

        Patch Inbox Rule  # noqa: E501
        """
        pass

    def test_inbox_rules_service_patch_inbox_rule_actions(self):
        """Test case for inbox_rules_service_patch_inbox_rule_actions

        Patch Inbox Rule Actions  # noqa: E501
        """
        pass

    def test_inbox_rules_service_patch_inbox_rule_subscribers(self):
        """Test case for inbox_rules_service_patch_inbox_rule_subscribers

        Patch Inbox Rule Subscribers  # noqa: E501
        """
        pass

    def test_inbox_rules_service_search_inbox_rule_conditions(self):
        """Test case for inbox_rules_service_search_inbox_rule_conditions

        Search Inbox Rule Conditions  # noqa: E501
        """
        pass

    def test_inbox_rules_service_search_inbox_rules(self):
        """Test case for inbox_rules_service_search_inbox_rules

        Search inbox rules  # noqa: E501
        """
        pass

    def test_inbox_rules_service_search_log(self):
        """Test case for inbox_rules_service_search_log

        Get Inbox Rule Logs By Inbox Rule Id  # noqa: E501
        """
        pass

    def test_inbox_rules_service_search_subscribers(self):
        """Test case for inbox_rules_service_search_subscribers

        Search inbox rule subscribers  # noqa: E501
        """
        pass

    def test_inbox_rules_service_subscribe_current_user_to_rule(self):
        """Test case for inbox_rules_service_subscribe_current_user_to_rule

        Subscribe Current User  # noqa: E501
        """
        pass

    def test_inbox_rules_service_unsubscribe_current_user_from_rule(self):
        """Test case for inbox_rules_service_unsubscribe_current_user_from_rule

        Unsubscribe current user  # noqa: E501
        """
        pass

    def test_inbox_rules_service_update_inbox_rule_condition(self):
        """Test case for inbox_rules_service_update_inbox_rule_condition

        Update Inbox Rule Condition  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
