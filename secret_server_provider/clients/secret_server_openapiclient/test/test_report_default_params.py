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
from secret_server_openapiclient.model.i_custom_report_parameter_value import ICustomReportParameterValue
globals()['ICustomReportParameterValue'] = ICustomReportParameterValue
from secret_server_openapiclient.model.report_default_params import ReportDefaultParams


class TestReportDefaultParams(unittest.TestCase):
    """ReportDefaultParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testReportDefaultParams(self):
        """Test ReportDefaultParams"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ReportDefaultParams()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
