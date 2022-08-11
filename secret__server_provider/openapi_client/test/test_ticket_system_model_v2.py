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
from plugins.model.force_require_ticket_system_options import ForceRequireTicketSystemOptions
from plugins.model.ticket_system_types import TicketSystemTypes
globals()['ForceRequireTicketSystemOptions'] = ForceRequireTicketSystemOptions
globals()['TicketSystemTypes'] = TicketSystemTypes
from plugins.model.ticket_system_model_v2 import TicketSystemModelV2


class TestTicketSystemModelV2(unittest.TestCase):
    """TicketSystemModelV2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTicketSystemModelV2(self):
        """Test TicketSystemModelV2"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TicketSystemModelV2()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
