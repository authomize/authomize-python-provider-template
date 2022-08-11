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
from plugins.model.multifactor_authentication_provider_types import MultifactorAuthenticationProviderTypes
globals()['MultifactorAuthenticationProviderTypes'] = MultifactorAuthenticationProviderTypes
from plugins.model.update_field_value_of_multifactor_authentication_provider_types import UpdateFieldValueOfMultifactorAuthenticationProviderTypes


class TestUpdateFieldValueOfMultifactorAuthenticationProviderTypes(unittest.TestCase):
    """UpdateFieldValueOfMultifactorAuthenticationProviderTypes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUpdateFieldValueOfMultifactorAuthenticationProviderTypes(self):
        """Test UpdateFieldValueOfMultifactorAuthenticationProviderTypes"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UpdateFieldValueOfMultifactorAuthenticationProviderTypes()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
