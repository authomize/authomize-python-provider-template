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
from secret_server_openapiclient.model.enable_radius_two_factor_for_users_model import EnableRadiusTwoFactorForUsersModel
globals()['EnableRadiusTwoFactorForUsersModel'] = EnableRadiusTwoFactorForUsersModel
from secret_server_openapiclient.model.enable_radius_two_factor_for_users_args import EnableRadiusTwoFactorForUsersArgs


class TestEnableRadiusTwoFactorForUsersArgs(unittest.TestCase):
    """EnableRadiusTwoFactorForUsersArgs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEnableRadiusTwoFactorForUsersArgs(self):
        """Test EnableRadiusTwoFactorForUsersArgs"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EnableRadiusTwoFactorForUsersArgs()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
