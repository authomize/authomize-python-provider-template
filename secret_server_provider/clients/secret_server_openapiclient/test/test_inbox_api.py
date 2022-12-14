"""
    Secret Server Rest API

    REST API documentation for Secret Server. This document describes how to use the REST API. All requests require an authentication token; please see the <a href=\"../OAuth/\">authentication document</a> for more information. The <a href=\"swagger.json\">Swagger specification</a> for this API is also available.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 11.2.2
    Contact: info@authomize.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import secret_server_openapiclient
from secret_server_openapiclient.api.inbox_api import InboxApi  # noqa: E501


class TestInboxApi(unittest.TestCase):
    """InboxApi unit test stubs"""

    def setUp(self):
        self.api = InboxApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_inbox_service_copy_inbox_template(self):
        """Test case for inbox_service_copy_inbox_template

        Copy an  inbox template  # noqa: E501
        """
        pass

    def test_inbox_service_create_inbox_template(self):
        """Test case for inbox_service_create_inbox_template

        Create inbox template  # noqa: E501
        """
        pass

    def test_inbox_service_create_inbox_template_locale(self):
        """Test case for inbox_service_create_inbox_template_locale

        Create inbox template locale  # noqa: E501
        """
        pass

    def test_inbox_service_delete_resource(self):
        """Test case for inbox_service_delete_resource

        Delete inbox resource  # noqa: E501
        """
        pass

    def test_inbox_service_get_inbox_message(self):
        """Test case for inbox_service_get_inbox_message

        Get Inbox Message by Id  # noqa: E501
        """
        pass

    def test_inbox_service_get_inbox_message_data_names(self):
        """Test case for inbox_service_get_inbox_message_data_names

        Inbox Message Type Data Names  # noqa: E501
        """
        pass

    def test_inbox_service_get_inbox_message_types(self):
        """Test case for inbox_service_get_inbox_message_types

        Get inbox message types  # noqa: E501
        """
        pass

    def test_inbox_service_get_inbox_template(self):
        """Test case for inbox_service_get_inbox_template

        Get inbox template  # noqa: E501
        """
        pass

    def test_inbox_service_get_inbox_template_locale(self):
        """Test case for inbox_service_get_inbox_template_locale

        Get inbox template locale  # noqa: E501
        """
        pass

    def test_inbox_service_get_inbox_templates(self):
        """Test case for inbox_service_get_inbox_templates

        Get inbox templates  # noqa: E501
        """
        pass

    def test_inbox_service_get_notifications(self):
        """Test case for inbox_service_get_notifications

        Get inbox notifications  # noqa: E501
        """
        pass

    def test_inbox_service_get_notifications_status(self):
        """Test case for inbox_service_get_notifications_status

        Notification Status  # noqa: E501
        """
        pass

    def test_inbox_service_get_resource(self):
        """Test case for inbox_service_get_resource

        Get inbox resource  # noqa: E501
        """
        pass

    def test_inbox_service_mark_alert_notification_read(self):
        """Test case for inbox_service_mark_alert_notification_read

        Mark alert notification as read  # noqa: E501
        """
        pass

    def test_inbox_service_mark_alert_notification_unread(self):
        """Test case for inbox_service_mark_alert_notification_unread

        Mark alert notification as unread  # noqa: E501
        """
        pass

    def test_inbox_service_patch_inbox_template(self):
        """Test case for inbox_service_patch_inbox_template

        Patch inbox template  # noqa: E501
        """
        pass

    def test_inbox_service_patch_inbox_template_locale(self):
        """Test case for inbox_service_patch_inbox_template_locale

        Patch inbox template locale  # noqa: E501
        """
        pass

    def test_inbox_service_search_inbox_messages(self):
        """Test case for inbox_service_search_inbox_messages

        Search inbox messages  # noqa: E501
        """
        pass

    def test_inbox_service_search_resources(self):
        """Test case for inbox_service_search_resources

        Get inbox resources  # noqa: E501
        """
        pass

    def test_inbox_service_send_test_message(self):
        """Test case for inbox_service_send_test_message

        Send Test Inbox Message  # noqa: E501
        """
        pass

    def test_inbox_service_update_message_read_status(self):
        """Test case for inbox_service_update_message_read_status

        Mark messages read or unread  # noqa: E501
        """
        pass

    def test_inbox_service_upload_resource(self):
        """Test case for inbox_service_upload_resource

        Upload an embedded resource  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
