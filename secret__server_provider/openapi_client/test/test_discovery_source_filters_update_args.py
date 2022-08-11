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
from plugins.model.discovery_source_filters_update_model import DiscoverySourceFiltersUpdateModel
globals()['DiscoverySourceFiltersUpdateModel'] = DiscoverySourceFiltersUpdateModel
from plugins.model.discovery_source_filters_update_args import DiscoverySourceFiltersUpdateArgs


class TestDiscoverySourceFiltersUpdateArgs(unittest.TestCase):
    """DiscoverySourceFiltersUpdateArgs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDiscoverySourceFiltersUpdateArgs(self):
        """Test DiscoverySourceFiltersUpdateArgs"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DiscoverySourceFiltersUpdateArgs()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
