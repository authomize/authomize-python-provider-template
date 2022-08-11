# plugins.BulkUserOperationsApi

All URIs are relative to *https://integrations.secretservercloud.com//api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_user_operations_service_add_users_to_group**](BulkUserOperationsApi.md#bulk_user_operations_service_add_users_to_group) | **POST** /v1/bulk-user-operations/add-to-group | Add To Group
[**bulk_user_operations_service_add_users_to_team**](BulkUserOperationsApi.md#bulk_user_operations_service_add_users_to_team) | **POST** /v1/bulk-user-operations/add-to-team | Add To Team
[**bulk_user_operations_service_disable_duo_auth_for_users**](BulkUserOperationsApi.md#bulk_user_operations_service_disable_duo_auth_for_users) | **POST** /v1/bulk-user-operations/disable-duo-auth | Disable Duo Auth
[**bulk_user_operations_service_disable_email_two_factor_for_users**](BulkUserOperationsApi.md#bulk_user_operations_service_disable_email_two_factor_for_users) | **POST** /v1/bulk-user-operations/disable-email-two-factor | Disable Email Two Factor
[**bulk_user_operations_service_disable_fido2_two_factor_for_users**](BulkUserOperationsApi.md#bulk_user_operations_service_disable_fido2_two_factor_for_users) | **POST** /v1/bulk-user-operations/disable-fido2-two-factor | Disable Fido2 Two Factor
[**bulk_user_operations_service_disable_radius_two_factor_for_users**](BulkUserOperationsApi.md#bulk_user_operations_service_disable_radius_two_factor_for_users) | **POST** /v1/bulk-user-operations/disable-radius-two-factor | Disable Radius Two Factor
[**bulk_user_operations_service_disable_totp_auth_for_users**](BulkUserOperationsApi.md#bulk_user_operations_service_disable_totp_auth_for_users) | **POST** /v1/bulk-user-operations/disable-totp-auth | Disable TOTP Auth
[**bulk_user_operations_service_disable_users**](BulkUserOperationsApi.md#bulk_user_operations_service_disable_users) | **POST** /v1/bulk-user-operations/disable | Disable
[**bulk_user_operations_service_enable_duo_auth_for_users**](BulkUserOperationsApi.md#bulk_user_operations_service_enable_duo_auth_for_users) | **POST** /v1/bulk-user-operations/enable-duo-auth | Enable Duo Auth
[**bulk_user_operations_service_enable_email_two_factor_for_users**](BulkUserOperationsApi.md#bulk_user_operations_service_enable_email_two_factor_for_users) | **POST** /v1/bulk-user-operations/enable-email-two-factor | Enable Email Two Factor
[**bulk_user_operations_service_enable_fido2_two_factor_for_users**](BulkUserOperationsApi.md#bulk_user_operations_service_enable_fido2_two_factor_for_users) | **POST** /v1/bulk-user-operations/enable-fido2-two-factor | Enable Fido2 Two Factor
[**bulk_user_operations_service_enable_radius_two_factor_for_users**](BulkUserOperationsApi.md#bulk_user_operations_service_enable_radius_two_factor_for_users) | **POST** /v1/bulk-user-operations/enable-radius-two-factor | Enable Radius Two Factor
[**bulk_user_operations_service_enable_totp_auth_for_users**](BulkUserOperationsApi.md#bulk_user_operations_service_enable_totp_auth_for_users) | **POST** /v1/bulk-user-operations/enable-totp-auth | Enable TOTP Auth
[**bulk_user_operations_service_enable_users**](BulkUserOperationsApi.md#bulk_user_operations_service_enable_users) | **POST** /v1/bulk-user-operations/enable | Enable
[**bulk_user_operations_service_force_logout_for_users**](BulkUserOperationsApi.md#bulk_user_operations_service_force_logout_for_users) | **POST** /v1/bulk-user-operations/force-logout | Force Logout
[**bulk_user_operations_service_lock_users**](BulkUserOperationsApi.md#bulk_user_operations_service_lock_users) | **POST** /v1/bulk-user-operations/lock | Lock
[**bulk_user_operations_service_remove_users_from_group**](BulkUserOperationsApi.md#bulk_user_operations_service_remove_users_from_group) | **POST** /v1/bulk-user-operations/remove-from-group | Remove From Group
[**bulk_user_operations_service_remove_users_from_team**](BulkUserOperationsApi.md#bulk_user_operations_service_remove_users_from_team) | **POST** /v1/bulk-user-operations/remove-from-team | Remove From Team
[**bulk_user_operations_service_reset_fido2_two_factor_for_users**](BulkUserOperationsApi.md#bulk_user_operations_service_reset_fido2_two_factor_for_users) | **POST** /v1/bulk-user-operations/reset-fido2-two-factor | Reset Fido2 Two Factor
[**bulk_user_operations_service_reset_totp_auth_for_users**](BulkUserOperationsApi.md#bulk_user_operations_service_reset_totp_auth_for_users) | **POST** /v1/bulk-user-operations/reset-totp-auth | Reset TOTP Auth
[**bulk_user_operations_service_unlock_users**](BulkUserOperationsApi.md#bulk_user_operations_service_unlock_users) | **POST** /v1/bulk-user-operations/unlock | Unlock


# **bulk_user_operations_service_add_users_to_group**
> BulkOperationResponseMessage bulk_user_operations_service_add_users_to_group()

Add To Group

Add selected Users to the specified Group.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import bulk_user_operations_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.bulk_operation_response_message import BulkOperationResponseMessage
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.add_users_to_group_args import AddUsersToGroupArgs
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
    api_instance = bulk_user_operations_api.BulkUserOperationsApi(api_client)
    add_users_to_group_args = AddUsersToGroupArgs(
        data=AddUsersToGroupModel(
            group_id=None,
            user_ids=[
                None,
            ],
        ),
    ) # AddUsersToGroupArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add To Group
        api_response = api_instance.bulk_user_operations_service_add_users_to_group(add_users_to_group_args=add_users_to_group_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling BulkUserOperationsApi->bulk_user_operations_service_add_users_to_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_users_to_group_args** | [**AddUsersToGroupArgs**](AddUsersToGroupArgs.md)| args | [optional]

### Return type

[**BulkOperationResponseMessage**](BulkOperationResponseMessage.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BulkOperationResponseMessage containing the Id of the created Bulk Operation |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_user_operations_service_add_users_to_team**
> BulkOperationResponseMessage bulk_user_operations_service_add_users_to_team()

Add To Team

Add selected Users to the specified Team.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import bulk_user_operations_api
from plugins.model.add_users_to_team_args import AddUsersToTeamArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.bulk_operation_response_message import BulkOperationResponseMessage
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
    api_instance = bulk_user_operations_api.BulkUserOperationsApi(api_client)
    add_users_to_team_args = AddUsersToTeamArgs(
        data=AddUsersToTeamModel(
            team_id=None,
            user_ids=[
                None,
            ],
        ),
    ) # AddUsersToTeamArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add To Team
        api_response = api_instance.bulk_user_operations_service_add_users_to_team(add_users_to_team_args=add_users_to_team_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling BulkUserOperationsApi->bulk_user_operations_service_add_users_to_team: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_users_to_team_args** | [**AddUsersToTeamArgs**](AddUsersToTeamArgs.md)| args | [optional]

### Return type

[**BulkOperationResponseMessage**](BulkOperationResponseMessage.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BulkOperationResponseMessage containing the Id of the created Bulk Operation |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_user_operations_service_disable_duo_auth_for_users**
> BulkOperationResponseMessage bulk_user_operations_service_disable_duo_auth_for_users()

Disable Duo Auth

Disable Duo Auth for each User.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import bulk_user_operations_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.bulk_operation_response_message import BulkOperationResponseMessage
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.disable_duo_auth_for_users_args import DisableDuoAuthForUsersArgs
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
    api_instance = bulk_user_operations_api.BulkUserOperationsApi(api_client)
    disable_duo_auth_for_users_args = DisableDuoAuthForUsersArgs(
        data=DisableDuoAuthForUsersModel(
            user_ids=[
                None,
            ],
        ),
    ) # DisableDuoAuthForUsersArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Disable Duo Auth
        api_response = api_instance.bulk_user_operations_service_disable_duo_auth_for_users(disable_duo_auth_for_users_args=disable_duo_auth_for_users_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling BulkUserOperationsApi->bulk_user_operations_service_disable_duo_auth_for_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disable_duo_auth_for_users_args** | [**DisableDuoAuthForUsersArgs**](DisableDuoAuthForUsersArgs.md)| args | [optional]

### Return type

[**BulkOperationResponseMessage**](BulkOperationResponseMessage.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BulkOperationResponseMessage containing the Id of the created Bulk Operation |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_user_operations_service_disable_email_two_factor_for_users**
> BulkOperationResponseMessage bulk_user_operations_service_disable_email_two_factor_for_users()

Disable Email Two Factor

Disable Email two factor for each User.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import bulk_user_operations_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.bulk_operation_response_message import BulkOperationResponseMessage
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.disable_email_two_factor_for_users_args import DisableEmailTwoFactorForUsersArgs
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
    api_instance = bulk_user_operations_api.BulkUserOperationsApi(api_client)
    disable_email_two_factor_for_users_args = DisableEmailTwoFactorForUsersArgs(
        data=DisableEmailTwoFactorForUsersModel(
            user_ids=[
                None,
            ],
        ),
    ) # DisableEmailTwoFactorForUsersArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Disable Email Two Factor
        api_response = api_instance.bulk_user_operations_service_disable_email_two_factor_for_users(disable_email_two_factor_for_users_args=disable_email_two_factor_for_users_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling BulkUserOperationsApi->bulk_user_operations_service_disable_email_two_factor_for_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disable_email_two_factor_for_users_args** | [**DisableEmailTwoFactorForUsersArgs**](DisableEmailTwoFactorForUsersArgs.md)| args | [optional]

### Return type

[**BulkOperationResponseMessage**](BulkOperationResponseMessage.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BulkOperationResponseMessage containing the Id of the created Bulk Operation |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_user_operations_service_disable_fido2_two_factor_for_users**
> BulkOperationResponseMessage bulk_user_operations_service_disable_fido2_two_factor_for_users()

Disable Fido2 Two Factor

Disable Fido2 two factor for each User.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import bulk_user_operations_api
from plugins.model.disable_fido2_two_factor_for_users_args import DisableFido2TwoFactorForUsersArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.bulk_operation_response_message import BulkOperationResponseMessage
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
    api_instance = bulk_user_operations_api.BulkUserOperationsApi(api_client)
    disable_fido2_two_factor_for_users_args = DisableFido2TwoFactorForUsersArgs(
        data=DisableFido2TwoFactorForUsersModel(
            user_ids=[
                None,
            ],
        ),
    ) # DisableFido2TwoFactorForUsersArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Disable Fido2 Two Factor
        api_response = api_instance.bulk_user_operations_service_disable_fido2_two_factor_for_users(disable_fido2_two_factor_for_users_args=disable_fido2_two_factor_for_users_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling BulkUserOperationsApi->bulk_user_operations_service_disable_fido2_two_factor_for_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disable_fido2_two_factor_for_users_args** | [**DisableFido2TwoFactorForUsersArgs**](DisableFido2TwoFactorForUsersArgs.md)| args | [optional]

### Return type

[**BulkOperationResponseMessage**](BulkOperationResponseMessage.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BulkOperationResponseMessage containing the Id of the created Bulk Operation |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_user_operations_service_disable_radius_two_factor_for_users**
> BulkOperationResponseMessage bulk_user_operations_service_disable_radius_two_factor_for_users()

Disable Radius Two Factor

Disable Radius two factor for each User.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import bulk_user_operations_api
from plugins.model.disable_radius_two_factor_for_users_args import DisableRadiusTwoFactorForUsersArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.bulk_operation_response_message import BulkOperationResponseMessage
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
    api_instance = bulk_user_operations_api.BulkUserOperationsApi(api_client)
    disable_radius_two_factor_for_users_args = DisableRadiusTwoFactorForUsersArgs(
        data=DisableRadiusTwoFactorForUsersModel(
            user_ids=[
                None,
            ],
        ),
    ) # DisableRadiusTwoFactorForUsersArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Disable Radius Two Factor
        api_response = api_instance.bulk_user_operations_service_disable_radius_two_factor_for_users(disable_radius_two_factor_for_users_args=disable_radius_two_factor_for_users_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling BulkUserOperationsApi->bulk_user_operations_service_disable_radius_two_factor_for_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disable_radius_two_factor_for_users_args** | [**DisableRadiusTwoFactorForUsersArgs**](DisableRadiusTwoFactorForUsersArgs.md)| args | [optional]

### Return type

[**BulkOperationResponseMessage**](BulkOperationResponseMessage.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BulkOperationResponseMessage containing the Id of the created Bulk Operation |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_user_operations_service_disable_totp_auth_for_users**
> BulkOperationResponseMessage bulk_user_operations_service_disable_totp_auth_for_users()

Disable TOTP Auth

Disable TOTP Auth for each User.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import bulk_user_operations_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.disable_totp_auth_for_users_args import DisableTOTPAuthForUsersArgs
from plugins.model.bulk_operation_response_message import BulkOperationResponseMessage
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
    api_instance = bulk_user_operations_api.BulkUserOperationsApi(api_client)
    disable_totp_auth_for_users_args = DisableTOTPAuthForUsersArgs(
        data=DisableTOTPAuthForUsersModel(
            user_ids=[
                None,
            ],
        ),
    ) # DisableTOTPAuthForUsersArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Disable TOTP Auth
        api_response = api_instance.bulk_user_operations_service_disable_totp_auth_for_users(disable_totp_auth_for_users_args=disable_totp_auth_for_users_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling BulkUserOperationsApi->bulk_user_operations_service_disable_totp_auth_for_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disable_totp_auth_for_users_args** | [**DisableTOTPAuthForUsersArgs**](DisableTOTPAuthForUsersArgs.md)| args | [optional]

### Return type

[**BulkOperationResponseMessage**](BulkOperationResponseMessage.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BulkOperationResponseMessage containing the Id of the created Bulk Operation |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_user_operations_service_disable_users**
> BulkOperationResponseMessage bulk_user_operations_service_disable_users()

Disable

Disable each User.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import bulk_user_operations_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.bulk_operation_response_message import BulkOperationResponseMessage
from plugins.model.disable_users_args import DisableUsersArgs
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
    api_instance = bulk_user_operations_api.BulkUserOperationsApi(api_client)
    disable_users_args = DisableUsersArgs(
        data=DisableUsersModel(
            user_ids=[
                None,
            ],
        ),
    ) # DisableUsersArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Disable
        api_response = api_instance.bulk_user_operations_service_disable_users(disable_users_args=disable_users_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling BulkUserOperationsApi->bulk_user_operations_service_disable_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disable_users_args** | [**DisableUsersArgs**](DisableUsersArgs.md)| args | [optional]

### Return type

[**BulkOperationResponseMessage**](BulkOperationResponseMessage.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BulkOperationResponseMessage containing the Id of the created Bulk Operation |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_user_operations_service_enable_duo_auth_for_users**
> BulkOperationResponseMessage bulk_user_operations_service_enable_duo_auth_for_users()

Enable Duo Auth

Enable Duo Auth for each User.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import bulk_user_operations_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.bulk_operation_response_message import BulkOperationResponseMessage
from plugins.model.enable_duo_auth_for_users_args import EnableDuoAuthForUsersArgs
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
    api_instance = bulk_user_operations_api.BulkUserOperationsApi(api_client)
    enable_duo_auth_for_users_args = EnableDuoAuthForUsersArgs(
        data=EnableDuoAuthForUsersModel(
            user_ids=[
                None,
            ],
        ),
    ) # EnableDuoAuthForUsersArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Enable Duo Auth
        api_response = api_instance.bulk_user_operations_service_enable_duo_auth_for_users(enable_duo_auth_for_users_args=enable_duo_auth_for_users_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling BulkUserOperationsApi->bulk_user_operations_service_enable_duo_auth_for_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enable_duo_auth_for_users_args** | [**EnableDuoAuthForUsersArgs**](EnableDuoAuthForUsersArgs.md)| args | [optional]

### Return type

[**BulkOperationResponseMessage**](BulkOperationResponseMessage.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BulkOperationResponseMessage containing the Id of the created Bulk Operation |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_user_operations_service_enable_email_two_factor_for_users**
> BulkOperationResponseMessage bulk_user_operations_service_enable_email_two_factor_for_users()

Enable Email Two Factor

Enable Email two factor for each User.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import bulk_user_operations_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.bulk_operation_response_message import BulkOperationResponseMessage
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.enable_email_two_factor_for_users_args import EnableEmailTwoFactorForUsersArgs
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
    api_instance = bulk_user_operations_api.BulkUserOperationsApi(api_client)
    enable_email_two_factor_for_users_args = EnableEmailTwoFactorForUsersArgs(
        data=EnableEmailTwoFactorForUsersModel(
            user_ids=[
                None,
            ],
        ),
    ) # EnableEmailTwoFactorForUsersArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Enable Email Two Factor
        api_response = api_instance.bulk_user_operations_service_enable_email_two_factor_for_users(enable_email_two_factor_for_users_args=enable_email_two_factor_for_users_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling BulkUserOperationsApi->bulk_user_operations_service_enable_email_two_factor_for_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enable_email_two_factor_for_users_args** | [**EnableEmailTwoFactorForUsersArgs**](EnableEmailTwoFactorForUsersArgs.md)| args | [optional]

### Return type

[**BulkOperationResponseMessage**](BulkOperationResponseMessage.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BulkOperationResponseMessage containing the Id of the created Bulk Operation |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_user_operations_service_enable_fido2_two_factor_for_users**
> BulkOperationResponseMessage bulk_user_operations_service_enable_fido2_two_factor_for_users()

Enable Fido2 Two Factor

Enable Fido2 two factor for each User.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import bulk_user_operations_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.enable_fido2_two_factor_for_users_args import EnableFido2TwoFactorForUsersArgs
from plugins.model.bulk_operation_response_message import BulkOperationResponseMessage
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
    api_instance = bulk_user_operations_api.BulkUserOperationsApi(api_client)
    enable_fido2_two_factor_for_users_args = EnableFido2TwoFactorForUsersArgs(
        data=EnableFido2TwoFactorForUsersModel(
            user_ids=[
                None,
            ],
        ),
    ) # EnableFido2TwoFactorForUsersArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Enable Fido2 Two Factor
        api_response = api_instance.bulk_user_operations_service_enable_fido2_two_factor_for_users(enable_fido2_two_factor_for_users_args=enable_fido2_two_factor_for_users_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling BulkUserOperationsApi->bulk_user_operations_service_enable_fido2_two_factor_for_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enable_fido2_two_factor_for_users_args** | [**EnableFido2TwoFactorForUsersArgs**](EnableFido2TwoFactorForUsersArgs.md)| args | [optional]

### Return type

[**BulkOperationResponseMessage**](BulkOperationResponseMessage.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BulkOperationResponseMessage containing the Id of the created Bulk Operation |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_user_operations_service_enable_radius_two_factor_for_users**
> BulkOperationResponseMessage bulk_user_operations_service_enable_radius_two_factor_for_users()

Enable Radius Two Factor

Enable Radius two factor for each User.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import bulk_user_operations_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.enable_radius_two_factor_for_users_args import EnableRadiusTwoFactorForUsersArgs
from plugins.model.bulk_operation_response_message import BulkOperationResponseMessage
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
    api_instance = bulk_user_operations_api.BulkUserOperationsApi(api_client)
    enable_radius_two_factor_for_users_args = EnableRadiusTwoFactorForUsersArgs(
        data=EnableRadiusTwoFactorForUsersModel(
            user_ids=[
                None,
            ],
        ),
    ) # EnableRadiusTwoFactorForUsersArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Enable Radius Two Factor
        api_response = api_instance.bulk_user_operations_service_enable_radius_two_factor_for_users(enable_radius_two_factor_for_users_args=enable_radius_two_factor_for_users_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling BulkUserOperationsApi->bulk_user_operations_service_enable_radius_two_factor_for_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enable_radius_two_factor_for_users_args** | [**EnableRadiusTwoFactorForUsersArgs**](EnableRadiusTwoFactorForUsersArgs.md)| args | [optional]

### Return type

[**BulkOperationResponseMessage**](BulkOperationResponseMessage.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BulkOperationResponseMessage containing the Id of the created Bulk Operation |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_user_operations_service_enable_totp_auth_for_users**
> BulkOperationResponseMessage bulk_user_operations_service_enable_totp_auth_for_users()

Enable TOTP Auth

Enable TOTP Auth for each User.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import bulk_user_operations_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.bulk_operation_response_message import BulkOperationResponseMessage
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.enable_totp_auth_for_users_args import EnableTOTPAuthForUsersArgs
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
    api_instance = bulk_user_operations_api.BulkUserOperationsApi(api_client)
    enable_totp_auth_for_users_args = EnableTOTPAuthForUsersArgs(
        data=EnableTOTPAuthForUsersModel(
            user_ids=[
                None,
            ],
        ),
    ) # EnableTOTPAuthForUsersArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Enable TOTP Auth
        api_response = api_instance.bulk_user_operations_service_enable_totp_auth_for_users(enable_totp_auth_for_users_args=enable_totp_auth_for_users_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling BulkUserOperationsApi->bulk_user_operations_service_enable_totp_auth_for_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enable_totp_auth_for_users_args** | [**EnableTOTPAuthForUsersArgs**](EnableTOTPAuthForUsersArgs.md)| args | [optional]

### Return type

[**BulkOperationResponseMessage**](BulkOperationResponseMessage.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BulkOperationResponseMessage containing the Id of the created Bulk Operation |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_user_operations_service_enable_users**
> BulkOperationResponseMessage bulk_user_operations_service_enable_users()

Enable

Enable each User.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import bulk_user_operations_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.bulk_operation_response_message import BulkOperationResponseMessage
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.enable_users_args import EnableUsersArgs
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
    api_instance = bulk_user_operations_api.BulkUserOperationsApi(api_client)
    enable_users_args = EnableUsersArgs(
        data=EnableUsersModel(
            user_ids=[
                None,
            ],
        ),
    ) # EnableUsersArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Enable
        api_response = api_instance.bulk_user_operations_service_enable_users(enable_users_args=enable_users_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling BulkUserOperationsApi->bulk_user_operations_service_enable_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enable_users_args** | [**EnableUsersArgs**](EnableUsersArgs.md)| args | [optional]

### Return type

[**BulkOperationResponseMessage**](BulkOperationResponseMessage.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BulkOperationResponseMessage containing the Id of the created Bulk Operation |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_user_operations_service_force_logout_for_users**
> BulkOperationResponseMessage bulk_user_operations_service_force_logout_for_users()

Force Logout

Force Logout for each User.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import bulk_user_operations_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.bulk_operation_response_message import BulkOperationResponseMessage
from plugins.model.force_logout_for_users_args import ForceLogoutForUsersArgs
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
    api_instance = bulk_user_operations_api.BulkUserOperationsApi(api_client)
    force_logout_for_users_args = ForceLogoutForUsersArgs(
        data=ForceLogoutForUsersModel(
            user_ids=[
                None,
            ],
        ),
    ) # ForceLogoutForUsersArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Force Logout
        api_response = api_instance.bulk_user_operations_service_force_logout_for_users(force_logout_for_users_args=force_logout_for_users_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling BulkUserOperationsApi->bulk_user_operations_service_force_logout_for_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **force_logout_for_users_args** | [**ForceLogoutForUsersArgs**](ForceLogoutForUsersArgs.md)| args | [optional]

### Return type

[**BulkOperationResponseMessage**](BulkOperationResponseMessage.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BulkOperationResponseMessage containing the Id of the created Bulk Operation |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_user_operations_service_lock_users**
> BulkOperationResponseMessage bulk_user_operations_service_lock_users()

Lock

Lock selected Users.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import bulk_user_operations_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.bulk_operation_response_message import BulkOperationResponseMessage
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.lock_users_args import LockUsersArgs
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
    api_instance = bulk_user_operations_api.BulkUserOperationsApi(api_client)
    lock_users_args = LockUsersArgs(
        data=LockUsersModel(
            user_ids=[
                None,
            ],
        ),
    ) # LockUsersArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Lock
        api_response = api_instance.bulk_user_operations_service_lock_users(lock_users_args=lock_users_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling BulkUserOperationsApi->bulk_user_operations_service_lock_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lock_users_args** | [**LockUsersArgs**](LockUsersArgs.md)| args | [optional]

### Return type

[**BulkOperationResponseMessage**](BulkOperationResponseMessage.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BulkOperationResponseMessage containing the Id of the created Bulk Operation |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_user_operations_service_remove_users_from_group**
> BulkOperationResponseMessage bulk_user_operations_service_remove_users_from_group()

Remove From Group

Remove selected Users from the specified Group.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import bulk_user_operations_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.bulk_operation_response_message import BulkOperationResponseMessage
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.remove_users_from_group_args import RemoveUsersFromGroupArgs
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
    api_instance = bulk_user_operations_api.BulkUserOperationsApi(api_client)
    remove_users_from_group_args = RemoveUsersFromGroupArgs(
        data=RemoveUsersFromGroupModel(
            group_id=None,
            user_ids=[
                None,
            ],
        ),
    ) # RemoveUsersFromGroupArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove From Group
        api_response = api_instance.bulk_user_operations_service_remove_users_from_group(remove_users_from_group_args=remove_users_from_group_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling BulkUserOperationsApi->bulk_user_operations_service_remove_users_from_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_users_from_group_args** | [**RemoveUsersFromGroupArgs**](RemoveUsersFromGroupArgs.md)| args | [optional]

### Return type

[**BulkOperationResponseMessage**](BulkOperationResponseMessage.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BulkOperationResponseMessage containing the Id of the created Bulk Operation |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_user_operations_service_remove_users_from_team**
> BulkOperationResponseMessage bulk_user_operations_service_remove_users_from_team()

Remove From Team

Remove selected Users from the specified Team.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import bulk_user_operations_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.bulk_operation_response_message import BulkOperationResponseMessage
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.remove_users_from_team_args import RemoveUsersFromTeamArgs
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
    api_instance = bulk_user_operations_api.BulkUserOperationsApi(api_client)
    remove_users_from_team_args = RemoveUsersFromTeamArgs(
        data=RemoveUsersFromTeamModel(
            team_id=None,
            user_ids=[
                None,
            ],
        ),
    ) # RemoveUsersFromTeamArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove From Team
        api_response = api_instance.bulk_user_operations_service_remove_users_from_team(remove_users_from_team_args=remove_users_from_team_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling BulkUserOperationsApi->bulk_user_operations_service_remove_users_from_team: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_users_from_team_args** | [**RemoveUsersFromTeamArgs**](RemoveUsersFromTeamArgs.md)| args | [optional]

### Return type

[**BulkOperationResponseMessage**](BulkOperationResponseMessage.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BulkOperationResponseMessage containing the Id of the created Bulk Operation |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_user_operations_service_reset_fido2_two_factor_for_users**
> BulkOperationResponseMessage bulk_user_operations_service_reset_fido2_two_factor_for_users()

Reset Fido2 Two Factor

Reset Fido2 two factor for each User.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import bulk_user_operations_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.bulk_operation_response_message import BulkOperationResponseMessage
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.reset_fido2_two_factor_for_users_args import ResetFido2TwoFactorForUsersArgs
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
    api_instance = bulk_user_operations_api.BulkUserOperationsApi(api_client)
    reset_fido2_two_factor_for_users_args = ResetFido2TwoFactorForUsersArgs(
        data=ResetFido2TwoFactorForUsersModel(
            user_ids=[
                None,
            ],
        ),
    ) # ResetFido2TwoFactorForUsersArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Reset Fido2 Two Factor
        api_response = api_instance.bulk_user_operations_service_reset_fido2_two_factor_for_users(reset_fido2_two_factor_for_users_args=reset_fido2_two_factor_for_users_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling BulkUserOperationsApi->bulk_user_operations_service_reset_fido2_two_factor_for_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reset_fido2_two_factor_for_users_args** | [**ResetFido2TwoFactorForUsersArgs**](ResetFido2TwoFactorForUsersArgs.md)| args | [optional]

### Return type

[**BulkOperationResponseMessage**](BulkOperationResponseMessage.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BulkOperationResponseMessage containing the Id of the created Bulk Operation |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_user_operations_service_reset_totp_auth_for_users**
> BulkOperationResponseMessage bulk_user_operations_service_reset_totp_auth_for_users()

Reset TOTP Auth

Reset TOTP Auth for each User.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import bulk_user_operations_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.reset_totp_auth_for_users_args import ResetTOTPAuthForUsersArgs
from plugins.model.bulk_operation_response_message import BulkOperationResponseMessage
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
    api_instance = bulk_user_operations_api.BulkUserOperationsApi(api_client)
    reset_totp_auth_for_users_args = ResetTOTPAuthForUsersArgs(
        data=ResetTOTPAuthForUsersModel(
            user_ids=[
                None,
            ],
        ),
    ) # ResetTOTPAuthForUsersArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Reset TOTP Auth
        api_response = api_instance.bulk_user_operations_service_reset_totp_auth_for_users(reset_totp_auth_for_users_args=reset_totp_auth_for_users_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling BulkUserOperationsApi->bulk_user_operations_service_reset_totp_auth_for_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reset_totp_auth_for_users_args** | [**ResetTOTPAuthForUsersArgs**](ResetTOTPAuthForUsersArgs.md)| args | [optional]

### Return type

[**BulkOperationResponseMessage**](BulkOperationResponseMessage.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BulkOperationResponseMessage containing the Id of the created Bulk Operation |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_user_operations_service_unlock_users**
> BulkOperationResponseMessage bulk_user_operations_service_unlock_users()

Unlock

Unlock selected Users.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import bulk_user_operations_api
from plugins.model.unlock_users_args import UnlockUsersArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.bulk_operation_response_message import BulkOperationResponseMessage
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
    api_instance = bulk_user_operations_api.BulkUserOperationsApi(api_client)
    unlock_users_args = UnlockUsersArgs(
        data=UnlockUsersModel(
            user_ids=[
                None,
            ],
        ),
    ) # UnlockUsersArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Unlock
        api_response = api_instance.bulk_user_operations_service_unlock_users(unlock_users_args=unlock_users_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling BulkUserOperationsApi->bulk_user_operations_service_unlock_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unlock_users_args** | [**UnlockUsersArgs**](UnlockUsersArgs.md)| args | [optional]

### Return type

[**BulkOperationResponseMessage**](BulkOperationResponseMessage.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BulkOperationResponseMessage containing the Id of the created Bulk Operation |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

