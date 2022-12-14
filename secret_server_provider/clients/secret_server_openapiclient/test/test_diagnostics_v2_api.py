"""
    Secret Server Rest API

    REST API documentation for Secret Server. This document describes how to use the REST API. All requests require an authentication token; please see the <a href=\"../OAuth/\">authentication document</a> for more information. The <a href=\"swagger.json\">Swagger specification</a> for this API is also available.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 11.2.2
    Contact: info@authomize.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import secret_server_openapiclient
from secret_server_openapiclient.api.diagnostics_v2_api import DiagnosticsV2Api  # noqa: E501


class TestDiagnosticsV2Api(unittest.TestCase):
    """DiagnosticsV2Api unit test stubs"""

    def setUp(self):
        self.api = DiagnosticsV2Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_diagnostics_v2_service_search_system_log(self):
        """Test case for diagnostics_v2_service_search_system_log

        Search system log  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
