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
from plugins.model.update_field_value_of_boolean import UpdateFieldValueOfBoolean
from plugins.model.update_field_value_of_field_data_type import UpdateFieldValueOfFieldDataType
from plugins.model.update_field_value_of_field_permission_type import UpdateFieldValueOfFieldPermissionType
from plugins.model.update_field_value_of_int32 import UpdateFieldValueOfInt32
from plugins.model.update_field_value_of_optional_int32 import UpdateFieldValueOfOptionalInt32
from plugins.model.update_field_value_of_secret_template_field_option_remove_model_array import UpdateFieldValueOfSecretTemplateFieldOptionRemoveModelArray
from plugins.model.update_field_value_of_secret_template_field_option_update_model_array import UpdateFieldValueOfSecretTemplateFieldOptionUpdateModelArray
from plugins.model.update_field_value_of_string import UpdateFieldValueOfString
from plugins.model.update_field_value_of_string_array import UpdateFieldValueOfStringArray
globals()['UpdateFieldValueOfBoolean'] = UpdateFieldValueOfBoolean
globals()['UpdateFieldValueOfFieldDataType'] = UpdateFieldValueOfFieldDataType
globals()['UpdateFieldValueOfFieldPermissionType'] = UpdateFieldValueOfFieldPermissionType
globals()['UpdateFieldValueOfInt32'] = UpdateFieldValueOfInt32
globals()['UpdateFieldValueOfOptionalInt32'] = UpdateFieldValueOfOptionalInt32
globals()['UpdateFieldValueOfSecretTemplateFieldOptionRemoveModelArray'] = UpdateFieldValueOfSecretTemplateFieldOptionRemoveModelArray
globals()['UpdateFieldValueOfSecretTemplateFieldOptionUpdateModelArray'] = UpdateFieldValueOfSecretTemplateFieldOptionUpdateModelArray
globals()['UpdateFieldValueOfString'] = UpdateFieldValueOfString
globals()['UpdateFieldValueOfStringArray'] = UpdateFieldValueOfStringArray
from plugins.model.secret_template_field_patch_model import SecretTemplateFieldPatchModel


class TestSecretTemplateFieldPatchModel(unittest.TestCase):
    """SecretTemplateFieldPatchModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecretTemplateFieldPatchModel(self):
        """Test SecretTemplateFieldPatchModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecretTemplateFieldPatchModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
