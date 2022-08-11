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
from plugins.model.sdk_client_rule_filter import SdkClientRuleFilter
from plugins.model.sdk_client_rule_summary import SdkClientRuleSummary
from plugins.model.severity import Severity
from plugins.model.sort import Sort
globals()['SdkClientRuleFilter'] = SdkClientRuleFilter
globals()['SdkClientRuleSummary'] = SdkClientRuleSummary
globals()['Severity'] = Severity
globals()['Sort'] = Sort
from plugins.model.paging_of_sdk_client_rule_summary_and_sdk_client_rule_filter import PagingOfSdkClientRuleSummaryAndSdkClientRuleFilter


class TestPagingOfSdkClientRuleSummaryAndSdkClientRuleFilter(unittest.TestCase):
    """PagingOfSdkClientRuleSummaryAndSdkClientRuleFilter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPagingOfSdkClientRuleSummaryAndSdkClientRuleFilter(self):
        """Test PagingOfSdkClientRuleSummaryAndSdkClientRuleFilter"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PagingOfSdkClientRuleSummaryAndSdkClientRuleFilter()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
