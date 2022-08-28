# plugins.SdkClientAccountsApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sdk_client_accounts_service_create_client_account**](SdkClientAccountsApi.md#sdk_client_accounts_service_create_client_account) | **POST** /v1/sdk-client-accounts | Create SDK Client Account
[**sdk_client_accounts_service_get**](SdkClientAccountsApi.md#sdk_client_accounts_service_get) | **GET** /v1/sdk-client-accounts/{id} | Get SDK Client Account
[**sdk_client_accounts_service_get_enabled**](SdkClientAccountsApi.md#sdk_client_accounts_service_get_enabled) | **GET** /v1/sdk-client-accounts/enabled | Get Current State
[**sdk_client_accounts_service_revoke**](SdkClientAccountsApi.md#sdk_client_accounts_service_revoke) | **POST** /v1/sdk-client-accounts/{id}/revoke | Revoke SDK Client Account
[**sdk_client_accounts_service_search_client_accounts**](SdkClientAccountsApi.md#sdk_client_accounts_service_search_client_accounts) | **GET** /v1/sdk-client-accounts | Search SDK Client Accounts
[**sdk_client_accounts_service_toggle_enabled**](SdkClientAccountsApi.md#sdk_client_accounts_service_toggle_enabled) | **POST** /v1/sdk-client-accounts/enabled | Toggle Current State
[**sdk_client_accounts_service_update_client_account**](SdkClientAccountsApi.md#sdk_client_accounts_service_update_client_account) | **PUT** /v1/sdk-client-accounts/{id} | Update SDK Client Account


# **sdk_client_accounts_service_create_client_account**
> SdkClientAccountModel sdk_client_accounts_service_create_client_account()

Create SDK Client Account

Create a new SDK Client account

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import sdk_client_accounts_api
from plugins.model.sdk_client_account_model import SdkClientAccountModel
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.sdk_client_account_create_args import SdkClientAccountCreateArgs
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
    api_instance = sdk_client_accounts_api.SdkClientAccountsApi(api_client)
    sdk_client_account_create_args = SdkClientAccountCreateArgs(
        client_id=None,
        description=None,
        name=None,
        onboarding_key=None,
        rule_name=None,
    ) # SdkClientAccountCreateArgs | SDK Client Account creation options (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create SDK Client Account
        api_response = api_instance.sdk_client_accounts_service_create_client_account(sdk_client_account_create_args=sdk_client_account_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SdkClientAccountsApi->sdk_client_accounts_service_create_client_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_client_account_create_args** | [**SdkClientAccountCreateArgs**](SdkClientAccountCreateArgs.md)| SDK Client Account creation options | [optional]

### Return type

[**SdkClientAccountModel**](SdkClientAccountModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SdkClientAccountModel |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sdk_client_accounts_service_get**
> SdkClientAccountModel sdk_client_accounts_service_get(id)

Get SDK Client Account

Get a single SDK Client account by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import sdk_client_accounts_api
from plugins.model.sdk_client_account_model import SdkClientAccountModel
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
    api_instance = sdk_client_accounts_api.SdkClientAccountsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | SDK Client Account Id

    # example passing only required values which don't have defaults set
    try:
        # Get SDK Client Account
        api_response = api_instance.sdk_client_accounts_service_get(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SdkClientAccountsApi->sdk_client_accounts_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| SDK Client Account Id |

### Return type

[**SdkClientAccountModel**](SdkClientAccountModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SdkClientAccountModel |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sdk_client_accounts_service_get_enabled**
> bool sdk_client_accounts_service_get_enabled()

Get Current State

Get the current state of SDK client account

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import sdk_client_accounts_api
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
    api_instance = sdk_client_accounts_api.SdkClientAccountsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Current State
        api_response = api_instance.sdk_client_accounts_service_get_enabled()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SdkClientAccountsApi->sdk_client_accounts_service_get_enabled: %s\n" % e)
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
**200** | bool |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sdk_client_accounts_service_revoke**
> bool sdk_client_accounts_service_revoke(id)

Revoke SDK Client Account

Revoke a single SDK Client account by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import sdk_client_accounts_api
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
    api_instance = sdk_client_accounts_api.SdkClientAccountsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | SDK Client Account Id

    # example passing only required values which don't have defaults set
    try:
        # Revoke SDK Client Account
        api_response = api_instance.sdk_client_accounts_service_revoke(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SdkClientAccountsApi->sdk_client_accounts_service_revoke: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| SDK Client Account Id |

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
**200** | bool |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sdk_client_accounts_service_search_client_accounts**
> PagingOfSdkClientAccountSummaryAndSdkClientAccountFilter sdk_client_accounts_service_search_client_accounts()

Search SDK Client Accounts

Search, filter, sort, and page app SDK Client accounts

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import sdk_client_accounts_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.paging_of_sdk_client_account_summary_and_sdk_client_account_filter import PagingOfSdkClientAccountSummaryAndSdkClientAccountFilter
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
    api_instance = sdk_client_accounts_api.SdkClientAccountsApi(api_client)
    filter_operator = None # bool, date, datetime, dict, float, int, list, str, none_type | Operator (optional)
    filter_search_text = None # bool, date, datetime, dict, float, int, list, str, none_type | SearchText (optional)
    filter_user_id = None # bool, date, datetime, dict, float, int, list, str, none_type | UserId (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search SDK Client Accounts
        api_response = api_instance.sdk_client_accounts_service_search_client_accounts(filter_operator=filter_operator, filter_search_text=filter_search_text, filter_user_id=filter_user_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SdkClientAccountsApi->sdk_client_accounts_service_search_client_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_operator** | **bool, date, datetime, dict, float, int, list, str, none_type**| Operator | [optional]
 **filter_search_text** | **bool, date, datetime, dict, float, int, list, str, none_type**| SearchText | [optional]
 **filter_user_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| UserId | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfSdkClientAccountSummaryAndSdkClientAccountFilter**](PagingOfSdkClientAccountSummaryAndSdkClientAccountFilter.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SDK Client Account search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sdk_client_accounts_service_toggle_enabled**
> bool sdk_client_accounts_service_toggle_enabled()

Toggle Current State

Toggle the current state of SDK client account

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import sdk_client_accounts_api
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
    api_instance = sdk_client_accounts_api.SdkClientAccountsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Toggle Current State
        api_response = api_instance.sdk_client_accounts_service_toggle_enabled()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SdkClientAccountsApi->sdk_client_accounts_service_toggle_enabled: %s\n" % e)
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
**200** | bool |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sdk_client_accounts_service_update_client_account**
> SdkClientAccountModel sdk_client_accounts_service_update_client_account(id)

Update SDK Client Account

Update a single SDK Client account by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import sdk_client_accounts_api
from plugins.model.sdk_client_account_model import SdkClientAccountModel
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.sdk_client_account_update_args import SdkClientAccountUpdateArgs
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
    api_instance = sdk_client_accounts_api.SdkClientAccountsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | SDK Client Account Id
    sdk_client_account_update_args = SdkClientAccountUpdateArgs(
        name=None,
        user_id=None,
    ) # SdkClientAccountUpdateArgs | SDK Client Account update options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update SDK Client Account
        api_response = api_instance.sdk_client_accounts_service_update_client_account(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SdkClientAccountsApi->sdk_client_accounts_service_update_client_account: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update SDK Client Account
        api_response = api_instance.sdk_client_accounts_service_update_client_account(id, sdk_client_account_update_args=sdk_client_account_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SdkClientAccountsApi->sdk_client_accounts_service_update_client_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| SDK Client Account Id |
 **sdk_client_account_update_args** | [**SdkClientAccountUpdateArgs**](SdkClientAccountUpdateArgs.md)| SDK Client Account update options | [optional]

### Return type

[**SdkClientAccountModel**](SdkClientAccountModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SdkClientAccountModel |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

