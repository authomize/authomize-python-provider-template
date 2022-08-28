# plugins.SecretsApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**secrets_service_change_password**](SecretsApi.md#secrets_service_change_password) | **POST** /v1/secrets/{id}/change-password | Change Secret Password
[**secrets_service_check_in**](SecretsApi.md#secrets_service_check_in) | **POST** /v1/secrets/{id}/check-in | Check In Secret
[**secrets_service_check_out**](SecretsApi.md#secrets_service_check_out) | **POST** /v1/secrets/{id}/check-out | Check Out Secret
[**secrets_service_convert_template**](SecretsApi.md#secrets_service_convert_template) | **POST** /v1/secrets/convert-template | Convert template
[**secrets_service_create_secret**](SecretsApi.md#secrets_service_create_secret) | **POST** /v1/secrets | Create Secret
[**secrets_service_delete**](SecretsApi.md#secrets_service_delete) | **DELETE** /v1/secrets/{id} | Deactivate a Secret
[**secrets_service_delete_list_field_list_definitions**](SecretsApi.md#secrets_service_delete_list_field_list_definitions) | **DELETE** /v1/secrets/{id}/fields/{slug}/listdetails | Delete Secret List Field List Data
[**secrets_service_expire**](SecretsApi.md#secrets_service_expire) | **POST** /v1/secrets/{id}/expire | Expire Secret
[**secrets_service_export_secrets**](SecretsApi.md#secrets_service_export_secrets) | **POST** /v1/secrets/export | Export Secrets
[**secrets_service_extend_check_out**](SecretsApi.md#secrets_service_extend_check_out) | **POST** /v1/secrets/{id}/extend-check-out | Extend Check Out
[**secrets_service_favorite**](SecretsApi.md#secrets_service_favorite) | **POST** /v1/secrets/{secretId}/favorite | Favorite a Secret
[**secrets_service_get_active_secret_sessions**](SecretsApi.md#secrets_service_get_active_secret_sessions) | **GET** /v1/secrets/launcher-sessions | Get Secret Launcher Sessions By Id
[**secrets_service_get_convert_info**](SecretsApi.md#secrets_service_get_convert_info) | **POST** /v1/secrets/get-convert-info | Convert template
[**secrets_service_get_favorites**](SecretsApi.md#secrets_service_get_favorites) | **GET** /v1/secrets/favorite | List a User&#39;s Favorite Secrets
[**secrets_service_get_field**](SecretsApi.md#secrets_service_get_field) | **GET** /v1/secrets/{id}/fields/{slug} | Get Secret Field
[**secrets_service_get_general**](SecretsApi.md#secrets_service_get_general) | **GET** /v1/secrets/secret-detail/{id}/general/{isEditMode?}/{loadReadOnlyFlags?} | Get Secret Detail General
[**secrets_service_get_list_field**](SecretsApi.md#secrets_service_get_list_field) | **GET** /v1/secrets/{id}/fields/{slug}/list | Get Secret List Field
[**secrets_service_get_list_field_list_definitions**](SecretsApi.md#secrets_service_get_list_field_list_definitions) | **GET** /v1/secrets/{id}/fields/{slug}/listdetails | Get Secret List Field List Data
[**secrets_service_get_lookup**](SecretsApi.md#secrets_service_get_lookup) | **GET** /v1/secrets/lookup/{id} | Lookup Secret
[**secrets_service_get_restricted**](SecretsApi.md#secrets_service_get_restricted) | **POST** /v1/secrets/{id}/restricted | Get Restricted Secret
[**secrets_service_get_secret_audits**](SecretsApi.md#secrets_service_get_secret_audits) | **GET** /v1/secrets/{id}/audits | Get Secret Audits by Filter
[**secrets_service_get_secret_extended_search_details**](SecretsApi.md#secrets_service_get_secret_extended_search_details) | **POST** /v1/secrets/extended-search-details | Secret Search Extended Details
[**secrets_service_get_secret_preview**](SecretsApi.md#secrets_service_get_secret_preview) | **GET** /v1/secrets/{id}/preview | Get Secret Preview
[**secrets_service_get_secret_rdp_proxy_info**](SecretsApi.md#secrets_service_get_secret_rdp_proxy_info) | **POST** /v1/secrets/rdpproxy | Get RDP Proxy Information
[**secrets_service_get_secret_settings**](SecretsApi.md#secrets_service_get_secret_settings) | **GET** /v1/secrets/{id}/settings | Get Secret Settings
[**secrets_service_get_secret_ssh_proxy_info**](SecretsApi.md#secrets_service_get_secret_ssh_proxy_info) | **POST** /v1/secrets/sshproxy | Get SSH Proxy Information
[**secrets_service_get_secret_ssh_terminal_details**](SecretsApi.md#secrets_service_get_secret_ssh_terminal_details) | **POST** /v1/secrets/sshterminal | Get SSH Terminal Details
[**secrets_service_get_secret_state**](SecretsApi.md#secrets_service_get_secret_state) | **GET** /v1/secrets/{id}/state | Get Secret State
[**secrets_service_get_secret_v2**](SecretsApi.md#secrets_service_get_secret_v2) | **GET** /v2/secrets/{id} | Get Secret
[**secrets_service_get_ssh_restricted_commands**](SecretsApi.md#secrets_service_get_ssh_restricted_commands) | **GET** /v1/secrets/{id}/ssh-restricted-commands | Get SSH Command Restrictions on a Secret
[**secrets_service_get_summary**](SecretsApi.md#secrets_service_get_summary) | **GET** /v1/secrets/{id}/summary | Get Secret Summary
[**secrets_service_put_field**](SecretsApi.md#secrets_service_put_field) | **PUT** /v1/secrets/{id}/fields/{slug} | Update Secret Field
[**secrets_service_restricted_field**](SecretsApi.md#secrets_service_restricted_field) | **POST** /v1/secrets/{id}/restricted/fields/{slug} | Get Restricted Secret Field
[**secrets_service_run_heart_beat**](SecretsApi.md#secrets_service_run_heart_beat) | **POST** /v1/secrets/{id}/heartbeat | Run Secret Heartbeat
[**secrets_service_search_secret_lookup**](SecretsApi.md#secrets_service_search_secret_lookup) | **GET** /v1/secrets/lookup | Lookup Secrets with Search
[**secrets_service_search_total_v2**](SecretsApi.md#secrets_service_search_total_v2) | **GET** /v2/secrets/search-total | Get Secret Search Total
[**secrets_service_search_v2**](SecretsApi.md#secrets_service_search_v2) | **GET** /v2/secrets | Search Secrets
[**secrets_service_stop_password_change**](SecretsApi.md#secrets_service_stop_password_change) | **POST** /v1/secrets/{id}/stop-password-change | Attempt to stop a password change
[**secrets_service_stub**](SecretsApi.md#secrets_service_stub) | **GET** /v1/secrets/stub | Get Secret Stub
[**secrets_service_undelete_secret**](SecretsApi.md#secrets_service_undelete_secret) | **PUT** /v1/secrets/{id}/activate | Undelete a Secret
[**secrets_service_undelete_secret_v2**](SecretsApi.md#secrets_service_undelete_secret_v2) | **PUT** /v2/secrets/{id}/activate | Undelete a Secret
[**secrets_service_update_email**](SecretsApi.md#secrets_service_update_email) | **PATCH** /v1/secrets/{id}/email | Update User Secret Email Settings
[**secrets_service_update_email_v2**](SecretsApi.md#secrets_service_update_email_v2) | **PATCH** /v2/secrets/{id}/email | Update User Secret Email Settings
[**secrets_service_update_expiration**](SecretsApi.md#secrets_service_update_expiration) | **PUT** /v1/secrets/{id}/expiration | Update a Secret expiration
[**secrets_service_update_general**](SecretsApi.md#secrets_service_update_general) | **PATCH** /v1/secrets/{id}/general | Update Secret General Information
[**secrets_service_update_general_v2**](SecretsApi.md#secrets_service_update_general_v2) | **PATCH** /v2/secrets/{id}/general | Update Secret General Information
[**secrets_service_update_jumpbox_route_selection**](SecretsApi.md#secrets_service_update_jumpbox_route_selection) | **PUT** /v1/secret-detail/{secretId}/jumpbox-route-selection | Update Jumpbox Route Selection
[**secrets_service_update_list_field_list_definitions**](SecretsApi.md#secrets_service_update_list_field_list_definitions) | **PUT** /v1/secrets/{id}/fields/{slug}/listdetails | Update Secret List Field List Data
[**secrets_service_update_rpc_script_secrets**](SecretsApi.md#secrets_service_update_rpc_script_secrets) | **PUT** /v1/secrets/{id}/rpc-script-secrets | Update which Secrets are available for RPC scripts
[**secrets_service_update_rpc_script_secrets_v2**](SecretsApi.md#secrets_service_update_rpc_script_secrets_v2) | **PUT** /v2/secrets/{id}/rpc-script-secrets | Update which Secrets are available for RPC scripts
[**secrets_service_update_secret**](SecretsApi.md#secrets_service_update_secret) | **PUT** /v1/secrets/{id} | Update Secret
[**secrets_service_update_secret_session**](SecretsApi.md#secrets_service_update_secret_session) | **PATCH** /v1/secrets/launcher-sessions | Update Secret Launcher Sessions
[**secrets_service_update_security**](SecretsApi.md#secrets_service_update_security) | **PATCH** /v1/secrets/{id}/security-general | Update Secret Security General Options
[**secrets_service_update_security_approval_v3**](SecretsApi.md#secrets_service_update_security_approval_v3) | **PUT** /v3/secrets/{id}/security-approval | Update Secret Security Approval Options
[**secrets_service_update_security_checkout_v3**](SecretsApi.md#secrets_service_update_security_checkout_v3) | **PATCH** /v3/secrets/{id}/security-checkout | Update Secret Security Checkout Options
[**secrets_service_update_security_v2**](SecretsApi.md#secrets_service_update_security_v2) | **PATCH** /v2/secrets/{id}/security-general | Update Secret Security General Options
[**secrets_service_update_ssh_restricted_commands**](SecretsApi.md#secrets_service_update_ssh_restricted_commands) | **PUT** /v1/secrets/{secretId}/update-ssh-restricted-commands | Update Restricted SSH Commands on a Secret


# **secrets_service_change_password**
> SecretSummary secrets_service_change_password(id)

Change Secret Password

Change a secret's password

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.secret_change_password_args import SecretChangePasswordArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_summary import SecretSummary
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret ID
    auto_check_in = True # bool | Automatically check in a secret after finding or updating. (optional)
    auto_checkout = True # bool | Automatically check out secret before finding or updating. (optional)
    auto_comment = None # bool, date, datetime, dict, float, int, list, str, none_type | Leave a comment when checking in or out. (optional)
    force_check_in = True # bool | If secret is checked out, then force a check in. (optional)
    secret_path = None # bool, date, datetime, dict, float, int, list, str, none_type | A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. (optional)
    secret_change_password_args = SecretChangePasswordArgs(
        comment=None,
        double_lock_password=None,
        force_check_in=True,
        include_inactive=True,
        new_password=None,
        no_auto_checkout=True,
        ssh_key_args=RotateSshKeyArgs(
            generate_passphrase=True,
            generate_ssh_keys=True,
            passphrase=None,
            private_key=None,
        ),
        ticket_number=None,
        ticket_system_id=None,
    ) # SecretChangePasswordArgs | Secret options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Change Secret Password
        api_response = api_instance.secrets_service_change_password(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_change_password: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Change Secret Password
        api_response = api_instance.secrets_service_change_password(id, auto_check_in=auto_check_in, auto_checkout=auto_checkout, auto_comment=auto_comment, force_check_in=force_check_in, secret_path=secret_path, secret_change_password_args=secret_change_password_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_change_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret ID |
 **auto_check_in** | **bool**| Automatically check in a secret after finding or updating. | [optional]
 **auto_checkout** | **bool**| Automatically check out secret before finding or updating. | [optional]
 **auto_comment** | **bool, date, datetime, dict, float, int, list, str, none_type**| Leave a comment when checking in or out. | [optional]
 **force_check_in** | **bool**| If secret is checked out, then force a check in. | [optional]
 **secret_path** | **bool, date, datetime, dict, float, int, list, str, none_type**| A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. | [optional]
 **secret_change_password_args** | [**SecretChangePasswordArgs**](SecretChangePasswordArgs.md)| Secret options | [optional]

### Return type

[**SecretSummary**](SecretSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret summary object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_check_in**
> SecretSummary secrets_service_check_in(id)

Check In Secret

Check in a secret. Checking a secret ends exclusive access to the secret and allows other users to check-out and view or edit it.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.secret_restricted_args import SecretRestrictedArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_summary import SecretSummary
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret ID
    secret_path = None # bool, date, datetime, dict, float, int, list, str, none_type | A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. (optional)
    secret_restricted_args = SecretRestrictedArgs(
        comment=None,
        double_lock_password=None,
        force_check_in=True,
        include_inactive=True,
        new_password=None,
        no_auto_checkout=True,
        ticket_number=None,
        ticket_system_id=None,
    ) # SecretRestrictedArgs | Secret options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Check In Secret
        api_response = api_instance.secrets_service_check_in(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_check_in: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Check In Secret
        api_response = api_instance.secrets_service_check_in(id, secret_path=secret_path, secret_restricted_args=secret_restricted_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_check_in: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret ID |
 **secret_path** | **bool, date, datetime, dict, float, int, list, str, none_type**| A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. | [optional]
 **secret_restricted_args** | [**SecretRestrictedArgs**](SecretRestrictedArgs.md)| Secret options | [optional]

### Return type

[**SecretSummary**](SecretSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret summary object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_check_out**
> SecretResponseCodeModel secrets_service_check_out(id)

Check Out Secret

Check Out a secret

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_response_code_model import SecretResponseCodeModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret ID
    secret_path = None # bool, date, datetime, dict, float, int, list, str, none_type | A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Check Out Secret
        api_response = api_instance.secrets_service_check_out(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_check_out: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Check Out Secret
        api_response = api_instance.secrets_service_check_out(id, secret_path=secret_path)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_check_out: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret ID |
 **secret_path** | **bool, date, datetime, dict, float, int, list, str, none_type**| A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. | [optional]

### Return type

[**SecretResponseCodeModel**](SecretResponseCodeModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Response Code Model object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_convert_template**
> SecretDetailConvertTemplateModel secrets_service_convert_template()

Convert template

Convert template

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_detail_convert_template_args import SecretDetailConvertTemplateArgs
from plugins.model.secret_detail_convert_template_model import SecretDetailConvertTemplateModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    secret_detail_convert_template_args = SecretDetailConvertTemplateArgs(
        data=ConvertTemplateActionModel(
            field_mapping=[
                ConvertTemplateFieldModel(
                    destination_field_id=None,
                    source_field_id=None,
                    source_field_value=None,
                ),
            ],
            folder_id=None,
            is_bulk=True,
            new_secret_name=None,
            secret_ids=[
                None,
            ],
            secret_template_id=None,
        ),
    ) # SecretDetailConvertTemplateArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Convert template
        api_response = api_instance.secrets_service_convert_template(secret_detail_convert_template_args=secret_detail_convert_template_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_convert_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_detail_convert_template_args** | [**SecretDetailConvertTemplateArgs**](SecretDetailConvertTemplateArgs.md)| args | [optional]

### Return type

[**SecretDetailConvertTemplateModel**](SecretDetailConvertTemplateModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Convert template result |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_create_secret**
> SecretModel secrets_service_create_secret()

Create Secret

Create a new secret

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_model import SecretModel
from plugins.model.secret_create_args import SecretCreateArgs
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    secret_create_args = SecretCreateArgs(
        auto_change_enabled=True,
        check_out_change_password_enabled=True,
        check_out_enabled=True,
        check_out_interval_minutes=None,
        delay_indexing=True,
        enable_inherit_permissions=True,
        enable_inherit_secret_policy=True,
        folder_id=None,
        items=[
            RestSecretItem(
                field_description=None,
                field_id=None,
                field_name=None,
                file_attachment_id=None,
                filename=None,
                is_file=True,
                is_list=True,
                is_notes=True,
                is_password=True,
                item_id=None,
                item_value=None,
                list_type=SecretFieldListType("{}"),
                slug=None,
            ),
        ],
        launcher_connect_as_secret_id=None,
        name=None,
        password_type_web_script_id=None,
        proxy_enabled=True,
        requires_comment=True,
        secret_policy_id=None,
        secret_template_id=None,
        session_recording_enabled=True,
        site_id=None,
        ssh_key_args=SshKeyArgs(
            generate_passphrase=True,
            generate_ssh_keys=True,
        ),
        web_launcher_requires_incognito_mode=True,
    ) # SecretCreateArgs | Secret creation options (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Secret
        api_response = api_instance.secrets_service_create_secret(secret_create_args=secret_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_create_secret: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_create_args** | [**SecretCreateArgs**](SecretCreateArgs.md)| Secret creation options | [optional]

### Return type

[**SecretModel**](SecretModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_delete**
> DeletedModel secrets_service_delete(id)

Deactivate a Secret

A deactivated secret is hidden from users who do not have a role containing the View Deleted Secrets permission. Secret Server uses these \"soft deletes\" to maintain the audit history for all data. However, deactivated secrets are still accessible by administrators (like a permanent Recycle Bin) to ensure that audit history is maintained and to support recovery. A user must have the \"View Deleted Secrets\" permission in addition to Owner permission on a secret to access the secret View page for a deleted secret. To permanently remove all information on a secret, use the \"Erase Secret\" function.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.deleted_model import DeletedModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret ID
    auto_check_in = True # bool | Automatically check in a secret after finding or updating. (optional)
    auto_checkout = True # bool | Automatically check out secret before finding or updating. (optional)
    auto_comment = None # bool, date, datetime, dict, float, int, list, str, none_type | Leave a comment when checking in or out. (optional)
    force_check_in = True # bool | If secret is checked out, then force a check in. (optional)
    secret_path = None # bool, date, datetime, dict, float, int, list, str, none_type | A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deactivate a Secret
        api_response = api_instance.secrets_service_delete(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deactivate a Secret
        api_response = api_instance.secrets_service_delete(id, auto_check_in=auto_check_in, auto_checkout=auto_checkout, auto_comment=auto_comment, force_check_in=force_check_in, secret_path=secret_path)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret ID |
 **auto_check_in** | **bool**| Automatically check in a secret after finding or updating. | [optional]
 **auto_checkout** | **bool**| Automatically check out secret before finding or updating. | [optional]
 **auto_comment** | **bool, date, datetime, dict, float, int, list, str, none_type**| Leave a comment when checking in or out. | [optional]
 **force_check_in** | **bool**| If secret is checked out, then force a check in. | [optional]
 **secret_path** | **bool, date, datetime, dict, float, int, list, str, none_type**| A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. | [optional]

### Return type

[**DeletedModel**](DeletedModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Object deletion result |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_delete_list_field_list_definitions**
> PagingOfCategorizedListSummary secrets_service_delete_list_field_list_definitions(id, slug)

Delete Secret List Field List Data

Deletes the lists associated to a secret list data field

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_categorized_list_summary import PagingOfCategorizedListSummary
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret ID
    slug = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret field name
    auto_check_in = True # bool | Automatically check in a secret after finding or updating. (optional)
    auto_checkout = True # bool | Automatically check out secret before finding or updating. (optional)
    auto_comment = None # bool, date, datetime, dict, float, int, list, str, none_type | Leave a comment when checking in or out. (optional)
    force_check_in = True # bool | If secret is checked out, then force a check in. (optional)
    list_guid = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete Secret List Field List Data
        api_response = api_instance.secrets_service_delete_list_field_list_definitions(id, slug)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_delete_list_field_list_definitions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Secret List Field List Data
        api_response = api_instance.secrets_service_delete_list_field_list_definitions(id, slug, auto_check_in=auto_check_in, auto_checkout=auto_checkout, auto_comment=auto_comment, force_check_in=force_check_in, list_guid=list_guid)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_delete_list_field_list_definitions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret ID |
 **slug** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret field name |
 **auto_check_in** | **bool**| Automatically check in a secret after finding or updating. | [optional]
 **auto_checkout** | **bool**| Automatically check out secret before finding or updating. | [optional]
 **auto_comment** | **bool, date, datetime, dict, float, int, list, str, none_type**| Leave a comment when checking in or out. | [optional]
 **force_check_in** | **bool**| If secret is checked out, then force a check in. | [optional]
 **list_guid** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret options | [optional]

### Return type

[**PagingOfCategorizedListSummary**](PagingOfCategorizedListSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Combined summary of all lists assigned to the secret field. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_expire**
> SecretSummary secrets_service_expire(id)

Expire Secret

Expire a secret

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.secret_restricted_args import SecretRestrictedArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_summary import SecretSummary
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret ID
    auto_check_in = True # bool | Automatically check in a secret after finding or updating. (optional)
    auto_checkout = True # bool | Automatically check out secret before finding or updating. (optional)
    auto_comment = None # bool, date, datetime, dict, float, int, list, str, none_type | Leave a comment when checking in or out. (optional)
    force_check_in = True # bool | If secret is checked out, then force a check in. (optional)
    secret_path = None # bool, date, datetime, dict, float, int, list, str, none_type | A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. (optional)
    secret_restricted_args = SecretRestrictedArgs(
        comment=None,
        double_lock_password=None,
        force_check_in=True,
        include_inactive=True,
        new_password=None,
        no_auto_checkout=True,
        ticket_number=None,
        ticket_system_id=None,
    ) # SecretRestrictedArgs | Secret options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Expire Secret
        api_response = api_instance.secrets_service_expire(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_expire: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Expire Secret
        api_response = api_instance.secrets_service_expire(id, auto_check_in=auto_check_in, auto_checkout=auto_checkout, auto_comment=auto_comment, force_check_in=force_check_in, secret_path=secret_path, secret_restricted_args=secret_restricted_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_expire: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret ID |
 **auto_check_in** | **bool**| Automatically check in a secret after finding or updating. | [optional]
 **auto_checkout** | **bool**| Automatically check out secret before finding or updating. | [optional]
 **auto_comment** | **bool, date, datetime, dict, float, int, list, str, none_type**| Leave a comment when checking in or out. | [optional]
 **force_check_in** | **bool**| If secret is checked out, then force a check in. | [optional]
 **secret_path** | **bool, date, datetime, dict, float, int, list, str, none_type**| A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. | [optional]
 **secret_restricted_args** | [**SecretRestrictedArgs**](SecretRestrictedArgs.md)| Secret options | [optional]

### Return type

[**SecretSummary**](SecretSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret summary object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_export_secrets**
> SecretsExportResultModel secrets_service_export_secrets()

Export Secrets

Exports secrets

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secrets_export_result_model import SecretsExportResultModel
from plugins.model.secrets_export_args import SecretsExportArgs
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    secrets_export_args = SecretsExportArgs(
        data=SecretsExportModel(
            double_lock_password=None,
            export_child_folders=True,
            export_file_type=ExportFileType("{}"),
            export_folder_path=True,
            export_totp=True,
            folder_id=None,
            notes=None,
            password=None,
        ),
    ) # SecretsExportArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export Secrets
        api_response = api_instance.secrets_service_export_secrets(secrets_export_args=secrets_export_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_export_secrets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secrets_export_args** | [**SecretsExportArgs**](SecretsExportArgs.md)| args | [optional]

### Return type

[**SecretsExportResultModel**](SecretsExportResultModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Exported secrets |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_extend_check_out**
> SecretCheckOutExtensionResponseModel secrets_service_extend_check_out(id)

Extend Check Out

Extend remaining check out time.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.secret_check_out_extension_response_model import SecretCheckOutExtensionResponseModel
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.secret_check_out_extension_args import SecretCheckOutExtensionArgs
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    secret_check_out_extension_args = SecretCheckOutExtensionArgs(
        data=SecretCheckOutExtensionModel(
            minutes_to_add=None,
            notes=None,
        ),
    ) # SecretCheckOutExtensionArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Extend Check Out
        api_response = api_instance.secrets_service_extend_check_out(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_extend_check_out: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Extend Check Out
        api_response = api_instance.secrets_service_extend_check_out(id, secret_check_out_extension_args=secret_check_out_extension_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_extend_check_out: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **secret_check_out_extension_args** | [**SecretCheckOutExtensionArgs**](SecretCheckOutExtensionArgs.md)| args | [optional]

### Return type

[**SecretCheckOutExtensionResponseModel**](SecretCheckOutExtensionResponseModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Check Out Extension Response |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_favorite**
> bool secrets_service_favorite(secret_id)

Favorite a Secret

Used to favorite or unfavorite an individual Secret

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.favorite_secret_args import FavoriteSecretArgs
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    secret_id = None # bool, date, datetime, dict, float, int, list, str, none_type | The secret to favorite or unfavorite.
    secret_path = None # bool, date, datetime, dict, float, int, list, str, none_type | A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. (optional)
    favorite_secret_args = FavoriteSecretArgs(
        is_favorite=True,
    ) # FavoriteSecretArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Favorite a Secret
        api_response = api_instance.secrets_service_favorite(secret_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_favorite: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Favorite a Secret
        api_response = api_instance.secrets_service_favorite(secret_id, secret_path=secret_path, favorite_secret_args=favorite_secret_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_favorite: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| The secret to favorite or unfavorite. |
 **secret_path** | **bool, date, datetime, dict, float, int, list, str, none_type**| A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. | [optional]
 **favorite_secret_args** | [**FavoriteSecretArgs**](FavoriteSecretArgs.md)| args | [optional]

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
**200** | Whether or not the secret is now favorited by the user. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_get_active_secret_sessions**
> PagingOfSecretLauncherSessionSummary secrets_service_get_active_secret_sessions()

Get Secret Launcher Sessions By Id

Get secret launcher sessions

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_secret_launcher_session_summary import PagingOfSecretLauncherSessionSummary
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    filter_secret_id = None # bool, date, datetime, dict, float, int, list, str, none_type | The Id of the associated Secret. (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Secret Launcher Sessions By Id
        api_response = api_instance.secrets_service_get_active_secret_sessions(filter_secret_id=filter_secret_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_get_active_secret_sessions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_secret_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| The Id of the associated Secret. | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfSecretLauncherSessionSummary**](PagingOfSecretLauncherSessionSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Launcher Sessions |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_get_convert_info**
> ConvertTemplateDetailsModel secrets_service_get_convert_info()

Convert template

Convert template

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.convert_template_details_model import ConvertTemplateDetailsModel
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_detail_convert_template_info_args import SecretDetailConvertTemplateInfoArgs
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    secret_detail_convert_template_info_args = SecretDetailConvertTemplateInfoArgs(
        data=ConvertTemplateInfoModel(
            destination_template_id=None,
            secret_ids=[
                None,
            ],
        ),
    ) # SecretDetailConvertTemplateInfoArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Convert template
        api_response = api_instance.secrets_service_get_convert_info(secret_detail_convert_template_info_args=secret_detail_convert_template_info_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_get_convert_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_detail_convert_template_info_args** | [**SecretDetailConvertTemplateInfoArgs**](SecretDetailConvertTemplateInfoArgs.md)| args | [optional]

### Return type

[**ConvertTemplateDetailsModel**](ConvertTemplateDetailsModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Convert template result |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_get_favorites**
> [WidgetSecretModel] secrets_service_get_favorites()

List a User's Favorite Secrets

Returns a list of secrets which the user has favorited.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.widget_secret_model import WidgetSecretModel
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List a User's Favorite Secrets
        api_response = api_instance.secrets_service_get_favorites()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_get_favorites: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[WidgetSecretModel]**](WidgetSecretModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Identifying information for each secret favorited |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_get_field**
> bool, date, datetime, dict, float, int, list, str, none_type secrets_service_get_field(id, slug)

Get Secret Field

Get a secret data field

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret ID
    slug = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret field name
    include_inactive = True # bool | Whether to include inactive secrets in the results (optional)
    no_auto_checkout = True # bool | Don't check out the secret if needed (optional)
    auto_check_in = True # bool | Automatically check in a secret after finding or updating. (optional)
    auto_checkout = True # bool | Automatically check out secret before finding or updating. (optional)
    auto_comment = None # bool, date, datetime, dict, float, int, list, str, none_type | Leave a comment when checking in or out. (optional)
    force_check_in = True # bool | If secret is checked out, then force a check in. (optional)
    secret_path = None # bool, date, datetime, dict, float, int, list, str, none_type | A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Secret Field
        api_response = api_instance.secrets_service_get_field(id, slug)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_get_field: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Secret Field
        api_response = api_instance.secrets_service_get_field(id, slug, include_inactive=include_inactive, no_auto_checkout=no_auto_checkout, auto_check_in=auto_check_in, auto_checkout=auto_checkout, auto_comment=auto_comment, force_check_in=force_check_in, secret_path=secret_path)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_get_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret ID |
 **slug** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret field name |
 **include_inactive** | **bool**| Whether to include inactive secrets in the results | [optional]
 **no_auto_checkout** | **bool**| Don&#39;t check out the secret if needed | [optional]
 **auto_check_in** | **bool**| Automatically check in a secret after finding or updating. | [optional]
 **auto_checkout** | **bool**| Automatically check out secret before finding or updating. | [optional]
 **auto_comment** | **bool, date, datetime, dict, float, int, list, str, none_type**| Leave a comment when checking in or out. | [optional]
 **force_check_in** | **bool**| If secret is checked out, then force a check in. | [optional]
 **secret_path** | **bool, date, datetime, dict, float, int, list, str, none_type**| A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret field value. If the field is a file attachment, the content type will be &#x60;application/octet-stream&#x60; and the response body will be the file contents. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_get_general**
> SecretDetailGeneralModel secrets_service_get_general(id)

Get Secret Detail General

Retrieve details about a secret.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.secret_detail_general_model import SecretDetailGeneralModel
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    is_edit_mode = True # bool | isEditMode (optional)
    load_read_only_flags = True # bool | loadReadOnlyFlags (optional)
    secret_path = None # bool, date, datetime, dict, float, int, list, str, none_type | A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Secret Detail General
        api_response = api_instance.secrets_service_get_general(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_get_general: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Secret Detail General
        api_response = api_instance.secrets_service_get_general(id, is_edit_mode=is_edit_mode, load_read_only_flags=load_read_only_flags, secret_path=secret_path)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_get_general: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **is_edit_mode** | **bool**| isEditMode | [optional]
 **load_read_only_flags** | **bool**| loadReadOnlyFlags | [optional]
 **secret_path** | **bool, date, datetime, dict, float, int, list, str, none_type**| A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. | [optional]

### Return type

[**SecretDetailGeneralModel**](SecretDetailGeneralModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Detail State View Model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_get_list_field**
> CategorizedListItemValueResult secrets_service_get_list_field(id, slug)

Get Secret List Field

Get the items associated to a secret list data field

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.categorized_list_item_value_result import CategorizedListItemValueResult
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret ID
    slug = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret field name
    auto_check_in = True # bool | Automatically check in a secret after finding or updating. (optional)
    auto_checkout = True # bool | Automatically check out secret before finding or updating. (optional)
    auto_comment = None # bool, date, datetime, dict, float, int, list, str, none_type | Leave a comment when checking in or out. (optional)
    force_check_in = True # bool | If secret is checked out, then force a check in. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Secret List Field
        api_response = api_instance.secrets_service_get_list_field(id, slug)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_get_list_field: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Secret List Field
        api_response = api_instance.secrets_service_get_list_field(id, slug, auto_check_in=auto_check_in, auto_checkout=auto_checkout, auto_comment=auto_comment, force_check_in=force_check_in)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_get_list_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret ID |
 **slug** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret field name |
 **auto_check_in** | **bool**| Automatically check in a secret after finding or updating. | [optional]
 **auto_checkout** | **bool**| Automatically check out secret before finding or updating. | [optional]
 **auto_comment** | **bool, date, datetime, dict, float, int, list, str, none_type**| Leave a comment when checking in or out. | [optional]
 **force_check_in** | **bool**| If secret is checked out, then force a check in. | [optional]

### Return type

[**CategorizedListItemValueResult**](CategorizedListItemValueResult.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Combined contents of all lists assigned to the secret field. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_get_list_field_list_definitions**
> PagingOfCategorizedListSummary secrets_service_get_list_field_list_definitions(id, slug)

Get Secret List Field List Data

Get the lists associated to a secret list data field

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_categorized_list_summary import PagingOfCategorizedListSummary
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret ID
    slug = None # bool, date, datetime, dict, float, int, list, str, none_type | The field slug name of the list field. This is the fieldSlugName property of the SecretField object. By default, it is the lower-case field name with all spaces replaced with dashes (-).
    auto_check_in = True # bool | Automatically check in a secret after finding or updating. (optional)
    auto_checkout = True # bool | Automatically check out secret before finding or updating. (optional)
    auto_comment = None # bool, date, datetime, dict, float, int, list, str, none_type | Leave a comment when checking in or out. (optional)
    force_check_in = True # bool | If secret is checked out, then force a check in. (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Secret List Field List Data
        api_response = api_instance.secrets_service_get_list_field_list_definitions(id, slug)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_get_list_field_list_definitions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Secret List Field List Data
        api_response = api_instance.secrets_service_get_list_field_list_definitions(id, slug, auto_check_in=auto_check_in, auto_checkout=auto_checkout, auto_comment=auto_comment, force_check_in=force_check_in, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_get_list_field_list_definitions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret ID |
 **slug** | **bool, date, datetime, dict, float, int, list, str, none_type**| The field slug name of the list field. This is the fieldSlugName property of the SecretField object. By default, it is the lower-case field name with all spaces replaced with dashes (-). |
 **auto_check_in** | **bool**| Automatically check in a secret after finding or updating. | [optional]
 **auto_checkout** | **bool**| Automatically check out secret before finding or updating. | [optional]
 **auto_comment** | **bool, date, datetime, dict, float, int, list, str, none_type**| Leave a comment when checking in or out. | [optional]
 **force_check_in** | **bool**| If secret is checked out, then force a check in. | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfCategorizedListSummary**](PagingOfCategorizedListSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Combined summary of all lists assigned to the secret field. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_get_lookup**
> SecretLookup secrets_service_get_lookup(id)

Lookup Secret

Look up secret by ID and return secret name and ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_lookup import SecretLookup
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret ID
    secret_path = None # bool, date, datetime, dict, float, int, list, str, none_type | A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Lookup Secret
        api_response = api_instance.secrets_service_get_lookup(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_get_lookup: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Lookup Secret
        api_response = api_instance.secrets_service_get_lookup(id, secret_path=secret_path)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_get_lookup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret ID |
 **secret_path** | **bool, date, datetime, dict, float, int, list, str, none_type**| A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. | [optional]

### Return type

[**SecretLookup**](SecretLookup.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret lookup result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_get_restricted**
> SecretModel secrets_service_get_restricted(id)

Get Restricted Secret

Get a restricted secret

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.secret_restricted_args import SecretRestrictedArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_model import SecretModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret ID
    auto_check_in = True # bool | Automatically check in a secret after finding or updating. (optional)
    auto_checkout = True # bool | Automatically check out secret before finding or updating. (optional)
    auto_comment = None # bool, date, datetime, dict, float, int, list, str, none_type | Leave a comment when checking in or out. (optional)
    force_check_in = True # bool | If secret is checked out, then force a check in. (optional)
    secret_path = None # bool, date, datetime, dict, float, int, list, str, none_type | A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. (optional)
    secret_restricted_args = SecretRestrictedArgs(
        comment=None,
        double_lock_password=None,
        force_check_in=True,
        include_inactive=True,
        new_password=None,
        no_auto_checkout=True,
        ticket_number=None,
        ticket_system_id=None,
    ) # SecretRestrictedArgs | Secret options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Restricted Secret
        api_response = api_instance.secrets_service_get_restricted(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_get_restricted: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Restricted Secret
        api_response = api_instance.secrets_service_get_restricted(id, auto_check_in=auto_check_in, auto_checkout=auto_checkout, auto_comment=auto_comment, force_check_in=force_check_in, secret_path=secret_path, secret_restricted_args=secret_restricted_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_get_restricted: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret ID |
 **auto_check_in** | **bool**| Automatically check in a secret after finding or updating. | [optional]
 **auto_checkout** | **bool**| Automatically check out secret before finding or updating. | [optional]
 **auto_comment** | **bool, date, datetime, dict, float, int, list, str, none_type**| Leave a comment when checking in or out. | [optional]
 **force_check_in** | **bool**| If secret is checked out, then force a check in. | [optional]
 **secret_path** | **bool, date, datetime, dict, float, int, list, str, none_type**| A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. | [optional]
 **secret_restricted_args** | [**SecretRestrictedArgs**](SecretRestrictedArgs.md)| Secret options | [optional]

### Return type

[**SecretModel**](SecretModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_get_secret_audits**
> PagingOfSecretAuditModel secrets_service_get_secret_audits(id)

Get Secret Audits by Filter

Get audits for a particular Secret for the given filter.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.paging_of_secret_audit_model import PagingOfSecretAuditModel
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    is_exporting = True # bool | isExporting (optional)
    filter_include_password_change_log = True # bool | Whether or not to include password changes in data (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)
    secret_path = None # bool, date, datetime, dict, float, int, list, str, none_type | A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Secret Audits by Filter
        api_response = api_instance.secrets_service_get_secret_audits(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_get_secret_audits: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Secret Audits by Filter
        api_response = api_instance.secrets_service_get_secret_audits(id, is_exporting=is_exporting, filter_include_password_change_log=filter_include_password_change_log, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take, secret_path=secret_path)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_get_secret_audits: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **is_exporting** | **bool**| isExporting | [optional]
 **filter_include_password_change_log** | **bool**| Whether or not to include password changes in data | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]
 **secret_path** | **bool, date, datetime, dict, float, int, list, str, none_type**| A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. | [optional]

### Return type

[**PagingOfSecretAuditModel**](PagingOfSecretAuditModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Audit Model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_get_secret_extended_search_details**
> [SecretSearchExtendedSummary] secrets_service_get_secret_extended_search_details()

Secret Search Extended Details

Pass an array of secret IDs, presumably the results of a secret search and get extended details such as has launchers or is favorite.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.secret_search_extended_args import SecretSearchExtendedArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_search_extended_summary import SecretSearchExtendedSummary
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    secret_search_extended_args = SecretSearchExtendedArgs(
        data=SecretSearchExtendedData(
            secret_ids=[
                None,
            ],
        ),
    ) # SecretSearchExtendedArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Secret Search Extended Details
        api_response = api_instance.secrets_service_get_secret_extended_search_details(secret_search_extended_args=secret_search_extended_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_get_secret_extended_search_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_search_extended_args** | [**SecretSearchExtendedArgs**](SecretSearchExtendedArgs.md)| args | [optional]

### Return type

[**[SecretSearchExtendedSummary]**](SecretSearchExtendedSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret search extended details |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_get_secret_preview**
> DashboardViewSecret secrets_service_get_secret_preview(id)

Get Secret Preview

Get a preview of an unrestricted secret by ID. Restricted secrets will return an AccessDeniedException.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.dashboard_view_secret import DashboardViewSecret
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret ID
    auto_check_in = True # bool | Automatically check in a secret after finding or updating. (optional)
    auto_checkout = True # bool | Automatically check out secret before finding or updating. (optional)
    auto_comment = None # bool, date, datetime, dict, float, int, list, str, none_type | Leave a comment when checking in or out. (optional)
    force_check_in = True # bool | If secret is checked out, then force a check in. (optional)
    secret_path = None # bool, date, datetime, dict, float, int, list, str, none_type | A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Secret Preview
        api_response = api_instance.secrets_service_get_secret_preview(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_get_secret_preview: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Secret Preview
        api_response = api_instance.secrets_service_get_secret_preview(id, auto_check_in=auto_check_in, auto_checkout=auto_checkout, auto_comment=auto_comment, force_check_in=force_check_in, secret_path=secret_path)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_get_secret_preview: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret ID |
 **auto_check_in** | **bool**| Automatically check in a secret after finding or updating. | [optional]
 **auto_checkout** | **bool**| Automatically check out secret before finding or updating. | [optional]
 **auto_comment** | **bool, date, datetime, dict, float, int, list, str, none_type**| Leave a comment when checking in or out. | [optional]
 **force_check_in** | **bool**| If secret is checked out, then force a check in. | [optional]
 **secret_path** | **bool, date, datetime, dict, float, int, list, str, none_type**| A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. | [optional]

### Return type

[**DashboardViewSecret**](DashboardViewSecret.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Preview object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_get_secret_rdp_proxy_info**
> SecretRdpProxyModel secrets_service_get_secret_rdp_proxy_info()

Get RDP Proxy Information

Get RDP Proxy Information

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.secret_rdp_proxy_model import SecretRdpProxyModel
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_proxy_args import SecretProxyArgs
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    auto_check_in = True # bool | Automatically check in a secret after finding or updating. (optional)
    auto_checkout = True # bool | Automatically check out secret before finding or updating. (optional)
    auto_comment = None # bool, date, datetime, dict, float, int, list, str, none_type | Leave a comment when checking in or out. (optional)
    force_check_in = True # bool | If secret is checked out, then force a check in. (optional)
    secret_proxy_args = SecretProxyArgs(
        launcher_type=None,
        machine=None,
        secret_id=None,
        site_id=None,
    ) # SecretProxyArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get RDP Proxy Information
        api_response = api_instance.secrets_service_get_secret_rdp_proxy_info(auto_check_in=auto_check_in, auto_checkout=auto_checkout, auto_comment=auto_comment, force_check_in=force_check_in, secret_proxy_args=secret_proxy_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_get_secret_rdp_proxy_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_check_in** | **bool**| Automatically check in a secret after finding or updating. | [optional]
 **auto_checkout** | **bool**| Automatically check out secret before finding or updating. | [optional]
 **auto_comment** | **bool, date, datetime, dict, float, int, list, str, none_type**| Leave a comment when checking in or out. | [optional]
 **force_check_in** | **bool**| If secret is checked out, then force a check in. | [optional]
 **secret_proxy_args** | [**SecretProxyArgs**](SecretProxyArgs.md)| args | [optional]

### Return type

[**SecretRdpProxyModel**](SecretRdpProxyModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RDP Proxy Information |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_get_secret_settings**
> SecretDetailSettingsModel secrets_service_get_secret_settings(id)

Get Secret Settings

Get Secret Settings

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.secret_detail_settings_model import SecretDetailSettingsModel
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    auto_check_in = True # bool | Automatically check in a secret after finding or updating. (optional)
    auto_checkout = True # bool | Automatically check out secret before finding or updating. (optional)
    auto_comment = None # bool, date, datetime, dict, float, int, list, str, none_type | Leave a comment when checking in or out. (optional)
    force_check_in = True # bool | If secret is checked out, then force a check in. (optional)
    secret_path = None # bool, date, datetime, dict, float, int, list, str, none_type | A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Secret Settings
        api_response = api_instance.secrets_service_get_secret_settings(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_get_secret_settings: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Secret Settings
        api_response = api_instance.secrets_service_get_secret_settings(id, auto_check_in=auto_check_in, auto_checkout=auto_checkout, auto_comment=auto_comment, force_check_in=force_check_in, secret_path=secret_path)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_get_secret_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **auto_check_in** | **bool**| Automatically check in a secret after finding or updating. | [optional]
 **auto_checkout** | **bool**| Automatically check out secret before finding or updating. | [optional]
 **auto_comment** | **bool, date, datetime, dict, float, int, list, str, none_type**| Leave a comment when checking in or out. | [optional]
 **force_check_in** | **bool**| If secret is checked out, then force a check in. | [optional]
 **secret_path** | **bool, date, datetime, dict, float, int, list, str, none_type**| A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. | [optional]

### Return type

[**SecretDetailSettingsModel**](SecretDetailSettingsModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Settings |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_get_secret_ssh_proxy_info**
> SecretSshProxyModel secrets_service_get_secret_ssh_proxy_info()

Get SSH Proxy Information

Get SSH Proxy Information

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.secret_ssh_proxy_model import SecretSshProxyModel
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_proxy_args import SecretProxyArgs
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    auto_check_in = True # bool | Automatically check in a secret after finding or updating. (optional)
    auto_checkout = True # bool | Automatically check out secret before finding or updating. (optional)
    auto_comment = None # bool, date, datetime, dict, float, int, list, str, none_type | Leave a comment when checking in or out. (optional)
    force_check_in = True # bool | If secret is checked out, then force a check in. (optional)
    secret_proxy_args = SecretProxyArgs(
        launcher_type=None,
        machine=None,
        secret_id=None,
        site_id=None,
    ) # SecretProxyArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get SSH Proxy Information
        api_response = api_instance.secrets_service_get_secret_ssh_proxy_info(auto_check_in=auto_check_in, auto_checkout=auto_checkout, auto_comment=auto_comment, force_check_in=force_check_in, secret_proxy_args=secret_proxy_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_get_secret_ssh_proxy_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_check_in** | **bool**| Automatically check in a secret after finding or updating. | [optional]
 **auto_checkout** | **bool**| Automatically check out secret before finding or updating. | [optional]
 **auto_comment** | **bool, date, datetime, dict, float, int, list, str, none_type**| Leave a comment when checking in or out. | [optional]
 **force_check_in** | **bool**| If secret is checked out, then force a check in. | [optional]
 **secret_proxy_args** | [**SecretProxyArgs**](SecretProxyArgs.md)| args | [optional]

### Return type

[**SecretSshProxyModel**](SecretSshProxyModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SSH Proxy Information |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_get_secret_ssh_terminal_details**
> SecretSshTerminalModel secrets_service_get_secret_ssh_terminal_details()

Get SSH Terminal Details

Get SSH Terminal Details

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_ssh_terminal_args import SecretSshTerminalArgs
from plugins.model.secret_ssh_terminal_model import SecretSshTerminalModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    auto_check_in = True # bool | Automatically check in a secret after finding or updating. (optional)
    auto_checkout = True # bool | Automatically check out secret before finding or updating. (optional)
    auto_comment = None # bool, date, datetime, dict, float, int, list, str, none_type | Leave a comment when checking in or out. (optional)
    force_check_in = True # bool | If secret is checked out, then force a check in. (optional)
    secret_ssh_terminal_args = SecretSshTerminalArgs(
        secret_id=None,
    ) # SecretSshTerminalArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get SSH Terminal Details
        api_response = api_instance.secrets_service_get_secret_ssh_terminal_details(auto_check_in=auto_check_in, auto_checkout=auto_checkout, auto_comment=auto_comment, force_check_in=force_check_in, secret_ssh_terminal_args=secret_ssh_terminal_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_get_secret_ssh_terminal_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_check_in** | **bool**| Automatically check in a secret after finding or updating. | [optional]
 **auto_checkout** | **bool**| Automatically check out secret before finding or updating. | [optional]
 **auto_comment** | **bool, date, datetime, dict, float, int, list, str, none_type**| Leave a comment when checking in or out. | [optional]
 **force_check_in** | **bool**| If secret is checked out, then force a check in. | [optional]
 **secret_ssh_terminal_args** | [**SecretSshTerminalArgs**](SecretSshTerminalArgs.md)| args | [optional]

### Return type

[**SecretSshTerminalModel**](SecretSshTerminalModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SSH Terminal Details |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_get_secret_state**
> SecretDetailStateViewModel secrets_service_get_secret_state(id)

Get Secret State

Retrieve state about a Secret such as whether it requires approval, doublelock, checkout, or other restricted actions to be performed before calling the get the secret.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_detail_state_view_model import SecretDetailStateViewModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    auto_check_in = True # bool | Automatically check in a secret after finding or updating. (optional)
    auto_checkout = True # bool | Automatically check out secret before finding or updating. (optional)
    auto_comment = None # bool, date, datetime, dict, float, int, list, str, none_type | Leave a comment when checking in or out. (optional)
    force_check_in = True # bool | If secret is checked out, then force a check in. (optional)
    secret_path = None # bool, date, datetime, dict, float, int, list, str, none_type | A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Secret State
        api_response = api_instance.secrets_service_get_secret_state(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_get_secret_state: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Secret State
        api_response = api_instance.secrets_service_get_secret_state(id, auto_check_in=auto_check_in, auto_checkout=auto_checkout, auto_comment=auto_comment, force_check_in=force_check_in, secret_path=secret_path)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_get_secret_state: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **auto_check_in** | **bool**| Automatically check in a secret after finding or updating. | [optional]
 **auto_checkout** | **bool**| Automatically check out secret before finding or updating. | [optional]
 **auto_comment** | **bool, date, datetime, dict, float, int, list, str, none_type**| Leave a comment when checking in or out. | [optional]
 **force_check_in** | **bool**| If secret is checked out, then force a check in. | [optional]
 **secret_path** | **bool, date, datetime, dict, float, int, list, str, none_type**| A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. | [optional]

### Return type

[**SecretDetailStateViewModel**](SecretDetailStateViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Detail State View Model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_get_secret_v2**
> SecretModelV2 secrets_service_get_secret_v2(id)

Get Secret

Get a single secret by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.secret_model_v2 import SecretModelV2
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret ID
    include_inactive = True # bool | Whether to include inactive secrets in the results (optional)
    no_auto_checkout = True # bool | Don't check out the secret if needed (optional)
    auto_check_in = True # bool | Automatically check in a secret after finding or updating. (optional)
    auto_checkout = True # bool | Automatically check out secret before finding or updating. (optional)
    auto_comment = None # bool, date, datetime, dict, float, int, list, str, none_type | Leave a comment when checking in or out. (optional)
    force_check_in = True # bool | If secret is checked out, then force a check in. (optional)
    secret_path = None # bool, date, datetime, dict, float, int, list, str, none_type | A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Secret
        api_response = api_instance.secrets_service_get_secret_v2(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_get_secret_v2: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Secret
        api_response = api_instance.secrets_service_get_secret_v2(id, include_inactive=include_inactive, no_auto_checkout=no_auto_checkout, auto_check_in=auto_check_in, auto_checkout=auto_checkout, auto_comment=auto_comment, force_check_in=force_check_in, secret_path=secret_path)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_get_secret_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret ID |
 **include_inactive** | **bool**| Whether to include inactive secrets in the results | [optional]
 **no_auto_checkout** | **bool**| Don&#39;t check out the secret if needed | [optional]
 **auto_check_in** | **bool**| Automatically check in a secret after finding or updating. | [optional]
 **auto_checkout** | **bool**| Automatically check out secret before finding or updating. | [optional]
 **auto_comment** | **bool, date, datetime, dict, float, int, list, str, none_type**| Leave a comment when checking in or out. | [optional]
 **force_check_in** | **bool**| If secret is checked out, then force a check in. | [optional]
 **secret_path** | **bool, date, datetime, dict, float, int, list, str, none_type**| A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. | [optional]

### Return type

[**SecretModelV2**](SecretModelV2.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_get_ssh_restricted_commands**
> SecretDetailRestrictedSshCommandViewModel secrets_service_get_ssh_restricted_commands(id)

Get SSH Command Restrictions on a Secret

Gets the SSH command restrictions for a Secret

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_detail_restricted_ssh_command_view_model import SecretDetailRestrictedSshCommandViewModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    auto_check_in = True # bool | Automatically check in a secret after finding or updating. (optional)
    auto_checkout = True # bool | Automatically check out secret before finding or updating. (optional)
    auto_comment = None # bool, date, datetime, dict, float, int, list, str, none_type | Leave a comment when checking in or out. (optional)
    force_check_in = True # bool | If secret is checked out, then force a check in. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get SSH Command Restrictions on a Secret
        api_response = api_instance.secrets_service_get_ssh_restricted_commands(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_get_ssh_restricted_commands: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get SSH Command Restrictions on a Secret
        api_response = api_instance.secrets_service_get_ssh_restricted_commands(id, auto_check_in=auto_check_in, auto_checkout=auto_checkout, auto_comment=auto_comment, force_check_in=force_check_in)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_get_ssh_restricted_commands: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **auto_check_in** | **bool**| Automatically check in a secret after finding or updating. | [optional]
 **auto_checkout** | **bool**| Automatically check out secret before finding or updating. | [optional]
 **auto_comment** | **bool, date, datetime, dict, float, int, list, str, none_type**| Leave a comment when checking in or out. | [optional]
 **force_check_in** | **bool**| If secret is checked out, then force a check in. | [optional]

### Return type

[**SecretDetailRestrictedSshCommandViewModel**](SecretDetailRestrictedSshCommandViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of restricted commands |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_get_summary**
> SecretSummary secrets_service_get_summary(id)

Get Secret Summary

Get the summary for a secret

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_summary import SecretSummary
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret ID
    auto_check_in = True # bool | Automatically check in a secret after finding or updating. (optional)
    auto_checkout = True # bool | Automatically check out secret before finding or updating. (optional)
    auto_comment = None # bool, date, datetime, dict, float, int, list, str, none_type | Leave a comment when checking in or out. (optional)
    force_check_in = True # bool | If secret is checked out, then force a check in. (optional)
    secret_path = None # bool, date, datetime, dict, float, int, list, str, none_type | A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Secret Summary
        api_response = api_instance.secrets_service_get_summary(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_get_summary: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Secret Summary
        api_response = api_instance.secrets_service_get_summary(id, auto_check_in=auto_check_in, auto_checkout=auto_checkout, auto_comment=auto_comment, force_check_in=force_check_in, secret_path=secret_path)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_get_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret ID |
 **auto_check_in** | **bool**| Automatically check in a secret after finding or updating. | [optional]
 **auto_checkout** | **bool**| Automatically check out secret before finding or updating. | [optional]
 **auto_comment** | **bool, date, datetime, dict, float, int, list, str, none_type**| Leave a comment when checking in or out. | [optional]
 **force_check_in** | **bool**| If secret is checked out, then force a check in. | [optional]
 **secret_path** | **bool, date, datetime, dict, float, int, list, str, none_type**| A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. | [optional]

### Return type

[**SecretSummary**](SecretSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret summary object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_put_field**
> bool, date, datetime, dict, float, int, list, str, none_type secrets_service_put_field(id, slug)

Update Secret Field

Update a secret data field

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.secret_item_update_args import SecretItemUpdateArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret ID
    slug = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret field name
    auto_check_in = True # bool | Automatically check in a secret after finding or updating. (optional)
    auto_checkout = True # bool | Automatically check out secret before finding or updating. (optional)
    auto_comment = None # bool, date, datetime, dict, float, int, list, str, none_type | Leave a comment when checking in or out. (optional)
    force_check_in = True # bool | If secret is checked out, then force a check in. (optional)
    secret_path = None # bool, date, datetime, dict, float, int, list, str, none_type | A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. (optional)
    secret_item_update_args = SecretItemUpdateArgs(
        comment=None,
        double_lock_password=None,
null,
        file_attachment=None,
        file_name=None,
        force_check_in=True,
        include_inactive=True,
        new_password=None,
        no_auto_checkout=True,
        ticket_number=None,
        ticket_system_id=None,
        value=None,
    ) # SecretItemUpdateArgs | Secret options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Secret Field
        api_response = api_instance.secrets_service_put_field(id, slug)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_put_field: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Secret Field
        api_response = api_instance.secrets_service_put_field(id, slug, auto_check_in=auto_check_in, auto_checkout=auto_checkout, auto_comment=auto_comment, force_check_in=force_check_in, secret_path=secret_path, secret_item_update_args=secret_item_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_put_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret ID |
 **slug** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret field name |
 **auto_check_in** | **bool**| Automatically check in a secret after finding or updating. | [optional]
 **auto_checkout** | **bool**| Automatically check out secret before finding or updating. | [optional]
 **auto_comment** | **bool, date, datetime, dict, float, int, list, str, none_type**| Leave a comment when checking in or out. | [optional]
 **force_check_in** | **bool**| If secret is checked out, then force a check in. | [optional]
 **secret_path** | **bool, date, datetime, dict, float, int, list, str, none_type**| A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. | [optional]
 **secret_item_update_args** | [**SecretItemUpdateArgs**](SecretItemUpdateArgs.md)| Secret options | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated value, or &#39;true&#39; if the field is a file attachment |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_restricted_field**
> bool, date, datetime, dict, float, int, list, str, none_type secrets_service_restricted_field(id, slug)

Get Restricted Secret Field

Get a restricted secret data field

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.secret_restricted_args import SecretRestrictedArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret ID
    slug = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret field name
    auto_check_in = True # bool | Automatically check in a secret after finding or updating. (optional)
    auto_checkout = True # bool | Automatically check out secret before finding or updating. (optional)
    auto_comment = None # bool, date, datetime, dict, float, int, list, str, none_type | Leave a comment when checking in or out. (optional)
    force_check_in = True # bool | If secret is checked out, then force a check in. (optional)
    secret_path = None # bool, date, datetime, dict, float, int, list, str, none_type | A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. (optional)
    secret_restricted_args = SecretRestrictedArgs(
        comment=None,
        double_lock_password=None,
        force_check_in=True,
        include_inactive=True,
        new_password=None,
        no_auto_checkout=True,
        ticket_number=None,
        ticket_system_id=None,
    ) # SecretRestrictedArgs | Secret options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Restricted Secret Field
        api_response = api_instance.secrets_service_restricted_field(id, slug)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_restricted_field: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Restricted Secret Field
        api_response = api_instance.secrets_service_restricted_field(id, slug, auto_check_in=auto_check_in, auto_checkout=auto_checkout, auto_comment=auto_comment, force_check_in=force_check_in, secret_path=secret_path, secret_restricted_args=secret_restricted_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_restricted_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret ID |
 **slug** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret field name |
 **auto_check_in** | **bool**| Automatically check in a secret after finding or updating. | [optional]
 **auto_checkout** | **bool**| Automatically check out secret before finding or updating. | [optional]
 **auto_comment** | **bool, date, datetime, dict, float, int, list, str, none_type**| Leave a comment when checking in or out. | [optional]
 **force_check_in** | **bool**| If secret is checked out, then force a check in. | [optional]
 **secret_path** | **bool, date, datetime, dict, float, int, list, str, none_type**| A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. | [optional]
 **secret_restricted_args** | [**SecretRestrictedArgs**](SecretRestrictedArgs.md)| Secret options | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/octet-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret field value. If the field is a file attachment, the content type will be &#x60;application/octet-stream&#x60; and the response body will be the file contents. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_run_heart_beat**
> SecretSummary secrets_service_run_heart_beat(id)

Run Secret Heartbeat

Check if secret is still valid

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_summary import SecretSummary
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret ID
    auto_check_in = True # bool | Automatically check in a secret after finding or updating. (optional)
    auto_checkout = True # bool | Automatically check out secret before finding or updating. (optional)
    auto_comment = None # bool, date, datetime, dict, float, int, list, str, none_type | Leave a comment when checking in or out. (optional)
    force_check_in = True # bool | If secret is checked out, then force a check in. (optional)
    secret_path = None # bool, date, datetime, dict, float, int, list, str, none_type | A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Run Secret Heartbeat
        api_response = api_instance.secrets_service_run_heart_beat(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_run_heart_beat: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Run Secret Heartbeat
        api_response = api_instance.secrets_service_run_heart_beat(id, auto_check_in=auto_check_in, auto_checkout=auto_checkout, auto_comment=auto_comment, force_check_in=force_check_in, secret_path=secret_path)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_run_heart_beat: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret ID |
 **auto_check_in** | **bool**| Automatically check in a secret after finding or updating. | [optional]
 **auto_checkout** | **bool**| Automatically check out secret before finding or updating. | [optional]
 **auto_comment** | **bool, date, datetime, dict, float, int, list, str, none_type**| Leave a comment when checking in or out. | [optional]
 **force_check_in** | **bool**| If secret is checked out, then force a check in. | [optional]
 **secret_path** | **bool, date, datetime, dict, float, int, list, str, none_type**| A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. | [optional]

### Return type

[**SecretSummary**](SecretSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret summary object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_search_secret_lookup**
> PagingOfSecretLookup secrets_service_search_secret_lookup()

Lookup Secrets with Search

Search, filter, sort, and page secrets, returning only secret ID and name

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.paging_of_secret_lookup import PagingOfSecretLookup
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    filter_allow_double_locks = True # bool | Whether to allow DoubleLocks as part of the search. True by default. (optional)
    filter_do_not_calculate_total = True # bool | Whether to return the total number of secrets matching the filters. False by default. If false, the total can be retrieved separately by calling /v1/secrets/search-total with the same arguments used in the search. (optional)
    filter_double_lock_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Only include Secrets with this DoubleLock ID assigned in the search results. (optional)
    filter_extended_fields = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | An array of names of Secret Template fields to return.  Only exposed fields can be returned. (optional)
    filter_extended_type_id = None # bool, date, datetime, dict, float, int, list, str, none_type | If not null, return only secrets matching the specified extended mapping type as defined on the secret’s template. (optional)
    filter_folder_id = None # bool, date, datetime, dict, float, int, list, str, none_type | If not null, returns only secrets within the specified folder. (optional)
    filter_heartbeat_status = None # bool, date, datetime, dict, float, int, list, str, none_type | If not null, returns only secrets with a certain heartbeat status. (optional)
    filter_include_active = True # bool | Whether to include active secrets in results (when excluded equals true). (optional)
    filter_include_inactive = True # bool | Whether to include inactive secrets in results. (optional)
    filter_include_restricted = True # bool | Whether to include restricted secrets in results. Restricted secrets are secrets that are DoubleLocked, require approval, or require a comment to view. (optional)
    filter_include_sub_folders = True # bool | Whether to include secrets in subfolders of the specified folder. (optional)
    filter_is_exact_match = True # bool | Whether to do an exact match of the search text or a partial match. If an exact match, the entire secret name, field value, or list option in a list field must match the search text. (optional)
    filter_only_rpc_enabled = True # bool | Whether to only include secrets whose template has Remote Password Changing enabled. (optional)
    filter_only_shared_with_me = True # bool | When true only Secrets where you are not the owner and the Secret was shared explicitly with your user id will be returned. (optional)
    filter_password_type_ids = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | If not null, returns only secrets matching the specified password types. (optional)
    filter_permission_required = None # bool, date, datetime, dict, float, int, list, str, none_type | Specify whether to filter by List, View, Edit, or Owner permission. Default is List. (optional)
    filter_scope = None # bool, date, datetime, dict, float, int, list, str, none_type | Specify whether to search All, Recent, or Favorites (optional)
    filter_search_field = None # bool, date, datetime, dict, float, int, list, str, none_type | If set, restricts the search to only match secrets where the value of the field specified by name contains the search text. (optional)
    filter_search_field_slug = None # bool, date, datetime, dict, float, int, list, str, none_type | If set, restricts the search to only match secrets where the value of the field specified by the slug name contains the search text. This will override SearchField. (optional)
    filter_search_text = None # bool, date, datetime, dict, float, int, list, str, none_type | The text to match in the secret name, field value, or list field contents. (optional)
    filter_secret_template_id = None # bool, date, datetime, dict, float, int, list, str, none_type | If not null, returns only secrets matching the specified template. (optional)
    filter_site_id = None # bool, date, datetime, dict, float, int, list, str, none_type | If not null, returns only secrets within a the specified site. (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Lookup Secrets with Search
        api_response = api_instance.secrets_service_search_secret_lookup(filter_allow_double_locks=filter_allow_double_locks, filter_do_not_calculate_total=filter_do_not_calculate_total, filter_double_lock_id=filter_double_lock_id, filter_extended_fields=filter_extended_fields, filter_extended_type_id=filter_extended_type_id, filter_folder_id=filter_folder_id, filter_heartbeat_status=filter_heartbeat_status, filter_include_active=filter_include_active, filter_include_inactive=filter_include_inactive, filter_include_restricted=filter_include_restricted, filter_include_sub_folders=filter_include_sub_folders, filter_is_exact_match=filter_is_exact_match, filter_only_rpc_enabled=filter_only_rpc_enabled, filter_only_shared_with_me=filter_only_shared_with_me, filter_password_type_ids=filter_password_type_ids, filter_permission_required=filter_permission_required, filter_scope=filter_scope, filter_search_field=filter_search_field, filter_search_field_slug=filter_search_field_slug, filter_search_text=filter_search_text, filter_secret_template_id=filter_secret_template_id, filter_site_id=filter_site_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_search_secret_lookup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_allow_double_locks** | **bool**| Whether to allow DoubleLocks as part of the search. True by default. | [optional]
 **filter_do_not_calculate_total** | **bool**| Whether to return the total number of secrets matching the filters. False by default. If false, the total can be retrieved separately by calling /v1/secrets/search-total with the same arguments used in the search. | [optional]
 **filter_double_lock_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Only include Secrets with this DoubleLock ID assigned in the search results. | [optional]
 **filter_extended_fields** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| An array of names of Secret Template fields to return.  Only exposed fields can be returned. | [optional]
 **filter_extended_type_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| If not null, return only secrets matching the specified extended mapping type as defined on the secret’s template. | [optional]
 **filter_folder_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| If not null, returns only secrets within the specified folder. | [optional]
 **filter_heartbeat_status** | **bool, date, datetime, dict, float, int, list, str, none_type**| If not null, returns only secrets with a certain heartbeat status. | [optional]
 **filter_include_active** | **bool**| Whether to include active secrets in results (when excluded equals true). | [optional]
 **filter_include_inactive** | **bool**| Whether to include inactive secrets in results. | [optional]
 **filter_include_restricted** | **bool**| Whether to include restricted secrets in results. Restricted secrets are secrets that are DoubleLocked, require approval, or require a comment to view. | [optional]
 **filter_include_sub_folders** | **bool**| Whether to include secrets in subfolders of the specified folder. | [optional]
 **filter_is_exact_match** | **bool**| Whether to do an exact match of the search text or a partial match. If an exact match, the entire secret name, field value, or list option in a list field must match the search text. | [optional]
 **filter_only_rpc_enabled** | **bool**| Whether to only include secrets whose template has Remote Password Changing enabled. | [optional]
 **filter_only_shared_with_me** | **bool**| When true only Secrets where you are not the owner and the Secret was shared explicitly with your user id will be returned. | [optional]
 **filter_password_type_ids** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| If not null, returns only secrets matching the specified password types. | [optional]
 **filter_permission_required** | **bool, date, datetime, dict, float, int, list, str, none_type**| Specify whether to filter by List, View, Edit, or Owner permission. Default is List. | [optional]
 **filter_scope** | **bool, date, datetime, dict, float, int, list, str, none_type**| Specify whether to search All, Recent, or Favorites | [optional]
 **filter_search_field** | **bool, date, datetime, dict, float, int, list, str, none_type**| If set, restricts the search to only match secrets where the value of the field specified by name contains the search text. | [optional]
 **filter_search_field_slug** | **bool, date, datetime, dict, float, int, list, str, none_type**| If set, restricts the search to only match secrets where the value of the field specified by the slug name contains the search text. This will override SearchField. | [optional]
 **filter_search_text** | **bool, date, datetime, dict, float, int, list, str, none_type**| The text to match in the secret name, field value, or list field contents. | [optional]
 **filter_secret_template_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| If not null, returns only secrets matching the specified template. | [optional]
 **filter_site_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| If not null, returns only secrets within a the specified site. | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfSecretLookup**](PagingOfSecretLookup.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_search_total_v2**
> bool, date, datetime, dict, float, int, list, str, none_type secrets_service_search_total_v2()

Get Secret Search Total

Gets the total number of secrets matching the secret search filter

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    filter_allow_double_locks = True # bool | Whether to allow DoubleLocks as part of the search. True by default. (optional)
    filter_do_not_calculate_total = True # bool | Whether to return the total number of secrets matching the filters. False by default. If false, the total can be retrieved separately by calling /v1/secrets/search-total with the same arguments used in the search. (optional)
    filter_double_lock_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Only include Secrets with this DoubleLock ID assigned in the search results. (optional)
    filter_extended_fields = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | An array of names of Secret Template fields to return.  Only exposed fields can be returned. (optional)
    filter_extended_type_id = None # bool, date, datetime, dict, float, int, list, str, none_type | If not null, return only secrets matching the specified extended mapping type as defined on the secret’s template. (optional)
    filter_folder_id = None # bool, date, datetime, dict, float, int, list, str, none_type | If not null, returns only secrets within the specified folder. (optional)
    filter_has_launcher = True # bool | Whether to only return secrets with or without launchers. If null, returns secrets regardless of whether they have launchers. (optional)
    filter_heartbeat_status = None # bool, date, datetime, dict, float, int, list, str, none_type | If not null, returns only secrets with a certain heartbeat status. (optional)
    filter_include_active = True # bool | Whether to include active secrets in results (when excluded equals true). (optional)
    filter_include_inactive = True # bool | Whether to include inactive secrets in results. (optional)
    filter_include_restricted = True # bool | Whether to include restricted secrets in results. Restricted secrets are secrets that are DoubleLocked, require approval, or require a comment to view. (optional)
    filter_include_sub_folders = True # bool | Whether to include secrets in subfolders of the specified folder. (optional)
    filter_is_exact_match = True # bool | Whether to do an exact match of the search text or a partial match. If an exact match, the entire secret name, field value, or list option in a list field must match the search text. (optional)
    filter_only_rpc_enabled = True # bool | Whether to only include secrets whose template has Remote Password Changing enabled. (optional)
    filter_only_shared_with_me = True # bool | When true only Secrets where you are not the owner and the Secret was shared explicitly with your user id will be returned. (optional)
    filter_password_type_ids = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | If not null, returns only secrets matching the specified password types. (optional)
    filter_permission_required = None # bool, date, datetime, dict, float, int, list, str, none_type | Specify whether to filter by List, View, Edit, or Owner permission. Default is List. (optional)
    filter_scope = None # bool, date, datetime, dict, float, int, list, str, none_type | Specify whether to search All, Recent, or Favorites (optional)
    filter_search_field = None # bool, date, datetime, dict, float, int, list, str, none_type | If set, restricts the search to only match secrets where the value of the field specified by name contains the search text. (optional)
    filter_search_field_slug = None # bool, date, datetime, dict, float, int, list, str, none_type | If set, restricts the search to only match secrets where the value of the field specified by the slug name contains the search text. This will override SearchField. (optional)
    filter_search_text = None # bool, date, datetime, dict, float, int, list, str, none_type | The text to match in the secret name, field value, or list field contents. (optional)
    filter_secret_template_ids = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | If not null or empty, returns only secrets matching the specified templates. (optional)
    filter_site_id = None # bool, date, datetime, dict, float, int, list, str, none_type | If not null, returns only secrets within a the specified site. (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Secret Search Total
        api_response = api_instance.secrets_service_search_total_v2(filter_allow_double_locks=filter_allow_double_locks, filter_do_not_calculate_total=filter_do_not_calculate_total, filter_double_lock_id=filter_double_lock_id, filter_extended_fields=filter_extended_fields, filter_extended_type_id=filter_extended_type_id, filter_folder_id=filter_folder_id, filter_has_launcher=filter_has_launcher, filter_heartbeat_status=filter_heartbeat_status, filter_include_active=filter_include_active, filter_include_inactive=filter_include_inactive, filter_include_restricted=filter_include_restricted, filter_include_sub_folders=filter_include_sub_folders, filter_is_exact_match=filter_is_exact_match, filter_only_rpc_enabled=filter_only_rpc_enabled, filter_only_shared_with_me=filter_only_shared_with_me, filter_password_type_ids=filter_password_type_ids, filter_permission_required=filter_permission_required, filter_scope=filter_scope, filter_search_field=filter_search_field, filter_search_field_slug=filter_search_field_slug, filter_search_text=filter_search_text, filter_secret_template_ids=filter_secret_template_ids, filter_site_id=filter_site_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_search_total_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_allow_double_locks** | **bool**| Whether to allow DoubleLocks as part of the search. True by default. | [optional]
 **filter_do_not_calculate_total** | **bool**| Whether to return the total number of secrets matching the filters. False by default. If false, the total can be retrieved separately by calling /v1/secrets/search-total with the same arguments used in the search. | [optional]
 **filter_double_lock_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Only include Secrets with this DoubleLock ID assigned in the search results. | [optional]
 **filter_extended_fields** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| An array of names of Secret Template fields to return.  Only exposed fields can be returned. | [optional]
 **filter_extended_type_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| If not null, return only secrets matching the specified extended mapping type as defined on the secret’s template. | [optional]
 **filter_folder_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| If not null, returns only secrets within the specified folder. | [optional]
 **filter_has_launcher** | **bool**| Whether to only return secrets with or without launchers. If null, returns secrets regardless of whether they have launchers. | [optional]
 **filter_heartbeat_status** | **bool, date, datetime, dict, float, int, list, str, none_type**| If not null, returns only secrets with a certain heartbeat status. | [optional]
 **filter_include_active** | **bool**| Whether to include active secrets in results (when excluded equals true). | [optional]
 **filter_include_inactive** | **bool**| Whether to include inactive secrets in results. | [optional]
 **filter_include_restricted** | **bool**| Whether to include restricted secrets in results. Restricted secrets are secrets that are DoubleLocked, require approval, or require a comment to view. | [optional]
 **filter_include_sub_folders** | **bool**| Whether to include secrets in subfolders of the specified folder. | [optional]
 **filter_is_exact_match** | **bool**| Whether to do an exact match of the search text or a partial match. If an exact match, the entire secret name, field value, or list option in a list field must match the search text. | [optional]
 **filter_only_rpc_enabled** | **bool**| Whether to only include secrets whose template has Remote Password Changing enabled. | [optional]
 **filter_only_shared_with_me** | **bool**| When true only Secrets where you are not the owner and the Secret was shared explicitly with your user id will be returned. | [optional]
 **filter_password_type_ids** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| If not null, returns only secrets matching the specified password types. | [optional]
 **filter_permission_required** | **bool, date, datetime, dict, float, int, list, str, none_type**| Specify whether to filter by List, View, Edit, or Owner permission. Default is List. | [optional]
 **filter_scope** | **bool, date, datetime, dict, float, int, list, str, none_type**| Specify whether to search All, Recent, or Favorites | [optional]
 **filter_search_field** | **bool, date, datetime, dict, float, int, list, str, none_type**| If set, restricts the search to only match secrets where the value of the field specified by name contains the search text. | [optional]
 **filter_search_field_slug** | **bool, date, datetime, dict, float, int, list, str, none_type**| If set, restricts the search to only match secrets where the value of the field specified by the slug name contains the search text. This will override SearchField. | [optional]
 **filter_search_text** | **bool, date, datetime, dict, float, int, list, str, none_type**| The text to match in the secret name, field value, or list field contents. | [optional]
 **filter_secret_template_ids** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| If not null or empty, returns only secrets matching the specified templates. | [optional]
 **filter_site_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| If not null, returns only secrets within a the specified site. | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Integer number of matching secrets |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_search_v2**
> PagingOfSecretSummary secrets_service_search_v2()

Search Secrets

Search, filter, sort, and page secrets

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.paging_of_secret_summary import PagingOfSecretSummary
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    filter_allow_double_locks = True # bool | Whether to allow DoubleLocks as part of the search. True by default. (optional)
    filter_do_not_calculate_total = True # bool | Whether to return the total number of secrets matching the filters. False by default. If false, the total can be retrieved separately by calling /v1/secrets/search-total with the same arguments used in the search. (optional)
    filter_double_lock_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Only include Secrets with this DoubleLock ID assigned in the search results. (optional)
    filter_extended_fields = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | An array of names of Secret Template fields to return.  Only exposed fields can be returned. (optional)
    filter_extended_type_id = None # bool, date, datetime, dict, float, int, list, str, none_type | If not null, return only secrets matching the specified extended mapping type as defined on the secret’s template. (optional)
    filter_folder_id = None # bool, date, datetime, dict, float, int, list, str, none_type | If not null, returns only secrets within the specified folder. (optional)
    filter_has_launcher = True # bool | Whether to only return secrets with or without launchers. If null, returns secrets regardless of whether they have launchers. (optional)
    filter_heartbeat_status = None # bool, date, datetime, dict, float, int, list, str, none_type | If not null, returns only secrets with a certain heartbeat status. (optional)
    filter_include_active = True # bool | Whether to include active secrets in results (when excluded equals true). (optional)
    filter_include_inactive = True # bool | Whether to include inactive secrets in results. (optional)
    filter_include_restricted = True # bool | Whether to include restricted secrets in results. Restricted secrets are secrets that are DoubleLocked, require approval, or require a comment to view. (optional)
    filter_include_sub_folders = True # bool | Whether to include secrets in subfolders of the specified folder. (optional)
    filter_is_exact_match = True # bool | Whether to do an exact match of the search text or a partial match. If an exact match, the entire secret name, field value, or list option in a list field must match the search text. (optional)
    filter_only_rpc_enabled = True # bool | Whether to only include secrets whose template has Remote Password Changing enabled. (optional)
    filter_only_shared_with_me = True # bool | When true only Secrets where you are not the owner and the Secret was shared explicitly with your user id will be returned. (optional)
    filter_password_type_ids = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | If not null, returns only secrets matching the specified password types. (optional)
    filter_permission_required = None # bool, date, datetime, dict, float, int, list, str, none_type | Specify whether to filter by List, View, Edit, or Owner permission. Default is List. (optional)
    filter_scope = None # bool, date, datetime, dict, float, int, list, str, none_type | Specify whether to search All, Recent, or Favorites (optional)
    filter_search_field = None # bool, date, datetime, dict, float, int, list, str, none_type | If set, restricts the search to only match secrets where the value of the field specified by name contains the search text. (optional)
    filter_search_field_slug = None # bool, date, datetime, dict, float, int, list, str, none_type | If set, restricts the search to only match secrets where the value of the field specified by the slug name contains the search text. This will override SearchField. (optional)
    filter_search_text = None # bool, date, datetime, dict, float, int, list, str, none_type | The text to match in the secret name, field value, or list field contents. (optional)
    filter_secret_template_ids = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | If not null or empty, returns only secrets matching the specified templates. (optional)
    filter_site_id = None # bool, date, datetime, dict, float, int, list, str, none_type | If not null, returns only secrets within a the specified site. (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Secrets
        api_response = api_instance.secrets_service_search_v2(filter_allow_double_locks=filter_allow_double_locks, filter_do_not_calculate_total=filter_do_not_calculate_total, filter_double_lock_id=filter_double_lock_id, filter_extended_fields=filter_extended_fields, filter_extended_type_id=filter_extended_type_id, filter_folder_id=filter_folder_id, filter_has_launcher=filter_has_launcher, filter_heartbeat_status=filter_heartbeat_status, filter_include_active=filter_include_active, filter_include_inactive=filter_include_inactive, filter_include_restricted=filter_include_restricted, filter_include_sub_folders=filter_include_sub_folders, filter_is_exact_match=filter_is_exact_match, filter_only_rpc_enabled=filter_only_rpc_enabled, filter_only_shared_with_me=filter_only_shared_with_me, filter_password_type_ids=filter_password_type_ids, filter_permission_required=filter_permission_required, filter_scope=filter_scope, filter_search_field=filter_search_field, filter_search_field_slug=filter_search_field_slug, filter_search_text=filter_search_text, filter_secret_template_ids=filter_secret_template_ids, filter_site_id=filter_site_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_search_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_allow_double_locks** | **bool**| Whether to allow DoubleLocks as part of the search. True by default. | [optional]
 **filter_do_not_calculate_total** | **bool**| Whether to return the total number of secrets matching the filters. False by default. If false, the total can be retrieved separately by calling /v1/secrets/search-total with the same arguments used in the search. | [optional]
 **filter_double_lock_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Only include Secrets with this DoubleLock ID assigned in the search results. | [optional]
 **filter_extended_fields** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| An array of names of Secret Template fields to return.  Only exposed fields can be returned. | [optional]
 **filter_extended_type_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| If not null, return only secrets matching the specified extended mapping type as defined on the secret’s template. | [optional]
 **filter_folder_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| If not null, returns only secrets within the specified folder. | [optional]
 **filter_has_launcher** | **bool**| Whether to only return secrets with or without launchers. If null, returns secrets regardless of whether they have launchers. | [optional]
 **filter_heartbeat_status** | **bool, date, datetime, dict, float, int, list, str, none_type**| If not null, returns only secrets with a certain heartbeat status. | [optional]
 **filter_include_active** | **bool**| Whether to include active secrets in results (when excluded equals true). | [optional]
 **filter_include_inactive** | **bool**| Whether to include inactive secrets in results. | [optional]
 **filter_include_restricted** | **bool**| Whether to include restricted secrets in results. Restricted secrets are secrets that are DoubleLocked, require approval, or require a comment to view. | [optional]
 **filter_include_sub_folders** | **bool**| Whether to include secrets in subfolders of the specified folder. | [optional]
 **filter_is_exact_match** | **bool**| Whether to do an exact match of the search text or a partial match. If an exact match, the entire secret name, field value, or list option in a list field must match the search text. | [optional]
 **filter_only_rpc_enabled** | **bool**| Whether to only include secrets whose template has Remote Password Changing enabled. | [optional]
 **filter_only_shared_with_me** | **bool**| When true only Secrets where you are not the owner and the Secret was shared explicitly with your user id will be returned. | [optional]
 **filter_password_type_ids** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| If not null, returns only secrets matching the specified password types. | [optional]
 **filter_permission_required** | **bool, date, datetime, dict, float, int, list, str, none_type**| Specify whether to filter by List, View, Edit, or Owner permission. Default is List. | [optional]
 **filter_scope** | **bool, date, datetime, dict, float, int, list, str, none_type**| Specify whether to search All, Recent, or Favorites | [optional]
 **filter_search_field** | **bool, date, datetime, dict, float, int, list, str, none_type**| If set, restricts the search to only match secrets where the value of the field specified by name contains the search text. | [optional]
 **filter_search_field_slug** | **bool, date, datetime, dict, float, int, list, str, none_type**| If set, restricts the search to only match secrets where the value of the field specified by the slug name contains the search text. This will override SearchField. | [optional]
 **filter_search_text** | **bool, date, datetime, dict, float, int, list, str, none_type**| The text to match in the secret name, field value, or list field contents. | [optional]
 **filter_secret_template_ids** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| If not null or empty, returns only secrets matching the specified templates. | [optional]
 **filter_site_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| If not null, returns only secrets within a the specified site. | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfSecretSummary**](PagingOfSecretSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_stop_password_change**
> SecretDetailStopPasswordResultModel secrets_service_stop_password_change(id)

Attempt to stop a password change

Attempt to stop a password change

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.secret_detail_stop_password_result_model import SecretDetailStopPasswordResultModel
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    secret_path = None # bool, date, datetime, dict, float, int, list, str, none_type | A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Attempt to stop a password change
        api_response = api_instance.secrets_service_stop_password_change(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_stop_password_change: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Attempt to stop a password change
        api_response = api_instance.secrets_service_stop_password_change(id, secret_path=secret_path)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_stop_password_change: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **secret_path** | **bool, date, datetime, dict, float, int, list, str, none_type**| A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. | [optional]

### Return type

[**SecretDetailStopPasswordResultModel**](SecretDetailStopPasswordResultModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Attempt to stop a password change |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_stub**
> SecretModel secrets_service_stub(secret_template_id)

Get Secret Stub

Return the default values for a new secret

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_model import SecretModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    secret_template_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret template ID
    folder_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Containing folder ID. May be null unless secrets are required to be in folders. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Secret Stub
        api_response = api_instance.secrets_service_stub(secret_template_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_stub: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Secret Stub
        api_response = api_instance.secrets_service_stub(secret_template_id, folder_id=folder_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_stub: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_template_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret template ID |
 **folder_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Containing folder ID. May be null unless secrets are required to be in folders. | [optional]

### Return type

[**SecretModel**](SecretModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_undelete_secret**
> SecretDetailGeneralModel secrets_service_undelete_secret(id)

Undelete a Secret

Undelete a Secret

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.secret_detail_general_model import SecretDetailGeneralModel
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    secret_path = None # bool, date, datetime, dict, float, int, list, str, none_type | A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Undelete a Secret
        api_response = api_instance.secrets_service_undelete_secret(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_undelete_secret: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Undelete a Secret
        api_response = api_instance.secrets_service_undelete_secret(id, secret_path=secret_path)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_undelete_secret: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **secret_path** | **bool, date, datetime, dict, float, int, list, str, none_type**| A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. | [optional]

### Return type

[**SecretDetailGeneralModel**](SecretDetailGeneralModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_undelete_secret_v2**
> SecretDetailGeneralModel secrets_service_undelete_secret_v2(id)

Undelete a Secret

Undelete a Secret

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.secret_detail_general_model import SecretDetailGeneralModel
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    secret_path = None # bool, date, datetime, dict, float, int, list, str, none_type | A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Undelete a Secret
        api_response = api_instance.secrets_service_undelete_secret_v2(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_undelete_secret_v2: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Undelete a Secret
        api_response = api_instance.secrets_service_undelete_secret_v2(id, secret_path=secret_path)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_undelete_secret_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **secret_path** | **bool, date, datetime, dict, float, int, list, str, none_type**| A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. | [optional]

### Return type

[**SecretDetailGeneralModel**](SecretDetailGeneralModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_update_email**
> SecretDetailSettingsModel secrets_service_update_email(id)

Update User Secret Email Settings

Update User Secret Email Settings

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.secret_detail_settings_model import SecretDetailSettingsModel
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_detail_update_email_args import SecretDetailUpdateEmailArgs
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    auto_check_in = True # bool | Automatically check in a secret after finding or updating. (optional)
    auto_checkout = True # bool | Automatically check out secret before finding or updating. (optional)
    auto_comment = None # bool, date, datetime, dict, float, int, list, str, none_type | Leave a comment when checking in or out. (optional)
    force_check_in = True # bool | If secret is checked out, then force a check in. (optional)
    secret_path = None # bool, date, datetime, dict, float, int, list, str, none_type | A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. (optional)
    secret_detail_update_email_args = SecretDetailUpdateEmailArgs(
        data=SecretDetailEmailUpdateModel(
            send_email_when_changed=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            send_email_when_heartbeat_fails=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            send_email_when_viewed=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
        ),
    ) # SecretDetailUpdateEmailArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update User Secret Email Settings
        api_response = api_instance.secrets_service_update_email(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_update_email: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update User Secret Email Settings
        api_response = api_instance.secrets_service_update_email(id, auto_check_in=auto_check_in, auto_checkout=auto_checkout, auto_comment=auto_comment, force_check_in=force_check_in, secret_path=secret_path, secret_detail_update_email_args=secret_detail_update_email_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_update_email: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **auto_check_in** | **bool**| Automatically check in a secret after finding or updating. | [optional]
 **auto_checkout** | **bool**| Automatically check out secret before finding or updating. | [optional]
 **auto_comment** | **bool, date, datetime, dict, float, int, list, str, none_type**| Leave a comment when checking in or out. | [optional]
 **force_check_in** | **bool**| If secret is checked out, then force a check in. | [optional]
 **secret_path** | **bool, date, datetime, dict, float, int, list, str, none_type**| A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. | [optional]
 **secret_detail_update_email_args** | [**SecretDetailUpdateEmailArgs**](SecretDetailUpdateEmailArgs.md)| args | [optional]

### Return type

[**SecretDetailSettingsModel**](SecretDetailSettingsModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SecretDetailSettingsViewModel |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_update_email_v2**
> SecretDetailSettingsModel secrets_service_update_email_v2(id)

Update User Secret Email Settings

Update User Secret Email Settings

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.secret_detail_settings_model import SecretDetailSettingsModel
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_detail_update_email_args import SecretDetailUpdateEmailArgs
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    auto_check_in = True # bool | Automatically check in a secret after finding or updating. (optional)
    auto_checkout = True # bool | Automatically check out secret before finding or updating. (optional)
    auto_comment = None # bool, date, datetime, dict, float, int, list, str, none_type | Leave a comment when checking in or out. (optional)
    force_check_in = True # bool | If secret is checked out, then force a check in. (optional)
    secret_path = None # bool, date, datetime, dict, float, int, list, str, none_type | A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. (optional)
    secret_detail_update_email_args = SecretDetailUpdateEmailArgs(
        data=SecretDetailEmailUpdateModel(
            send_email_when_changed=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            send_email_when_heartbeat_fails=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            send_email_when_viewed=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
        ),
    ) # SecretDetailUpdateEmailArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update User Secret Email Settings
        api_response = api_instance.secrets_service_update_email_v2(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_update_email_v2: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update User Secret Email Settings
        api_response = api_instance.secrets_service_update_email_v2(id, auto_check_in=auto_check_in, auto_checkout=auto_checkout, auto_comment=auto_comment, force_check_in=force_check_in, secret_path=secret_path, secret_detail_update_email_args=secret_detail_update_email_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_update_email_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **auto_check_in** | **bool**| Automatically check in a secret after finding or updating. | [optional]
 **auto_checkout** | **bool**| Automatically check out secret before finding or updating. | [optional]
 **auto_comment** | **bool, date, datetime, dict, float, int, list, str, none_type**| Leave a comment when checking in or out. | [optional]
 **force_check_in** | **bool**| If secret is checked out, then force a check in. | [optional]
 **secret_path** | **bool, date, datetime, dict, float, int, list, str, none_type**| A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. | [optional]
 **secret_detail_update_email_args** | [**SecretDetailUpdateEmailArgs**](SecretDetailUpdateEmailArgs.md)| args | [optional]

### Return type

[**SecretDetailSettingsModel**](SecretDetailSettingsModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SecretDetailSettingsViewModel |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_update_expiration**
> SecretDetailSettingsModel secrets_service_update_expiration(id)

Update a Secret expiration

Update a Secret expiration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.secret_detail_settings_model import SecretDetailSettingsModel
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_detail_update_expiration_args import SecretDetailUpdateExpirationArgs
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    auto_check_in = True # bool | Automatically check in a secret after finding or updating. (optional)
    auto_checkout = True # bool | Automatically check out secret before finding or updating. (optional)
    auto_comment = None # bool, date, datetime, dict, float, int, list, str, none_type | Leave a comment when checking in or out. (optional)
    force_check_in = True # bool | If secret is checked out, then force a check in. (optional)
    secret_path = None # bool, date, datetime, dict, float, int, list, str, none_type | A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. (optional)
    secret_detail_update_expiration_args = SecretDetailUpdateExpirationArgs(
        data=SecretDetailExpirationUpdateModel(
            expiration_date=UpdateFieldValueOfOptionalDateTime(
                dirty=True,
                value=None,
            ),
            expiration_day_interval=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=None,
            ),
            expiration_type=UpdateFieldValueOfSecretDetailExpirationUpdateType(
                dirty=True,
                value=SecretDetailExpirationUpdateType("Template"),
            ),
        ),
    ) # SecretDetailUpdateExpirationArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a Secret expiration
        api_response = api_instance.secrets_service_update_expiration(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_update_expiration: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Secret expiration
        api_response = api_instance.secrets_service_update_expiration(id, auto_check_in=auto_check_in, auto_checkout=auto_checkout, auto_comment=auto_comment, force_check_in=force_check_in, secret_path=secret_path, secret_detail_update_expiration_args=secret_detail_update_expiration_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_update_expiration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **auto_check_in** | **bool**| Automatically check in a secret after finding or updating. | [optional]
 **auto_checkout** | **bool**| Automatically check out secret before finding or updating. | [optional]
 **auto_comment** | **bool, date, datetime, dict, float, int, list, str, none_type**| Leave a comment when checking in or out. | [optional]
 **force_check_in** | **bool**| If secret is checked out, then force a check in. | [optional]
 **secret_path** | **bool, date, datetime, dict, float, int, list, str, none_type**| A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. | [optional]
 **secret_detail_update_expiration_args** | [**SecretDetailUpdateExpirationArgs**](SecretDetailUpdateExpirationArgs.md)| args | [optional]

### Return type

[**SecretDetailSettingsModel**](SecretDetailSettingsModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated secret settings |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_update_general**
> SecretDetailGeneralViewModel secrets_service_update_general(id)

Update Secret General Information

Update Secret General Information

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.secret_detail_general_view_model import SecretDetailGeneralViewModel
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_detail_update_general_args import SecretDetailUpdateGeneralArgs
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    auto_check_in = True # bool | Automatically check in a secret after finding or updating. (optional)
    auto_checkout = True # bool | Automatically check out secret before finding or updating. (optional)
    auto_comment = None # bool, date, datetime, dict, float, int, list, str, none_type | Leave a comment when checking in or out. (optional)
    force_check_in = True # bool | If secret is checked out, then force a check in. (optional)
    secret_path = None # bool, date, datetime, dict, float, int, list, str, none_type | A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. (optional)
    secret_detail_update_general_args = SecretDetailUpdateGeneralArgs(
        data=SecretDetailGeneralUpdateModel(
            active=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            enable_inherit_secret_policy=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            folder=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=None,
            ),
            generate_ssh_keys=True,
            heartbeat_enabled=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            is_out_of_sync=UpdateFieldValueOfOptionalBoolean(
                dirty=True,
                value=True,
            ),
            name=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            secret_fields=[
                UpdateTemplateFieldOfString(
                    dirty=True,
                    slug=None,
                    value=None,
                ),
            ],
            secret_policy=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=None,
            ),
            site=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=None,
            ),
            template=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=None,
            ),
        ),
    ) # SecretDetailUpdateGeneralArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Secret General Information
        api_response = api_instance.secrets_service_update_general(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_update_general: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Secret General Information
        api_response = api_instance.secrets_service_update_general(id, auto_check_in=auto_check_in, auto_checkout=auto_checkout, auto_comment=auto_comment, force_check_in=force_check_in, secret_path=secret_path, secret_detail_update_general_args=secret_detail_update_general_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_update_general: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **auto_check_in** | **bool**| Automatically check in a secret after finding or updating. | [optional]
 **auto_checkout** | **bool**| Automatically check out secret before finding or updating. | [optional]
 **auto_comment** | **bool, date, datetime, dict, float, int, list, str, none_type**| Leave a comment when checking in or out. | [optional]
 **force_check_in** | **bool**| If secret is checked out, then force a check in. | [optional]
 **secret_path** | **bool, date, datetime, dict, float, int, list, str, none_type**| A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. | [optional]
 **secret_detail_update_general_args** | [**SecretDetailUpdateGeneralArgs**](SecretDetailUpdateGeneralArgs.md)| args | [optional]

### Return type

[**SecretDetailGeneralViewModel**](SecretDetailGeneralViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret General Information |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_update_general_v2**
> SecretDetailGeneralModel secrets_service_update_general_v2(id)

Update Secret General Information

Update Secret General Information

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.secret_detail_general_model import SecretDetailGeneralModel
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_detail_update_general_args import SecretDetailUpdateGeneralArgs
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    auto_check_in = True # bool | Automatically check in a secret after finding or updating. (optional)
    auto_checkout = True # bool | Automatically check out secret before finding or updating. (optional)
    auto_comment = None # bool, date, datetime, dict, float, int, list, str, none_type | Leave a comment when checking in or out. (optional)
    force_check_in = True # bool | If secret is checked out, then force a check in. (optional)
    secret_path = None # bool, date, datetime, dict, float, int, list, str, none_type | A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. (optional)
    secret_detail_update_general_args = SecretDetailUpdateGeneralArgs(
        data=SecretDetailGeneralUpdateModel(
            active=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            enable_inherit_secret_policy=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            folder=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=None,
            ),
            generate_ssh_keys=True,
            heartbeat_enabled=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            is_out_of_sync=UpdateFieldValueOfOptionalBoolean(
                dirty=True,
                value=True,
            ),
            name=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            secret_fields=[
                UpdateTemplateFieldOfString(
                    dirty=True,
                    slug=None,
                    value=None,
                ),
            ],
            secret_policy=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=None,
            ),
            site=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=None,
            ),
            template=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=None,
            ),
        ),
    ) # SecretDetailUpdateGeneralArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Secret General Information
        api_response = api_instance.secrets_service_update_general_v2(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_update_general_v2: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Secret General Information
        api_response = api_instance.secrets_service_update_general_v2(id, auto_check_in=auto_check_in, auto_checkout=auto_checkout, auto_comment=auto_comment, force_check_in=force_check_in, secret_path=secret_path, secret_detail_update_general_args=secret_detail_update_general_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_update_general_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **auto_check_in** | **bool**| Automatically check in a secret after finding or updating. | [optional]
 **auto_checkout** | **bool**| Automatically check out secret before finding or updating. | [optional]
 **auto_comment** | **bool, date, datetime, dict, float, int, list, str, none_type**| Leave a comment when checking in or out. | [optional]
 **force_check_in** | **bool**| If secret is checked out, then force a check in. | [optional]
 **secret_path** | **bool, date, datetime, dict, float, int, list, str, none_type**| A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. | [optional]
 **secret_detail_update_general_args** | [**SecretDetailUpdateGeneralArgs**](SecretDetailUpdateGeneralArgs.md)| args | [optional]

### Return type

[**SecretDetailGeneralModel**](SecretDetailGeneralModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret General Information |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_update_jumpbox_route_selection**
> JumpboxRouteSummaryModel secrets_service_update_jumpbox_route_selection(secret_id)

Update Jumpbox Route Selection

Update Jumpbox Route Selection

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.secret_detail_jumpbox_update_args import SecretDetailJumpboxUpdateArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.jumpbox_route_summary_model import JumpboxRouteSummaryModel
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    secret_id = None # bool, date, datetime, dict, float, int, list, str, none_type | secretId
    secret_detail_jumpbox_update_args = SecretDetailJumpboxUpdateArgs(
        jumpbox_route_id=None,
    ) # SecretDetailJumpboxUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Jumpbox Route Selection
        api_response = api_instance.secrets_service_update_jumpbox_route_selection(secret_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_update_jumpbox_route_selection: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Jumpbox Route Selection
        api_response = api_instance.secrets_service_update_jumpbox_route_selection(secret_id, secret_detail_jumpbox_update_args=secret_detail_jumpbox_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_update_jumpbox_route_selection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| secretId |
 **secret_detail_jumpbox_update_args** | [**SecretDetailJumpboxUpdateArgs**](SecretDetailJumpboxUpdateArgs.md)| args | [optional]

### Return type

[**JumpboxRouteSummaryModel**](JumpboxRouteSummaryModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Jumpbox Route View Model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_update_list_field_list_definitions**
> PagingOfCategorizedListSummary secrets_service_update_list_field_list_definitions(id, slug)

Update Secret List Field List Data

Updates the lists associated to a secret list data field

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_categorized_list_summary import PagingOfCategorizedListSummary
from plugins.model.secret_list_field_list_args import SecretListFieldListArgs
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret ID
    slug = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret field name
    auto_check_in = True # bool | Automatically check in a secret after finding or updating. (optional)
    auto_checkout = True # bool | Automatically check out secret before finding or updating. (optional)
    auto_comment = None # bool, date, datetime, dict, float, int, list, str, none_type | Leave a comment when checking in or out. (optional)
    force_check_in = True # bool | If secret is checked out, then force a check in. (optional)
    secret_list_field_list_args = SecretListFieldListArgs(
        list_guids=[
            None,
        ],
    ) # SecretListFieldListArgs | Secret options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Secret List Field List Data
        api_response = api_instance.secrets_service_update_list_field_list_definitions(id, slug)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_update_list_field_list_definitions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Secret List Field List Data
        api_response = api_instance.secrets_service_update_list_field_list_definitions(id, slug, auto_check_in=auto_check_in, auto_checkout=auto_checkout, auto_comment=auto_comment, force_check_in=force_check_in, secret_list_field_list_args=secret_list_field_list_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_update_list_field_list_definitions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret ID |
 **slug** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret field name |
 **auto_check_in** | **bool**| Automatically check in a secret after finding or updating. | [optional]
 **auto_checkout** | **bool**| Automatically check out secret before finding or updating. | [optional]
 **auto_comment** | **bool, date, datetime, dict, float, int, list, str, none_type**| Leave a comment when checking in or out. | [optional]
 **force_check_in** | **bool**| If secret is checked out, then force a check in. | [optional]
 **secret_list_field_list_args** | [**SecretListFieldListArgs**](SecretListFieldListArgs.md)| Secret options | [optional]

### Return type

[**PagingOfCategorizedListSummary**](PagingOfCategorizedListSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Combined summary of all lists assigned to the secret field. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_update_rpc_script_secrets**
> SecretDetailRpcModel secrets_service_update_rpc_script_secrets(id)

Update which Secrets are available for RPC scripts

Update which Secrets are available for RPC scripts

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.secret_detail_update_rpc_script_secrets_args import SecretDetailUpdateRpcScriptSecretsArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_detail_rpc_model import SecretDetailRpcModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    auto_check_in = True # bool | Automatically check in a secret after finding or updating. (optional)
    auto_checkout = True # bool | Automatically check out secret before finding or updating. (optional)
    auto_comment = None # bool, date, datetime, dict, float, int, list, str, none_type | Leave a comment when checking in or out. (optional)
    force_check_in = True # bool | If secret is checked out, then force a check in. (optional)
    secret_path = None # bool, date, datetime, dict, float, int, list, str, none_type | A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. (optional)
    secret_detail_update_rpc_script_secrets_args = SecretDetailUpdateRpcScriptSecretsArgs(
        data=SecretDetailRpcScriptSecretsUpdateModel(
            reset_secret_ids=UpdateFieldValueOfInt32Array(
                dirty=True,
                value=[
                    None,
                ],
            ),
        ),
    ) # SecretDetailUpdateRpcScriptSecretsArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update which Secrets are available for RPC scripts
        api_response = api_instance.secrets_service_update_rpc_script_secrets(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_update_rpc_script_secrets: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update which Secrets are available for RPC scripts
        api_response = api_instance.secrets_service_update_rpc_script_secrets(id, auto_check_in=auto_check_in, auto_checkout=auto_checkout, auto_comment=auto_comment, force_check_in=force_check_in, secret_path=secret_path, secret_detail_update_rpc_script_secrets_args=secret_detail_update_rpc_script_secrets_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_update_rpc_script_secrets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **auto_check_in** | **bool**| Automatically check in a secret after finding or updating. | [optional]
 **auto_checkout** | **bool**| Automatically check out secret before finding or updating. | [optional]
 **auto_comment** | **bool, date, datetime, dict, float, int, list, str, none_type**| Leave a comment when checking in or out. | [optional]
 **force_check_in** | **bool**| If secret is checked out, then force a check in. | [optional]
 **secret_path** | **bool, date, datetime, dict, float, int, list, str, none_type**| A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. | [optional]
 **secret_detail_update_rpc_script_secrets_args** | [**SecretDetailUpdateRpcScriptSecretsArgs**](SecretDetailUpdateRpcScriptSecretsArgs.md)| args | [optional]

### Return type

[**SecretDetailRpcModel**](SecretDetailRpcModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SecretDetailRpcViewModel |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_update_rpc_script_secrets_v2**
> SecretDetailRpcModel secrets_service_update_rpc_script_secrets_v2(id)

Update which Secrets are available for RPC scripts

Update which Secrets are available for RPC scripts

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.secret_detail_update_rpc_script_secrets_args import SecretDetailUpdateRpcScriptSecretsArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_detail_rpc_model import SecretDetailRpcModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    auto_check_in = True # bool | Automatically check in a secret after finding or updating. (optional)
    auto_checkout = True # bool | Automatically check out secret before finding or updating. (optional)
    auto_comment = None # bool, date, datetime, dict, float, int, list, str, none_type | Leave a comment when checking in or out. (optional)
    force_check_in = True # bool | If secret is checked out, then force a check in. (optional)
    secret_path = None # bool, date, datetime, dict, float, int, list, str, none_type | A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. (optional)
    secret_detail_update_rpc_script_secrets_args = SecretDetailUpdateRpcScriptSecretsArgs(
        data=SecretDetailRpcScriptSecretsUpdateModel(
            reset_secret_ids=UpdateFieldValueOfInt32Array(
                dirty=True,
                value=[
                    None,
                ],
            ),
        ),
    ) # SecretDetailUpdateRpcScriptSecretsArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update which Secrets are available for RPC scripts
        api_response = api_instance.secrets_service_update_rpc_script_secrets_v2(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_update_rpc_script_secrets_v2: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update which Secrets are available for RPC scripts
        api_response = api_instance.secrets_service_update_rpc_script_secrets_v2(id, auto_check_in=auto_check_in, auto_checkout=auto_checkout, auto_comment=auto_comment, force_check_in=force_check_in, secret_path=secret_path, secret_detail_update_rpc_script_secrets_args=secret_detail_update_rpc_script_secrets_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_update_rpc_script_secrets_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **auto_check_in** | **bool**| Automatically check in a secret after finding or updating. | [optional]
 **auto_checkout** | **bool**| Automatically check out secret before finding or updating. | [optional]
 **auto_comment** | **bool, date, datetime, dict, float, int, list, str, none_type**| Leave a comment when checking in or out. | [optional]
 **force_check_in** | **bool**| If secret is checked out, then force a check in. | [optional]
 **secret_path** | **bool, date, datetime, dict, float, int, list, str, none_type**| A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. | [optional]
 **secret_detail_update_rpc_script_secrets_args** | [**SecretDetailUpdateRpcScriptSecretsArgs**](SecretDetailUpdateRpcScriptSecretsArgs.md)| args | [optional]

### Return type

[**SecretDetailRpcModel**](SecretDetailRpcModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SecretDetailRpcViewModel |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_update_secret**
> SecretModel secrets_service_update_secret(id)

Update Secret

Update a single secret by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.secret_update_args import SecretUpdateArgs
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_model import SecretModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret ID
    auto_check_in = True # bool | Automatically check in a secret after finding or updating. (optional)
    auto_checkout = True # bool | Automatically check out secret before finding or updating. (optional)
    auto_comment = None # bool, date, datetime, dict, float, int, list, str, none_type | Leave a comment when checking in or out. (optional)
    force_check_in = True # bool | If secret is checked out, then force a check in. (optional)
    secret_path = None # bool, date, datetime, dict, float, int, list, str, none_type | A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. (optional)
    secret_update_args = SecretUpdateArgs(
        access_request_workflow_map_id=None,
        active=True,
        auto_change_enabled=True,
        auto_change_next_password=None,
        check_out_change_password_enabled=True,
        check_out_enabled=True,
        check_out_interval_minutes=None,
        comment=None,
        double_lock_password=None,
        enable_inherit_permissions=True,
        enable_inherit_secret_policy=True,
        folder_id=None,
        force_check_in=True,
        id=None,
        include_inactive=True,
        items=[
            RestSecretItem(
                field_description=None,
                field_id=None,
                field_name=None,
                file_attachment_id=None,
                filename=None,
                is_file=True,
                is_list=True,
                is_notes=True,
                is_password=True,
                item_id=None,
                item_value=None,
                list_type=SecretFieldListType("{}"),
                slug=None,
            ),
        ],
        launcher_connect_as_secret_id=None,
        name=None,
        new_password=None,
        no_auto_checkout=True,
        password_type_web_script_id=None,
        proxy_enabled=True,
        requires_comment=True,
        secret_policy_id=None,
        session_recording_enabled=True,
        site_id=None,
        ssh_key_args=SshKeyArgs(
            generate_passphrase=True,
            generate_ssh_keys=True,
        ),
        ticket_number=None,
        ticket_system_id=None,
        web_launcher_requires_incognito_mode=True,
    ) # SecretUpdateArgs | Secret update options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Secret
        api_response = api_instance.secrets_service_update_secret(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_update_secret: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Secret
        api_response = api_instance.secrets_service_update_secret(id, auto_check_in=auto_check_in, auto_checkout=auto_checkout, auto_comment=auto_comment, force_check_in=force_check_in, secret_path=secret_path, secret_update_args=secret_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_update_secret: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret ID |
 **auto_check_in** | **bool**| Automatically check in a secret after finding or updating. | [optional]
 **auto_checkout** | **bool**| Automatically check out secret before finding or updating. | [optional]
 **auto_comment** | **bool, date, datetime, dict, float, int, list, str, none_type**| Leave a comment when checking in or out. | [optional]
 **force_check_in** | **bool**| If secret is checked out, then force a check in. | [optional]
 **secret_path** | **bool, date, datetime, dict, float, int, list, str, none_type**| A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. | [optional]
 **secret_update_args** | [**SecretUpdateArgs**](SecretUpdateArgs.md)| Secret update options | [optional]

### Return type

[**SecretModel**](SecretModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_update_secret_session**
> SecretLauncherSessionActionResult secrets_service_update_secret_session()

Update Secret Launcher Sessions

Update or Terminate Secret Launcher Sessions

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.secret_launcher_session_args import SecretLauncherSessionArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.secret_launcher_session_action_result import SecretLauncherSessionActionResult
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    secret_launcher_session_args = SecretLauncherSessionArgs(
        action=SessionActions("Terminate"),
        message=None,
        secret_id=None,
        secret_session_id=None,
    ) # SecretLauncherSessionArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Secret Launcher Sessions
        api_response = api_instance.secrets_service_update_secret_session(secret_launcher_session_args=secret_launcher_session_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_update_secret_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_launcher_session_args** | [**SecretLauncherSessionArgs**](SecretLauncherSessionArgs.md)| args | [optional]

### Return type

[**SecretLauncherSessionActionResult**](SecretLauncherSessionActionResult.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of the update Secret Launcher Session Request |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_update_security**
> SecretDetailSecurityViewModel secrets_service_update_security(id)

Update Secret Security General Options

Update Secret Security General Options

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.secret_detail_update_security_general_args import SecretDetailUpdateSecurityGeneralArgs
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_detail_security_view_model import SecretDetailSecurityViewModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    auto_check_in = True # bool | Automatically check in a secret after finding or updating. (optional)
    auto_checkout = True # bool | Automatically check out secret before finding or updating. (optional)
    auto_comment = None # bool, date, datetime, dict, float, int, list, str, none_type | Leave a comment when checking in or out. (optional)
    force_check_in = True # bool | If secret is checked out, then force a check in. (optional)
    secret_path = None # bool, date, datetime, dict, float, int, list, str, none_type | A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. (optional)
    secret_detail_update_security_general_args = SecretDetailUpdateSecurityGeneralArgs(
        data=SecretDetailSecurityGeneralUpdateModel(
            double_lock_id=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            enable_double_lock=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            hide_launcher_password=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            proxy_enabled=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            requires_comment=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            session_recording_enabled=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            web_launcher_requires_incognito_mode=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
        ),
    ) # SecretDetailUpdateSecurityGeneralArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Secret Security General Options
        api_response = api_instance.secrets_service_update_security(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_update_security: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Secret Security General Options
        api_response = api_instance.secrets_service_update_security(id, auto_check_in=auto_check_in, auto_checkout=auto_checkout, auto_comment=auto_comment, force_check_in=force_check_in, secret_path=secret_path, secret_detail_update_security_general_args=secret_detail_update_security_general_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_update_security: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **auto_check_in** | **bool**| Automatically check in a secret after finding or updating. | [optional]
 **auto_checkout** | **bool**| Automatically check out secret before finding or updating. | [optional]
 **auto_comment** | **bool, date, datetime, dict, float, int, list, str, none_type**| Leave a comment when checking in or out. | [optional]
 **force_check_in** | **bool**| If secret is checked out, then force a check in. | [optional]
 **secret_path** | **bool, date, datetime, dict, float, int, list, str, none_type**| A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. | [optional]
 **secret_detail_update_security_general_args** | [**SecretDetailUpdateSecurityGeneralArgs**](SecretDetailUpdateSecurityGeneralArgs.md)| args | [optional]

### Return type

[**SecretDetailSecurityViewModel**](SecretDetailSecurityViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SecretDetailSecurityViewModel |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_update_security_approval_v3**
> SecretSecurityUpdateResponse secrets_service_update_security_approval_v3(id)

Update Secret Security Approval Options

Update Secret Security Approval Options

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.secret_detail_update_security_approval_args import SecretDetailUpdateSecurityApprovalArgs
from plugins.model.secret_security_update_response import SecretSecurityUpdateResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    auto_check_in = True # bool | Automatically check in a secret after finding or updating. (optional)
    auto_checkout = True # bool | Automatically check out secret before finding or updating. (optional)
    auto_comment = None # bool, date, datetime, dict, float, int, list, str, none_type | Leave a comment when checking in or out. (optional)
    force_check_in = True # bool | If secret is checked out, then force a check in. (optional)
    secret_path = None # bool, date, datetime, dict, float, int, list, str, none_type | A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. (optional)
    secret_detail_update_security_approval_args = SecretDetailUpdateSecurityApprovalArgs(
        data=SecretDetailSecurityApprovalUpdateModel(
            approvers=UpdateFieldValueOfInt32Array(
                dirty=True,
                value=[
                    None,
                ],
            ),
            require_approval_type=UpdateFieldValueOfOptionalSecretDetailApprovalType(
                dirty=True,
                value=None,
            ),
            workflow_template_id=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
        ),
    ) # SecretDetailUpdateSecurityApprovalArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Secret Security Approval Options
        api_response = api_instance.secrets_service_update_security_approval_v3(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_update_security_approval_v3: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Secret Security Approval Options
        api_response = api_instance.secrets_service_update_security_approval_v3(id, auto_check_in=auto_check_in, auto_checkout=auto_checkout, auto_comment=auto_comment, force_check_in=force_check_in, secret_path=secret_path, secret_detail_update_security_approval_args=secret_detail_update_security_approval_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_update_security_approval_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **auto_check_in** | **bool**| Automatically check in a secret after finding or updating. | [optional]
 **auto_checkout** | **bool**| Automatically check out secret before finding or updating. | [optional]
 **auto_comment** | **bool, date, datetime, dict, float, int, list, str, none_type**| Leave a comment when checking in or out. | [optional]
 **force_check_in** | **bool**| If secret is checked out, then force a check in. | [optional]
 **secret_path** | **bool, date, datetime, dict, float, int, list, str, none_type**| A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. | [optional]
 **secret_detail_update_security_approval_args** | [**SecretDetailUpdateSecurityApprovalArgs**](SecretDetailUpdateSecurityApprovalArgs.md)| args | [optional]

### Return type

[**SecretSecurityUpdateResponse**](SecretSecurityUpdateResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SecretDetailSecurityViewModel |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_update_security_checkout_v3**
> SecretSecurityUpdateResponse secrets_service_update_security_checkout_v3(id)

Update Secret Security Checkout Options

Update Secret Security Checkout Options

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.secret_security_update_response import SecretSecurityUpdateResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_detail_update_security_checkout_args import SecretDetailUpdateSecurityCheckoutArgs
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    auto_check_in = True # bool | Automatically check in a secret after finding or updating. (optional)
    auto_checkout = True # bool | Automatically check out secret before finding or updating. (optional)
    auto_comment = None # bool, date, datetime, dict, float, int, list, str, none_type | Leave a comment when checking in or out. (optional)
    force_check_in = True # bool | If secret is checked out, then force a check in. (optional)
    secret_path = None # bool, date, datetime, dict, float, int, list, str, none_type | A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. (optional)
    secret_detail_update_security_checkout_args = SecretDetailUpdateSecurityCheckoutArgs(
        data=SecretDetailSecurityCheckoutUpdateModel(
            check_out_change_password_enabled=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            check_out_enabled=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            check_out_interval_minutes=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=None,
            ),
        ),
    ) # SecretDetailUpdateSecurityCheckoutArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Secret Security Checkout Options
        api_response = api_instance.secrets_service_update_security_checkout_v3(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_update_security_checkout_v3: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Secret Security Checkout Options
        api_response = api_instance.secrets_service_update_security_checkout_v3(id, auto_check_in=auto_check_in, auto_checkout=auto_checkout, auto_comment=auto_comment, force_check_in=force_check_in, secret_path=secret_path, secret_detail_update_security_checkout_args=secret_detail_update_security_checkout_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_update_security_checkout_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **auto_check_in** | **bool**| Automatically check in a secret after finding or updating. | [optional]
 **auto_checkout** | **bool**| Automatically check out secret before finding or updating. | [optional]
 **auto_comment** | **bool, date, datetime, dict, float, int, list, str, none_type**| Leave a comment when checking in or out. | [optional]
 **force_check_in** | **bool**| If secret is checked out, then force a check in. | [optional]
 **secret_path** | **bool, date, datetime, dict, float, int, list, str, none_type**| A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. | [optional]
 **secret_detail_update_security_checkout_args** | [**SecretDetailUpdateSecurityCheckoutArgs**](SecretDetailUpdateSecurityCheckoutArgs.md)| args | [optional]

### Return type

[**SecretSecurityUpdateResponse**](SecretSecurityUpdateResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A model with the updated security options if available and a success code |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_update_security_v2**
> SecretDetailSecurityModel secrets_service_update_security_v2(id)

Update Secret Security General Options

Update Secret Security General Options

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.secret_detail_update_security_general_args import SecretDetailUpdateSecurityGeneralArgs
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_detail_security_model import SecretDetailSecurityModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    auto_check_in = True # bool | Automatically check in a secret after finding or updating. (optional)
    auto_checkout = True # bool | Automatically check out secret before finding or updating. (optional)
    auto_comment = None # bool, date, datetime, dict, float, int, list, str, none_type | Leave a comment when checking in or out. (optional)
    force_check_in = True # bool | If secret is checked out, then force a check in. (optional)
    secret_path = None # bool, date, datetime, dict, float, int, list, str, none_type | A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. (optional)
    secret_detail_update_security_general_args = SecretDetailUpdateSecurityGeneralArgs(
        data=SecretDetailSecurityGeneralUpdateModel(
            double_lock_id=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            enable_double_lock=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            hide_launcher_password=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            proxy_enabled=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            requires_comment=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            session_recording_enabled=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            web_launcher_requires_incognito_mode=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
        ),
    ) # SecretDetailUpdateSecurityGeneralArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Secret Security General Options
        api_response = api_instance.secrets_service_update_security_v2(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_update_security_v2: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Secret Security General Options
        api_response = api_instance.secrets_service_update_security_v2(id, auto_check_in=auto_check_in, auto_checkout=auto_checkout, auto_comment=auto_comment, force_check_in=force_check_in, secret_path=secret_path, secret_detail_update_security_general_args=secret_detail_update_security_general_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_update_security_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **auto_check_in** | **bool**| Automatically check in a secret after finding or updating. | [optional]
 **auto_checkout** | **bool**| Automatically check out secret before finding or updating. | [optional]
 **auto_comment** | **bool, date, datetime, dict, float, int, list, str, none_type**| Leave a comment when checking in or out. | [optional]
 **force_check_in** | **bool**| If secret is checked out, then force a check in. | [optional]
 **secret_path** | **bool, date, datetime, dict, float, int, list, str, none_type**| A full path including folder and secret name can be passed as a query string parameter when the secret ID is set to 0.  This will lookup the secret ID by path. | [optional]
 **secret_detail_update_security_general_args** | [**SecretDetailUpdateSecurityGeneralArgs**](SecretDetailUpdateSecurityGeneralArgs.md)| args | [optional]

### Return type

[**SecretDetailSecurityModel**](SecretDetailSecurityModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SecretDetailSecurityViewModel |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_service_update_ssh_restricted_commands**
> bool secrets_service_update_ssh_restricted_commands(secret_id)

Update Restricted SSH Commands on a Secret

Update the restricted SSH commands configured on a Secret

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secrets_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_detail_ssh_restricted_command_update_args import SecretDetailSshRestrictedCommandUpdateArgs
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
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
with plugins.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = secrets_api.SecretsApi(api_client)
    secret_id = None # bool, date, datetime, dict, float, int, list, str, none_type | secretId
    auto_check_in = True # bool | Automatically check in a secret after finding or updating. (optional)
    auto_checkout = True # bool | Automatically check out secret before finding or updating. (optional)
    auto_comment = None # bool, date, datetime, dict, float, int, list, str, none_type | Leave a comment when checking in or out. (optional)
    force_check_in = True # bool | If secret is checked out, then force a check in. (optional)
    secret_detail_ssh_restricted_command_update_args = SecretDetailSshRestrictedCommandUpdateArgs(
        data=SecretDetailSshCommandUpdateData(
            allow_owners_unrestricted_commands=True,
            command_restriction_type=CommandRestrictionType("{}"),
            restrict_ssh_commands=True,
            ssh_command_blocklists=[
                SecretDetailRestrictedSshCommandBlocklistPermissionUpdateModel(
                    role_permission_id=None,
                    ssh_command_blocklist_id=None,
                ),
            ],
            ssh_command_menus=[
                SecretDetailRestrictedSshCommandMenuPermissionUpdateModel(
                    group_id=None,
                    ssh_command_menu_id=None,
                ),
            ],
        ),
    ) # SecretDetailSshRestrictedCommandUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Restricted SSH Commands on a Secret
        api_response = api_instance.secrets_service_update_ssh_restricted_commands(secret_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_update_ssh_restricted_commands: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Restricted SSH Commands on a Secret
        api_response = api_instance.secrets_service_update_ssh_restricted_commands(secret_id, auto_check_in=auto_check_in, auto_checkout=auto_checkout, auto_comment=auto_comment, force_check_in=force_check_in, secret_detail_ssh_restricted_command_update_args=secret_detail_ssh_restricted_command_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretsApi->secrets_service_update_ssh_restricted_commands: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| secretId |
 **auto_check_in** | **bool**| Automatically check in a secret after finding or updating. | [optional]
 **auto_checkout** | **bool**| Automatically check out secret before finding or updating. | [optional]
 **auto_comment** | **bool, date, datetime, dict, float, int, list, str, none_type**| Leave a comment when checking in or out. | [optional]
 **force_check_in** | **bool**| If secret is checked out, then force a check in. | [optional]
 **secret_detail_ssh_restricted_command_update_args** | [**SecretDetailSshRestrictedCommandUpdateArgs**](SecretDetailSshRestrictedCommandUpdateArgs.md)| args | [optional]

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
**200** | Success / Fail |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

