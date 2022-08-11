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
from plugins.model.edit_requires_options import EditRequiresOptions
from plugins.model.list_type import ListType
globals()['EditRequiresOptions'] = EditRequiresOptions
globals()['ListType'] = ListType
from plugins.model.secret_template_field import SecretTemplateField


class TestSecretTemplateField(unittest.TestCase):
    """SecretTemplateField unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecretTemplateField(self):
        """Test SecretTemplateField"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecretTemplateField()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
