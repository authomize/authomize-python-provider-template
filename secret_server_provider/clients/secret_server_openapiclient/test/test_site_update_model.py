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
from secret_server_openapiclient.model.update_field_value_of_boolean import UpdateFieldValueOfBoolean
from secret_server_openapiclient.model.update_field_value_of_int32 import UpdateFieldValueOfInt32
from secret_server_openapiclient.model.update_field_value_of_optional_boolean import UpdateFieldValueOfOptionalBoolean
from secret_server_openapiclient.model.update_field_value_of_optional_int32 import UpdateFieldValueOfOptionalInt32
from secret_server_openapiclient.model.update_field_value_of_processing_location_type import UpdateFieldValueOfProcessingLocationType
from secret_server_openapiclient.model.update_field_value_of_string import UpdateFieldValueOfString
globals()['UpdateFieldValueOfBoolean'] = UpdateFieldValueOfBoolean
globals()['UpdateFieldValueOfInt32'] = UpdateFieldValueOfInt32
globals()['UpdateFieldValueOfOptionalBoolean'] = UpdateFieldValueOfOptionalBoolean
globals()['UpdateFieldValueOfOptionalInt32'] = UpdateFieldValueOfOptionalInt32
globals()['UpdateFieldValueOfProcessingLocationType'] = UpdateFieldValueOfProcessingLocationType
globals()['UpdateFieldValueOfString'] = UpdateFieldValueOfString
from secret_server_openapiclient.model.site_update_model import SiteUpdateModel


class TestSiteUpdateModel(unittest.TestCase):
    """SiteUpdateModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSiteUpdateModel(self):
        """Test SiteUpdateModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SiteUpdateModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
