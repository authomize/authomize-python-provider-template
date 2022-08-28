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
from secret_server_openapiclient.model.view_field_value_of_boolean import ViewFieldValueOfBoolean
from secret_server_openapiclient.model.view_field_value_of_int32 import ViewFieldValueOfInt32
from secret_server_openapiclient.model.view_field_value_of_setting_for_display import ViewFieldValueOfSettingForDisplay
from secret_server_openapiclient.model.view_field_value_of_string import ViewFieldValueOfString
from secret_server_openapiclient.model.view_field_value_read_only_of_optional_int32 import ViewFieldValueReadOnlyOfOptionalInt32
from secret_server_openapiclient.model.view_field_value_read_only_of_string import ViewFieldValueReadOnlyOfString
globals()['ViewFieldValueOfBoolean'] = ViewFieldValueOfBoolean
globals()['ViewFieldValueOfInt32'] = ViewFieldValueOfInt32
globals()['ViewFieldValueOfSettingForDisplay'] = ViewFieldValueOfSettingForDisplay
globals()['ViewFieldValueOfString'] = ViewFieldValueOfString
globals()['ViewFieldValueReadOnlyOfOptionalInt32'] = ViewFieldValueReadOnlyOfOptionalInt32
globals()['ViewFieldValueReadOnlyOfString'] = ViewFieldValueReadOnlyOfString
from secret_server_openapiclient.model.event_pipeline_filter_setting_value_map_view_model import EventPipelineFilterSettingValueMapViewModel


class TestEventPipelineFilterSettingValueMapViewModel(unittest.TestCase):
    """EventPipelineFilterSettingValueMapViewModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEventPipelineFilterSettingValueMapViewModel(self):
        """Test EventPipelineFilterSettingValueMapViewModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EventPipelineFilterSettingValueMapViewModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()