"""
    Secret Server Rest API

    REST API documentation for Secret Server. This document describes how to use the REST API. All requests require an authentication token; please see the <a href=\"../OAuth/\">authentication document</a> for more information. The <a href=\"swagger.json\">Swagger specification</a> for this API is also available.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 11.2.2
    Contact: info@authomize.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import plugins
from plugins.model.i_dual_control_approval_group import IDualControlApprovalGroup
globals()['IDualControlApprovalGroup'] = IDualControlApprovalGroup
from plugins.model.dual_control_create_args import DualControlCreateArgs


class TestDualControlCreateArgs(unittest.TestCase):
    """DualControlCreateArgs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDualControlCreateArgs(self):
        """Test DualControlCreateArgs"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DualControlCreateArgs()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
