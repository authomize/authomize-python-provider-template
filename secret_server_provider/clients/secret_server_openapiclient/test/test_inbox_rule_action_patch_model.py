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
from secret_server_openapiclient.model.update_field_value_of_boolean import UpdateFieldValueOfBoolean
from secret_server_openapiclient.model.update_field_value_of_optional_int32 import UpdateFieldValueOfOptionalInt32
globals()['UpdateFieldValueOfBoolean'] = UpdateFieldValueOfBoolean
globals()['UpdateFieldValueOfOptionalInt32'] = UpdateFieldValueOfOptionalInt32
from secret_server_openapiclient.model.inbox_rule_action_patch_model import InboxRuleActionPatchModel


class TestInboxRuleActionPatchModel(unittest.TestCase):
    """InboxRuleActionPatchModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInboxRuleActionPatchModel(self):
        """Test InboxRuleActionPatchModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = InboxRuleActionPatchModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()