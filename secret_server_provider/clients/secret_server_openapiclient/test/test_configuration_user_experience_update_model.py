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
from secret_server_openapiclient.model.update_field_value_of_int32 import UpdateFieldValueOfInt32
from secret_server_openapiclient.model.update_field_value_of_optional_int32 import UpdateFieldValueOfOptionalInt32
from secret_server_openapiclient.model.update_field_value_of_string import UpdateFieldValueOfString
globals()['UpdateFieldValueOfBoolean'] = UpdateFieldValueOfBoolean
globals()['UpdateFieldValueOfInt32'] = UpdateFieldValueOfInt32
globals()['UpdateFieldValueOfOptionalInt32'] = UpdateFieldValueOfOptionalInt32
globals()['UpdateFieldValueOfString'] = UpdateFieldValueOfString
from secret_server_openapiclient.model.configuration_user_experience_update_model import ConfigurationUserExperienceUpdateModel


class TestConfigurationUserExperienceUpdateModel(unittest.TestCase):
    """ConfigurationUserExperienceUpdateModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testConfigurationUserExperienceUpdateModel(self):
        """Test ConfigurationUserExperienceUpdateModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ConfigurationUserExperienceUpdateModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()