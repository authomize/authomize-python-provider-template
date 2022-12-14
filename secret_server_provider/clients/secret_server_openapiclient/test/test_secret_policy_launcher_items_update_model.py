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
from secret_server_openapiclient.model.update_field_value_of_secret_policy_data_item_of_launcher_settings_data import UpdateFieldValueOfSecretPolicyDataItemOfLauncherSettingsData
from secret_server_openapiclient.model.update_field_value_of_secret_policy_data_item_of_optional_boolean import UpdateFieldValueOfSecretPolicyDataItemOfOptionalBoolean
globals()['UpdateFieldValueOfSecretPolicyDataItemOfLauncherSettingsData'] = UpdateFieldValueOfSecretPolicyDataItemOfLauncherSettingsData
globals()['UpdateFieldValueOfSecretPolicyDataItemOfOptionalBoolean'] = UpdateFieldValueOfSecretPolicyDataItemOfOptionalBoolean
from secret_server_openapiclient.model.secret_policy_launcher_items_update_model import SecretPolicyLauncherItemsUpdateModel


class TestSecretPolicyLauncherItemsUpdateModel(unittest.TestCase):
    """SecretPolicyLauncherItemsUpdateModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecretPolicyLauncherItemsUpdateModel(self):
        """Test SecretPolicyLauncherItemsUpdateModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecretPolicyLauncherItemsUpdateModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
