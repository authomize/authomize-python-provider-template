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
from secret_server_openapiclient.model.inbox_rule_model import InboxRuleModel
from secret_server_openapiclient.model.inbox_template_type import InboxTemplateType
globals()['InboxRuleModel'] = InboxRuleModel
globals()['InboxTemplateType'] = InboxTemplateType
from secret_server_openapiclient.model.inbox_template_model import InboxTemplateModel


class TestInboxTemplateModel(unittest.TestCase):
    """InboxTemplateModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInboxTemplateModel(self):
        """Test InboxTemplateModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = InboxTemplateModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
