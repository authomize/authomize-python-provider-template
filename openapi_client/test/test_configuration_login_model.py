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
from plugins.model.configuration_login_ssh_key_integration_model import ConfigurationLoginSshKeyIntegrationModel
from plugins.model.configuration_login_two_factor_model import ConfigurationLoginTwoFactorModel
globals()['ConfigurationLoginSshKeyIntegrationModel'] = ConfigurationLoginSshKeyIntegrationModel
globals()['ConfigurationLoginTwoFactorModel'] = ConfigurationLoginTwoFactorModel
from plugins.model.configuration_login_model import ConfigurationLoginModel


class TestConfigurationLoginModel(unittest.TestCase):
    """ConfigurationLoginModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testConfigurationLoginModel(self):
        """Test ConfigurationLoginModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ConfigurationLoginModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()