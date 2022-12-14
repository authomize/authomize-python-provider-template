"""
    Secret Server Rest API

    REST API documentation for Secret Server. This document describes how to use the REST API. All requests require an authentication token; please see the <a href=\"../OAuth/\">authentication document</a> for more information. The <a href=\"swagger.json\">Swagger specification</a> for this API is also available.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 11.2.2
    Contact: info@authomize.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import secret_server_openapiclient
from secret_server_openapiclient.api.discovery_api import DiscoveryApi  # noqa: E501


class TestDiscoveryApi(unittest.TestCase):
    """DiscoveryApi unit test stubs"""

    def setUp(self):
        self.api = DiscoveryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_discovery_service_create_discovery_source(self):
        """Test case for discovery_service_create_discovery_source

        Create a new discovery source  # noqa: E501
        """
        pass

    def test_discovery_service_create_discovery_source_scanner_settings(self):
        """Test case for discovery_service_create_discovery_source_scanner_settings

        Create scanner setting  # noqa: E501
        """
        pass

    def test_discovery_service_get_available_discovery_source_scanners(self):
        """Test case for discovery_service_get_available_discovery_source_scanners

        Get Discovery Source Available Scanners  # noqa: E501
        """
        pass

    def test_discovery_service_get_discovery_configuration(self):
        """Test case for discovery_service_get_discovery_configuration

        Get Discovery Configuration  # noqa: E501
        """
        pass

    def test_discovery_service_get_discovery_source(self):
        """Test case for discovery_service_get_discovery_source

        Get discovery source  # noqa: E501
        """
        pass

    def test_discovery_service_get_discovery_source_audits(self):
        """Test case for discovery_service_get_discovery_source_audits

        Get Discovery Source Audits  # noqa: E501
        """
        pass

    def test_discovery_service_get_discovery_source_filter(self):
        """Test case for discovery_service_get_discovery_source_filter

        Get the source filter for a discovery source  # noqa: E501
        """
        pass

    def test_discovery_service_get_discovery_source_stub(self):
        """Test case for discovery_service_get_discovery_source_stub

        Get a Discovery Source Stub  # noqa: E501
        """
        pass

    def test_discovery_service_get_discovery_status(self):
        """Test case for discovery_service_get_discovery_status

        Get Discovery Status  # noqa: E501
        """
        pass

    def test_discovery_service_get_scan_types(self):
        """Test case for discovery_service_get_scan_types

        Get Discovery Scan Types  # noqa: E501
        """
        pass

    def test_discovery_service_patch_discovery_source_filter(self):
        """Test case for discovery_service_patch_discovery_source_filter

        Patches discovery source filter  # noqa: E501
        """
        pass

    def test_discovery_service_run_discovery_now(self):
        """Test case for discovery_service_run_discovery_now

        Run a discovery command  # noqa: E501
        """
        pass

    def test_discovery_service_search_discovery_source_scanner_settings(self):
        """Test case for discovery_service_search_discovery_source_scanner_settings

        Get Scanner Settings  # noqa: E501
        """
        pass

    def test_discovery_service_search_discovery_sources(self):
        """Test case for discovery_service_search_discovery_sources

        Get discovery sources  # noqa: E501
        """
        pass

    def test_discovery_service_search_for_domain_ou(self):
        """Test case for discovery_service_search_for_domain_ou

        Get and include or exclude for discovery  # noqa: E501
        """
        pass

    def test_discovery_service_update_discovery_configuration(self):
        """Test case for discovery_service_update_discovery_configuration

        Update discovery configuration  # noqa: E501
        """
        pass

    def test_discovery_service_update_discovery_source(self):
        """Test case for discovery_service_update_discovery_source

        Update a discovery source  # noqa: E501
        """
        pass

    def test_discovery_service_update_discovery_source_filters(self):
        """Test case for discovery_service_update_discovery_source_filters

        Updates discovery source filters  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
