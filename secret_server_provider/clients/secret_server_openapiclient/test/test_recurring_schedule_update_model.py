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
from secret_server_openapiclient.model.update_field_value_of_date_time import UpdateFieldValueOfDateTime
from secret_server_openapiclient.model.update_field_value_of_int32 import UpdateFieldValueOfInt32
from secret_server_openapiclient.model.update_field_value_of_recurring_schedule_type import UpdateFieldValueOfRecurringScheduleType
from secret_server_openapiclient.model.update_field_value_of_recurring_schedule_value_model_array import UpdateFieldValueOfRecurringScheduleValueModelArray
from secret_server_openapiclient.model.update_field_value_of_string import UpdateFieldValueOfString
globals()['UpdateFieldValueOfBoolean'] = UpdateFieldValueOfBoolean
globals()['UpdateFieldValueOfDateTime'] = UpdateFieldValueOfDateTime
globals()['UpdateFieldValueOfInt32'] = UpdateFieldValueOfInt32
globals()['UpdateFieldValueOfRecurringScheduleType'] = UpdateFieldValueOfRecurringScheduleType
globals()['UpdateFieldValueOfRecurringScheduleValueModelArray'] = UpdateFieldValueOfRecurringScheduleValueModelArray
globals()['UpdateFieldValueOfString'] = UpdateFieldValueOfString
from secret_server_openapiclient.model.recurring_schedule_update_model import RecurringScheduleUpdateModel


class TestRecurringScheduleUpdateModel(unittest.TestCase):
    """RecurringScheduleUpdateModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRecurringScheduleUpdateModel(self):
        """Test RecurringScheduleUpdateModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = RecurringScheduleUpdateModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()