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
from plugins.model.setting_for_display import SettingForDisplay
from plugins.model.view_field_link import ViewFieldLink
globals()['SettingForDisplay'] = SettingForDisplay
globals()['ViewFieldLink'] = ViewFieldLink
from plugins.model.view_field_value_of_setting_for_display import ViewFieldValueOfSettingForDisplay


class TestViewFieldValueOfSettingForDisplay(unittest.TestCase):
    """ViewFieldValueOfSettingForDisplay unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testViewFieldValueOfSettingForDisplay(self):
        """Test ViewFieldValueOfSettingForDisplay"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ViewFieldValueOfSettingForDisplay()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()