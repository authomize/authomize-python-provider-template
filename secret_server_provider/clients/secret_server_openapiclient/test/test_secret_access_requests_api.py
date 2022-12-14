"""
    Secret Server Rest API

    REST API documentation for Secret Server. This document describes how to use the REST API. All requests require an authentication token; please see the <a href=\"../OAuth/\">authentication document</a> for more information. The <a href=\"swagger.json\">Swagger specification</a> for this API is also available.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 11.2.2
    Contact: info@authomize.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import secret_server_openapiclient
from secret_server_openapiclient.api.secret_access_requests_api import SecretAccessRequestsApi  # noqa: E501


class TestSecretAccessRequestsApi(unittest.TestCase):
    """SecretAccessRequestsApi unit test stubs"""

    def setUp(self):
        self.api = SecretAccessRequestsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_secret_access_requests_service_create_request(self):
        """Test case for secret_access_requests_service_create_request

        Create a new Secret Access Request  # noqa: E501
        """
        pass

    def test_secret_access_requests_service_create_view_comment(self):
        """Test case for secret_access_requests_service_create_view_comment

        Create a new View Comment on a secret.  # noqa: E501
        """
        pass

    def test_secret_access_requests_service_get_history(self):
        """Test case for secret_access_requests_service_get_history

        Get Secret access request history for the user that created the request.  # noqa: E501
        """
        pass

    def test_secret_access_requests_service_get_options_by_secret(self):
        """Test case for secret_access_requests_service_get_options_by_secret

        Get Secret Access Options by Secret ID  # noqa: E501
        """
        pass

    def test_secret_access_requests_service_get_pending_request(self):
        """Test case for secret_access_requests_service_get_pending_request

        Get Secret Access Request with Current and Eligible Reviewers by ID  # noqa: E501
        """
        pass

    def test_secret_access_requests_service_get_request(self):
        """Test case for secret_access_requests_service_get_request

        Get Secret Access Request by ID  # noqa: E501
        """
        pass

    def test_secret_access_requests_service_get_requests_for_secret(self):
        """Test case for secret_access_requests_service_get_requests_for_secret

        Get Secret Access Requests by Status for Current User.  # noqa: E501
        """
        pass

    def test_secret_access_requests_service_search_requests(self):
        """Test case for secret_access_requests_service_search_requests

        Search Secret Access Requests by Status for Current User.  # noqa: E501
        """
        pass

    def test_secret_access_requests_service_update_request(self):
        """Test case for secret_access_requests_service_update_request

        Update a Secret Access Request  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
