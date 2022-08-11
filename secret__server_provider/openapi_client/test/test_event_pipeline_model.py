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
from plugins.model.event_pipeline_filter_model import EventPipelineFilterModel
from plugins.model.event_pipeline_task_model import EventPipelineTaskModel
from plugins.model.event_pipeline_trigger_model import EventPipelineTriggerModel
globals()['EventPipelineFilterModel'] = EventPipelineFilterModel
globals()['EventPipelineTaskModel'] = EventPipelineTaskModel
globals()['EventPipelineTriggerModel'] = EventPipelineTriggerModel
from plugins.model.event_pipeline_model import EventPipelineModel


class TestEventPipelineModel(unittest.TestCase):
    """EventPipelineModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEventPipelineModel(self):
        """Test EventPipelineModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EventPipelineModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
