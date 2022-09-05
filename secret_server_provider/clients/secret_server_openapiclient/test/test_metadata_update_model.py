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
from secret_server_openapiclient.model.update_field_value_of_optional_boolean import UpdateFieldValueOfOptionalBoolean
from secret_server_openapiclient.model.update_field_value_of_optional_date_time import UpdateFieldValueOfOptionalDateTime
from secret_server_openapiclient.model.update_field_value_of_optional_double import UpdateFieldValueOfOptionalDouble
from secret_server_openapiclient.model.update_field_value_of_optional_int32 import UpdateFieldValueOfOptionalInt32
from secret_server_openapiclient.model.update_field_value_of_string import UpdateFieldValueOfString
globals()['UpdateFieldValueOfBoolean'] = UpdateFieldValueOfBoolean
globals()['UpdateFieldValueOfOptionalBoolean'] = UpdateFieldValueOfOptionalBoolean
globals()['UpdateFieldValueOfOptionalDateTime'] = UpdateFieldValueOfOptionalDateTime
globals()['UpdateFieldValueOfOptionalDouble'] = UpdateFieldValueOfOptionalDouble
globals()['UpdateFieldValueOfOptionalInt32'] = UpdateFieldValueOfOptionalInt32
globals()['UpdateFieldValueOfString'] = UpdateFieldValueOfString
from secret_server_openapiclient.model.metadata_update_model import MetadataUpdateModel


class TestMetadataUpdateModel(unittest.TestCase):
    """MetadataUpdateModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMetadataUpdateModel(self):
        """Test MetadataUpdateModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MetadataUpdateModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
