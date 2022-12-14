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
from secret_server_openapiclient.model.view_field_value_of_int32 import ViewFieldValueOfInt32
from secret_server_openapiclient.model.view_field_value_read_only_of_event_pipeline_filter_setting_value_map_view_model_array import ViewFieldValueReadOnlyOfEventPipelineFilterSettingValueMapViewModelArray
from secret_server_openapiclient.model.view_field_value_read_only_of_int32 import ViewFieldValueReadOnlyOfInt32
from secret_server_openapiclient.model.view_field_value_read_only_of_optional_int32 import ViewFieldValueReadOnlyOfOptionalInt32
from secret_server_openapiclient.model.view_field_value_read_only_of_string import ViewFieldValueReadOnlyOfString
globals()['ViewFieldValueOfInt32'] = ViewFieldValueOfInt32
globals()['ViewFieldValueReadOnlyOfEventPipelineFilterSettingValueMapViewModelArray'] = ViewFieldValueReadOnlyOfEventPipelineFilterSettingValueMapViewModelArray
globals()['ViewFieldValueReadOnlyOfInt32'] = ViewFieldValueReadOnlyOfInt32
globals()['ViewFieldValueReadOnlyOfOptionalInt32'] = ViewFieldValueReadOnlyOfOptionalInt32
globals()['ViewFieldValueReadOnlyOfString'] = ViewFieldValueReadOnlyOfString
from secret_server_openapiclient.model.event_pipeline_filter_view_model import EventPipelineFilterViewModel


class TestEventPipelineFilterViewModel(unittest.TestCase):
    """EventPipelineFilterViewModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEventPipelineFilterViewModel(self):
        """Test EventPipelineFilterViewModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EventPipelineFilterViewModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
