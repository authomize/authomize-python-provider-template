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
from plugins.model.domain_action_type import DomainActionType
from plugins.model.view_field_drop_down_value_of_string import ViewFieldDropDownValueOfString
from plugins.model.view_field_value_of_string import ViewFieldValueOfString
globals()['DomainActionType'] = DomainActionType
globals()['ViewFieldDropDownValueOfString'] = ViewFieldDropDownValueOfString
globals()['ViewFieldValueOfString'] = ViewFieldValueOfString
from plugins.model.ldap_sync_settings_view_model import LdapSyncSettingsViewModel


class TestLdapSyncSettingsViewModel(unittest.TestCase):
    """LdapSyncSettingsViewModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLdapSyncSettingsViewModel(self):
        """Test LdapSyncSettingsViewModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LdapSyncSettingsViewModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
