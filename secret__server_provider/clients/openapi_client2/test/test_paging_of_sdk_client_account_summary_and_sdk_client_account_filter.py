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
from plugins.model.sdk_client_account_filter import SdkClientAccountFilter
from plugins.model.sdk_client_account_summary import SdkClientAccountSummary
from plugins.model.severity import Severity
from plugins.model.sort import Sort
globals()['SdkClientAccountFilter'] = SdkClientAccountFilter
globals()['SdkClientAccountSummary'] = SdkClientAccountSummary
globals()['Severity'] = Severity
globals()['Sort'] = Sort
from plugins.model.paging_of_sdk_client_account_summary_and_sdk_client_account_filter import PagingOfSdkClientAccountSummaryAndSdkClientAccountFilter


class TestPagingOfSdkClientAccountSummaryAndSdkClientAccountFilter(unittest.TestCase):
    """PagingOfSdkClientAccountSummaryAndSdkClientAccountFilter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPagingOfSdkClientAccountSummaryAndSdkClientAccountFilter(self):
        """Test PagingOfSdkClientAccountSummaryAndSdkClientAccountFilter"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PagingOfSdkClientAccountSummaryAndSdkClientAccountFilter()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
