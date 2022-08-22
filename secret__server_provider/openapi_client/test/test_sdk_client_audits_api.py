"""
    Secret Server Rest API

    REST API documentation for Secret Server. This document describes how to use the REST API. All requests require an authentication token; please see the <a href=\"../OAuth/\">authentication document</a> for more information. The <a href=\"swagger.json\">Swagger specification</a> for this API is also available.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 11.2.2
    Contact: info@authomize.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import plugins
from plugins.api.sdk_client_audits_api import SdkClientAuditsApi  # noqa: E501


class TestSdkClientAuditsApi(unittest.TestCase):
    """SdkClientAuditsApi unit test stubs"""

    def setUp(self):
        self.api = SdkClientAuditsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sdk_client_audits_service_search_client_audit(self):
        """Test case for sdk_client_audits_service_search_client_audit

        Search SDK Client Audits  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()