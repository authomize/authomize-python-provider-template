"""
    Secret Server Rest API

    REST API documentation for Secret Server. This document describes how to use the REST API. All requests require an authentication token; please see the <a href=\"../OAuth/\">authentication document</a> for more information. The <a href=\"swagger.json\">Swagger specification</a> for this API is also available.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 11.2.2
    Contact: info@authomize.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import secret_server_openapiclient
from secret_server_openapiclient.api.event_subscriptions_api import EventSubscriptionsApi  # noqa: E501


class TestEventSubscriptionsApi(unittest.TestCase):
    """EventSubscriptionsApi unit test stubs"""

    def setUp(self):
        self.api = EventSubscriptionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_event_subscriptions_service_create_event_subscription(self):
        """Test case for event_subscriptions_service_create_event_subscription

        Create event subscription  # noqa: E501
        """
        pass

    def test_event_subscriptions_service_get_event_subscription(self):
        """Test case for event_subscriptions_service_get_event_subscription

        event subscription  # noqa: E501
        """
        pass

    def test_event_subscriptions_service_get_subscription_entity_types(self):
        """Test case for event_subscriptions_service_get_subscription_entity_types

        Get an Event Subscription Types and Actions  # noqa: E501
        """
        pass

    def test_event_subscriptions_service_get_subscription_stub(self):
        """Test case for event_subscriptions_service_get_subscription_stub

        Get an empty event subscription  # noqa: E501
        """
        pass

    def test_event_subscriptions_service_search_event_subscriptions(self):
        """Test case for event_subscriptions_service_search_event_subscriptions

        Search event subscriptions  # noqa: E501
        """
        pass

    def test_event_subscriptions_service_update_event_subscription(self):
        """Test case for event_subscriptions_service_update_event_subscription

        Update event subscription  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()