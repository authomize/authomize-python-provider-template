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
from secret_server_openapiclient.model.edit_requires_options import EditRequiresOptions
from secret_server_openapiclient.model.list_type import ListType
globals()['EditRequiresOptions'] = EditRequiresOptions
globals()['ListType'] = ListType
from secret_server_openapiclient.model.secret_template_field_update_args import SecretTemplateFieldUpdateArgs


class TestSecretTemplateFieldUpdateArgs(unittest.TestCase):
    """SecretTemplateFieldUpdateArgs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecretTemplateFieldUpdateArgs(self):
        """Test SecretTemplateFieldUpdateArgs"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecretTemplateFieldUpdateArgs()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()