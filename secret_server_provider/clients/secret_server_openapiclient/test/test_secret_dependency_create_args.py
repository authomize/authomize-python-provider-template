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
from secret_server_openapiclient.model.secret_dependency_run_script import SecretDependencyRunScript
from secret_server_openapiclient.model.secret_dependency_setting_map_for_display import SecretDependencySettingMapForDisplay
from secret_server_openapiclient.model.secret_dependency_template import SecretDependencyTemplate
globals()['SecretDependencyRunScript'] = SecretDependencyRunScript
globals()['SecretDependencySettingMapForDisplay'] = SecretDependencySettingMapForDisplay
globals()['SecretDependencyTemplate'] = SecretDependencyTemplate
from secret_server_openapiclient.model.secret_dependency_create_args import SecretDependencyCreateArgs


class TestSecretDependencyCreateArgs(unittest.TestCase):
    """SecretDependencyCreateArgs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecretDependencyCreateArgs(self):
        """Test SecretDependencyCreateArgs"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecretDependencyCreateArgs()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
