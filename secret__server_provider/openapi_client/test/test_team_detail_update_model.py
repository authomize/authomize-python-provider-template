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
from plugins.model.update_field_value_of_optional_boolean import UpdateFieldValueOfOptionalBoolean
from plugins.model.update_field_value_of_optional_int32 import UpdateFieldValueOfOptionalInt32
from plugins.model.update_field_value_of_string import UpdateFieldValueOfString
globals()['UpdateFieldValueOfOptionalBoolean'] = UpdateFieldValueOfOptionalBoolean
globals()['UpdateFieldValueOfOptionalInt32'] = UpdateFieldValueOfOptionalInt32
globals()['UpdateFieldValueOfString'] = UpdateFieldValueOfString
from plugins.model.team_detail_update_model import TeamDetailUpdateModel


class TestTeamDetailUpdateModel(unittest.TestCase):
    """TeamDetailUpdateModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTeamDetailUpdateModel(self):
        """Test TeamDetailUpdateModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TeamDetailUpdateModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()