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
from secret_server_openapiclient.model.name_value_header_value import NameValueHeaderValue
from secret_server_openapiclient.model.optional_date_time_offset import OptionalDateTimeOffset
globals()['NameValueHeaderValue'] = NameValueHeaderValue
globals()['OptionalDateTimeOffset'] = OptionalDateTimeOffset
from secret_server_openapiclient.model.content_disposition_header_value import ContentDispositionHeaderValue


class TestContentDispositionHeaderValue(unittest.TestCase):
    """ContentDispositionHeaderValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testContentDispositionHeaderValue(self):
        """Test ContentDispositionHeaderValue"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ContentDispositionHeaderValue()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
