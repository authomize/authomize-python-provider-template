"""
    Secret Server Rest API

    REST API documentation for Secret Server. This document describes how to use the REST API. All requests require an authentication token; please see the <a href=\"../OAuth/\">authentication document</a> for more information. The <a href=\"swagger.json\">Swagger specification</a> for this API is also available.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 11.2.2
    Contact: info@authomize.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import secret_server_openapiclient
from secret_server_openapiclient.api.diagnostics_api import DiagnosticsApi  # noqa: E501


class TestDiagnosticsApi(unittest.TestCase):
    """DiagnosticsApi unit test stubs"""

    def setUp(self):
        self.api = DiagnosticsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_diagnostics_service_clear_quartz_job_errors(self):
        """Test case for diagnostics_service_clear_quartz_job_errors

        Clear Quartz Job Errors  # noqa: E501
        """
        pass

    def test_diagnostics_service_clear_upgrade_in_progress(self):
        """Test case for diagnostics_service_clear_upgrade_in_progress

        Clear Upgrade In Progress  # noqa: E501
        """
        pass

    def test_diagnostics_service_get_app_settings(self):
        """Test case for diagnostics_service_get_app_settings

        Get App Settings  # noqa: E501
        """
        pass

    def test_diagnostics_service_get_background_processes(self):
        """Test case for diagnostics_service_get_background_processes

        Get Background Processes  # noqa: E501
        """
        pass

    def test_diagnostics_service_get_computer_scan_logs(self):
        """Test case for diagnostics_service_get_computer_scan_logs

        Get ComputerScan Logs  # noqa: E501
        """
        pass

    def test_diagnostics_service_get_connectivity_report(self):
        """Test case for diagnostics_service_get_connectivity_report

        Get Connectivity Report  # noqa: E501
        """
        pass

    def test_diagnostics_service_get_diagnostic_information(self):
        """Test case for diagnostics_service_get_diagnostic_information

        Get Diagnostic Information  # noqa: E501
        """
        pass

    def test_diagnostics_service_get_discovery_logs(self):
        """Test case for diagnostics_service_get_discovery_logs

        Get Discovery Logs  # noqa: E501
        """
        pass

    def test_diagnostics_service_get_general_logs(self):
        """Test case for diagnostics_service_get_general_logs

        Get General Logs  # noqa: E501
        """
        pass

    def test_diagnostics_service_get_heartbeat_logs(self):
        """Test case for diagnostics_service_get_heartbeat_logs

        Get Heartbeat Logs  # noqa: E501
        """
        pass

    def test_diagnostics_service_get_quartz_jobs(self):
        """Test case for diagnostics_service_get_quartz_jobs

        Get Quartz Jobs  # noqa: E501
        """
        pass

    def test_diagnostics_service_get_rpc_logs(self):
        """Test case for diagnostics_service_get_rpc_logs

        Get RPC Logs  # noqa: E501
        """
        pass

    def test_diagnostics_service_get_system_logs(self):
        """Test case for diagnostics_service_get_system_logs

        Get System Logs  # noqa: E501
        """
        pass

    def test_diagnostics_service_test_event_log(self):
        """Test case for diagnostics_service_test_event_log

        Test Event Log  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()