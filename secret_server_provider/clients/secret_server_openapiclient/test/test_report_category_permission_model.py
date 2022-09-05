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
from secret_server_openapiclient.model.report_permission_group_model import ReportPermissionGroupModel
from secret_server_openapiclient.model.report_role_permission_model import ReportRolePermissionModel
globals()['ReportPermissionGroupModel'] = ReportPermissionGroupModel
globals()['ReportRolePermissionModel'] = ReportRolePermissionModel
from secret_server_openapiclient.model.report_category_permission_model import ReportCategoryPermissionModel


class TestReportCategoryPermissionModel(unittest.TestCase):
    """ReportCategoryPermissionModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testReportCategoryPermissionModel(self):
        """Test ReportCategoryPermissionModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ReportCategoryPermissionModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()