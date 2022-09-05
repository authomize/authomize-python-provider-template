"""
    Secret Server Rest API

    REST API documentation for Secret Server. This document describes how to use the REST API. All requests require an authentication token; please see the <a href=\"../OAuth/\">authentication document</a> for more information. The <a href=\"swagger.json\">Swagger specification</a> for this API is also available.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 11.2.2
    Contact: info@authomize.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import secret_server_openapiclient
from secret_server_openapiclient.api.bulk_operations_api import BulkOperationsApi  # noqa: E501


class TestBulkOperationsApi(unittest.TestCase):
    """BulkOperationsApi unit test stubs"""

    def setUp(self):
        self.api = BulkOperationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_bulk_operations_service_get_progress(self):
        """Test case for bulk_operations_service_get_progress

        Progress  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
