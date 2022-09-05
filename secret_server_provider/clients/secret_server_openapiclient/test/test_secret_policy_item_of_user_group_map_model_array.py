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
from secret_server_openapiclient.model.policy_apply_type import PolicyApplyType
from secret_server_openapiclient.model.user_group_map_model import UserGroupMapModel
globals()['PolicyApplyType'] = PolicyApplyType
globals()['UserGroupMapModel'] = UserGroupMapModel
from secret_server_openapiclient.model.secret_policy_item_of_user_group_map_model_array import SecretPolicyItemOfUserGroupMapModelArray


class TestSecretPolicyItemOfUserGroupMapModelArray(unittest.TestCase):
    """SecretPolicyItemOfUserGroupMapModelArray unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecretPolicyItemOfUserGroupMapModelArray(self):
        """Test SecretPolicyItemOfUserGroupMapModelArray"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecretPolicyItemOfUserGroupMapModelArray()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
