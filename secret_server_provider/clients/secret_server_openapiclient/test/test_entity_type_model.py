"""
    Secret Server Rest API

    REST API documentation for Secret Server. This document describes how to use the REST API. All requests require an authentication token; please see the <a href=\"../OAuth/\">authentication document</a> for more information. The <a href=\"swagger.json\">Swagger specification</a> for this API is also available.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 11.2.2
    Contact: info@authomize.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import secret_server_openapiclient
from secret_server_openapiclient.model.event_subscription_condition_type_option_model import EventSubscriptionConditionTypeOptionModel
from secret_server_openapiclient.model.event_subscription_entity import EventSubscriptionEntity
from secret_server_openapiclient.model.event_subscription_type_action_model import EventSubscriptionTypeActionModel
globals()['EventSubscriptionConditionTypeOptionModel'] = EventSubscriptionConditionTypeOptionModel
globals()['EventSubscriptionEntity'] = EventSubscriptionEntity
globals()['EventSubscriptionTypeActionModel'] = EventSubscriptionTypeActionModel
from secret_server_openapiclient.model.entity_type_model import EntityTypeModel


class TestEntityTypeModel(unittest.TestCase):
    """EntityTypeModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEntityTypeModel(self):
        """Test EntityTypeModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EntityTypeModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
