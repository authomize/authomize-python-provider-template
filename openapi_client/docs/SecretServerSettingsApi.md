# plugins.SecretServerSettingsApi

All URIs are relative to *https://integrations.secretservercloud.com//api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**secret_server_settings_service_get_export**](SecretServerSettingsApi.md#secret_server_settings_service_get_export) | **GET** /v1/secretserversettings/export | Get Secret Server Settings
[**secret_server_settings_service_get_export_import_capabilities**](SecretServerSettingsApi.md#secret_server_settings_service_get_export_import_capabilities) | **POST** /v1/secretserversettings/capabilities | Get Import/Export Capabilities
[**secret_server_settings_service_get_export_stub**](SecretServerSettingsApi.md#secret_server_settings_service_get_export_stub) | **GET** /v1/secretserversettings/export/stub | Stub an empty Secret Server Settings export
[**secret_server_settings_service_import_setting**](SecretServerSettingsApi.md#secret_server_settings_service_import_setting) | **POST** /v1/secretserversettings/import | Import Secret Server Settings


# **secret_server_settings_service_get_export**
> SecretServerSettingsModel secret_server_settings_service_get_export()

Get Secret Server Settings

Get Secret Server Settings

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_server_settings_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.secret_server_settings_model import SecretServerSettingsModel
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com//api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
    host = "https://integrations.secretservercloud.com//api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'

# Enter a context with an instance of the API client
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secret_server_settings_api.SecretServerSettingsApi(api_client)
    load_advanced_settings = True # bool | LoadAdvancedSettings (optional)
    load_all = True # bool | LoadAll (optional)
    load_application_settings = True # bool | LoadApplicationSettings (optional)
    load_email = True # bool | LoadEmail (optional)
    load_folder_settings = True # bool | LoadFolderSettings (optional)
    load_launcher_settings = True # bool | LoadLauncherSettings (optional)
    load_licenses = True # bool | LoadLicenses (optional)
    load_local_user_passwords = True # bool | LoadLocalUserPasswords (optional)
    load_login = True # bool | LoadLogin (optional)
    load_permission_options = True # bool | LoadPermissionOptions (optional)
    load_protocol_handler_settings = True # bool | LoadProtocolHandlerSettings (optional)
    load_saml = True # bool | LoadSaml (optional)
    load_security = True # bool | LoadSecurity (optional)
    load_session_recording = True # bool | LoadSessionRecording (optional)
    load_ssh_commands = True # bool | LoadSshCommands (optional)
    load_ticket_system = True # bool | LoadTicketSystem (optional)
    load_user_experience = True # bool | LoadUserExperience (optional)
    load_user_interface = True # bool | LoadUserInterface (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Secret Server Settings
        api_response = api_instance.secret_server_settings_service_get_export(load_advanced_settings=load_advanced_settings, load_all=load_all, load_application_settings=load_application_settings, load_email=load_email, load_folder_settings=load_folder_settings, load_launcher_settings=load_launcher_settings, load_licenses=load_licenses, load_local_user_passwords=load_local_user_passwords, load_login=load_login, load_permission_options=load_permission_options, load_protocol_handler_settings=load_protocol_handler_settings, load_saml=load_saml, load_security=load_security, load_session_recording=load_session_recording, load_ssh_commands=load_ssh_commands, load_ticket_system=load_ticket_system, load_user_experience=load_user_experience, load_user_interface=load_user_interface)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretServerSettingsApi->secret_server_settings_service_get_export: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **load_advanced_settings** | **bool**| LoadAdvancedSettings | [optional]
 **load_all** | **bool**| LoadAll | [optional]
 **load_application_settings** | **bool**| LoadApplicationSettings | [optional]
 **load_email** | **bool**| LoadEmail | [optional]
 **load_folder_settings** | **bool**| LoadFolderSettings | [optional]
 **load_launcher_settings** | **bool**| LoadLauncherSettings | [optional]
 **load_licenses** | **bool**| LoadLicenses | [optional]
 **load_local_user_passwords** | **bool**| LoadLocalUserPasswords | [optional]
 **load_login** | **bool**| LoadLogin | [optional]
 **load_permission_options** | **bool**| LoadPermissionOptions | [optional]
 **load_protocol_handler_settings** | **bool**| LoadProtocolHandlerSettings | [optional]
 **load_saml** | **bool**| LoadSaml | [optional]
 **load_security** | **bool**| LoadSecurity | [optional]
 **load_session_recording** | **bool**| LoadSessionRecording | [optional]
 **load_ssh_commands** | **bool**| LoadSshCommands | [optional]
 **load_ticket_system** | **bool**| LoadTicketSystem | [optional]
 **load_user_experience** | **bool**| LoadUserExperience | [optional]
 **load_user_interface** | **bool**| LoadUserInterface | [optional]

### Return type

[**SecretServerSettingsModel**](SecretServerSettingsModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Server Settings |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_server_settings_service_get_export_import_capabilities**
> SecretServerSettingsImportCapabilityModel secret_server_settings_service_get_export_import_capabilities()

Get Import/Export Capabilities

Returns model indicating what the user can import and export.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_server_settings_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.secret_server_settings_import_capability_model import SecretServerSettingsImportCapabilityModel
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_server_settings_import_capabilities_args import SecretServerSettingsImportCapabilitiesArgs
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com//api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
    host = "https://integrations.secretservercloud.com//api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'

# Enter a context with an instance of the API client
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secret_server_settings_api.SecretServerSettingsApi(api_client)
    secret_server_settings_import_capabilities_args = SecretServerSettingsImportCapabilitiesArgs(
        file=None,
        is_import=True,
    ) # SecretServerSettingsImportCapabilitiesArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Import/Export Capabilities
        api_response = api_instance.secret_server_settings_service_get_export_import_capabilities(secret_server_settings_import_capabilities_args=secret_server_settings_import_capabilities_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretServerSettingsApi->secret_server_settings_service_get_export_import_capabilities: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_server_settings_import_capabilities_args** | [**SecretServerSettingsImportCapabilitiesArgs**](SecretServerSettingsImportCapabilitiesArgs.md)| args | [optional]

### Return type

[**SecretServerSettingsImportCapabilityModel**](SecretServerSettingsImportCapabilityModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Capability model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_server_settings_service_get_export_stub**
> SecretServerSettingsModel secret_server_settings_service_get_export_stub()

Stub an empty Secret Server Settings export

Returns an empty Secret Server Settings export to be filled out.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_server_settings_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.secret_server_settings_model import SecretServerSettingsModel
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com//api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
    host = "https://integrations.secretservercloud.com//api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'

# Enter a context with an instance of the API client
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secret_server_settings_api.SecretServerSettingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Stub an empty Secret Server Settings export
        api_response = api_instance.secret_server_settings_service_get_export_stub()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretServerSettingsApi->secret_server_settings_service_get_export_stub: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SecretServerSettingsModel**](SecretServerSettingsModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An empty Secret Server Settings export |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_server_settings_service_import_setting**
> SecretServerSettingsImportResultModel secret_server_settings_service_import_setting()

Import Secret Server Settings

Apply a set of Secret Server Settings via a JSON upload.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_server_settings_api
from plugins.model.secret_server_settings_import_args import SecretServerSettingsImportArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_server_settings_import_result_model import SecretServerSettingsImportResultModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com//api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
    host = "https://integrations.secretservercloud.com//api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'

# Enter a context with an instance of the API client
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secret_server_settings_api.SecretServerSettingsApi(api_client)
    secret_server_settings_import_args = SecretServerSettingsImportArgs(
        data=SecretServerSettingsPatchModel(
            advanced_settings=[
                ConfigurationAdvancedUpdateArgs(
                    advanced_setting_id=None,
                    value=None,
                ),
            ],
            application_settings=ConfigurationApplicationSettingsPatchModel(
                allow_send_telemetry=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                allow_software_update_checks=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                api_refresh_tokens_enabled=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                api_session_timeout_days=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=None,
                ),
                api_session_timeout_hours=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=None,
                ),
                api_session_timeout_minutes=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=None,
                ),
                api_session_timeout_unlimited=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                configuration_early_adopter_enabled=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                custom_url=UpdateFieldValueOfString(
                    dirty=True,
                    value=None,
                ),
                display_downtime_message_to_admins_only=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                enable_cred_ssp=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                enable_syslog_cef_logging=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                enable_web_services=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                external_instance_id=True,
                maximum_token_refreshes_allowed=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=None,
                ),
                max_secret_log_length=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=None,
                ),
                mobile_max_offline_days=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=None,
                ),
                mobile_max_offline_hours=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=None,
                ),
                obfuscate_personally_identifiable_information=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                pii_obfuscation_level=UpdateFieldValueOfString(
                    dirty=True,
                    value=None,
                ),
                prevent_application_from_sleeping=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                prevent_direct_api_authentication=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                syslog_cef_log_site=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=None,
                ),
                syslog_cef_port=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=None,
                ),
                syslog_cef_protocol=UpdateFieldValueOfSyslogCefProtocolType(
                    dirty=True,
                    value=SyslogCefProtocolType("{}"),
                ),
                syslog_cef_server=UpdateFieldValueOfString(
                    dirty=True,
                    value=None,
                ),
                syslog_cef_time_zone=UpdateFieldValueOfSyslogCefTimeZoneType(
                    dirty=True,
                    value=SyslogCefTimeZoneType("{}"),
                ),
                tms_installation_path=UpdateFieldValueOfString(
                    dirty=True,
                    value=None,
                ),
                win_rm_endpoint_url=UpdateFieldValueOfString(
                    dirty=True,
                    value=None,
                ),
                write_syslog_to_event_log=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
            ),
            configuration_version=None,
            email=ConfigurationEmailPatchModel(
                from_email_address=UpdateFieldValueOfString(
                    dirty=True,
                    value=None,
                ),
                from_email_name=UpdateFieldValueOfString(
                    dirty=True,
                    value=None,
                ),
                send_legacy_emails=UpdateFieldValueOfOptionalBoolean(
                    dirty=True,
                    value=True,
                ),
                smtp_check_certificate_revocation=UpdateFieldValueOfOptionalBoolean(
                    dirty=True,
                    value=True,
                ),
                smtp_domain=UpdateFieldValueOfString(
                    dirty=True,
                    value=None,
                ),
                smtp_password=UpdateFieldValueOfString(
                    dirty=True,
                    value=None,
                ),
                smtp_port=UpdateFieldValueOfOptionalInt32(
                    dirty=True,
                    value=None,
                ),
                smtp_server=UpdateFieldValueOfString(
                    dirty=True,
                    value=None,
                ),
                smtp_use_credentials=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                smtp_use_implicit_ssl=UpdateFieldValueOfOptionalBoolean(
                    dirty=True,
                    value=True,
                ),
                smtp_user_name=UpdateFieldValueOfString(
                    dirty=True,
                    value=None,
                ),
                smtp_use_ssl=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
            ),
            external_instance_id=None,
            folder_settings=ConfigurationFoldersPatchModel(
                enable_personal_folders=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                personal_folder_name=UpdateFieldValueOfString(
                    dirty=True,
                    value=None,
                ),
                personal_folder_name_option=UpdateFieldValueOfPersonalFolderNameOptionType(
                    dirty=True,
                    value=PersonalFolderNameOptionType("{}"),
                ),
                personal_folder_warning=UpdateFieldValueOfString(
                    dirty=True,
                    value=None,
                ),
                require_view_folder_permission=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                show_personal_folder_warning=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
            ),
            launcher_settings=ConfigurationLauncherSettingsPatchModel(
                check_in_secret_on_last_launcher_close=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                close_launcher_on_check_in_secret=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                enable_domain_download=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                enable_domain_upload=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                enable_launcher=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                enable_launcher_auto_update=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                enable_web_parsing=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                launcher_deployment_type=UpdateFieldValueOfLauncherDeploymentType(
                    dirty=True,
                    value=LauncherDeploymentType("{}"),
                ),
                send_secret_url_to_launcher=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
            ),
            licenses=[
                LicenseModel(
                    description=None,
                    license_key=None,
                    license_name=None,
                ),
            ],
            local_user_passwords=ConfigurationLocalPasswordPatchModel(
                allow_users_to_reset_forgotten_passwords=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                enable_local_user_password_expiration=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                enable_minimum_password_age=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                enable_password_history=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                local_user_password_expiration_days=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=None,
                ),
                local_user_password_expiration_hours=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=None,
                ),
                local_user_password_expiration_minutes=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=None,
                ),
                minimum_password_age_days=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=None,
                ),
                minimum_password_age_hours=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=None,
                ),
                minimum_password_age_minutes=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=None,
                ),
                password_history_items=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=None,
                ),
                password_history_items_all=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                password_minimum_length=UpdateFieldValueOfOptionalInt32(
                    dirty=True,
                    value=None,
                ),
                password_require_lowercase=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                password_require_numbers=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                password_require_symbols=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                password_require_uppercase=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
            ),
            login=ConfigurationLoginPatchModel(
                allow_auto_complete=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                allow_remember_me=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                cache_ad_credentials=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                default_login_domain=UpdateFieldValueOfString(
                    dirty=True,
                    value=None,
                ),
                enable_domain_selector=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=None,
                ),
                enable_login_failure_captcha=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                max_concurrent_logins_per_user=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=None,
                ),
                maximum_login_failures=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=None,
                ),
                max_login_failures_before_captcha=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=None,
                ),
                remember_me_time_out_minutes=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=None,
                ),
                ssh_key_integration=ConfigurationLoginSshKeyIntegrationPatchModel(
                    authentication_method=UpdateFieldValueOfInt32(
                        dirty=True,
                        value=None,
                    ),
                    enable=UpdateFieldValueOfBoolean(
                        dirty=True,
                        value=True,
                    ),
                    expiration_in_hours=UpdateFieldValueOfInt32(
                        dirty=True,
                        value=None,
                    ),
                    key_expires=UpdateFieldValueOfBoolean(
                        dirty=True,
                        value=True,
                    ),
                    two_factor_bypass=UpdateFieldValueOfBoolean(
                        dirty=True,
                        value=True,
                    ),
                ),
                two_factor=ConfigurationLoginTwoFactorPatchModel(
                    allow_two_factor_remember_me=UpdateFieldValueOfBoolean(
                        dirty=True,
                        value=True,
                    ),
                    duo=ConfigurationLoginTwoFactorDuoPatchModel(
                        api_hostname=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        enable=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                        integration_key=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        secret_key=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        use_radius_username=UpdateFieldValueOfOptionalBoolean(
                            dirty=True,
                            value=True,
                        ),
                    ),
                    open_id_connect=ConfigurationLoginTwoFactorOpenIdConnectPatchModel(
                        add_new_users_to_thycotic_one=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                        client_id=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        client_secret=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        enable=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                        logout_url=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        server_url=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        use_thycotic_one_auth_as_default=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                    ),
                    radius=ConfigurationLoginTwoFactorRadiusPatchModel(
                        attempt_user_password=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                        client_port_range=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        default_username=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        disable_nas_ip_address_attribute=UpdateFieldValueOfOptionalBoolean(
                            dirty=True,
                            value=True,
                        ),
                        enable=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                        enable_failover_server=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                        enable_radius_nas_id=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                        failover_server_ip=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        failover_server_port=UpdateFieldValueOfInt32(
                            dirty=True,
                            value=None,
                        ),
                        failover_shared_secret=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        failover_timeout_seconds=UpdateFieldValueOfInt32(
                            dirty=True,
                            value=None,
                        ),
                        login_explanation=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        nas_id=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        protocol=UpdateFieldValueOfInt32(
                            dirty=True,
                            value=None,
                        ),
                        server_ip=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        server_port=UpdateFieldValueOfInt32(
                            dirty=True,
                            value=None,
                        ),
                        shared_secret=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        shared_secret_same_for_all_users=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                        timeout_seconds=UpdateFieldValueOfInt32(
                            dirty=True,
                            value=None,
                        ),
                    ),
                    require_two_factor_for_web_login=UpdateFieldValueOfBoolean(
                        dirty=True,
                        value=True,
                    ),
                    require_two_factor_for_web_services=UpdateFieldValueOfBoolean(
                        dirty=True,
                        value=True,
                    ),
                    two_factor_remember_me_time_out_days=UpdateFieldValueOfInt32(
                        dirty=True,
                        value=None,
                    ),
                ),
                user_lockout_time_minutes=UpdateFieldValueOfOptionalInt32(
                    dirty=True,
                    value=None,
                ),
                visual_encrypted_keyboard_enabled=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                visual_encrypted_keyboard_required=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
            ),
            permission_options=ConfigurationPermissionOptionsPatchModel(
                allow_duplicate_secret_names=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                allow_view_user_to_retrieve_auto_change_next_password=UpdateFieldValueOfOptionalBoolean(
                    dirty=True,
                    value=True,
                ),
                default_secret_permissions=UpdateFieldValueOfDefaultSecretPermissionsType(
                    dirty=True,
                    value=DefaultSecretPermissionsType("{}"),
                ),
                enable_approval_from_email=UpdateFieldValueOfOptionalBoolean(
                    dirty=True,
                    value=True,
                ),
                force_secret_approval=UpdateFieldValueOfOptionalForceSecretApprovalType(
                    dirty=True,
                    value=None,
                ),
            ),
            protocol_handler_settings=ConfigurationProtocolHandlerSettingsPatchModel(
                protocol_handler_install_time_allowed_domains=UpdateFieldValueOfString(
                    dirty=True,
                    value=None,
                ),
                protocol_handler_install_time_disable_auto_update=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                protocol_handler_install_time_settings_enabled=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
            ),
            saml=ConfigurationSamlPatchModel(
                enabled=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                enable_legacy_slo=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                identity_providers=[
                    ConfigurationSamlIdentityProviderPatchModel(
                        active=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                        authn_context=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        clock_skew=UpdateFieldValueOfInt32(
                            dirty=True,
                            value=None,
                        ),
                        description=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        disable_assertion_replay_check=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                        disable_audience_restriction_check=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                        disable_authn_context_check=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                        disable_destination_check=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                        disable_inbound_logout=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                        disable_in_response_to_check=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                        disable_pending_logout_check=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                        disable_recipient_check=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                        disable_time_period_check=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                        display_name=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        domain_attribute=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        enable_detailed_log=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                        enable_slo=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                        force_authentication=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                        identity_provider_id=None,
                        logout_request_life_time=UpdateFieldValueOfInt32(
                            dirty=True,
                            value=None,
                        ),
                        name=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        override_pending_authn_request=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                        public_certificate=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        sign_authn_request=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                        sign_logout_request=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                        sign_logout_response=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                        single_logout_service_response_url=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        single_logout_service_url=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        sso_service_binding=UpdateFieldValueOfInt32(
                            dirty=True,
                            value=None,
                        ),
                        sso_service_url=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        username_attribute=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        want_assertion_encrypted=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                        want_assertion_or_response_signed=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                        want_assertion_signed=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                        want_logout_request_signed=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                        want_logout_response_signed=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                        want_saml_response_signed=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                    ),
                ],
                legacy_username_attribute=UpdateFieldValueOfString(
                    dirty=True,
                    value=None,
                ),
                service_provider_certificate=UpdateFieldValueOfString(
                    dirty=True,
                    value=None,
                ),
                service_provider_certificate_password=UpdateFieldValueOfString(
                    dirty=True,
                    value=None,
                ),
                service_provider_name=UpdateFieldValueOfString(
                    dirty=True,
                    value=None,
                ),
                use_legacy=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
            ),
            security=ConfigurationSecurityPatchModel(
                allow_web_service_http_get=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                audit_tls_errors=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                audit_tls_errors_debug=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                certificate_chain_policy_options=UpdateFieldValueOfString(
                    dirty=True,
                    value=None,
                ),
                client_certificate_ids=UpdateFieldValueOfString(
                    dirty=True,
                    value=None,
                ),
                database_integrity_monitoring_symmetric_key=UpdateFieldValueOfString(
                    dirty=True,
                    value=None,
                ),
                enable_database_integrity_monitoring=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                enable_file_restrictions=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                enable_frame_blocking=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                enable_hsts=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                enable_secret_erase=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                file_extension_restrictions=UpdateFieldValueOfString(
                    dirty=True,
                    value=None,
                ),
                fips_enabled=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                force_https=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                hide_version_number=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                hsts_max_age=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=None,
                ),
                ignore_certificate_revocation_failures=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                maximum_file_size_bytes=UpdateFieldValueOfString(
                    dirty=True,
                    value=None,
                ),
                maximum_file_size_supported=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                secret_erase_workflow=UpdateFieldValueOfOptionalInt32(
                    dirty=True,
                    value=None,
                ),
                web_password_filler_requires_full_domain_match=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
            ),
            session_recording=ConfigurationSessionRecordingPatchModel(
                archive_location_by_site=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                archive_path=UpdateFieldValueOfString(
                    dirty=True,
                    value=None,
                ),
                days_until_archive=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=None,
                ),
                days_until_delete=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=None,
                ),
                enable_archive=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                enable_delete=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                enable_hardware_acceleration=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                enable_inactivity_timeout=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                enable_on_demand_video_processing=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                enable_session_recording=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                encrypt_archive=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                hide_recording_indicator=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                inactivity_timeout_minutes=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=None,
                ),
                max_session_length=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=None,
                ),
                rdp_proxy_record_key_strokes=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                rdp_proxy_record_video=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                ssh_proxy_record_key_strokes=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                ssh_proxy_record_video=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                store_in_database=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                use_temporary_archives=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                video_codec_id=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=None,
                ),
            ),
            ssh_commands=ConfigurationSshCommandImportModel(
                ssh_command_blocklists=[
                    SshCommandBlocklistPatchModel(
                        active=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                        description=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        name=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        ssh_command_blocklist_id=None,
                        ssh_command_ids=UpdateFieldValueOfGuidArray(
                            dirty=True,
                            value=[
                                None,
                            ],
                        ),
                    ),
                ],
                ssh_command_menu_maps=[
                    ConfigurationSshCommandMenuMapModel(
                        sort_order=None,
                        ssh_command_guid=None,
                        ssh_command_menu_guid=None,
                    ),
                ],
                ssh_command_menus=[
                    ConfigurationSshCommandMenuModel(
                        active=True,
                        description=None,
                        name=None,
                        ssh_command_menu_guid=None,
                        ssh_command_menu_id=None,
                    ),
                ],
                ssh_commands=[
                    SshCommandPatchModel(
                        command=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        name=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        sort_order=UpdateFieldValueOfInt32(
                            dirty=True,
                            value=None,
                        ),
                        ssh_command_guid=None,
                        ssh_command_id=None,
                    ),
                ],
            ),
            ticket_system=ConfigurationTicketSystemListCreateOrPatchModel(
                ticket_system_list=[
                    TicketSystemPatchModel(
                        active=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                        add_comments_to_ticket=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                        bmc_change_management_comment_work_type=UpdateFieldValueOfOptionalBmcChangeManagementCommentWorkType(
                            dirty=True,
                            value=None,
                        ),
                        bmc_incident_management_comment_work_type=UpdateFieldValueOfOptionalBmcIncidentManagementCommentWorkType(
                            dirty=True,
                            value=None,
                        ),
                        bmc_remedy_authentication=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        bmc_remedy_url_endpoint=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        description=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        display_message=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        force_require_ticket_number=UpdateFieldValueOfForceRequireTicketSystemOptions(
                            dirty=True,
                            value=ForceRequireTicketSystemOptions("{}"),
                        ),
                        is_default=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                        name=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        power_shell_add_comment_script_arguments=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        power_shell_add_comment_script_id=UpdateFieldValueOfOptionalInt32(
                            dirty=True,
                            value=None,
                        ),
                        power_shell_add_ticket_comment_script_arguments=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        power_shell_add_ticket_comment_script_id=UpdateFieldValueOfOptionalInt32(
                            dirty=True,
                            value=None,
                        ),
                        power_shell_run_as_account_secret_id=UpdateFieldValueOfOptionalInt32(
                            dirty=True,
                            value=None,
                        ),
                        power_shell_ticket_status_script_arguments=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        power_shell_ticket_status_script_id=UpdateFieldValueOfOptionalInt32(
                            dirty=True,
                            value=None,
                        ),
                        service_now_allowed_statuses=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        service_now_domain_name=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        site_id=UpdateFieldValueOfOptionalInt32(
                            dirty=True,
                            value=None,
                        ),
                        system_credential_secret_id=UpdateFieldValueOfOptionalInt32(
                            dirty=True,
                            value=None,
                        ),
                        ticket_number_error_message=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        ticket_number_validation=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        ticket_system_id=None,
                        ticket_system_type=UpdateFieldValueOfTicketSystemTypes(
                            dirty=True,
                            value=TicketSystemTypes("{}"),
                        ),
                        view_ticket_url=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                    ),
                ],
            ),
            user_experience=ConfigurationUserExperiencePatchModel(
                application_language=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=None,
                ),
                checkout_notification_threshold=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=None,
                ),
                default_date_format=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=None,
                ),
                default_new_user_role_id=UpdateFieldValueOfOptionalInt32(
                    dirty=True,
                    value=None,
                ),
                default_time_format=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=None,
                ),
                force_inactivity_timeout=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                force_inactivity_timeout_minutes=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=None,
                ),
                require_folder_for_secret=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                search_delay_ms=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=None,
                ),
                secret_password_history_restriction_all=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                secret_password_history_restriction_count=UpdateFieldValueOfOptionalInt32(
                    dirty=True,
                    value=None,
                ),
                secret_view_interval_minutes=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=None,
                ),
                server_time_zone_id=UpdateFieldValueOfString(
                    dirty=True,
                    value=None,
                ),
                ui_inactivity_sleep_minutes=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=None,
                ),
            ),
            user_interface=ConfigurationUserInterfacePatchModel(
                allow_user_to_select_theme=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                custom_logo_collapsed=UpdateFieldValueOfString(
                    dirty=True,
                    value=None,
                ),
                custom_logo_full_size=UpdateFieldValueOfString(
                    dirty=True,
                    value=None,
                ),
                default_classic_theme=UpdateFieldValueOfString(
                    dirty=True,
                    value=None,
                ),
                disable_legacy_ui=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                new_ui_default=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
            ),
        ),
        filter=SecretServerSettingsQuery(
            load_advanced_settings=True,
            load_all=True,
            load_application_settings=True,
            load_email=True,
            load_folder_settings=True,
            load_launcher_settings=True,
            load_licenses=True,
            load_local_user_passwords=True,
            load_login=True,
            load_permission_options=True,
            load_protocol_handler_settings=True,
            load_saml=True,
            load_security=True,
            load_session_recording=True,
            load_ssh_commands=True,
            load_ticket_system=True,
            load_user_experience=True,
            load_user_interface=True,
        ),
    ) # SecretServerSettingsImportArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Import Secret Server Settings
        api_response = api_instance.secret_server_settings_service_import_setting(secret_server_settings_import_args=secret_server_settings_import_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretServerSettingsApi->secret_server_settings_service_import_setting: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_server_settings_import_args** | [**SecretServerSettingsImportArgs**](SecretServerSettingsImportArgs.md)| args | [optional]

### Return type

[**SecretServerSettingsImportResultModel**](SecretServerSettingsImportResultModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The now active configuration. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

