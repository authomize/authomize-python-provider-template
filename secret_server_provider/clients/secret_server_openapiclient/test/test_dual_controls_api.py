"""
    Secret Server Rest API

    REST API documentation for Secret Server. This document describes how to use the REST API. All requests require an authentication token; please see the <a href=\"../OAuth/\">authentication document</a> for more information. The <a href=\"swagger.json\">Swagger specification</a> for this API is also available.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 11.2.2
    Contact: info@authomize.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import secret_server_openapiclient
from secret_server_openapiclient.api.dual_controls_api import DualControlsApi  # noqa: E501


class TestDualControlsApi(unittest.TestCase):
    """DualControlsApi unit test stubs"""

    def setUp(self):
        self.api = DualControlsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_dual_controls_service_authorize_dual_control(self):
        """Test case for dual_controls_service_authorize_dual_control

        Authorize a dual control  # noqa: E501
        """
        pass

    def test_dual_controls_service_create(self):
        """Test case for dual_controls_service_create

        Create Dual Control  # noqa: E501
        """
        pass

    def test_dual_controls_service_delete(self):
        """Test case for dual_controls_service_delete

        Delete Dual Control  # noqa: E501
        """
        pass

    def test_dual_controls_service_get(self):
        """Test case for dual_controls_service_get

        Get Dual Control  # noqa: E501
        """
        pass

    def test_dual_controls_service_get_all_reports(self):
        """Test case for dual_controls_service_get_all_reports

        Get dual control state for the current item  # noqa: E501
        """
        pass

    def test_dual_controls_service_get_types(self):
        """Test case for dual_controls_service_get_types

        Get Dual Control Types  # noqa: E501
        """
        pass

    def test_dual_controls_service_search_dual_controls(self):
        """Test case for dual_controls_service_search_dual_controls

        Search Dual Controls  # noqa: E501
        """
        pass

    def test_dual_controls_service_stub(self):
        """Test case for dual_controls_service_stub

        Get Dual Control Stub  # noqa: E501
        """
        pass

    def test_dual_controls_service_update(self):
        """Test case for dual_controls_service_update

        Update Dual Control  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
