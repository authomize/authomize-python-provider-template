"""
    Secret Server Rest API

    REST API documentation for Secret Server. This document describes how to use the REST API. All requests require an authentication token; please see the <a href=\"../OAuth/\">authentication document</a> for more information. The <a href=\"swagger.json\">Swagger specification</a> for this API is also available.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 11.2.2
    Contact: info@authomize.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import secret_server_openapiclient
from secret_server_openapiclient.model.configuration_application_settings_model import ConfigurationApplicationSettingsModel
from secret_server_openapiclient.model.configuration_email_model import ConfigurationEmailModel
from secret_server_openapiclient.model.configuration_folders_model import ConfigurationFoldersModel
from secret_server_openapiclient.model.configuration_launcher_settings_model import ConfigurationLauncherSettingsModel
from secret_server_openapiclient.model.configuration_local_user_passwords_model import ConfigurationLocalUserPasswordsModel
from secret_server_openapiclient.model.configuration_login_v2_model import ConfigurationLoginV2Model
from secret_server_openapiclient.model.configuration_permission_options_model import ConfigurationPermissionOptionsModel
from secret_server_openapiclient.model.configuration_protocol_handler_settings_model import ConfigurationProtocolHandlerSettingsModel
from secret_server_openapiclient.model.configuration_security_model import ConfigurationSecurityModel
from secret_server_openapiclient.model.configuration_session_recording_model import ConfigurationSessionRecordingModel
from secret_server_openapiclient.model.configuration_user_experience_model import ConfigurationUserExperienceModel
from secret_server_openapiclient.model.configuration_user_interface_model import ConfigurationUserInterfaceModel
from secret_server_openapiclient.model.unlimited_admin_model import UnlimitedAdminModel
globals()['ConfigurationApplicationSettingsModel'] = ConfigurationApplicationSettingsModel
globals()['ConfigurationEmailModel'] = ConfigurationEmailModel
globals()['ConfigurationFoldersModel'] = ConfigurationFoldersModel
globals()['ConfigurationLauncherSettingsModel'] = ConfigurationLauncherSettingsModel
globals()['ConfigurationLocalUserPasswordsModel'] = ConfigurationLocalUserPasswordsModel
globals()['ConfigurationLoginV2Model'] = ConfigurationLoginV2Model
globals()['ConfigurationPermissionOptionsModel'] = ConfigurationPermissionOptionsModel
globals()['ConfigurationProtocolHandlerSettingsModel'] = ConfigurationProtocolHandlerSettingsModel
globals()['ConfigurationSecurityModel'] = ConfigurationSecurityModel
globals()['ConfigurationSessionRecordingModel'] = ConfigurationSessionRecordingModel
globals()['ConfigurationUserExperienceModel'] = ConfigurationUserExperienceModel
globals()['ConfigurationUserInterfaceModel'] = ConfigurationUserInterfaceModel
globals()['UnlimitedAdminModel'] = UnlimitedAdminModel
from secret_server_openapiclient.model.configuration_general_v2_model import ConfigurationGeneralV2Model


class TestConfigurationGeneralV2Model(unittest.TestCase):
    """ConfigurationGeneralV2Model unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testConfigurationGeneralV2Model(self):
        """Test ConfigurationGeneralV2Model"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ConfigurationGeneralV2Model()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
