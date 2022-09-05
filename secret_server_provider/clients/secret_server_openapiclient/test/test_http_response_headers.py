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
from secret_server_openapiclient.model.authentication_header_value import AuthenticationHeaderValue
from secret_server_openapiclient.model.cache_control_header_value import CacheControlHeaderValue
from secret_server_openapiclient.model.entity_tag_header_value import EntityTagHeaderValue
from secret_server_openapiclient.model.name_value_header_value import NameValueHeaderValue
from secret_server_openapiclient.model.optional_date_time_offset import OptionalDateTimeOffset
from secret_server_openapiclient.model.product_header_value import ProductHeaderValue
from secret_server_openapiclient.model.product_info_header_value import ProductInfoHeaderValue
from secret_server_openapiclient.model.retry_condition_header_value import RetryConditionHeaderValue
from secret_server_openapiclient.model.transfer_coding_header_value import TransferCodingHeaderValue
from secret_server_openapiclient.model.uri import Uri
from secret_server_openapiclient.model.via_header_value import ViaHeaderValue
from secret_server_openapiclient.model.warning_header_value import WarningHeaderValue
globals()['AuthenticationHeaderValue'] = AuthenticationHeaderValue
globals()['CacheControlHeaderValue'] = CacheControlHeaderValue
globals()['EntityTagHeaderValue'] = EntityTagHeaderValue
globals()['NameValueHeaderValue'] = NameValueHeaderValue
globals()['OptionalDateTimeOffset'] = OptionalDateTimeOffset
globals()['ProductHeaderValue'] = ProductHeaderValue
globals()['ProductInfoHeaderValue'] = ProductInfoHeaderValue
globals()['RetryConditionHeaderValue'] = RetryConditionHeaderValue
globals()['TransferCodingHeaderValue'] = TransferCodingHeaderValue
globals()['Uri'] = Uri
globals()['ViaHeaderValue'] = ViaHeaderValue
globals()['WarningHeaderValue'] = WarningHeaderValue
from secret_server_openapiclient.model.http_response_headers import HttpResponseHeaders


class TestHttpResponseHeaders(unittest.TestCase):
    """HttpResponseHeaders unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testHttpResponseHeaders(self):
        """Test HttpResponseHeaders"""
        # FIXME: construct object with mandatory attributes with example values
        # model = HttpResponseHeaders()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
