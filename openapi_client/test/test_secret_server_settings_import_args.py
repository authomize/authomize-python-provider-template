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
from plugins.model.secret_server_settings_patch_model import SecretServerSettingsPatchModel
from plugins.model.secret_server_settings_query import SecretServerSettingsQuery
globals()['SecretServerSettingsPatchModel'] = SecretServerSettingsPatchModel
globals()['SecretServerSettingsQuery'] = SecretServerSettingsQuery
from plugins.model.secret_server_settings_import_args import SecretServerSettingsImportArgs


class TestSecretServerSettingsImportArgs(unittest.TestCase):
    """SecretServerSettingsImportArgs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecretServerSettingsImportArgs(self):
        """Test SecretServerSettingsImportArgs"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecretServerSettingsImportArgs()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()