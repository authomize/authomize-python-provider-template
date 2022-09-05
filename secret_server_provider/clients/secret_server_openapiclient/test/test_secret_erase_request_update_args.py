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
from secret_server_openapiclient.model.optional_date_time_offset import OptionalDateTimeOffset
from secret_server_openapiclient.model.secret_erase_request_model_status import SecretEraseRequestModelStatus
globals()['OptionalDateTimeOffset'] = OptionalDateTimeOffset
globals()['SecretEraseRequestModelStatus'] = SecretEraseRequestModelStatus
from secret_server_openapiclient.model.secret_erase_request_update_args import SecretEraseRequestUpdateArgs


class TestSecretEraseRequestUpdateArgs(unittest.TestCase):
    """SecretEraseRequestUpdateArgs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecretEraseRequestUpdateArgs(self):
        """Test SecretEraseRequestUpdateArgs"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecretEraseRequestUpdateArgs()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
