"""
    Secret Server Rest API

    REST API documentation for Secret Server. This document describes how to use the REST API. All requests require an authentication token; please see the <a href=\"../OAuth/\">authentication document</a> for more information. The <a href=\"swagger.json\">Swagger specification</a> for this API is also available.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 11.2.2
    Contact: info@authomize.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import plugins
from plugins.api.slack_api import SlackApi  # noqa: E501


class TestSlackApi(unittest.TestCase):
    """SlackApi unit test stubs"""

    def setUp(self):
        self.api = SlackApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_slack_service_get_configuration_v3(self):
        """Test case for slack_service_get_configuration_v3

        Get Slack Configuration  # noqa: E501
        """
        pass

    def test_slack_service_handle_event(self):
        """Test case for slack_service_handle_event

        Slack Event  # noqa: E501
        """
        pass

    def test_slack_service_handle_interaction(self):
        """Test case for slack_service_handle_interaction

        Slack Interaction  # noqa: E501
        """
        pass

    def test_slack_service_send_test_slack_message(self):
        """Test case for slack_service_send_test_slack_message

        Test Slack Configuration  # noqa: E501
        """
        pass

    def test_slack_service_update_configuration_v3(self):
        """Test case for slack_service_update_configuration_v3

        Slack Configuration  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()