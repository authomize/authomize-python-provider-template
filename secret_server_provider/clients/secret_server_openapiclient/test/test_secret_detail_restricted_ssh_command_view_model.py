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
from secret_server_openapiclient.model.command_restriction_type import CommandRestrictionType
from secret_server_openapiclient.model.secret_detail_restricted_ssh_command_blocklist_view_model import SecretDetailRestrictedSshCommandBlocklistViewModel
from secret_server_openapiclient.model.secret_detail_restricted_ssh_command_menu_view_model import SecretDetailRestrictedSshCommandMenuViewModel
globals()['CommandRestrictionType'] = CommandRestrictionType
globals()['SecretDetailRestrictedSshCommandBlocklistViewModel'] = SecretDetailRestrictedSshCommandBlocklistViewModel
globals()['SecretDetailRestrictedSshCommandMenuViewModel'] = SecretDetailRestrictedSshCommandMenuViewModel
from secret_server_openapiclient.model.secret_detail_restricted_ssh_command_view_model import SecretDetailRestrictedSshCommandViewModel


class TestSecretDetailRestrictedSshCommandViewModel(unittest.TestCase):
    """SecretDetailRestrictedSshCommandViewModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecretDetailRestrictedSshCommandViewModel(self):
        """Test SecretDetailRestrictedSshCommandViewModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecretDetailRestrictedSshCommandViewModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
