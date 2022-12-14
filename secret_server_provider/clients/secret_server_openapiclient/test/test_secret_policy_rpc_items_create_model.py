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
from secret_server_openapiclient.model.secret_policy_data_item_of_auto_change_schedule_data_model import SecretPolicyDataItemOfAutoChangeScheduleDataModel
from secret_server_openapiclient.model.secret_policy_data_item_of_optional_boolean import SecretPolicyDataItemOfOptionalBoolean
from secret_server_openapiclient.model.secret_policy_data_item_of_optional_int32 import SecretPolicyDataItemOfOptionalInt32
globals()['SecretPolicyDataItemOfAutoChangeScheduleDataModel'] = SecretPolicyDataItemOfAutoChangeScheduleDataModel
globals()['SecretPolicyDataItemOfOptionalBoolean'] = SecretPolicyDataItemOfOptionalBoolean
globals()['SecretPolicyDataItemOfOptionalInt32'] = SecretPolicyDataItemOfOptionalInt32
from secret_server_openapiclient.model.secret_policy_rpc_items_create_model import SecretPolicyRpcItemsCreateModel


class TestSecretPolicyRpcItemsCreateModel(unittest.TestCase):
    """SecretPolicyRpcItemsCreateModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecretPolicyRpcItemsCreateModel(self):
        """Test SecretPolicyRpcItemsCreateModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecretPolicyRpcItemsCreateModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
