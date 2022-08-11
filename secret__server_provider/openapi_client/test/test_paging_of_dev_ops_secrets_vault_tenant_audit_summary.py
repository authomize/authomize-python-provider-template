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
from plugins.model.dev_ops_secrets_vault_tenant_audit_summary import DevOpsSecretsVaultTenantAuditSummary
from plugins.model.severity import Severity
from plugins.model.sort import Sort
globals()['DevOpsSecretsVaultTenantAuditSummary'] = DevOpsSecretsVaultTenantAuditSummary
globals()['Severity'] = Severity
globals()['Sort'] = Sort
from plugins.model.paging_of_dev_ops_secrets_vault_tenant_audit_summary import PagingOfDevOpsSecretsVaultTenantAuditSummary


class TestPagingOfDevOpsSecretsVaultTenantAuditSummary(unittest.TestCase):
    """PagingOfDevOpsSecretsVaultTenantAuditSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPagingOfDevOpsSecretsVaultTenantAuditSummary(self):
        """Test PagingOfDevOpsSecretsVaultTenantAuditSummary"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PagingOfDevOpsSecretsVaultTenantAuditSummary()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
