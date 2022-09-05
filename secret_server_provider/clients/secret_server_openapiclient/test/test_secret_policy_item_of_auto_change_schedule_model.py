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
from secret_server_openapiclient.model.auto_change_schedule_model import AutoChangeScheduleModel
from secret_server_openapiclient.model.policy_apply_type import PolicyApplyType
globals()['AutoChangeScheduleModel'] = AutoChangeScheduleModel
globals()['PolicyApplyType'] = PolicyApplyType
from secret_server_openapiclient.model.secret_policy_item_of_auto_change_schedule_model import SecretPolicyItemOfAutoChangeScheduleModel


class TestSecretPolicyItemOfAutoChangeScheduleModel(unittest.TestCase):
    """SecretPolicyItemOfAutoChangeScheduleModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecretPolicyItemOfAutoChangeScheduleModel(self):
        """Test SecretPolicyItemOfAutoChangeScheduleModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecretPolicyItemOfAutoChangeScheduleModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()