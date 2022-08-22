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
from plugins.model.disaster_recovery_data_replica_update_model import DisasterRecoveryDataReplicaUpdateModel
globals()['DisasterRecoveryDataReplicaUpdateModel'] = DisasterRecoveryDataReplicaUpdateModel
from plugins.model.disaster_recovery_data_replica_args import DisasterRecoveryDataReplicaArgs


class TestDisasterRecoveryDataReplicaArgs(unittest.TestCase):
    """DisasterRecoveryDataReplicaArgs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDisasterRecoveryDataReplicaArgs(self):
        """Test DisasterRecoveryDataReplicaArgs"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DisasterRecoveryDataReplicaArgs()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()