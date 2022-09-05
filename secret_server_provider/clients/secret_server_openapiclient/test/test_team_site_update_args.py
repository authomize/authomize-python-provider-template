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
from secret_server_openapiclient.model.update_field_value_of_int32_array import UpdateFieldValueOfInt32Array
from secret_server_openapiclient.model.update_field_value_of_optional_boolean import UpdateFieldValueOfOptionalBoolean
globals()['UpdateFieldValueOfInt32Array'] = UpdateFieldValueOfInt32Array
globals()['UpdateFieldValueOfOptionalBoolean'] = UpdateFieldValueOfOptionalBoolean
from secret_server_openapiclient.model.team_site_update_args import TeamSiteUpdateArgs


class TestTeamSiteUpdateArgs(unittest.TestCase):
    """TeamSiteUpdateArgs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTeamSiteUpdateArgs(self):
        """Test TeamSiteUpdateArgs"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TeamSiteUpdateArgs()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
