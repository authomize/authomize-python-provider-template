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
from secret_server_openapiclient.model.severity import Severity
from secret_server_openapiclient.model.sort import Sort
from secret_server_openapiclient.model.team_audit_model import TeamAuditModel
globals()['Severity'] = Severity
globals()['Sort'] = Sort
globals()['TeamAuditModel'] = TeamAuditModel
from secret_server_openapiclient.model.paging_of_team_audit_model import PagingOfTeamAuditModel


class TestPagingOfTeamAuditModel(unittest.TestCase):
    """PagingOfTeamAuditModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPagingOfTeamAuditModel(self):
        """Test PagingOfTeamAuditModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PagingOfTeamAuditModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()