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
from secret_server_openapiclient.model.update_field_value_of_string import UpdateFieldValueOfString
globals()['UpdateFieldValueOfBoolean'] = UpdateFieldValueOfBoolean
globals()['UpdateFieldValueOfString'] = UpdateFieldValueOfString
from secret_server_openapiclient.model.configuration_user_interface_patch_model import ConfigurationUserInterfacePatchModel


class TestConfigurationUserInterfacePatchModel(unittest.TestCase):
    """ConfigurationUserInterfacePatchModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testConfigurationUserInterfacePatchModel(self):
        """Test ConfigurationUserInterfacePatchModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ConfigurationUserInterfacePatchModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()