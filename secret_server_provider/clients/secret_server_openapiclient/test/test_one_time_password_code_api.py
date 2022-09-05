"""
    Secret Server Rest API

    REST API documentation for Secret Server. This document describes how to use the REST API. All requests require an authentication token; please see the <a href=\"../OAuth/\">authentication document</a> for more information. The <a href=\"swagger.json\">Swagger specification</a> for this API is also available.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 11.2.2
    Contact: info@authomize.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import secret_server_openapiclient
from secret_server_openapiclient.api.one_time_password_code_api import OneTimePasswordCodeApi  # noqa: E501


class TestOneTimePasswordCodeApi(unittest.TestCase):
    """OneTimePasswordCodeApi unit test stubs"""

    def setUp(self):
        self.api = OneTimePasswordCodeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_one_time_password_code_service_get(self):
        """Test case for one_time_password_code_service_get

        Get one time password code and seconds  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
