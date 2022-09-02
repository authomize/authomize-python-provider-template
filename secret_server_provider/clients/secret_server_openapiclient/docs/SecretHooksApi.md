# secret_server_openapiclient.SecretHooksApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**secret_hooks_service_create_hook**](SecretHooksApi.md#secret_hooks_service_create_hook) | **POST** /v1/secret-detail/{secretId}/hook | Create Secret hook
[**secret_hooks_service_create_hook_v2**](SecretHooksApi.md#secret_hooks_service_create_hook_v2) | **POST** /v2/secret-detail/{secretId}/hook | Create Secret hook v2
[**secret_hooks_service_delete_hook**](SecretHooksApi.md#secret_hooks_service_delete_hook) | **DELETE** /v1/secret-detail/{secretId}/hook/{secretHookId} | Delete Secret Hook
[**secret_hooks_service_get_hook**](SecretHooksApi.md#secret_hooks_service_get_hook) | **GET** /v1/secret-detail/{secretId}/hook/get/{secretHookId} | Get Secret hook details
[**secret_hooks_service_get_hook_v2**](SecretHooksApi.md#secret_hooks_service_get_hook_v2) | **GET** /v2/secret-detail/{secretId}/hook/get/{secretHookId} | Get Secret hook details
[**secret_hooks_service_get_hooks**](SecretHooksApi.md#secret_hooks_service_get_hooks) | **GET** /v1/secret-detail/{secretId}/hooks | Get Secret Hooks
[**secret_hooks_service_get_hooks_v2**](SecretHooksApi.md#secret_hooks_service_get_hooks_v2) | **GET** /v2/secret-detail/{secretId}/hooks | Get Secret Hooks
[**secret_hooks_service_stub_hook**](SecretHooksApi.md#secret_hooks_service_stub_hook) | **GET** /v1/secret-detail/{secretId}/hook/stub/{scriptId} | Stub Hook
[**secret_hooks_service_stub_hook_v2**](SecretHooksApi.md#secret_hooks_service_stub_hook_v2) | **GET** /v2/secret-detail/{secretId}/hook/stub/{scriptId} | Stub Hook
[**secret_hooks_service_update_hook**](SecretHooksApi.md#secret_hooks_service_update_hook) | **PUT** /v1/secret-detail/{secretId}/hook/{secretHookId} | Update Secret Hook
[**secret_hooks_service_update_hook_v2**](SecretHooksApi.md#secret_hooks_service_update_hook_v2) | **PUT** /v2/secret-detail/{secretId}/hook/{secretHookId} | Update Secret Hook


# **secret_hooks_service_create_hook**
> SecretDetailHookModel secret_hooks_service_create_hook(secret_id)

Create Secret hook

Create Secret hook

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_hooks_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.secret_detail_hook_create_args import SecretDetailHookCreateArgs
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.secret_detail_hook_model import SecretDetailHookModel
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
    api_instance = secret_hooks_api.SecretHooksApi(api_client)
    secret_id = 1 # int | secretId
    secret_detail_hook_create_args = SecretDetailHookCreateArgs(
        data=SecretDetailHooksCreateModel(
            arguments="arguments_example",
            database="database_example",
            description="description_example",
            event_action_id=1,
            failure_message="failure_message_example",
            name="name_example",
            parameters=[
                SecretDetailHookParameterViewModel(
                    parameter_name="parameter_name_example",
                    parameter_type="parameter_type_example",
                    parameter_value="parameter_value_example",
                ),
            ],
            port="port_example",
            pre_post_option="pre_post_option_example",
            privileged_secret_id=1,
            script_id=1,
            secret_id=1,
            server_key_digest="server_key_digest_example",
            server_name="server_name_example",
            ssh_key_secret_id=1,
            stop_on_failure=True,
        ),
    ) # SecretDetailHookCreateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Secret hook
        api_response = api_instance.secret_hooks_service_create_hook(secret_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretHooksApi->secret_hooks_service_create_hook: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Secret hook
        api_response = api_instance.secret_hooks_service_create_hook(secret_id, secret_detail_hook_create_args=secret_detail_hook_create_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretHooksApi->secret_hooks_service_create_hook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_id** | **int**| secretId |
 **secret_detail_hook_create_args** | [**SecretDetailHookCreateArgs**](SecretDetailHookCreateArgs.md)| args | [optional]

### Return type

[**SecretDetailHookModel**](SecretDetailHookModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Newly created Secret hook |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_hooks_service_create_hook_v2**
> SecretDetailHookModel secret_hooks_service_create_hook_v2(secret_id)

Create Secret hook v2

Create Secret hook v2

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_hooks_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.secret_detail_hook_create_args import SecretDetailHookCreateArgs
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.secret_detail_hook_model import SecretDetailHookModel
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
    api_instance = secret_hooks_api.SecretHooksApi(api_client)
    secret_id = 1 # int | secretId
    secret_detail_hook_create_args = SecretDetailHookCreateArgs(
        data=SecretDetailHooksCreateModel(
            arguments="arguments_example",
            database="database_example",
            description="description_example",
            event_action_id=1,
            failure_message="failure_message_example",
            name="name_example",
            parameters=[
                SecretDetailHookParameterViewModel(
                    parameter_name="parameter_name_example",
                    parameter_type="parameter_type_example",
                    parameter_value="parameter_value_example",
                ),
            ],
            port="port_example",
            pre_post_option="pre_post_option_example",
            privileged_secret_id=1,
            script_id=1,
            secret_id=1,
            server_key_digest="server_key_digest_example",
            server_name="server_name_example",
            ssh_key_secret_id=1,
            stop_on_failure=True,
        ),
    ) # SecretDetailHookCreateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Secret hook v2
        api_response = api_instance.secret_hooks_service_create_hook_v2(secret_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretHooksApi->secret_hooks_service_create_hook_v2: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Secret hook v2
        api_response = api_instance.secret_hooks_service_create_hook_v2(secret_id, secret_detail_hook_create_args=secret_detail_hook_create_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretHooksApi->secret_hooks_service_create_hook_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_id** | **int**| secretId |
 **secret_detail_hook_create_args** | [**SecretDetailHookCreateArgs**](SecretDetailHookCreateArgs.md)| args | [optional]

### Return type

[**SecretDetailHookModel**](SecretDetailHookModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Newly created Secret hook |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_hooks_service_delete_hook**
> bool secret_hooks_service_delete_hook(secret_hook_id, secret_id)

Delete Secret Hook

Delete Secret Hook

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_hooks_api
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
    api_instance = secret_hooks_api.SecretHooksApi(api_client)
    secret_hook_id = 1 # int | secretHookId
    secret_id = 1 # int | secretId

    # example passing only required values which don't have defaults set
    try:
        # Delete Secret Hook
        api_response = api_instance.secret_hooks_service_delete_hook(secret_hook_id, secret_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretHooksApi->secret_hooks_service_delete_hook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_hook_id** | **int**| secretHookId |
 **secret_id** | **int**| secretId |

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
**200** | Success or failure |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_hooks_service_get_hook**
> SecretDetailHookModel secret_hooks_service_get_hook(secret_hook_id, secret_id)

Get Secret hook details

Get Secret hook details

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_hooks_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.secret_detail_hook_model import SecretDetailHookModel
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
    api_instance = secret_hooks_api.SecretHooksApi(api_client)
    secret_hook_id = 1 # int | secretHookId
    secret_id = 1 # int | secretId

    # example passing only required values which don't have defaults set
    try:
        # Get Secret hook details
        api_response = api_instance.secret_hooks_service_get_hook(secret_hook_id, secret_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretHooksApi->secret_hooks_service_get_hook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_hook_id** | **int**| secretHookId |
 **secret_id** | **int**| secretId |

### Return type

[**SecretDetailHookModel**](SecretDetailHookModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret hook details |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_hooks_service_get_hook_v2**
> SecretDetailHookModel secret_hooks_service_get_hook_v2(secret_hook_id, secret_id)

Get Secret hook details

Get Secret hook details

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_hooks_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.secret_detail_hook_model import SecretDetailHookModel
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
    api_instance = secret_hooks_api.SecretHooksApi(api_client)
    secret_hook_id = 1 # int | secretHookId
    secret_id = 1 # int | secretId

    # example passing only required values which don't have defaults set
    try:
        # Get Secret hook details
        api_response = api_instance.secret_hooks_service_get_hook_v2(secret_hook_id, secret_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretHooksApi->secret_hooks_service_get_hook_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_hook_id** | **int**| secretHookId |
 **secret_id** | **int**| secretId |

### Return type

[**SecretDetailHookModel**](SecretDetailHookModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret hook details |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_hooks_service_get_hooks**
> [SecretDetailHookSummaryViewModel] secret_hooks_service_get_hooks(secret_id)

Get Secret Hooks

Get all of the hooks for the specified secret

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_hooks_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.secret_detail_hook_summary_view_model import SecretDetailHookSummaryViewModel
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
    api_instance = secret_hooks_api.SecretHooksApi(api_client)
    secret_id = 1 # int | secretId

    # example passing only required values which don't have defaults set
    try:
        # Get Secret Hooks
        api_response = api_instance.secret_hooks_service_get_hooks(secret_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretHooksApi->secret_hooks_service_get_hooks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_id** | **int**| secretId |

### Return type

[**[SecretDetailHookSummaryViewModel]**](SecretDetailHookSummaryViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_hooks_service_get_hooks_v2**
> [SecretDetailHookSummaryViewModel] secret_hooks_service_get_hooks_v2(secret_id)

Get Secret Hooks

Get all of the hooks for the specified secret

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_hooks_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.secret_detail_hook_summary_view_model import SecretDetailHookSummaryViewModel
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
    api_instance = secret_hooks_api.SecretHooksApi(api_client)
    secret_id = 1 # int | secretId

    # example passing only required values which don't have defaults set
    try:
        # Get Secret Hooks
        api_response = api_instance.secret_hooks_service_get_hooks_v2(secret_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretHooksApi->secret_hooks_service_get_hooks_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_id** | **int**| secretId |

### Return type

[**[SecretDetailHookSummaryViewModel]**](SecretDetailHookSummaryViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_hooks_service_stub_hook**
> SecretDetailHookModel secret_hooks_service_stub_hook(script_id, secret_id)

Stub Hook

Get stub for a new Secret hook

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_hooks_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.secret_detail_hook_model import SecretDetailHookModel
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
    api_instance = secret_hooks_api.SecretHooksApi(api_client)
    script_id = 1 # int | scriptId
    secret_id = 1 # int | secretId

    # example passing only required values which don't have defaults set
    try:
        # Stub Hook
        api_response = api_instance.secret_hooks_service_stub_hook(script_id, secret_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretHooksApi->secret_hooks_service_stub_hook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **script_id** | **int**| scriptId |
 **secret_id** | **int**| secretId |

### Return type

[**SecretDetailHookModel**](SecretDetailHookModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stub for a new Secret hook |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_hooks_service_stub_hook_v2**
> SecretDetailHookModel secret_hooks_service_stub_hook_v2(script_id, secret_id)

Stub Hook

Get stub for a new Secret hook

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_hooks_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.secret_detail_hook_model import SecretDetailHookModel
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
    api_instance = secret_hooks_api.SecretHooksApi(api_client)
    script_id = 1 # int | scriptId
    secret_id = 1 # int | secretId

    # example passing only required values which don't have defaults set
    try:
        # Stub Hook
        api_response = api_instance.secret_hooks_service_stub_hook_v2(script_id, secret_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretHooksApi->secret_hooks_service_stub_hook_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **script_id** | **int**| scriptId |
 **secret_id** | **int**| secretId |

### Return type

[**SecretDetailHookModel**](SecretDetailHookModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stub for a new Secret hook |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_hooks_service_update_hook**
> SecretDetailHookModel secret_hooks_service_update_hook(secret_hook_id, secret_id)

Update Secret Hook

Update Secret hook

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_hooks_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.secret_detail_hook_model import SecretDetailHookModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.secret_detail_hook_update_args import SecretDetailHookUpdateArgs
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
    api_instance = secret_hooks_api.SecretHooksApi(api_client)
    secret_hook_id = 1 # int | secretHookId
    secret_id = 1 # int | secretId
    secret_detail_hook_update_args = SecretDetailHookUpdateArgs(
        data=SecretDetailHookUpdateModel(
            arguments=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            database=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            description=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            event_action_id=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            failure_message=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            name=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            parameters=[
                SecretDetailHookParameterViewModel(
                    parameter_name="parameter_name_example",
                    parameter_type="parameter_type_example",
                    parameter_value="parameter_value_example",
                ),
            ],
            port=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            pre_post_option=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            privileged_secret_id=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=1,
            ),
            script_id=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=1,
            ),
            script_type_id=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            server_key_digest=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            server_name=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            sort_order=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            ssh_key_secret_id=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=1,
            ),
            status=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            stop_on_failure=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
        ),
    ) # SecretDetailHookUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Secret Hook
        api_response = api_instance.secret_hooks_service_update_hook(secret_hook_id, secret_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretHooksApi->secret_hooks_service_update_hook: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Secret Hook
        api_response = api_instance.secret_hooks_service_update_hook(secret_hook_id, secret_id, secret_detail_hook_update_args=secret_detail_hook_update_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretHooksApi->secret_hooks_service_update_hook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_hook_id** | **int**| secretHookId |
 **secret_id** | **int**| secretId |
 **secret_detail_hook_update_args** | [**SecretDetailHookUpdateArgs**](SecretDetailHookUpdateArgs.md)| args | [optional]

### Return type

[**SecretDetailHookModel**](SecretDetailHookModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret hook retrieved after updates |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_hooks_service_update_hook_v2**
> SecretDetailHookModel secret_hooks_service_update_hook_v2(secret_hook_id, secret_id)

Update Secret Hook

Update Secret hook

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_hooks_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.secret_detail_hook_model import SecretDetailHookModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.secret_detail_hook_update_args import SecretDetailHookUpdateArgs
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
    api_instance = secret_hooks_api.SecretHooksApi(api_client)
    secret_hook_id = 1 # int | secretHookId
    secret_id = 1 # int | secretId
    secret_detail_hook_update_args = SecretDetailHookUpdateArgs(
        data=SecretDetailHookUpdateModel(
            arguments=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            database=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            description=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            event_action_id=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            failure_message=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            name=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            parameters=[
                SecretDetailHookParameterViewModel(
                    parameter_name="parameter_name_example",
                    parameter_type="parameter_type_example",
                    parameter_value="parameter_value_example",
                ),
            ],
            port=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            pre_post_option=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            privileged_secret_id=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=1,
            ),
            script_id=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=1,
            ),
            script_type_id=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            server_key_digest=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            server_name=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            sort_order=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            ssh_key_secret_id=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=1,
            ),
            status=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            stop_on_failure=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
        ),
    ) # SecretDetailHookUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Secret Hook
        api_response = api_instance.secret_hooks_service_update_hook_v2(secret_hook_id, secret_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretHooksApi->secret_hooks_service_update_hook_v2: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Secret Hook
        api_response = api_instance.secret_hooks_service_update_hook_v2(secret_hook_id, secret_id, secret_detail_hook_update_args=secret_detail_hook_update_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretHooksApi->secret_hooks_service_update_hook_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_hook_id** | **int**| secretHookId |
 **secret_id** | **int**| secretId |
 **secret_detail_hook_update_args** | [**SecretDetailHookUpdateArgs**](SecretDetailHookUpdateArgs.md)| args | [optional]

### Return type

[**SecretDetailHookModel**](SecretDetailHookModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret hook retrieved after updates |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

