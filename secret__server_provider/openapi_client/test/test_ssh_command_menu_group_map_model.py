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
from plugins.model.user_group_map_type import UserGroupMapType
globals()['UserGroupMapType'] = UserGroupMapType
from plugins.model.ssh_command_menu_group_map_model import SshCommandMenuGroupMapModel


class TestSshCommandMenuGroupMapModel(unittest.TestCase):
    """SshCommandMenuGroupMapModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSshCommandMenuGroupMapModel(self):
        """Test SshCommandMenuGroupMapModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SshCommandMenuGroupMapModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
