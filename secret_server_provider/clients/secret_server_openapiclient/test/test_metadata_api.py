"""
    Secret Server Rest API

    REST API documentation for Secret Server. This document describes how to use the REST API. All requests require an authentication token; please see the <a href=\"../OAuth/\">authentication document</a> for more information. The <a href=\"swagger.json\">Swagger specification</a> for this API is also available.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 11.2.2
    Contact: info@authomize.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import secret_server_openapiclient
from secret_server_openapiclient.api.metadata_api import MetadataApi  # noqa: E501


class TestMetadataApi(unittest.TestCase):
    """MetadataApi unit test stubs"""

    def setUp(self):
        self.api = MetadataApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_metadata_service_create_metadata(self):
        """Test case for metadata_service_create_metadata

        Create Metadata  # noqa: E501
        """
        pass

    def test_metadata_service_delete_metadata(self):
        """Test case for metadata_service_delete_metadata

        Delete Metadata  # noqa: E501
        """
        pass

    def test_metadata_service_get_field_sections(self):
        """Test case for metadata_service_get_field_sections

        Get metadata field sections  # noqa: E501
        """
        pass

    def test_metadata_service_get_fields(self):
        """Test case for metadata_service_get_fields

        Get metadata fields  # noqa: E501
        """
        pass

    def test_metadata_service_search_metadata(self):
        """Test case for metadata_service_search_metadata

        Search metadata  # noqa: E501
        """
        pass

    def test_metadata_service_search_metadata_history(self):
        """Test case for metadata_service_search_metadata_history

        Search metadata history  # noqa: E501
        """
        pass

    def test_metadata_service_update_metadata(self):
        """Test case for metadata_service_update_metadata

        Update or Create Metadata  # noqa: E501
        """
        pass

    def test_metadata_service_update_metadata_field_section(self):
        """Test case for metadata_service_update_metadata_field_section

        Update a metadata field section  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()