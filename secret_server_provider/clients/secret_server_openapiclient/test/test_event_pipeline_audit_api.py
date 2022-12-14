"""
    Secret Server Rest API

    REST API documentation for Secret Server. This document describes how to use the REST API. All requests require an authentication token; please see the <a href=\"../OAuth/\">authentication document</a> for more information. The <a href=\"swagger.json\">Swagger specification</a> for this API is also available.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 11.2.2
    Contact: info@authomize.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import secret_server_openapiclient
from secret_server_openapiclient.api.event_pipeline_audit_api import EventPipelineAuditApi  # noqa: E501


class TestEventPipelineAuditApi(unittest.TestCase):
    """EventPipelineAuditApi unit test stubs"""

    def setUp(self):
        self.api = EventPipelineAuditApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_event_pipeline_audit_service_get_all_pipeline_and_policy_audits(self):
        """Test case for event_pipeline_audit_service_get_all_pipeline_and_policy_audits

        Get Pipeline / Policy Audits  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
