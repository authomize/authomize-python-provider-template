# secret_server_openapiclient.ConfigurationApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configuration_service_cancel_rotate_secret_keys**](ConfigurationApi.md#configuration_service_cancel_rotate_secret_keys) | **POST** /v1/configuration/security/cancel-rotate-secret-keys | Cancel Rotate Secret Keys
[**configuration_service_clear_ad_credentials**](ConfigurationApi.md#configuration_service_clear_ad_credentials) | **POST** /v1/configuration/login/clear-ad-credentials | Clear AD Credentials
[**configuration_service_clear_system_log**](ConfigurationApi.md#configuration_service_clear_system_log) | **GET** /v1/configuration/system-log/clear | Clear system log
[**configuration_service_delete_saml_configuration_identity_provider**](ConfigurationApi.md#configuration_service_delete_saml_configuration_identity_provider) | **DELETE** /v1/configuration/saml/identity-provider/{id} | Delete Saml Configuration Identity Provider
[**configuration_service_get_auto_export_configuration**](ConfigurationApi.md#configuration_service_get_auto_export_configuration) | **GET** /v1/configuration/auto-export | Get Automatic Export Configuration
[**configuration_service_get_auto_export_configuration_audits**](ConfigurationApi.md#configuration_service_get_auto_export_configuration_audits) | **GET** /v1/configuration/auto-export-audits | Get Automatic Export Configuration Audits
[**configuration_service_get_auto_export_logs**](ConfigurationApi.md#configuration_service_get_auto_export_logs) | **GET** /v1/configuration/auto-export-logs | Get Automatic Export Logs
[**configuration_service_get_auto_export_storage_item**](ConfigurationApi.md#configuration_service_get_auto_export_storage_item) | **GET** /v1/configuration/auto-export-storage/item/{id} | Get Automatic Export Storage Item
[**configuration_service_get_auto_export_storage_items**](ConfigurationApi.md#configuration_service_get_auto_export_storage_items) | **GET** /v1/configuration/auto-export-storage/{id} | Get Automatic Export Storage Items For Configuration
[**configuration_service_get_auto_export_storage_items_default**](ConfigurationApi.md#configuration_service_get_auto_export_storage_items_default) | **GET** /v1/configuration/auto-export-storage | Get Automatic Export Storage Items
[**configuration_service_get_backup_logs_v2**](ConfigurationApi.md#configuration_service_get_backup_logs_v2) | **GET** /v2/configuration/backup-logs | Get Backup Logs
[**configuration_service_get_configuration_audit**](ConfigurationApi.md#configuration_service_get_configuration_audit) | **GET** /v1/configuration/audit | Audit of system configuration changes
[**configuration_service_get_configuration_read_only_mode**](ConfigurationApi.md#configuration_service_get_configuration_read_only_mode) | **GET** /v1/configuration/read-only-mode | Get Read Only Mode Configuration
[**configuration_service_get_configuration_state**](ConfigurationApi.md#configuration_service_get_configuration_state) | **GET** /v1/configuration/state | The allowed permissions for configuration for the current user
[**configuration_service_get_database_backup_configuration**](ConfigurationApi.md#configuration_service_get_database_backup_configuration) | **GET** /v1/configuration/backup | Get Backup Configuration
[**configuration_service_get_database_configuration**](ConfigurationApi.md#configuration_service_get_database_configuration) | **GET** /v1/configuration/database | Get the database configuration
[**configuration_service_get_general_configuration_v2**](ConfigurationApi.md#configuration_service_get_general_configuration_v2) | **GET** /v2/configuration/general | Get the general configuration
[**configuration_service_get_internal_site_configuration**](ConfigurationApi.md#configuration_service_get_internal_site_configuration) | **GET** /v1/configuration/internal-site-connector | Internal Site Connector Configuration
[**configuration_service_get_local_password_configuration**](ConfigurationApi.md#configuration_service_get_local_password_configuration) | **GET** /v1/configuration/local-user-passwords | Get the local user password configuration
[**configuration_service_get_login_configuration_v2**](ConfigurationApi.md#configuration_service_get_login_configuration_v2) | **GET** /v2/configuration/login | Get Login configuration
[**configuration_service_get_login_policy_configuration**](ConfigurationApi.md#configuration_service_get_login_policy_configuration) | **GET** /v1/configuration/login-policy | Get Login Policy configuration
[**configuration_service_get_platform_configuration**](ConfigurationApi.md#configuration_service_get_platform_configuration) | **GET** /v1/configuration/platform | Get Platform Configuration
[**configuration_service_get_platform_configuration_audits**](ConfigurationApi.md#configuration_service_get_platform_configuration_audits) | **GET** /v1/configuration/platform-audits | Get Platform Configuration Audits
[**configuration_service_get_public_ssh_key_expiration**](ConfigurationApi.md#configuration_service_get_public_ssh_key_expiration) | **GET** /v1/configuration/public-ssh-key | Public SSH Key Expiration
[**configuration_service_get_rotate_secret_keys_status**](ConfigurationApi.md#configuration_service_get_rotate_secret_keys_status) | **GET** /v1/configuration/security/rotate-secret-keys-status | Get Rotate Secret Keys Status
[**configuration_service_get_rpc_configuration**](ConfigurationApi.md#configuration_service_get_rpc_configuration) | **GET** /v1/configuration/rpc | Get RPC configuration
[**configuration_service_get_saml_configuration**](ConfigurationApi.md#configuration_service_get_saml_configuration) | **GET** /v1/configuration/saml | Get Saml configuration
[**configuration_service_get_saml_identity_provider_configuration**](ConfigurationApi.md#configuration_service_get_saml_identity_provider_configuration) | **GET** /v1/configuration/saml/identity-provider/{id} | Get Saml Identity Provider configuration
[**configuration_service_get_saml_identity_provider_configuration_stub**](ConfigurationApi.md#configuration_service_get_saml_identity_provider_configuration_stub) | **GET** /v1/configuration/saml/identity-provider/stub | Get Saml Identity Provider configuration stub
[**configuration_service_get_secret_search_indexer_configuration**](ConfigurationApi.md#configuration_service_get_secret_search_indexer_configuration) | **GET** /v1/configuration/secret-search-indexer | Secret Search Indexer Configuration
[**configuration_service_get_security_configuration**](ConfigurationApi.md#configuration_service_get_security_configuration) | **GET** /v1/configuration/security | Get Security configuration
[**configuration_service_get_session_recording_advanced_configuration**](ConfigurationApi.md#configuration_service_get_session_recording_advanced_configuration) | **GET** /v1/configuration/sessionrecording-advanced | Get Session Recording Advanced
[**configuration_service_get_site_connectors**](ConfigurationApi.md#configuration_service_get_site_connectors) | **GET** /v1/configuration/site-connector | Site Connectors
[**configuration_service_get_system_log_configuration**](ConfigurationApi.md#configuration_service_get_system_log_configuration) | **GET** /v1/configuration/system-log | Get system log configuration
[**configuration_service_get_ticket_system_configuration**](ConfigurationApi.md#configuration_service_get_ticket_system_configuration) | **GET** /v1/configuration/ticket-system | Get the ticket system configuration
[**configuration_service_get_unlimited_admin**](ConfigurationApi.md#configuration_service_get_unlimited_admin) | **GET** /v1/configuration/unlimited-admin | Get Unlimited Admin
[**configuration_service_import_saml_configuration**](ConfigurationApi.md#configuration_service_import_saml_configuration) | **PUT** /v1/configuration/saml/identity-provider/import | Import Saml configuration Identity Provider
[**configuration_service_patch_application_settings_configuration**](ConfigurationApi.md#configuration_service_patch_application_settings_configuration) | **PATCH** /v1/configuration/application-settings | Update the application settings configuration
[**configuration_service_patch_automatic_export_configuration**](ConfigurationApi.md#configuration_service_patch_automatic_export_configuration) | **PATCH** /v1/configuration/auto-export | Patch Automatic Export Configuration
[**configuration_service_patch_configuration_read_only_mode**](ConfigurationApi.md#configuration_service_patch_configuration_read_only_mode) | **PATCH** /v1/configuration/read-only-mode | Patch Read Only Mode Configuration
[**configuration_service_patch_database_backup_configuration**](ConfigurationApi.md#configuration_service_patch_database_backup_configuration) | **PATCH** /v1/configuration/backup | Patch Backup Configuration
[**configuration_service_patch_database_configuration**](ConfigurationApi.md#configuration_service_patch_database_configuration) | **PATCH** /v1/configuration/database | Update the database configuration
[**configuration_service_patch_email_configuration**](ConfigurationApi.md#configuration_service_patch_email_configuration) | **PATCH** /v1/configuration/email | Update the email configuration
[**configuration_service_patch_folder_configuration**](ConfigurationApi.md#configuration_service_patch_folder_configuration) | **PATCH** /v1/configuration/folder | Folder
[**configuration_service_patch_general_configuration**](ConfigurationApi.md#configuration_service_patch_general_configuration) | **PATCH** /v1/configuration/general | Update general configuration
[**configuration_service_patch_internal_site_configuration**](ConfigurationApi.md#configuration_service_patch_internal_site_configuration) | **PATCH** /v1/configuration/internal-site-connector | Update Internal Site Connector
[**configuration_service_patch_launcher_settings_configuration**](ConfigurationApi.md#configuration_service_patch_launcher_settings_configuration) | **PATCH** /v1/configuration/launcher-settings | Update the launcher settings configuration
[**configuration_service_patch_local_password_configuration**](ConfigurationApi.md#configuration_service_patch_local_password_configuration) | **PATCH** /v1/configuration/local-user-passwords | Update the local user password configuration
[**configuration_service_patch_login_configuration_v2**](ConfigurationApi.md#configuration_service_patch_login_configuration_v2) | **PATCH** /v2/configuration/login | Update Login configuration
[**configuration_service_patch_login_policy_configuration**](ConfigurationApi.md#configuration_service_patch_login_policy_configuration) | **PATCH** /v1/configuration/login-policy | Update Login Policy configuration
[**configuration_service_patch_permission_options_configuration**](ConfigurationApi.md#configuration_service_patch_permission_options_configuration) | **PATCH** /v1/configuration/permission-options | Update the permission options configuration
[**configuration_service_patch_platform_configuration**](ConfigurationApi.md#configuration_service_patch_platform_configuration) | **PATCH** /v1/configuration/platform | Patch Platform Configuration
[**configuration_service_patch_protocol_handler_settings_configuration**](ConfigurationApi.md#configuration_service_patch_protocol_handler_settings_configuration) | **PATCH** /v1/configuration/protocol-handler-settings | Update the protocol handler settings configuration
[**configuration_service_patch_rpc_configuration**](ConfigurationApi.md#configuration_service_patch_rpc_configuration) | **PATCH** /v1/configuration/rpc | Update RPC configuration
[**configuration_service_patch_saml_configuration**](ConfigurationApi.md#configuration_service_patch_saml_configuration) | **PATCH** /v1/configuration/saml | Update Saml configuration
[**configuration_service_patch_saml_identity_provider_configuration**](ConfigurationApi.md#configuration_service_patch_saml_identity_provider_configuration) | **PATCH** /v1/configuration/saml/identity-provider | Update Saml Identity Provider configuration
[**configuration_service_patch_secret_search_indexer_configuration**](ConfigurationApi.md#configuration_service_patch_secret_search_indexer_configuration) | **PATCH** /v1/configuration/secret-search-indexer | Update Secret Search Indexer Configuration
[**configuration_service_patch_security_configuration**](ConfigurationApi.md#configuration_service_patch_security_configuration) | **PATCH** /v1/configuration/security | Update Security configuration
[**configuration_service_patch_session_recording_advanced_configuration**](ConfigurationApi.md#configuration_service_patch_session_recording_advanced_configuration) | **PATCH** /v1/configuration/sessionrecording-advanced | Update Session Recording Advanced
[**configuration_service_patch_session_recording_configuration**](ConfigurationApi.md#configuration_service_patch_session_recording_configuration) | **PATCH** /v1/configuration/sessionrecording | Session Recording
[**configuration_service_patch_system_log_configuration**](ConfigurationApi.md#configuration_service_patch_system_log_configuration) | **PATCH** /v1/configuration/system-log | Patch system log configuration
[**configuration_service_patch_ticket_system_configuration**](ConfigurationApi.md#configuration_service_patch_ticket_system_configuration) | **PATCH** /v1/configuration/ticket-system | Update the ticket system configuration
[**configuration_service_patch_user_experience_configuration**](ConfigurationApi.md#configuration_service_patch_user_experience_configuration) | **PATCH** /v1/configuration/user-experience | Update the user experience configuration
[**configuration_service_patch_user_interface_configuration**](ConfigurationApi.md#configuration_service_patch_user_interface_configuration) | **PATCH** /v1/configuration/user-interface | Update the user interface configuration
[**configuration_service_post_saml_configuration**](ConfigurationApi.md#configuration_service_post_saml_configuration) | **POST** /v1/configuration/saml/identity-provider | Create Saml configuration
[**configuration_service_rebuild_secret_search_indexer_configuration**](ConfigurationApi.md#configuration_service_rebuild_secret_search_indexer_configuration) | **POST** /v1/configuration/secret-search-indexer/rebuild-index | Rebuild Secret Search Index
[**configuration_service_rotate_secret_keys**](ConfigurationApi.md#configuration_service_rotate_secret_keys) | **POST** /v1/configuration/security/rotate-secret-keys | Rotate Secret Keys
[**configuration_service_run_auto_export_now**](ConfigurationApi.md#configuration_service_run_auto_export_now) | **POST** /v1/configuration/auto-export/run-now | Start Automatic Export
[**configuration_service_run_backup_now**](ConfigurationApi.md#configuration_service_run_backup_now) | **POST** /v1/configuration/backup/run-now | Start Backup
[**configuration_service_run_heartbeat_now**](ConfigurationApi.md#configuration_service_run_heartbeat_now) | **POST** /v1/configuration/heartbeat/run-now | Run Heartbeat Now
[**configuration_service_run_rpc_now**](ConfigurationApi.md#configuration_service_run_rpc_now) | **POST** /v1/configuration/rpc/run-now | Run RPC Now
[**configuration_service_test_email**](ConfigurationApi.md#configuration_service_test_email) | **POST** /v1/configuration/email/test | TestEmail
[**configuration_service_test_radius_login**](ConfigurationApi.md#configuration_service_test_radius_login) | **POST** /v1/configuration/login/radius/test | Test Radius Login
[**configuration_service_update_unlimited_admin**](ConfigurationApi.md#configuration_service_update_unlimited_admin) | **PATCH** /v1/configuration/unlimited-admin | Update Unlimited Admin


# **configuration_service_cancel_rotate_secret_keys**
> RotateSecretKeysStatusModel configuration_service_cancel_rotate_secret_keys()

Cancel Rotate Secret Keys

Cancel Rotate Secret Keys

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.rotate_secret_keys_status_model import RotateSecretKeysStatusModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Cancel Rotate Secret Keys
        api_response = api_instance.configuration_service_cancel_rotate_secret_keys()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_cancel_rotate_secret_keys: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**RotateSecretKeysStatusModel**](RotateSecretKeysStatusModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of running Cancel Rotate Secret Keys |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_clear_ad_credentials**
> ClearCachedADCredentialsResultModel configuration_service_clear_ad_credentials()

Clear AD Credentials

Clear AD Credentials

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.clear_cached_ad_credentials_result_model import ClearCachedADCredentialsResultModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Clear AD Credentials
        api_response = api_instance.configuration_service_clear_ad_credentials()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_clear_ad_credentials: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ClearCachedADCredentialsResultModel**](ClearCachedADCredentialsResultModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Clear AD Credentials Result |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_clear_system_log**
> bool configuration_service_clear_system_log()

Clear system log

Clear system log

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Clear system log
        api_response = api_instance.configuration_service_clear_system_log()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_clear_system_log: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cleared System Log Result |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_delete_saml_configuration_identity_provider**
> ConfigurationSamlIdentityProviderDeleteResultModel configuration_service_delete_saml_configuration_identity_provider(id)

Delete Saml Configuration Identity Provider

Delete Saml Configuration Identity Provider

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.configuration_saml_identity_provider_delete_result_model import ConfigurationSamlIdentityProviderDeleteResultModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    id = 1 # int | id

    # example passing only required values which don't have defaults set
    try:
        # Delete Saml Configuration Identity Provider
        api_response = api_instance.configuration_service_delete_saml_configuration_identity_provider(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_delete_saml_configuration_identity_provider: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id |

### Return type

[**ConfigurationSamlIdentityProviderDeleteResultModel**](ConfigurationSamlIdentityProviderDeleteResultModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_get_auto_export_configuration**
> AutoExportConfigurationModel configuration_service_get_auto_export_configuration()

Get Automatic Export Configuration

Retrieve the settings and descriptions for the automatic export configuration view model.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.auto_export_configuration_model import AutoExportConfigurationModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Automatic Export Configuration
        api_response = api_instance.configuration_service_get_auto_export_configuration()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_get_auto_export_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AutoExportConfigurationModel**](AutoExportConfigurationModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Automatic Export Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_get_auto_export_configuration_audits**
> PagingOfAutoExportConfigurationAuditViewModel configuration_service_get_auto_export_configuration_audits()

Get Automatic Export Configuration Audits

Retrieve the audits for the automatic export configuration.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.paging_of_auto_export_configuration_audit_view_model import PagingOfAutoExportConfigurationAuditViewModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    is_exporting = True # bool | isExporting (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Automatic Export Configuration Audits
        api_response = api_instance.configuration_service_get_auto_export_configuration_audits(is_exporting=is_exporting, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_get_auto_export_configuration_audits: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_exporting** | **bool**| isExporting | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfAutoExportConfigurationAuditViewModel**](PagingOfAutoExportConfigurationAuditViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Automatic Export Configuration Audits |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_get_auto_export_logs**
> PagingOfAutoExportLogViewModel configuration_service_get_auto_export_logs()

Get Automatic Export Logs

Retrieve the logs for the automatic exports.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.paging_of_auto_export_log_view_model import PagingOfAutoExportLogViewModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Automatic Export Logs
        api_response = api_instance.configuration_service_get_auto_export_logs(skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_get_auto_export_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfAutoExportLogViewModel**](PagingOfAutoExportLogViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Automatic Export Logs |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_get_auto_export_storage_item**
> StreamContent configuration_service_get_auto_export_storage_item(id)

Get Automatic Export Storage Item

Retrieves the automatic export storage item's contents.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.stream_content import StreamContent
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    id = 1 # int | id

    # example passing only required values which don't have defaults set
    try:
        # Get Automatic Export Storage Item
        api_response = api_instance.configuration_service_get_auto_export_storage_item(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_get_auto_export_storage_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id |

### Return type

[**StreamContent**](StreamContent.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Automatic Export Storage Item |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_get_auto_export_storage_items**
> PagingOfAutoExportStorageItemViewModel configuration_service_get_auto_export_storage_items(id)

Get Automatic Export Storage Items For Configuration

Retrieves a list of the items in automatic export storage for a configuration.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.paging_of_auto_export_storage_item_view_model import PagingOfAutoExportStorageItemViewModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    id = 1 # int | id
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Automatic Export Storage Items For Configuration
        api_response = api_instance.configuration_service_get_auto_export_storage_items(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_get_auto_export_storage_items: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Automatic Export Storage Items For Configuration
        api_response = api_instance.configuration_service_get_auto_export_storage_items(id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_get_auto_export_storage_items: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id |
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfAutoExportStorageItemViewModel**](PagingOfAutoExportStorageItemViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Automatic Export Storage Items For Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_get_auto_export_storage_items_default**
> PagingOfAutoExportStorageItemViewModel configuration_service_get_auto_export_storage_items_default()

Get Automatic Export Storage Items

Retrieves a list of the items in automatic export storage.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.paging_of_auto_export_storage_item_view_model import PagingOfAutoExportStorageItemViewModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Automatic Export Storage Items
        api_response = api_instance.configuration_service_get_auto_export_storage_items_default(skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_get_auto_export_storage_items_default: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfAutoExportStorageItemViewModel**](PagingOfAutoExportStorageItemViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Automatic Export Storage Items |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_get_backup_logs_v2**
> IPagingOfBackupLogViewModel configuration_service_get_backup_logs_v2()

Get Backup Logs

Retrieve the logs for the backups run.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.i_paging_of_backup_log_view_model import IPagingOfBackupLogViewModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Backup Logs
        api_response = api_instance.configuration_service_get_backup_logs_v2(skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_get_backup_logs_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**IPagingOfBackupLogViewModel**](IPagingOfBackupLogViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Backup Logs |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_get_configuration_audit**
> PagingOfConfigurationAuditItem configuration_service_get_configuration_audit()

Audit of system configuration changes

Audit of system configuration changes

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.paging_of_configuration_audit_item import PagingOfConfigurationAuditItem
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    is_exporting = True # bool | isExporting (optional)
    filter_search_term = "filter.searchTerm_example" # str | SearchTerm (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Audit of system configuration changes
        api_response = api_instance.configuration_service_get_configuration_audit(is_exporting=is_exporting, filter_search_term=filter_search_term, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_get_configuration_audit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_exporting** | **bool**| isExporting | [optional]
 **filter_search_term** | **str**| SearchTerm | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfConfigurationAuditItem**](PagingOfConfigurationAuditItem.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Configuration audit items |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_get_configuration_read_only_mode**
> ConfigurationReadOnlyModeModel configuration_service_get_configuration_read_only_mode()

Get Read Only Mode Configuration

Get Read Only Mode Configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.configuration_read_only_mode_model import ConfigurationReadOnlyModeModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Read Only Mode Configuration
        api_response = api_instance.configuration_service_get_configuration_read_only_mode()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_get_configuration_read_only_mode: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigurationReadOnlyModeModel**](ConfigurationReadOnlyModeModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Read Only Mode Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_get_configuration_state**
> ConfigurationStateModel configuration_service_get_configuration_state()

The allowed permissions for configuration for the current user

The allowed permissions for configuration for the current user

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.configuration_state_model import ConfigurationStateModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # The allowed permissions for configuration for the current user
        api_response = api_instance.configuration_service_get_configuration_state()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_get_configuration_state: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigurationStateModel**](ConfigurationStateModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The allowed configuration for the current user |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_get_database_backup_configuration**
> BackupConfigurationModel configuration_service_get_database_backup_configuration()

Get Backup Configuration

Retrieve the settings and descriptions for the backup configuration view model.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.backup_configuration_model import BackupConfigurationModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Backup Configuration
        api_response = api_instance.configuration_service_get_database_backup_configuration()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_get_database_backup_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**BackupConfigurationModel**](BackupConfigurationModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Backup Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_get_database_configuration**
> ConfigurationDatabaseModel configuration_service_get_database_configuration()

Get the database configuration

Get the database configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.configuration_database_model import ConfigurationDatabaseModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the database configuration
        api_response = api_instance.configuration_service_get_database_configuration()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_get_database_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigurationDatabaseModel**](ConfigurationDatabaseModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Database Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_get_general_configuration_v2**
> ConfigurationGeneralV2Model configuration_service_get_general_configuration_v2()

Get the general configuration

Get configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.configuration_general_v2_model import ConfigurationGeneralV2Model
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    load_all = True # bool | Load all configuration sections (optional)
    load_application_settings = True # bool | Load application settings section (optional)
    load_email = True # bool | Load email section (optional)
    load_folders = True # bool | Load folder configuration section (optional)
    load_launcher_settings = True # bool | Load launcher settings section (optional)
    load_local_user_passwords = True # bool | Load local user passwords section (optional)
    load_login = True # bool | Load log in section (optional)
    load_permission_options = True # bool | Load permission options configuration section (optional)
    load_protocol_handler_settings = True # bool | Load security protocol hander section (optional)
    load_security = True # bool | Load security section (optional)
    load_session_recording = True # bool | Load the session recording section (optional)
    load_unlimited_admin = True # bool | Load unlimited admin section (optional)
    load_user_experience = True # bool | Load user experience configuration section (optional)
    load_user_interface = True # bool | Load user interface section (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the general configuration
        api_response = api_instance.configuration_service_get_general_configuration_v2(load_all=load_all, load_application_settings=load_application_settings, load_email=load_email, load_folders=load_folders, load_launcher_settings=load_launcher_settings, load_local_user_passwords=load_local_user_passwords, load_login=load_login, load_permission_options=load_permission_options, load_protocol_handler_settings=load_protocol_handler_settings, load_security=load_security, load_session_recording=load_session_recording, load_unlimited_admin=load_unlimited_admin, load_user_experience=load_user_experience, load_user_interface=load_user_interface)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_get_general_configuration_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **load_all** | **bool**| Load all configuration sections | [optional]
 **load_application_settings** | **bool**| Load application settings section | [optional]
 **load_email** | **bool**| Load email section | [optional]
 **load_folders** | **bool**| Load folder configuration section | [optional]
 **load_launcher_settings** | **bool**| Load launcher settings section | [optional]
 **load_local_user_passwords** | **bool**| Load local user passwords section | [optional]
 **load_login** | **bool**| Load log in section | [optional]
 **load_permission_options** | **bool**| Load permission options configuration section | [optional]
 **load_protocol_handler_settings** | **bool**| Load security protocol hander section | [optional]
 **load_security** | **bool**| Load security section | [optional]
 **load_session_recording** | **bool**| Load the session recording section | [optional]
 **load_unlimited_admin** | **bool**| Load unlimited admin section | [optional]
 **load_user_experience** | **bool**| Load user experience configuration section | [optional]
 **load_user_interface** | **bool**| Load user interface section | [optional]

### Return type

[**ConfigurationGeneralV2Model**](ConfigurationGeneralV2Model.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_get_internal_site_configuration**
> ConfigurationInternalSiteConnectorModel configuration_service_get_internal_site_configuration()

Internal Site Connector Configuration

Internal Site Connector Configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.configuration_internal_site_connector_model import ConfigurationInternalSiteConnectorModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Internal Site Connector Configuration
        api_response = api_instance.configuration_service_get_internal_site_configuration()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_get_internal_site_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigurationInternalSiteConnectorModel**](ConfigurationInternalSiteConnectorModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Internal Site Connector Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_get_local_password_configuration**
> ConfigurationLocalUserPasswordsModel configuration_service_get_local_password_configuration()

Get the local user password configuration

Get the local user password configuration.  Password requirements only require an authenticated user.  Extended fields will be null unless you have the View / Administer Configuration role permission.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.configuration_local_user_passwords_model import ConfigurationLocalUserPasswordsModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the local user password configuration
        api_response = api_instance.configuration_service_get_local_password_configuration()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_get_local_password_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigurationLocalUserPasswordsModel**](ConfigurationLocalUserPasswordsModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Local User Password Configuration Settings |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_get_login_configuration_v2**
> ConfigurationLoginV2Model configuration_service_get_login_configuration_v2()

Get Login configuration

Get Login Configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.configuration_login_v2_model import ConfigurationLoginV2Model
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Login configuration
        api_response = api_instance.configuration_service_get_login_configuration_v2()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_get_login_configuration_v2: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigurationLoginV2Model**](ConfigurationLoginV2Model.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Login Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_get_login_policy_configuration**
> ConfigurationLoginPolicyModel configuration_service_get_login_policy_configuration()

Get Login Policy configuration

Get Login Policy Configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.configuration_login_policy_model import ConfigurationLoginPolicyModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Login Policy configuration
        api_response = api_instance.configuration_service_get_login_policy_configuration()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_get_login_policy_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigurationLoginPolicyModel**](ConfigurationLoginPolicyModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Login Policy Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_get_platform_configuration**
> PlatformConfigurationModel configuration_service_get_platform_configuration()

Get Platform Configuration

Retrieve the settings and descriptions for the Platform configuration view model.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.platform_configuration_model import PlatformConfigurationModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Platform Configuration
        api_response = api_instance.configuration_service_get_platform_configuration()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_get_platform_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**PlatformConfigurationModel**](PlatformConfigurationModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Platform Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_get_platform_configuration_audits**
> PagingOfPlatformConfigurationAuditViewModel configuration_service_get_platform_configuration_audits()

Get Platform Configuration Audits

Retrieve the audits for the Platform configuration.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.paging_of_platform_configuration_audit_view_model import PagingOfPlatformConfigurationAuditViewModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    is_exporting = True # bool | isExporting (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Platform Configuration Audits
        api_response = api_instance.configuration_service_get_platform_configuration_audits(is_exporting=is_exporting, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_get_platform_configuration_audits: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_exporting** | **bool**| isExporting | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfPlatformConfigurationAuditViewModel**](PagingOfPlatformConfigurationAuditViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Platform Configuration Audits |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_get_public_ssh_key_expiration**
> PublicSshKeyConfigurationViewModel configuration_service_get_public_ssh_key_expiration()

Public SSH Key Expiration

Public SSH Key Expiration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.public_ssh_key_configuration_view_model import PublicSshKeyConfigurationViewModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Public SSH Key Expiration
        api_response = api_instance.configuration_service_get_public_ssh_key_expiration()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_get_public_ssh_key_expiration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**PublicSshKeyConfigurationViewModel**](PublicSshKeyConfigurationViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Public SSH Key Expiration Result |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_get_rotate_secret_keys_status**
> RotateSecretKeysStatusModel configuration_service_get_rotate_secret_keys_status()

Get Rotate Secret Keys Status

Get Rotate Secret Keys Status

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.rotate_secret_keys_status_model import RotateSecretKeysStatusModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Rotate Secret Keys Status
        api_response = api_instance.configuration_service_get_rotate_secret_keys_status()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_get_rotate_secret_keys_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**RotateSecretKeysStatusModel**](RotateSecretKeysStatusModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status of Rotate Secret Keys |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_get_rpc_configuration**
> ConfigurationRpcModel configuration_service_get_rpc_configuration()

Get RPC configuration

Get Remote Password Configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.configuration_rpc_model import ConfigurationRpcModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get RPC configuration
        api_response = api_instance.configuration_service_get_rpc_configuration()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_get_rpc_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigurationRpcModel**](ConfigurationRpcModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RPC Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_get_saml_configuration**
> ConfigurationSamlModel configuration_service_get_saml_configuration()

Get Saml configuration

Get Saml Configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.configuration_saml_model import ConfigurationSamlModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Saml configuration
        api_response = api_instance.configuration_service_get_saml_configuration()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_get_saml_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigurationSamlModel**](ConfigurationSamlModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Saml Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_get_saml_identity_provider_configuration**
> ConfigurationSamlIdentityProviderModel configuration_service_get_saml_identity_provider_configuration(id)

Get Saml Identity Provider configuration

Get Saml Identity Provider Configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.configuration_saml_identity_provider_model import ConfigurationSamlIdentityProviderModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    id = 1 # int | Saml Identity Provider Id

    # example passing only required values which don't have defaults set
    try:
        # Get Saml Identity Provider configuration
        api_response = api_instance.configuration_service_get_saml_identity_provider_configuration(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_get_saml_identity_provider_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Saml Identity Provider Id |

### Return type

[**ConfigurationSamlIdentityProviderModel**](ConfigurationSamlIdentityProviderModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Saml Identity Provider configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_get_saml_identity_provider_configuration_stub**
> ConfigurationSamlIdentityProviderModel configuration_service_get_saml_identity_provider_configuration_stub()

Get Saml Identity Provider configuration stub

Get Saml Identity Provider Configuration stub

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.configuration_saml_identity_provider_model import ConfigurationSamlIdentityProviderModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Saml Identity Provider configuration stub
        api_response = api_instance.configuration_service_get_saml_identity_provider_configuration_stub()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_get_saml_identity_provider_configuration_stub: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigurationSamlIdentityProviderModel**](ConfigurationSamlIdentityProviderModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Saml Identity Provider configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_get_secret_search_indexer_configuration**
> SearchIndexerModel configuration_service_get_secret_search_indexer_configuration()

Secret Search Indexer Configuration

Secret Search Indexer Configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.search_indexer_model import SearchIndexerModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Secret Search Indexer Configuration
        api_response = api_instance.configuration_service_get_secret_search_indexer_configuration()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_get_secret_search_indexer_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SearchIndexerModel**](SearchIndexerModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Search Indexer Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_get_security_configuration**
> ConfigurationSecurityModel configuration_service_get_security_configuration()

Get Security configuration

Get Security Configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.configuration_security_model import ConfigurationSecurityModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Security configuration
        api_response = api_instance.configuration_service_get_security_configuration()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_get_security_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigurationSecurityModel**](ConfigurationSecurityModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Security Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_get_session_recording_advanced_configuration**
> ConfigurationSessionRecordingAdvancedModel configuration_service_get_session_recording_advanced_configuration()

Get Session Recording Advanced

Get Session Recording Advanced Configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.configuration_session_recording_advanced_model import ConfigurationSessionRecordingAdvancedModel
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Session Recording Advanced
        api_response = api_instance.configuration_service_get_session_recording_advanced_configuration()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_get_session_recording_advanced_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigurationSessionRecordingAdvancedModel**](ConfigurationSessionRecordingAdvancedModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Session Recording Advanced Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_get_site_connectors**
> [SiteConnectorsSummaryModel] configuration_service_get_site_connectors()

Site Connectors

Site Connectors

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.site_connectors_summary_model import SiteConnectorsSummaryModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    include_inactive = True # bool | includeInactive (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Site Connectors
        api_response = api_instance.configuration_service_get_site_connectors(include_inactive=include_inactive)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_get_site_connectors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_inactive** | **bool**| includeInactive | [optional]

### Return type

[**[SiteConnectorsSummaryModel]**](SiteConnectorsSummaryModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Site Connectors |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_get_system_log_configuration**
> SystemLogConfigurationViewModel configuration_service_get_system_log_configuration()

Get system log configuration

Get system log configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.system_log_configuration_view_model import SystemLogConfigurationViewModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get system log configuration
        api_response = api_instance.configuration_service_get_system_log_configuration()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_get_system_log_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemLogConfigurationViewModel**](SystemLogConfigurationViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | System log configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_get_ticket_system_configuration**
> ConfigurationTicketSystemViewModel configuration_service_get_ticket_system_configuration()

Get the ticket system configuration

Get the ticket system configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.configuration_ticket_system_view_model import ConfigurationTicketSystemViewModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the ticket system configuration
        api_response = api_instance.configuration_service_get_ticket_system_configuration()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_get_ticket_system_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigurationTicketSystemViewModel**](ConfigurationTicketSystemViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ticket System Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_get_unlimited_admin**
> UnlimitedAdminModel configuration_service_get_unlimited_admin()

Get Unlimited Admin

Get Unlimited Admin

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.unlimited_admin_model import UnlimitedAdminModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Unlimited Admin
        api_response = api_instance.configuration_service_get_unlimited_admin()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_get_unlimited_admin: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**UnlimitedAdminModel**](UnlimitedAdminModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The value of unlimited admin |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_import_saml_configuration**
> [ConfigurationSamlIdentityProviderModel] configuration_service_import_saml_configuration()

Import Saml configuration Identity Provider

Import Saml configuration Identity Provider

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.configuration_saml_identity_provider_model import ConfigurationSamlIdentityProviderModel
from secret_server_openapiclient.model.configuration_saml_identity_provider_import_args import ConfigurationSamlIdentityProviderImportArgs
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    configuration_saml_identity_provider_import_args = ConfigurationSamlIdentityProviderImportArgs(
null,
        import_file_data=open('/path/to/file', 'rb'),
    ) # ConfigurationSamlIdentityProviderImportArgs | Saml Identity Provider import args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Import Saml configuration Identity Provider
        api_response = api_instance.configuration_service_import_saml_configuration(configuration_saml_identity_provider_import_args=configuration_saml_identity_provider_import_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_import_saml_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_saml_identity_provider_import_args** | [**ConfigurationSamlIdentityProviderImportArgs**](ConfigurationSamlIdentityProviderImportArgs.md)| Saml Identity Provider import args | [optional]

### Return type

[**[ConfigurationSamlIdentityProviderModel]**](ConfigurationSamlIdentityProviderModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Saml configuration Identity Provider after import |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_patch_application_settings_configuration**
> ConfigurationApplicationSettingsModel configuration_service_patch_application_settings_configuration()

Update the application settings configuration

Update the application settings configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.configuration_application_settings_patch_args import ConfigurationApplicationSettingsPatchArgs
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.configuration_application_settings_model import ConfigurationApplicationSettingsModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    configuration_application_settings_patch_args = ConfigurationApplicationSettingsPatchArgs(
        data=ConfigurationApplicationSettingsPatchModel(
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
                value=1,
            ),
            api_session_timeout_hours=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            api_session_timeout_minutes=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
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
                value="value_example",
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
                value=1,
            ),
            max_secret_log_length=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            mobile_max_offline_days=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            mobile_max_offline_hours=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            obfuscate_personally_identifiable_information=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            pii_obfuscation_level=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
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
                value=1,
            ),
            syslog_cef_port=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            syslog_cef_protocol=UpdateFieldValueOfSyslogCefProtocolType(
                dirty=True,
                value=SyslogCefProtocolType("UDP"),
            ),
            syslog_cef_server=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            syslog_cef_time_zone=UpdateFieldValueOfSyslogCefTimeZoneType(
                dirty=True,
                value=SyslogCefTimeZoneType("ServerTime"),
            ),
            tms_installation_path=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            win_rm_endpoint_url=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            write_syslog_to_event_log=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
        ),
    ) # ConfigurationApplicationSettingsPatchArgs | Application settings update args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the application settings configuration
        api_response = api_instance.configuration_service_patch_application_settings_configuration(configuration_application_settings_patch_args=configuration_application_settings_patch_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_patch_application_settings_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_application_settings_patch_args** | [**ConfigurationApplicationSettingsPatchArgs**](ConfigurationApplicationSettingsPatchArgs.md)| Application settings update args | [optional]

### Return type

[**ConfigurationApplicationSettingsModel**](ConfigurationApplicationSettingsModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Application Settings Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_patch_automatic_export_configuration**
> AutoExportConfigurationModel configuration_service_patch_automatic_export_configuration()

Patch Automatic Export Configuration

Patch Automatic Export Configuration by sending one or more fields with dirty set to true.  This will return the actual updated view model.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.auto_export_configuration_model import AutoExportConfigurationModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.auto_export_configuration_args import AutoExportConfigurationArgs
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    auto_export_configuration_args = AutoExportConfigurationArgs(
        data=AutoExportConfigurationUpdateModel(
            enable_auto_export=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            export_child_folders=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            export_folder_paths=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            export_password_secret_id=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=1,
            ),
            export_path=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            export_totp_settings=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            folder_id=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=1,
            ),
            frequency_days=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
        ),
    ) # AutoExportConfigurationArgs | Automatic Export Update Settings (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Patch Automatic Export Configuration
        api_response = api_instance.configuration_service_patch_automatic_export_configuration(auto_export_configuration_args=auto_export_configuration_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_patch_automatic_export_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_export_configuration_args** | [**AutoExportConfigurationArgs**](AutoExportConfigurationArgs.md)| Automatic Export Update Settings | [optional]

### Return type

[**AutoExportConfigurationModel**](AutoExportConfigurationModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Automatic Export Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_patch_configuration_read_only_mode**
> ConfigurationReadOnlyModeModel configuration_service_patch_configuration_read_only_mode()

Patch Read Only Mode Configuration

Patch Read Only Mode Configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.configuration_read_only_mode_model import ConfigurationReadOnlyModeModel
from secret_server_openapiclient.model.configuration_read_only_mode_args import ConfigurationReadOnlyModeArgs
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    configuration_read_only_mode_args = ConfigurationReadOnlyModeArgs(
        data=ConfigurationReadOnlyModeUpdateModel(
            enabled=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
        ),
    ) # ConfigurationReadOnlyModeArgs | Configuration Read Only Mode Patch Settings (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Patch Read Only Mode Configuration
        api_response = api_instance.configuration_service_patch_configuration_read_only_mode(configuration_read_only_mode_args=configuration_read_only_mode_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_patch_configuration_read_only_mode: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_read_only_mode_args** | [**ConfigurationReadOnlyModeArgs**](ConfigurationReadOnlyModeArgs.md)| Configuration Read Only Mode Patch Settings | [optional]

### Return type

[**ConfigurationReadOnlyModeModel**](ConfigurationReadOnlyModeModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Read Only Mode Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_patch_database_backup_configuration**
> BackupConfigurationModel configuration_service_patch_database_backup_configuration()

Patch Backup Configuration

Patch Backup Configuration by sending one or more fields with dirty set to true.  This will return the actual updated view model.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.backup_configuration_model import BackupConfigurationModel
from secret_server_openapiclient.model.backup_configuration_args import BackupConfigurationArgs
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    backup_configuration_args = BackupConfigurationArgs(
        data=BackupConfigurationUpdateModel(
            backup_database_path=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            backup_failure_notification=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            backup_path=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            backup_start_date_time=UpdateFieldValueOfDateTime(
                dirty=True,
                value=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
            configuration_sql_backup_timeout_minutes=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            copy_only_database_backup=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            enable_database_backup=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            enable_scheduled_backup=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            enable_tms_backup=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            enable_web_application_backup=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            number_of_backups_to_keep=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            repeat_days=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            repeat_hours=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            repeat_minutes=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            tms_installation_path=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
        ),
    ) # BackupConfigurationArgs | Backup Configuration Update Settings (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Patch Backup Configuration
        api_response = api_instance.configuration_service_patch_database_backup_configuration(backup_configuration_args=backup_configuration_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_patch_database_backup_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup_configuration_args** | [**BackupConfigurationArgs**](BackupConfigurationArgs.md)| Backup Configuration Update Settings | [optional]

### Return type

[**BackupConfigurationModel**](BackupConfigurationModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Backup Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_patch_database_configuration**
> ConfigurationDatabaseModel configuration_service_patch_database_configuration()

Update the database configuration

Update the database configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.configuration_database_model import ConfigurationDatabaseModel
from secret_server_openapiclient.model.configuration_database_patch_args import ConfigurationDatabasePatchArgs
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    configuration_database_patch_args = ConfigurationDatabasePatchArgs(
        data=ConfigurationDatabasePatchModel(
            authentication_type=UpdateFieldValueOfSqlAuthenticationType(
                dirty=True,
                value=SqlAuthenticationType("{}"),
            ),
            connection_timeout=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=1,
            ),
            database_name=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            enable_multi_subnet_failover=UpdateFieldValueOfOptionalBoolean(
                dirty=True,
                value=True,
            ),
            enable_ssl_encryption=UpdateFieldValueOfOptionalBoolean(
                dirty=True,
                value=True,
            ),
            failover_partner=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            file_override_password=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            file_override_user_name=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            password=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            server_name=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            trust_server_certificate=UpdateFieldValueOfOptionalBoolean(
                dirty=True,
                value=True,
            ),
            user_name=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
        ),
    ) # ConfigurationDatabasePatchArgs | Database configuration update args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the database configuration
        api_response = api_instance.configuration_service_patch_database_configuration(configuration_database_patch_args=configuration_database_patch_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_patch_database_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_database_patch_args** | [**ConfigurationDatabasePatchArgs**](ConfigurationDatabasePatchArgs.md)| Database configuration update args | [optional]

### Return type

[**ConfigurationDatabaseModel**](ConfigurationDatabaseModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Database Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_patch_email_configuration**
> ConfigurationEmailModel configuration_service_patch_email_configuration()

Update the email configuration

Update the email configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.configuration_email_model import ConfigurationEmailModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.configuration_email_patch_args import ConfigurationEmailPatchArgs
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    configuration_email_patch_args = ConfigurationEmailPatchArgs(
        data=ConfigurationEmailPatchModel(
            from_email_address=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            from_email_name=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
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
                value="value_example",
            ),
            smtp_password=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            smtp_port=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=1,
            ),
            smtp_server=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
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
                value="value_example",
            ),
            smtp_use_ssl=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
        ),
    ) # ConfigurationEmailPatchArgs | Email update args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the email configuration
        api_response = api_instance.configuration_service_patch_email_configuration(configuration_email_patch_args=configuration_email_patch_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_patch_email_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_email_patch_args** | [**ConfigurationEmailPatchArgs**](ConfigurationEmailPatchArgs.md)| Email update args | [optional]

### Return type

[**ConfigurationEmailModel**](ConfigurationEmailModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Email Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_patch_folder_configuration**
> ConfigurationFoldersModel configuration_service_patch_folder_configuration()

Folder

Update Folder Configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.configuration_folders_model import ConfigurationFoldersModel
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.configuration_folders_patch_args import ConfigurationFoldersPatchArgs
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    configuration_folders_patch_args = ConfigurationFoldersPatchArgs(
        data=ConfigurationFoldersPatchModel(
            enable_personal_folders=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            personal_folder_name=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            personal_folder_name_option=UpdateFieldValueOfPersonalFolderNameOptionType(
                dirty=True,
                value=PersonalFolderNameOptionType("{}"),
            ),
            personal_folder_warning=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
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
    ) # ConfigurationFoldersPatchArgs | Folders configuration args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Folder
        api_response = api_instance.configuration_service_patch_folder_configuration(configuration_folders_patch_args=configuration_folders_patch_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_patch_folder_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_folders_patch_args** | [**ConfigurationFoldersPatchArgs**](ConfigurationFoldersPatchArgs.md)| Folders configuration args | [optional]

### Return type

[**ConfigurationFoldersModel**](ConfigurationFoldersModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folder Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_patch_general_configuration**
> ConfigurationGeneralModel configuration_service_patch_general_configuration()

Update general configuration

Update general configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.configuration_general_model import ConfigurationGeneralModel
from secret_server_openapiclient.model.configuration_general_patch_args import ConfigurationGeneralPatchArgs
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    configuration_general_patch_args = ConfigurationGeneralPatchArgs(
        data=ConfigurationGeneralUpdateModel(
            folders=ConfigurationFoldersUpdateModel(
                enable_personal_folders=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                personal_folder_name=UpdateFieldValueOfString(
                    dirty=True,
                    value="value_example",
                ),
                personal_folder_name_option=UpdateFieldValueOfPersonalFolderNameOptionType(
                    dirty=True,
                    value=PersonalFolderNameOptionType("{}"),
                ),
                personal_folder_warning=UpdateFieldValueOfString(
                    dirty=True,
                    value="value_example",
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
            permission_options=ConfigurationPermissionOptionsUpdateModel(
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
                    value="value_example",
                ),
            ),
            user_experience=ConfigurationUserExperienceUpdateModel(
                application_language=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=1,
                ),
                default_date_format=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=1,
                ),
                default_new_user_role_id=UpdateFieldValueOfOptionalInt32(
                    dirty=True,
                    value=1,
                ),
                default_time_format=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=1,
                ),
                force_inactivity_timeout=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                force_inactivity_timeout_minutes=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=1,
                ),
                require_folder_for_secret=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                secret_password_history_restriction_all=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                secret_password_history_restriction_count=UpdateFieldValueOfOptionalInt32(
                    dirty=True,
                    value=1,
                ),
                secret_view_interval_minutes=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=1,
                ),
                server_time_zone_id=UpdateFieldValueOfString(
                    dirty=True,
                    value="value_example",
                ),
                ui_inactivity_sleep_minutes=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=1,
                ),
            ),
        ),
    ) # ConfigurationGeneralPatchArgs | Local user password update args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update general configuration
        api_response = api_instance.configuration_service_patch_general_configuration(configuration_general_patch_args=configuration_general_patch_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_patch_general_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_general_patch_args** | [**ConfigurationGeneralPatchArgs**](ConfigurationGeneralPatchArgs.md)| Local user password update args | [optional]

### Return type

[**ConfigurationGeneralModel**](ConfigurationGeneralModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_patch_internal_site_configuration**
> ConfigurationInternalSiteConnectorModel configuration_service_patch_internal_site_configuration()

Update Internal Site Connector

Update Internal Site Connector

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.configuration_internal_site_connector_model import ConfigurationInternalSiteConnectorModel
from secret_server_openapiclient.model.configuration_internal_site_connector_patch_args import ConfigurationInternalSiteConnectorPatchArgs
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    configuration_internal_site_connector_patch_args = ConfigurationInternalSiteConnectorPatchArgs(
        data=ConfigurationInternalSiteConnectorPatchModel(
            site_connector_id=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=1,
            ),
        ),
    ) # ConfigurationInternalSiteConnectorPatchArgs | Internal Site Connector Update Options (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Internal Site Connector
        api_response = api_instance.configuration_service_patch_internal_site_configuration(configuration_internal_site_connector_patch_args=configuration_internal_site_connector_patch_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_patch_internal_site_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_internal_site_connector_patch_args** | [**ConfigurationInternalSiteConnectorPatchArgs**](ConfigurationInternalSiteConnectorPatchArgs.md)| Internal Site Connector Update Options | [optional]

### Return type

[**ConfigurationInternalSiteConnectorModel**](ConfigurationInternalSiteConnectorModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Internal Site Connector Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_patch_launcher_settings_configuration**
> ConfigurationLauncherSettingsModel configuration_service_patch_launcher_settings_configuration()

Update the launcher settings configuration

Update the launcher settings configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.configuration_launcher_settings_patch_args import ConfigurationLauncherSettingsPatchArgs
from secret_server_openapiclient.model.configuration_launcher_settings_model import ConfigurationLauncherSettingsModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    configuration_launcher_settings_patch_args = ConfigurationLauncherSettingsPatchArgs(
        data=ConfigurationLauncherSettingsPatchModel(
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
                value=LauncherDeploymentType("ClickOnce"),
            ),
            send_secret_url_to_launcher=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
        ),
    ) # ConfigurationLauncherSettingsPatchArgs | Launcher settings update args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the launcher settings configuration
        api_response = api_instance.configuration_service_patch_launcher_settings_configuration(configuration_launcher_settings_patch_args=configuration_launcher_settings_patch_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_patch_launcher_settings_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_launcher_settings_patch_args** | [**ConfigurationLauncherSettingsPatchArgs**](ConfigurationLauncherSettingsPatchArgs.md)| Launcher settings update args | [optional]

### Return type

[**ConfigurationLauncherSettingsModel**](ConfigurationLauncherSettingsModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | launcher settings Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_patch_local_password_configuration**
> ConfigurationLocalUserPasswordsModel configuration_service_patch_local_password_configuration()

Update the local user password configuration

Update the local user password configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.configuration_local_password_patch_args import ConfigurationLocalPasswordPatchArgs
from secret_server_openapiclient.model.configuration_local_user_passwords_model import ConfigurationLocalUserPasswordsModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    configuration_local_password_patch_args = ConfigurationLocalPasswordPatchArgs(
        data=ConfigurationLocalPasswordPatchModel(
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
                value=1,
            ),
            local_user_password_expiration_hours=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            local_user_password_expiration_minutes=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            minimum_password_age_days=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            minimum_password_age_hours=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            minimum_password_age_minutes=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            password_history_items=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            password_history_items_all=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            password_minimum_length=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=1,
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
    ) # ConfigurationLocalPasswordPatchArgs | Local user password update args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the local user password configuration
        api_response = api_instance.configuration_service_patch_local_password_configuration(configuration_local_password_patch_args=configuration_local_password_patch_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_patch_local_password_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_local_password_patch_args** | [**ConfigurationLocalPasswordPatchArgs**](ConfigurationLocalPasswordPatchArgs.md)| Local user password update args | [optional]

### Return type

[**ConfigurationLocalUserPasswordsModel**](ConfigurationLocalUserPasswordsModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Local User Password Configuration Settings |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_patch_login_configuration_v2**
> ConfigurationLoginV2Model configuration_service_patch_login_configuration_v2()

Update Login configuration

Update Login Configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.configuration_login_v2_patch_args import ConfigurationLoginV2PatchArgs
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.configuration_login_v2_model import ConfigurationLoginV2Model
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    configuration_login_v2_patch_args = ConfigurationLoginV2PatchArgs(
        data=ConfigurationLoginV2PatchModel(
            allow_remember_me=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            cache_ad_credentials=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            default_login_domain=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            enable_domain_selector=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            enable_login_failure_captcha=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            max_concurrent_logins_per_user=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            maximum_login_failures=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            max_login_failures_before_captcha=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            remember_me_time_out_minutes=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            ssh_key_integration=ConfigurationLoginSshKeyIntegrationPatchModel(
                authentication_method=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=1,
                ),
                enable=UpdateFieldValueOfBoolean(
                    dirty=True,
                    value=True,
                ),
                expiration_in_hours=UpdateFieldValueOfInt32(
                    dirty=True,
                    value=1,
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
                        value="value_example",
                    ),
                    enable=UpdateFieldValueOfBoolean(
                        dirty=True,
                        value=True,
                    ),
                    integration_key=UpdateFieldValueOfString(
                        dirty=True,
                        value="value_example",
                    ),
                    secret_key=UpdateFieldValueOfString(
                        dirty=True,
                        value="value_example",
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
                        value="value_example",
                    ),
                    client_secret=UpdateFieldValueOfString(
                        dirty=True,
                        value="value_example",
                    ),
                    enable=UpdateFieldValueOfBoolean(
                        dirty=True,
                        value=True,
                    ),
                    logout_url=UpdateFieldValueOfString(
                        dirty=True,
                        value="value_example",
                    ),
                    server_url=UpdateFieldValueOfString(
                        dirty=True,
                        value="value_example",
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
                        value="value_example",
                    ),
                    default_username=UpdateFieldValueOfString(
                        dirty=True,
                        value="value_example",
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
                        value="value_example",
                    ),
                    failover_server_port=UpdateFieldValueOfInt32(
                        dirty=True,
                        value=1,
                    ),
                    failover_shared_secret=UpdateFieldValueOfString(
                        dirty=True,
                        value="value_example",
                    ),
                    failover_timeout_seconds=UpdateFieldValueOfInt32(
                        dirty=True,
                        value=1,
                    ),
                    login_explanation=UpdateFieldValueOfString(
                        dirty=True,
                        value="value_example",
                    ),
                    nas_id=UpdateFieldValueOfString(
                        dirty=True,
                        value="value_example",
                    ),
                    protocol=UpdateFieldValueOfInt32(
                        dirty=True,
                        value=1,
                    ),
                    server_ip=UpdateFieldValueOfString(
                        dirty=True,
                        value="value_example",
                    ),
                    server_port=UpdateFieldValueOfInt32(
                        dirty=True,
                        value=1,
                    ),
                    shared_secret=UpdateFieldValueOfString(
                        dirty=True,
                        value="value_example",
                    ),
                    shared_secret_same_for_all_users=UpdateFieldValueOfBoolean(
                        dirty=True,
                        value=True,
                    ),
                    timeout_seconds=UpdateFieldValueOfInt32(
                        dirty=True,
                        value=1,
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
                    value=1,
                ),
            ),
            user_lockout_time_minutes=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=1,
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
    ) # ConfigurationLoginV2PatchArgs | Login update args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Login configuration
        api_response = api_instance.configuration_service_patch_login_configuration_v2(configuration_login_v2_patch_args=configuration_login_v2_patch_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_patch_login_configuration_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_login_v2_patch_args** | [**ConfigurationLoginV2PatchArgs**](ConfigurationLoginV2PatchArgs.md)| Login update args | [optional]

### Return type

[**ConfigurationLoginV2Model**](ConfigurationLoginV2Model.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Login configuration after updates |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_patch_login_policy_configuration**
> ConfigurationLoginPolicyModel configuration_service_patch_login_policy_configuration()

Update Login Policy configuration

Update Login Policy Configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.configuration_login_policy_patch_args import ConfigurationLoginPolicyPatchArgs
from secret_server_openapiclient.model.configuration_login_policy_model import ConfigurationLoginPolicyModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    configuration_login_policy_patch_args = ConfigurationLoginPolicyPatchArgs(
        data=ConfigurationLoginPolicyPatchModel(
            enable_login_policy=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            force_login_policy=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            login_policy=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
        ),
    ) # ConfigurationLoginPolicyPatchArgs | Login Policy update args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Login Policy configuration
        api_response = api_instance.configuration_service_patch_login_policy_configuration(configuration_login_policy_patch_args=configuration_login_policy_patch_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_patch_login_policy_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_login_policy_patch_args** | [**ConfigurationLoginPolicyPatchArgs**](ConfigurationLoginPolicyPatchArgs.md)| Login Policy update args | [optional]

### Return type

[**ConfigurationLoginPolicyModel**](ConfigurationLoginPolicyModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Login Policy configuration after updates |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_patch_permission_options_configuration**
> ConfigurationPermissionOptionsModel configuration_service_patch_permission_options_configuration()

Update the permission options configuration

Update the permission options configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.configuration_permission_options_patch_args import ConfigurationPermissionOptionsPatchArgs
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.configuration_permission_options_model import ConfigurationPermissionOptionsModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    configuration_permission_options_patch_args = ConfigurationPermissionOptionsPatchArgs(
        data=ConfigurationPermissionOptionsPatchModel(
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
                value="value_example",
            ),
        ),
    ) # ConfigurationPermissionOptionsPatchArgs | Permission options update args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the permission options configuration
        api_response = api_instance.configuration_service_patch_permission_options_configuration(configuration_permission_options_patch_args=configuration_permission_options_patch_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_patch_permission_options_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_permission_options_patch_args** | [**ConfigurationPermissionOptionsPatchArgs**](ConfigurationPermissionOptionsPatchArgs.md)| Permission options update args | [optional]

### Return type

[**ConfigurationPermissionOptionsModel**](ConfigurationPermissionOptionsModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Permission Options Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_patch_platform_configuration**
> PlatformConfigurationModel configuration_service_patch_platform_configuration()

Patch Platform Configuration

Patch Platform Configuration by sending one or more fields with dirty set to true.  This will return the actual updated view model.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.platform_configuration_args import PlatformConfigurationArgs
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.platform_configuration_model import PlatformConfigurationModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    platform_configuration_args = PlatformConfigurationArgs(
        data=PlatformConfigurationUpdateModel(
            create_groups_during_synchronization=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            enable_synchronization=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            open_id_connect_client_id=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            open_id_connect_client_secret=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            open_id_connect_enabled=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            open_id_connect_login_url=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            open_id_connect_logout_url=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            profile_name=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            synchronization_interval_days=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            synchronization_interval_hours=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
        ),
    ) # PlatformConfigurationArgs | Platform Update Settings (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Patch Platform Configuration
        api_response = api_instance.configuration_service_patch_platform_configuration(platform_configuration_args=platform_configuration_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_patch_platform_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_configuration_args** | [**PlatformConfigurationArgs**](PlatformConfigurationArgs.md)| Platform Update Settings | [optional]

### Return type

[**PlatformConfigurationModel**](PlatformConfigurationModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Platform Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_patch_protocol_handler_settings_configuration**
> ConfigurationProtocolHandlerSettingsModel configuration_service_patch_protocol_handler_settings_configuration()

Update the protocol handler settings configuration

Update the protocol handler settings configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.configuration_protocol_handler_settings_model import ConfigurationProtocolHandlerSettingsModel
from secret_server_openapiclient.model.configuration_protocol_handler_settings_patch_args import ConfigurationProtocolHandlerSettingsPatchArgs
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    configuration_protocol_handler_settings_patch_args = ConfigurationProtocolHandlerSettingsPatchArgs(
        data=ConfigurationProtocolHandlerSettingsPatchModel(
            protocol_handler_install_time_allowed_domains=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
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
    ) # ConfigurationProtocolHandlerSettingsPatchArgs | Protocol handler settings update args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the protocol handler settings configuration
        api_response = api_instance.configuration_service_patch_protocol_handler_settings_configuration(configuration_protocol_handler_settings_patch_args=configuration_protocol_handler_settings_patch_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_patch_protocol_handler_settings_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_protocol_handler_settings_patch_args** | [**ConfigurationProtocolHandlerSettingsPatchArgs**](ConfigurationProtocolHandlerSettingsPatchArgs.md)| Protocol handler settings update args | [optional]

### Return type

[**ConfigurationProtocolHandlerSettingsModel**](ConfigurationProtocolHandlerSettingsModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | protocol handler settings Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_patch_rpc_configuration**
> ConfigurationRpcModel configuration_service_patch_rpc_configuration()

Update RPC configuration

Update Remote Password Configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.configuration_rpc_model import ConfigurationRpcModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.configuration_rpc_patch_args import ConfigurationRpcPatchArgs
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    configuration_rpc_patch_args = ConfigurationRpcPatchArgs(
        data=ConfigurationRpcPatchModel(
            check_out_interval_days=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            check_out_interval_hours=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            check_out_interval_minutes=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            days_to_keep_logs=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            enable_heartbeat=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            enable_password_change_on_check_in=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            enable_rpc=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
        ),
    ) # ConfigurationRpcPatchArgs | Local user password update args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update RPC configuration
        api_response = api_instance.configuration_service_patch_rpc_configuration(configuration_rpc_patch_args=configuration_rpc_patch_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_patch_rpc_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_rpc_patch_args** | [**ConfigurationRpcPatchArgs**](ConfigurationRpcPatchArgs.md)| Local user password update args | [optional]

### Return type

[**ConfigurationRpcModel**](ConfigurationRpcModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RPC configuration after updates |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_patch_saml_configuration**
> ConfigurationSamlModel configuration_service_patch_saml_configuration()

Update Saml configuration

Update Saml Configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.configuration_saml_model import ConfigurationSamlModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.configuration_saml_patch_args import ConfigurationSamlPatchArgs
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    configuration_saml_patch_args = ConfigurationSamlPatchArgs(
        data=ConfigurationSamlPatchModel(
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
                        value="value_example",
                    ),
                    clock_skew=UpdateFieldValueOfInt32(
                        dirty=True,
                        value=1,
                    ),
                    description=UpdateFieldValueOfString(
                        dirty=True,
                        value="value_example",
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
                        value="value_example",
                    ),
                    domain_attribute=UpdateFieldValueOfString(
                        dirty=True,
                        value="value_example",
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
                    identity_provider_id=1,
                    logout_request_life_time=UpdateFieldValueOfInt32(
                        dirty=True,
                        value=1,
                    ),
                    name=UpdateFieldValueOfString(
                        dirty=True,
                        value="value_example",
                    ),
                    override_pending_authn_request=UpdateFieldValueOfBoolean(
                        dirty=True,
                        value=True,
                    ),
                    public_certificate=UpdateFieldValueOfString(
                        dirty=True,
                        value="value_example",
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
                        value="value_example",
                    ),
                    single_logout_service_url=UpdateFieldValueOfString(
                        dirty=True,
                        value="value_example",
                    ),
                    sso_service_binding=UpdateFieldValueOfInt32(
                        dirty=True,
                        value=1,
                    ),
                    sso_service_url=UpdateFieldValueOfString(
                        dirty=True,
                        value="value_example",
                    ),
                    username_attribute=UpdateFieldValueOfString(
                        dirty=True,
                        value="value_example",
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
                value="value_example",
            ),
            service_provider_certificate=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            service_provider_certificate_password=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            service_provider_name=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            use_legacy=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
        ),
    ) # ConfigurationSamlPatchArgs | Saml update args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Saml configuration
        api_response = api_instance.configuration_service_patch_saml_configuration(configuration_saml_patch_args=configuration_saml_patch_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_patch_saml_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_saml_patch_args** | [**ConfigurationSamlPatchArgs**](ConfigurationSamlPatchArgs.md)| Saml update args | [optional]

### Return type

[**ConfigurationSamlModel**](ConfigurationSamlModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Saml configuration after updates |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_patch_saml_identity_provider_configuration**
> ConfigurationSamlIdentityProviderModel configuration_service_patch_saml_identity_provider_configuration()

Update Saml Identity Provider configuration

Update Saml Identity Provider Configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.configuration_saml_identity_provider_model import ConfigurationSamlIdentityProviderModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.configuration_saml_identity_provider_patch_args import ConfigurationSamlIdentityProviderPatchArgs
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    configuration_saml_identity_provider_patch_args = ConfigurationSamlIdentityProviderPatchArgs(
        data=ConfigurationSamlIdentityProviderPatchModel(
            active=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            authn_context=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            clock_skew=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            description=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
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
                value="value_example",
            ),
            domain_attribute=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
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
            identity_provider_id=1,
            logout_request_life_time=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            name=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            override_pending_authn_request=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            public_certificate=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
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
                value="value_example",
            ),
            single_logout_service_url=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            sso_service_binding=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            sso_service_url=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            username_attribute=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
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
    ) # ConfigurationSamlIdentityProviderPatchArgs | Saml Identity Provider update args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Saml Identity Provider configuration
        api_response = api_instance.configuration_service_patch_saml_identity_provider_configuration(configuration_saml_identity_provider_patch_args=configuration_saml_identity_provider_patch_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_patch_saml_identity_provider_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_saml_identity_provider_patch_args** | [**ConfigurationSamlIdentityProviderPatchArgs**](ConfigurationSamlIdentityProviderPatchArgs.md)| Saml Identity Provider update args | [optional]

### Return type

[**ConfigurationSamlIdentityProviderModel**](ConfigurationSamlIdentityProviderModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Saml Identity Provider configuration after updates |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_patch_secret_search_indexer_configuration**
> SearchIndexerModel configuration_service_patch_secret_search_indexer_configuration()

Update Secret Search Indexer Configuration

Update Secret Search Indexer Configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.search_indexer_update_args import SearchIndexerUpdateArgs
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.search_indexer_model import SearchIndexerModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    search_indexer_update_args = SearchIndexerUpdateArgs(
        data=SearchIndexerUpdateModel(
            days_to_keep_logs=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            enabled=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            indexing_separators=UpdateFieldValueOfStringArray(
                dirty=True,
                value=[
                    "value_example",
                ],
            ),
            index_mode=UpdateFieldValueOfSearchIndexMode(
                dirty=True,
                value=SearchIndexMode("{}"),
            ),
        ),
    ) # SearchIndexerUpdateArgs | Secret Search Indexer Configuration Update Settings (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Secret Search Indexer Configuration
        api_response = api_instance.configuration_service_patch_secret_search_indexer_configuration(search_indexer_update_args=search_indexer_update_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_patch_secret_search_indexer_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_indexer_update_args** | [**SearchIndexerUpdateArgs**](SearchIndexerUpdateArgs.md)| Secret Search Indexer Configuration Update Settings | [optional]

### Return type

[**SearchIndexerModel**](SearchIndexerModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Secret Search Indexer Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_patch_security_configuration**
> ConfigurationSecurityModel configuration_service_patch_security_configuration()

Update Security configuration

Update Security Configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.configuration_security_model import ConfigurationSecurityModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.configuration_security_patch_args import ConfigurationSecurityPatchArgs
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    configuration_security_patch_args = ConfigurationSecurityPatchArgs(
        data=ConfigurationSecurityPatchModel(
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
                value="value_example",
            ),
            client_certificate_ids=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            database_integrity_monitoring_symmetric_key=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
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
                value="value_example",
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
                value=1,
            ),
            ignore_certificate_revocation_failures=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            maximum_file_size_bytes=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            maximum_file_size_supported=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            secret_erase_workflow=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=1,
            ),
            web_password_filler_requires_full_domain_match=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
        ),
    ) # ConfigurationSecurityPatchArgs | Security update args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Security configuration
        api_response = api_instance.configuration_service_patch_security_configuration(configuration_security_patch_args=configuration_security_patch_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_patch_security_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_security_patch_args** | [**ConfigurationSecurityPatchArgs**](ConfigurationSecurityPatchArgs.md)| Security update args | [optional]

### Return type

[**ConfigurationSecurityModel**](ConfigurationSecurityModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Security configuration after updates |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_patch_session_recording_advanced_configuration**
> ConfigurationSessionRecordingAdvancedModel configuration_service_patch_session_recording_advanced_configuration()

Update Session Recording Advanced

Update Session Recording Advanced Configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.configuration_session_recording_advanced_model import ConfigurationSessionRecordingAdvancedModel
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.configuration_session_recording_advanced_patch_args import ConfigurationSessionRecordingAdvancedPatchArgs
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    configuration_session_recording_advanced_patch_args = ConfigurationSessionRecordingAdvancedPatchArgs(
        data=ConfigurationSessionRecordingAdvancedPatchModel(
            agent_callback_url=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            enable_advanced_session_recording=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
        ),
    ) # ConfigurationSessionRecordingAdvancedPatchArgs | Session recording advanced update args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Session Recording Advanced
        api_response = api_instance.configuration_service_patch_session_recording_advanced_configuration(configuration_session_recording_advanced_patch_args=configuration_session_recording_advanced_patch_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_patch_session_recording_advanced_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_session_recording_advanced_patch_args** | [**ConfigurationSessionRecordingAdvancedPatchArgs**](ConfigurationSessionRecordingAdvancedPatchArgs.md)| Session recording advanced update args | [optional]

### Return type

[**ConfigurationSessionRecordingAdvancedModel**](ConfigurationSessionRecordingAdvancedModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Session Recording Advanced Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_patch_session_recording_configuration**
> ConfigurationSessionRecordingModel configuration_service_patch_session_recording_configuration()

Session Recording

Update Session Recording Configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.configuration_session_recording_model import ConfigurationSessionRecordingModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.configuration_session_recording_patch_args import ConfigurationSessionRecordingPatchArgs
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    configuration_session_recording_patch_args = ConfigurationSessionRecordingPatchArgs(
        data=ConfigurationSessionRecordingPatchModel(
            archive_location_by_site=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            archive_path=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            archive_path_mappings=UpdateFieldValueOfConfigurationSessionRecordingSiteArchiveUpdateModelArray(
                dirty=True,
                value=[
                    ConfigurationSessionRecordingSiteArchiveUpdateModel(
                        path="path_example",
                        site_id=1,
                    ),
                ],
            ),
            days_until_archive=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            days_until_delete=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
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
                value=1,
            ),
            max_session_length=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
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
                value=1,
            ),
        ),
    ) # ConfigurationSessionRecordingPatchArgs | Local user password update args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Session Recording
        api_response = api_instance.configuration_service_patch_session_recording_configuration(configuration_session_recording_patch_args=configuration_session_recording_patch_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_patch_session_recording_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_session_recording_patch_args** | [**ConfigurationSessionRecordingPatchArgs**](ConfigurationSessionRecordingPatchArgs.md)| Local user password update args | [optional]

### Return type

[**ConfigurationSessionRecordingModel**](ConfigurationSessionRecordingModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Session Recording Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_patch_system_log_configuration**
> SystemLogConfigurationViewModel configuration_service_patch_system_log_configuration()

Patch system log configuration

Patch system log configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.system_log_configuration_update_args import SystemLogConfigurationUpdateArgs
from secret_server_openapiclient.model.system_log_configuration_view_model import SystemLogConfigurationViewModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    system_log_configuration_update_args = SystemLogConfigurationUpdateArgs(
        data=SystemLogConfigurationUpdateModel(
            allow_viewing_online=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            enable_system_log=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            max_log_length=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=1,
            ),
            notify_when_shrunk=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
        ),
    ) # SystemLogConfigurationUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Patch system log configuration
        api_response = api_instance.configuration_service_patch_system_log_configuration(system_log_configuration_update_args=system_log_configuration_update_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_patch_system_log_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_log_configuration_update_args** | [**SystemLogConfigurationUpdateArgs**](SystemLogConfigurationUpdateArgs.md)| args | [optional]

### Return type

[**SystemLogConfigurationViewModel**](SystemLogConfigurationViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | System log configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_patch_ticket_system_configuration**
> ConfigurationTicketSystemViewModel configuration_service_patch_ticket_system_configuration()

Update the ticket system configuration

Update the ticket system configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.configuration_ticket_system_view_model import ConfigurationTicketSystemViewModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.configuration_ticket_system_args import ConfigurationTicketSystemArgs
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    configuration_ticket_system_args = ConfigurationTicketSystemArgs(
        data=[
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
                    value="value_example",
                ),
                bmc_incident_management_comment_work_type=UpdateFieldValueOfOptionalBmcIncidentManagementCommentWorkType(
                    dirty=True,
                    value="value_example",
                ),
                bmc_remedy_authentication=UpdateFieldValueOfString(
                    dirty=True,
                    value="value_example",
                ),
                bmc_remedy_url_endpoint=UpdateFieldValueOfString(
                    dirty=True,
                    value="value_example",
                ),
                description=UpdateFieldValueOfString(
                    dirty=True,
                    value="value_example",
                ),
                display_message=UpdateFieldValueOfString(
                    dirty=True,
                    value="value_example",
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
                    value="value_example",
                ),
                power_shell_add_comment_script_arguments=UpdateFieldValueOfString(
                    dirty=True,
                    value="value_example",
                ),
                power_shell_add_comment_script_id=UpdateFieldValueOfOptionalInt32(
                    dirty=True,
                    value=1,
                ),
                power_shell_add_ticket_comment_script_arguments=UpdateFieldValueOfString(
                    dirty=True,
                    value="value_example",
                ),
                power_shell_add_ticket_comment_script_id=UpdateFieldValueOfOptionalInt32(
                    dirty=True,
                    value=1,
                ),
                power_shell_run_as_account_secret_id=UpdateFieldValueOfOptionalInt32(
                    dirty=True,
                    value=1,
                ),
                power_shell_ticket_status_script_arguments=UpdateFieldValueOfString(
                    dirty=True,
                    value="value_example",
                ),
                power_shell_ticket_status_script_id=UpdateFieldValueOfOptionalInt32(
                    dirty=True,
                    value=1,
                ),
                service_now_allowed_statuses=UpdateFieldValueOfString(
                    dirty=True,
                    value="value_example",
                ),
                service_now_domain_name=UpdateFieldValueOfString(
                    dirty=True,
                    value="value_example",
                ),
                site_id=UpdateFieldValueOfOptionalInt32(
                    dirty=True,
                    value=1,
                ),
                system_credential_secret_id=UpdateFieldValueOfOptionalInt32(
                    dirty=True,
                    value=1,
                ),
                ticket_number_error_message=UpdateFieldValueOfString(
                    dirty=True,
                    value="value_example",
                ),
                ticket_number_validation=UpdateFieldValueOfString(
                    dirty=True,
                    value="value_example",
                ),
                ticket_system_id=1,
                ticket_system_type=UpdateFieldValueOfTicketSystemTypes(
                    dirty=True,
                    value=TicketSystemTypes("{}"),
                ),
                view_ticket_url=UpdateFieldValueOfString(
                    dirty=True,
                    value="value_example",
                ),
            ),
        ],
    ) # ConfigurationTicketSystemArgs | Ticket System update args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the ticket system configuration
        api_response = api_instance.configuration_service_patch_ticket_system_configuration(configuration_ticket_system_args=configuration_ticket_system_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_patch_ticket_system_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_ticket_system_args** | [**ConfigurationTicketSystemArgs**](ConfigurationTicketSystemArgs.md)| Ticket System update args | [optional]

### Return type

[**ConfigurationTicketSystemViewModel**](ConfigurationTicketSystemViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ticket System Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_patch_user_experience_configuration**
> ConfigurationUserExperienceModel configuration_service_patch_user_experience_configuration()

Update the user experience configuration

Update the user experience configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.configuration_user_experience_patch_args import ConfigurationUserExperiencePatchArgs
from secret_server_openapiclient.model.configuration_user_experience_model import ConfigurationUserExperienceModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    configuration_user_experience_patch_args = ConfigurationUserExperiencePatchArgs(
        data=ConfigurationUserExperiencePatchModel(
            application_language=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            checkout_notification_threshold=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            default_date_format=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            default_new_user_role_id=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=1,
            ),
            default_time_format=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            force_inactivity_timeout=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            force_inactivity_timeout_minutes=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            require_folder_for_secret=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            search_delay_ms=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            secret_password_history_restriction_all=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            secret_password_history_restriction_count=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=1,
            ),
            secret_view_interval_minutes=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            server_time_zone_id=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            ui_inactivity_sleep_minutes=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
        ),
    ) # ConfigurationUserExperiencePatchArgs | User experience update args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the user experience configuration
        api_response = api_instance.configuration_service_patch_user_experience_configuration(configuration_user_experience_patch_args=configuration_user_experience_patch_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_patch_user_experience_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_user_experience_patch_args** | [**ConfigurationUserExperiencePatchArgs**](ConfigurationUserExperiencePatchArgs.md)| User experience update args | [optional]

### Return type

[**ConfigurationUserExperienceModel**](ConfigurationUserExperienceModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User Experience Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_patch_user_interface_configuration**
> ConfigurationUserInterfaceModel configuration_service_patch_user_interface_configuration()

Update the user interface configuration

Update the user interface configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.configuration_user_interface_patch_args import ConfigurationUserInterfacePatchArgs
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.configuration_user_interface_model import ConfigurationUserInterfaceModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    configuration_user_interface_patch_args = ConfigurationUserInterfacePatchArgs(
        data=ConfigurationUserInterfacePatchModel(
            allow_user_to_select_theme=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            custom_logo_collapsed=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            custom_logo_full_size=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            default_classic_theme=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
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
    ) # ConfigurationUserInterfacePatchArgs | User interface update args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the user interface configuration
        api_response = api_instance.configuration_service_patch_user_interface_configuration(configuration_user_interface_patch_args=configuration_user_interface_patch_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_patch_user_interface_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_user_interface_patch_args** | [**ConfigurationUserInterfacePatchArgs**](ConfigurationUserInterfacePatchArgs.md)| User interface update args | [optional]

### Return type

[**ConfigurationUserInterfaceModel**](ConfigurationUserInterfaceModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User Interface Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_post_saml_configuration**
> ConfigurationSamlIdentityProviderModel configuration_service_post_saml_configuration()

Create Saml configuration

Create Saml Configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.configuration_saml_identity_provider_create_args import ConfigurationSamlIdentityProviderCreateArgs
from secret_server_openapiclient.model.configuration_saml_identity_provider_model import ConfigurationSamlIdentityProviderModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    configuration_saml_identity_provider_create_args = ConfigurationSamlIdentityProviderCreateArgs(
        data=ConfigurationSamlIdentityProviderCreateModel(
            active=True,
            authn_context="authn_context_example",
            clock_skew=1,
            description="description_example",
            disable_assertion_replay_check=True,
            disable_audience_restriction_check=True,
            disable_authn_context_check=True,
            disable_destination_check=True,
            disable_inbound_logout=True,
            disable_in_response_to_check=True,
            disable_pending_logout_check=True,
            disable_recipient_check=True,
            disable_time_period_check=True,
            display_name="display_name_example",
            domain_attribute="domain_attribute_example",
            enable_detailed_log=True,
            enable_slo=True,
            force_authentication=True,
            logout_request_life_time=1,
            name="name_example",
            override_pending_authn_request=True,
            public_certificate="public_certificate_example",
            sign_authn_request=True,
            sign_logout_request=True,
            sign_logout_response=True,
            single_logout_service_response_url="single_logout_service_response_url_example",
            single_logout_service_url="single_logout_service_url_example",
            sso_service_binding=1,
            sso_service_url="sso_service_url_example",
            username_attribute="username_attribute_example",
            want_assertion_encrypted=True,
            want_assertion_or_response_signed=True,
            want_assertion_signed=True,
            want_logout_request_signed=True,
            want_logout_response_signed=True,
            want_saml_response_signed=True,
        ),
    ) # ConfigurationSamlIdentityProviderCreateArgs | Saml create args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Saml configuration
        api_response = api_instance.configuration_service_post_saml_configuration(configuration_saml_identity_provider_create_args=configuration_saml_identity_provider_create_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_post_saml_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_saml_identity_provider_create_args** | [**ConfigurationSamlIdentityProviderCreateArgs**](ConfigurationSamlIdentityProviderCreateArgs.md)| Saml create args | [optional]

### Return type

[**ConfigurationSamlIdentityProviderModel**](ConfigurationSamlIdentityProviderModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Saml configuration after create |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_rebuild_secret_search_indexer_configuration**
> bool configuration_service_rebuild_secret_search_indexer_configuration()

Rebuild Secret Search Index

Start Rebuilding the Secret Search Index.  This method just indicates that a background process should start to process the index.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Rebuild Secret Search Index
        api_response = api_instance.configuration_service_rebuild_secret_search_indexer_configuration()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_rebuild_secret_search_indexer_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | true if the job was queued |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_rotate_secret_keys**
> RotateSecretKeysStatusModel configuration_service_rotate_secret_keys()

Rotate Secret Keys

Rotate Secret Keys

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.rotate_secret_keys_status_model import RotateSecretKeysStatusModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Rotate Secret Keys
        api_response = api_instance.configuration_service_rotate_secret_keys()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_rotate_secret_keys: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**RotateSecretKeysStatusModel**](RotateSecretKeysStatusModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of running Rotate Secret Keys |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_run_auto_export_now**
> bool configuration_service_run_auto_export_now()

Start Automatic Export

Start the automatic export as configured

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Start Automatic Export
        api_response = api_instance.configuration_service_run_auto_export_now()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_run_auto_export_now: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | True if the job was queued |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_run_backup_now**
> bool configuration_service_run_backup_now()

Start Backup

Start the backup as configured

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Start Backup
        api_response = api_instance.configuration_service_run_backup_now()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_run_backup_now: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | true if the job was queued |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_run_heartbeat_now**
> ConfigurationHeartbeatRunNowResultModel configuration_service_run_heartbeat_now()

Run Heartbeat Now

Run Heartbeat Now

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.configuration_heartbeat_run_now_result_model import ConfigurationHeartbeatRunNowResultModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Run Heartbeat Now
        api_response = api_instance.configuration_service_run_heartbeat_now()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_run_heartbeat_now: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigurationHeartbeatRunNowResultModel**](ConfigurationHeartbeatRunNowResultModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of running Heartbeat now |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_run_rpc_now**
> ConfigurationRpcRunNowResultModel configuration_service_run_rpc_now()

Run RPC Now

Run RPC Now

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.configuration_rpc_run_now_result_model import ConfigurationRpcRunNowResultModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Run RPC Now
        api_response = api_instance.configuration_service_run_rpc_now()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_run_rpc_now: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigurationRpcRunNowResultModel**](ConfigurationRpcRunNowResultModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of running RPC now |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_test_email**
> TestEmailResponse configuration_service_test_email()

TestEmail

Send Test Email

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.test_email_response import TestEmailResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # TestEmail
        api_response = api_instance.configuration_service_test_email()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_test_email: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**TestEmailResponse**](TestEmailResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Test Email Response |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_test_radius_login**
> TestRadiusLoginResponseModel configuration_service_test_radius_login()

Test Radius Login

Test a Radius Login

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.test_radius_login_args import TestRadiusLoginArgs
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.test_radius_login_response_model import TestRadiusLoginResponseModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    test_radius_login_args = TestRadiusLoginArgs(
        data=TestRadiusLoginRequestModel(
            radius_password="radius_password_example",
            radius_username="radius_username_example",
        ),
    ) # TestRadiusLoginArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Test Radius Login
        api_response = api_instance.configuration_service_test_radius_login(test_radius_login_args=test_radius_login_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_test_radius_login: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_radius_login_args** | [**TestRadiusLoginArgs**](TestRadiusLoginArgs.md)| args | [optional]

### Return type

[**TestRadiusLoginResponseModel**](TestRadiusLoginResponseModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Test Radius Login Response |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_service_update_unlimited_admin**
> bool configuration_service_update_unlimited_admin()

Update Unlimited Admin

Update Unlimited Admin

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import configuration_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.unlimited_admin_update_args import UnlimitedAdminUpdateArgs
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = secret_server_openapiclient.Configuration(
    host = "https://integrations.secretservercloud.com/api"
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
with secret_server_openapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_api.ConfigurationApi(api_client)
    unlimited_admin_update_args = UnlimitedAdminUpdateArgs(
        data=UnlimitedAdminUpdateModel(
            enabled=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            notes=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
        ),
    ) # UnlimitedAdminUpdateArgs | Unlimited Admin Update Options (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Unlimited Admin
        api_response = api_instance.configuration_service_update_unlimited_admin(unlimited_admin_update_args=unlimited_admin_update_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConfigurationApi->configuration_service_update_unlimited_admin: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unlimited_admin_update_args** | [**UnlimitedAdminUpdateArgs**](UnlimitedAdminUpdateArgs.md)| Unlimited Admin Update Options | [optional]

### Return type

**bool**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

