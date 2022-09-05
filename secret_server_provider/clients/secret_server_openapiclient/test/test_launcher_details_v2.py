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
from secret_server_openapiclient.model.i_categorized_list_item_value import ICategorizedListItemValue
from secret_server_openapiclient.model.i_launcher_type_field import ILauncherTypeField
globals()['ICategorizedListItemValue'] = ICategorizedListItemValue
globals()['ILauncherTypeField'] = ILauncherTypeField
from secret_server_openapiclient.model.launcher_details_v2 import LauncherDetailsV2


class TestLauncherDetailsV2(unittest.TestCase):
    """LauncherDetailsV2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLauncherDetailsV2(self):
        """Test LauncherDetailsV2"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LauncherDetailsV2()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()