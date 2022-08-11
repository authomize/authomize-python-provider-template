"""
    Secret Server Rest API

    REST API documentation for Secret Server. This document describes how to use the REST API. All requests require an authentication token; please see the <a href=\"../OAuth/\">authentication document</a> for more information. The <a href=\"swagger.json\">Swagger specification</a> for this API is also available.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 11.2.2
    Contact: info@authomize.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import plugins
from plugins.api.event_pipeline_api import EventPipelineApi  # noqa: E501


class TestEventPipelineApi(unittest.TestCase):
    """EventPipelineApi unit test stubs"""

    def setUp(self):
        self.api = EventPipelineApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_event_pipeline_service_create_event_pipelines(self):
        """Test case for event_pipeline_service_create_event_pipelines

        Create a new Event Pipeline  # noqa: E501
        """
        pass

    def test_event_pipeline_service_get_event_pipeline(self):
        """Test case for event_pipeline_service_get_event_pipeline

        Get an Event Pipeline  # noqa: E501
        """
        pass

    def test_event_pipeline_service_get_event_pipeline_runs(self):
        """Test case for event_pipeline_service_get_event_pipeline_runs

        Get Event Pipeline Runs  # noqa: E501
        """
        pass

    def test_event_pipeline_service_get_event_pipeline_stub(self):
        """Test case for event_pipeline_service_get_event_pipeline_stub

        Stub an empty Event Pipeline  # noqa: E501
        """
        pass

    def test_event_pipeline_service_get_event_pipeline_summaries(self):
        """Test case for event_pipeline_service_get_event_pipeline_summaries

        Get summaries of Event Pipelines  # noqa: E501
        """
        pass

    def test_event_pipeline_service_get_event_pipelines(self):
        """Test case for event_pipeline_service_get_event_pipelines

        Get a list of Event Pipelines  # noqa: E501
        """
        pass

    def test_event_pipeline_service_reorder_pipeline(self):
        """Test case for event_pipeline_service_reorder_pipeline

        Reorder an Event Pipeline  # noqa: E501
        """
        pass

    def test_event_pipeline_service_toggle_pipeline_active(self):
        """Test case for event_pipeline_service_toggle_pipeline_active

        Update an Event Pipeline active value  # noqa: E501
        """
        pass

    def test_event_pipeline_service_update_event_pipelines(self):
        """Test case for event_pipeline_service_update_event_pipelines

        Update an Event Pipeline  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
