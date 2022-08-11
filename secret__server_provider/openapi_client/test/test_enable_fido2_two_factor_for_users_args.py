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
from plugins.model.enable_fido2_two_factor_for_users_model import EnableFido2TwoFactorForUsersModel
globals()['EnableFido2TwoFactorForUsersModel'] = EnableFido2TwoFactorForUsersModel
from plugins.model.enable_fido2_two_factor_for_users_args import EnableFido2TwoFactorForUsersArgs


class TestEnableFido2TwoFactorForUsersArgs(unittest.TestCase):
    """EnableFido2TwoFactorForUsersArgs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEnableFido2TwoFactorForUsersArgs(self):
        """Test EnableFido2TwoFactorForUsersArgs"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EnableFido2TwoFactorForUsersArgs()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
