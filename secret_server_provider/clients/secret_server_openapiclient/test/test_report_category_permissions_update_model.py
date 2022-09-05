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
from secret_server_openapiclient.model.update_field_value_of_report_category_permission_update_model_array import UpdateFieldValueOfReportCategoryPermissionUpdateModelArray
globals()['UpdateFieldValueOfReportCategoryPermissionUpdateModelArray'] = UpdateFieldValueOfReportCategoryPermissionUpdateModelArray
from secret_server_openapiclient.model.report_category_permissions_update_model import ReportCategoryPermissionsUpdateModel


class TestReportCategoryPermissionsUpdateModel(unittest.TestCase):
    """ReportCategoryPermissionsUpdateModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testReportCategoryPermissionsUpdateModel(self):
        """Test ReportCategoryPermissionsUpdateModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ReportCategoryPermissionsUpdateModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
