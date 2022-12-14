"""
    Secret Server Rest API

    REST API documentation for Secret Server. This document describes how to use the REST API. All requests require an authentication token; please see the <a href=\"../OAuth/\">authentication document</a> for more information. The <a href=\"swagger.json\">Swagger specification</a> for this API is also available.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 11.2.2
    Contact: info@authomize.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import secret_server_openapiclient
from secret_server_openapiclient.api.proxy_api import ProxyApi  # noqa: E501


class TestProxyApi(unittest.TestCase):
    """ProxyApi unit test stubs"""

    def setUp(self):
        self.api = ProxyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_proxy_service_create_terminal_client_overrides(self):
        """Test case for proxy_service_create_terminal_client_overrides

        Creates SSH Terminal client overrides  # noqa: E501
        """
        pass

    def test_proxy_service_delete_terminal_client_overrides(self):
        """Test case for proxy_service_delete_terminal_client_overrides

        Deletes SSH Terminal client overrides  # noqa: E501
        """
        pass

    def test_proxy_service_generate_rdp_proxy_certificate(self):
        """Test case for proxy_service_generate_rdp_proxy_certificate

        Generate RDP server certificate  # noqa: E501
        """
        pass

    def test_proxy_service_generate_ssh_host_key(self):
        """Test case for proxy_service_generate_ssh_host_key

        Generate SSH Host Key  # noqa: E501
        """
        pass

    def test_proxy_service_get_audits(self):
        """Test case for proxy_service_get_audits

        Get the Proxy Audit List  # noqa: E501
        """
        pass

    def test_proxy_service_get_endpoint_notification(self):
        """Test case for proxy_service_get_endpoint_notification

        Get endpoint warnings  # noqa: E501
        """
        pass

    def test_proxy_service_get_endpoints(self):
        """Test case for proxy_service_get_endpoints

        Get the proxy endpoints list  # noqa: E501
        """
        pass

    def test_proxy_service_get_explanations(self):
        """Test case for proxy_service_get_explanations

        Get Proxy Explanations  # noqa: E501
        """
        pass

    def test_proxy_service_get_proxying_state(self):
        """Test case for proxy_service_get_proxying_state

        Get proxy state  # noqa: E501
        """
        pass

    def test_proxy_service_get_rdp_endpoint_notification(self):
        """Test case for proxy_service_get_rdp_endpoint_notification

        Get a notification of where the RDP proxy is running  # noqa: E501
        """
        pass

    def test_proxy_service_get_rdp_proxy_configuration(self):
        """Test case for proxy_service_get_rdp_proxy_configuration

        Get the RDP proxy configuration  # noqa: E501
        """
        pass

    def test_proxy_service_get_ssh_endpoint_notification(self):
        """Test case for proxy_service_get_ssh_endpoint_notification

        Get a notification of where the SSH proxy is running  # noqa: E501
        """
        pass

    def test_proxy_service_get_ssh_proxy_configuration(self):
        """Test case for proxy_service_get_ssh_proxy_configuration

        Get the SSH proxy configuration  # noqa: E501
        """
        pass

    def test_proxy_service_get_terminal_client_history(self):
        """Test case for proxy_service_get_terminal_client_history

        Get SSH Terminal client history  # noqa: E501
        """
        pass

    def test_proxy_service_get_terminal_client_overrides(self):
        """Test case for proxy_service_get_terminal_client_overrides

        Get SSH Terminal client overrides  # noqa: E501
        """
        pass

    def test_proxy_service_get_terminal_clients(self):
        """Test case for proxy_service_get_terminal_clients

        Get SSH Terminal clients  # noqa: E501
        """
        pass

    def test_proxy_service_patch_engine(self):
        """Test case for proxy_service_patch_engine

        Update an engine proxy configuration  # noqa: E501
        """
        pass

    def test_proxy_service_patch_node(self):
        """Test case for proxy_service_patch_node

        Update a node proxy configuration  # noqa: E501
        """
        pass

    def test_proxy_service_patch_rdp_proxy_configuration(self):
        """Test case for proxy_service_patch_rdp_proxy_configuration

        Update the RDP proxy configuration  # noqa: E501
        """
        pass

    def test_proxy_service_patch_site(self):
        """Test case for proxy_service_patch_site

        Update a site proxy configuration  # noqa: E501
        """
        pass

    def test_proxy_service_patch_ssh_proxy_configuration(self):
        """Test case for proxy_service_patch_ssh_proxy_configuration

        Update the SSH proxy configuration  # noqa: E501
        """
        pass

    def test_proxy_service_update_terminal_client_overrides(self):
        """Test case for proxy_service_update_terminal_client_overrides

        Updates SSH Terminal client overrides  # noqa: E501
        """
        pass

    def test_proxy_service_update_terminal_client_type(self):
        """Test case for proxy_service_update_terminal_client_type

        Updates a SSH Terminal client type  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
