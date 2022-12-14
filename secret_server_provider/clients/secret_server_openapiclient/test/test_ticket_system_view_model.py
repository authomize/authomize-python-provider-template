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
from secret_server_openapiclient.model.view_field_value_of_force_require_ticket_system_options import ViewFieldValueOfForceRequireTicketSystemOptions
from secret_server_openapiclient.model.view_field_value_of_int32 import ViewFieldValueOfInt32
from secret_server_openapiclient.model.view_field_value_of_optional_bmc_change_management_comment_work_type import ViewFieldValueOfOptionalBmcChangeManagementCommentWorkType
from secret_server_openapiclient.model.view_field_value_of_optional_bmc_incident_management_comment_work_type import ViewFieldValueOfOptionalBmcIncidentManagementCommentWorkType
from secret_server_openapiclient.model.view_field_value_of_optional_int32 import ViewFieldValueOfOptionalInt32
from secret_server_openapiclient.model.view_field_value_of_string import ViewFieldValueOfString
from secret_server_openapiclient.model.view_field_value_of_ticket_system_types import ViewFieldValueOfTicketSystemTypes
globals()['ViewFieldValueOfBoolean'] = ViewFieldValueOfBoolean
globals()['ViewFieldValueOfForceRequireTicketSystemOptions'] = ViewFieldValueOfForceRequireTicketSystemOptions
globals()['ViewFieldValueOfInt32'] = ViewFieldValueOfInt32
globals()['ViewFieldValueOfOptionalBmcChangeManagementCommentWorkType'] = ViewFieldValueOfOptionalBmcChangeManagementCommentWorkType
globals()['ViewFieldValueOfOptionalBmcIncidentManagementCommentWorkType'] = ViewFieldValueOfOptionalBmcIncidentManagementCommentWorkType
globals()['ViewFieldValueOfOptionalInt32'] = ViewFieldValueOfOptionalInt32
globals()['ViewFieldValueOfString'] = ViewFieldValueOfString
globals()['ViewFieldValueOfTicketSystemTypes'] = ViewFieldValueOfTicketSystemTypes
from secret_server_openapiclient.model.ticket_system_view_model import TicketSystemViewModel


class TestTicketSystemViewModel(unittest.TestCase):
    """TicketSystemViewModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTicketSystemViewModel(self):
        """Test TicketSystemViewModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TicketSystemViewModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
