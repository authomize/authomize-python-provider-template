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
from secret_server_openapiclient.model.auto_change_schedule_data_model import AutoChangeScheduleDataModel
from secret_server_openapiclient.model.policy_apply_type import PolicyApplyType
globals()['AutoChangeScheduleDataModel'] = AutoChangeScheduleDataModel
globals()['PolicyApplyType'] = PolicyApplyType
from secret_server_openapiclient.model.secret_policy_data_item_of_auto_change_schedule_data_model import SecretPolicyDataItemOfAutoChangeScheduleDataModel


class TestSecretPolicyDataItemOfAutoChangeScheduleDataModel(unittest.TestCase):
    """SecretPolicyDataItemOfAutoChangeScheduleDataModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecretPolicyDataItemOfAutoChangeScheduleDataModel(self):
        """Test SecretPolicyDataItemOfAutoChangeScheduleDataModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecretPolicyDataItemOfAutoChangeScheduleDataModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
