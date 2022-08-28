# plugins.SecretEraseRequestsApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**secret_erase_requests_service_create_request**](SecretEraseRequestsApi.md#secret_erase_requests_service_create_request) | **POST** /v1/secret-erase-requests | Create a new Secret Erase Request
[**secret_erase_requests_service_get_history**](SecretEraseRequestsApi.md#secret_erase_requests_service_get_history) | **GET** /v1/secret-erase-requests/{id}/history | Get Secret Erase History by Secret Erase Request ID
[**secret_erase_requests_service_get_request**](SecretEraseRequestsApi.md#secret_erase_requests_service_get_request) | **GET** /v1/secret-erase-requests/{id} | Get Secret Erase Request by ID
[**secret_erase_requests_service_get_request_secrets**](SecretEraseRequestsApi.md#secret_erase_requests_service_get_request_secrets) | **GET** /v1/secret-erase-requests/secrets | Get Secret Erase Request Secrets by Secret Erase Request ID
[**secret_erase_requests_service_inbox_search**](SecretEraseRequestsApi.md#secret_erase_requests_service_inbox_search) | **GET** /v1/secret-erase-requests/inbox | Get Secret Erase Requests by Status for Current User.
[**secret_erase_requests_service_process_now**](SecretEraseRequestsApi.md#secret_erase_requests_service_process_now) | **GET** /v1/secret-erase-requests/run-now | Process approved SecretEraseRequests whose EraseAfter time has passed.
[**secret_erase_requests_service_search**](SecretEraseRequestsApi.md#secret_erase_requests_service_search) | **GET** /v1/secret-erase-requests/search | Search Secret Erase Requests by Status for Current User.
[**secret_erase_requests_service_update_request**](SecretEraseRequestsApi.md#secret_erase_requests_service_update_request) | **PUT** /v1/secret-erase-requests | Update a Secret Erase Request


# **secret_erase_requests_service_create_request**
> SecretEraseRequestActionResultModel secret_erase_requests_service_create_request()

Create a new Secret Erase Request

Create a new Secret Erase Request

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_erase_requests_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_erase_request_create_args import SecretEraseRequestCreateArgs
from plugins.model.secret_erase_request_action_result_model import SecretEraseRequestActionResultModel
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
    api_instance = secret_erase_requests_api.SecretEraseRequestsApi(api_client)
    secret_erase_request_create_args = SecretEraseRequestCreateArgs(
        erase_after=dateutil_parser('1970-01-01T00:00:00.00Z'),
        request_comment="request_comment_example",
        secret_ids=[
            1,
        ],
    ) # SecretEraseRequestCreateArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new Secret Erase Request
        api_response = api_instance.secret_erase_requests_service_create_request(secret_erase_request_create_args=secret_erase_request_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretEraseRequestsApi->secret_erase_requests_service_create_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_erase_request_create_args** | [**SecretEraseRequestCreateArgs**](SecretEraseRequestCreateArgs.md)| args | [optional]

### Return type

[**SecretEraseRequestActionResultModel**](SecretEraseRequestActionResultModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Erase Request Model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_erase_requests_service_get_history**
> PagingOfSecretEraseRequestHistoryModel secret_erase_requests_service_get_history(id)

Get Secret Erase History by Secret Erase Request ID

Get Secret Erase History by Secret Erase Request ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_erase_requests_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.paging_of_secret_erase_request_history_model import PagingOfSecretEraseRequestHistoryModel
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
    api_instance = secret_erase_requests_api.SecretEraseRequestsApi(api_client)
    id = 1 # int | Secret Erase Request ID
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Secret Erase History by Secret Erase Request ID
        api_response = api_instance.secret_erase_requests_service_get_history(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretEraseRequestsApi->secret_erase_requests_service_get_history: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Secret Erase History by Secret Erase Request ID
        api_response = api_instance.secret_erase_requests_service_get_history(id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretEraseRequestsApi->secret_erase_requests_service_get_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Secret Erase Request ID |
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfSecretEraseRequestHistoryModel**](PagingOfSecretEraseRequestHistoryModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Erase Request Model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_erase_requests_service_get_request**
> SecretEraseRequestModel secret_erase_requests_service_get_request(id)

Get Secret Erase Request by ID

Get Secret Erase Request by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_erase_requests_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.secret_erase_request_model import SecretEraseRequestModel
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
    api_instance = secret_erase_requests_api.SecretEraseRequestsApi(api_client)
    id = 1 # int | Secret Erase Request ID

    # example passing only required values which don't have defaults set
    try:
        # Get Secret Erase Request by ID
        api_response = api_instance.secret_erase_requests_service_get_request(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretEraseRequestsApi->secret_erase_requests_service_get_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Secret Erase Request ID |

### Return type

[**SecretEraseRequestModel**](SecretEraseRequestModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Erase Request Model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_erase_requests_service_get_request_secrets**
> PagingOfSecretEraseRequestSecretModel secret_erase_requests_service_get_request_secrets()

Get Secret Erase Request Secrets by Secret Erase Request ID

Get Secret Erase Request Secrets by Secret Erase Request ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_erase_requests_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_secret_erase_request_secret_model import PagingOfSecretEraseRequestSecretModel
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
    api_instance = secret_erase_requests_api.SecretEraseRequestsApi(api_client)
    filter_erased = True # bool | Erased (optional)
    filter_secret_erase_request_id = 1 # int | SecretEraseRequestId (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Secret Erase Request Secrets by Secret Erase Request ID
        api_response = api_instance.secret_erase_requests_service_get_request_secrets(filter_erased=filter_erased, filter_secret_erase_request_id=filter_secret_erase_request_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretEraseRequestsApi->secret_erase_requests_service_get_request_secrets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_erased** | **bool**| Erased | [optional]
 **filter_secret_erase_request_id** | **int**| SecretEraseRequestId | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfSecretEraseRequestSecretModel**](PagingOfSecretEraseRequestSecretModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Erase Request Secret Model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_erase_requests_service_inbox_search**
> PagingOfSecretEraseRequestModel secret_erase_requests_service_inbox_search()

Get Secret Erase Requests by Status for Current User.

Get Secret Erase Requests by Status for Current User.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_erase_requests_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.paging_of_secret_erase_request_model import PagingOfSecretEraseRequestModel
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
    api_instance = secret_erase_requests_api.SecretEraseRequestsApi(api_client)
    filter_is_my_request = True # bool | IsMyRequest (optional)
    filter_status = "filter.status_example" # str | Status (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Secret Erase Requests by Status for Current User.
        api_response = api_instance.secret_erase_requests_service_inbox_search(filter_is_my_request=filter_is_my_request, filter_status=filter_status, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretEraseRequestsApi->secret_erase_requests_service_inbox_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_is_my_request** | **bool**| IsMyRequest | [optional]
 **filter_status** | **str**| Status | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfSecretEraseRequestModel**](PagingOfSecretEraseRequestModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Erase Request Model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_erase_requests_service_process_now**
> bool secret_erase_requests_service_process_now()

Process approved SecretEraseRequests whose EraseAfter time has passed.

Process approved SecretEraseRequests whose EraseAfter time has passed.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_erase_requests_api
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
    api_instance = secret_erase_requests_api.SecretEraseRequestsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Process approved SecretEraseRequests whose EraseAfter time has passed.
        api_response = api_instance.secret_erase_requests_service_process_now()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretEraseRequestsApi->secret_erase_requests_service_process_now: %s\n" % e)
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
**200** | Attempt to process ready requests. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_erase_requests_service_search**
> PagingOfSecretEraseRequestModel secret_erase_requests_service_search()

Search Secret Erase Requests by Status for Current User.

Search Secret Erase Requests by Status for Current User.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_erase_requests_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.paging_of_secret_erase_request_model import PagingOfSecretEraseRequestModel
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
    api_instance = secret_erase_requests_api.SecretEraseRequestsApi(api_client)
    filter_is_my_request = True # bool | IsMyRequest (optional)
    filter_secret_id = 1 # int | SecretId (optional)
    filter_status = "filter.status_example" # str | Status (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Secret Erase Requests by Status for Current User.
        api_response = api_instance.secret_erase_requests_service_search(filter_is_my_request=filter_is_my_request, filter_secret_id=filter_secret_id, filter_status=filter_status, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretEraseRequestsApi->secret_erase_requests_service_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_is_my_request** | **bool**| IsMyRequest | [optional]
 **filter_secret_id** | **int**| SecretId | [optional]
 **filter_status** | **str**| Status | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfSecretEraseRequestModel**](PagingOfSecretEraseRequestModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Erase Request Model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_erase_requests_service_update_request**
> SecretEraseRequestActionResultModel secret_erase_requests_service_update_request()

Update a Secret Erase Request

Update a Secret Erase Request

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_erase_requests_api
from plugins.model.secret_erase_request_update_args import SecretEraseRequestUpdateArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_erase_request_action_result_model import SecretEraseRequestActionResultModel
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
    api_instance = secret_erase_requests_api.SecretEraseRequestsApi(api_client)
    secret_erase_request_update_args = SecretEraseRequestUpdateArgs(
        erase_after=OptionalDateTimeOffset(
            date=dateutil_parser('1970-01-01T00:00:00.00Z'),
            date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            day=1,
            day_of_week=DayOfWeek("{}"),
            day_of_year=1,
            hour=1,
            local_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            millisecond=1,
            minute=1,
            month=1,
            offset="offset_example",
            second=1,
            ticks=1,
            time_of_day="time_of_day_example",
            utc_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            utc_ticks=1,
            year=1,
        ),
        response_comment="response_comment_example",
        secret_erase_request_id=1,
        status=SecretEraseRequestModelStatus("Pending"),
    ) # SecretEraseRequestUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Secret Erase Request
        api_response = api_instance.secret_erase_requests_service_update_request(secret_erase_request_update_args=secret_erase_request_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretEraseRequestsApi->secret_erase_requests_service_update_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_erase_request_update_args** | [**SecretEraseRequestUpdateArgs**](SecretEraseRequestUpdateArgs.md)| args | [optional]

### Return type

[**SecretEraseRequestActionResultModel**](SecretEraseRequestActionResultModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Erase Request Model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

