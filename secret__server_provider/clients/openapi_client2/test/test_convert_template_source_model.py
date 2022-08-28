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
from plugins.model.convert_template_detail_field_model import ConvertTemplateDetailFieldModel
globals()['ConvertTemplateDetailFieldModel'] = ConvertTemplateDetailFieldModel
from plugins.model.convert_template_source_model import ConvertTemplateSourceModel


class TestConvertTemplateSourceModel(unittest.TestCase):
    """ConvertTemplateSourceModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testConvertTemplateSourceModel(self):
        """Test ConvertTemplateSourceModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ConvertTemplateSourceModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
