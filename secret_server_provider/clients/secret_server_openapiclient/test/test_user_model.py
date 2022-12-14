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
from secret_server_openapiclient.model.external_user_source_types import ExternalUserSourceTypes
from secret_server_openapiclient.model.platform_integration_type import PlatformIntegrationType
from secret_server_openapiclient.model.unix_authentication_method_type import UnixAuthenticationMethodType
from secret_server_openapiclient.model.user_ip_address_restriction_model import UserIpAddressRestrictionModel
globals()['ExternalUserSourceTypes'] = ExternalUserSourceTypes
globals()['PlatformIntegrationType'] = PlatformIntegrationType
globals()['UnixAuthenticationMethodType'] = UnixAuthenticationMethodType
globals()['UserIpAddressRestrictionModel'] = UserIpAddressRestrictionModel
from secret_server_openapiclient.model.user_model import UserModel


class TestUserModel(unittest.TestCase):
    """UserModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUserModel(self):
        """Test UserModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UserModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
