# plugins.SecretAccessRequestsApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**secret_access_requests_service_create_request**](SecretAccessRequestsApi.md#secret_access_requests_service_create_request) | **POST** /v1/secret-access-requests | Create a new Secret Access Request
[**secret_access_requests_service_create_view_comment**](SecretAccessRequestsApi.md#secret_access_requests_service_create_view_comment) | **POST** /v1/secret-access-requests/secrets/{id}/view-comment | Create a new View Comment on a secret.
[**secret_access_requests_service_get_history**](SecretAccessRequestsApi.md#secret_access_requests_service_get_history) | **GET** /v1/secret-access-requests/{id}/history | Get Secret access request history for the user that created the request.
[**secret_access_requests_service_get_options_by_secret**](SecretAccessRequestsApi.md#secret_access_requests_service_get_options_by_secret) | **GET** /v1/secret-access-requests/secrets/{id}/options | Get Secret Access Options by Secret ID
[**secret_access_requests_service_get_pending_request**](SecretAccessRequestsApi.md#secret_access_requests_service_get_pending_request) | **GET** /v1/secret-access-requests/{id}/pending | Get Secret Access Request with Current and Eligible Reviewers by ID
[**secret_access_requests_service_get_request**](SecretAccessRequestsApi.md#secret_access_requests_service_get_request) | **GET** /v1/secret-access-requests/{id} | Get Secret Access Request by ID
[**secret_access_requests_service_get_requests_for_secret**](SecretAccessRequestsApi.md#secret_access_requests_service_get_requests_for_secret) | **GET** /v1/secret-access-requests/secrets/{id} | Get Secret Access Requests by Status for Current User.
[**secret_access_requests_service_search_requests**](SecretAccessRequestsApi.md#secret_access_requests_service_search_requests) | **GET** /v1/secret-access-requests | Search Secret Access Requests by Status for Current User.
[**secret_access_requests_service_update_request**](SecretAccessRequestsApi.md#secret_access_requests_service_update_request) | **PUT** /v1/secret-access-requests | Update a Secret Access Request


# **secret_access_requests_service_create_request**
> SecretAccessModel secret_access_requests_service_create_request()

Create a new Secret Access Request

Create a new Secret Access Request

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_access_requests_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.secret_access_create_args import SecretAccessCreateArgs
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_access_model import SecretAccessModel
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
    api_instance = secret_access_requests_api.SecretAccessRequestsApi(api_client)
    secret_access_create_args = SecretAccessCreateArgs(
        expiration_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        request_comment="request_comment_example",
        secret_id=1,
        start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ticket_number="ticket_number_example",
        ticket_system_id=1,
    ) # SecretAccessCreateArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new Secret Access Request
        api_response = api_instance.secret_access_requests_service_create_request(secret_access_create_args=secret_access_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretAccessRequestsApi->secret_access_requests_service_create_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_access_create_args** | [**SecretAccessCreateArgs**](SecretAccessCreateArgs.md)| args | [optional]

### Return type

[**SecretAccessModel**](SecretAccessModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Access Model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_access_requests_service_create_view_comment**
> bool secret_access_requests_service_create_view_comment(id)

Create a new View Comment on a secret.

Create a new View Comment on a secret.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_access_requests_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_access_view_comment_args import SecretAccessViewCommentArgs
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
    api_instance = secret_access_requests_api.SecretAccessRequestsApi(api_client)
    id = 1 # int | Secret ID
    secret_access_view_comment_args = SecretAccessViewCommentArgs(
        comment="comment_example",
        ticket_number="ticket_number_example",
        ticket_system_id=1,
    ) # SecretAccessViewCommentArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new View Comment on a secret.
        api_response = api_instance.secret_access_requests_service_create_view_comment(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretAccessRequestsApi->secret_access_requests_service_create_view_comment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new View Comment on a secret.
        api_response = api_instance.secret_access_requests_service_create_view_comment(id, secret_access_view_comment_args=secret_access_view_comment_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretAccessRequestsApi->secret_access_requests_service_create_view_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Secret ID |
 **secret_access_view_comment_args** | [**SecretAccessViewCommentArgs**](SecretAccessViewCommentArgs.md)| args | [optional]

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
**200** | Success or Failure of the save. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_access_requests_service_get_history**
> PagingOfSecretAccessRequestHistoryModel secret_access_requests_service_get_history(id)

Get Secret access request history for the user that created the request.

Get Secret access request history for the user that created the request.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_access_requests_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_secret_access_request_history_model import PagingOfSecretAccessRequestHistoryModel
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
    api_instance = secret_access_requests_api.SecretAccessRequestsApi(api_client)
    id = 1 # int | Secret Access Request Id
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Secret access request history for the user that created the request.
        api_response = api_instance.secret_access_requests_service_get_history(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretAccessRequestsApi->secret_access_requests_service_get_history: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Secret access request history for the user that created the request.
        api_response = api_instance.secret_access_requests_service_get_history(id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretAccessRequestsApi->secret_access_requests_service_get_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Secret Access Request Id |
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfSecretAccessRequestHistoryModel**](PagingOfSecretAccessRequestHistoryModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Access Request History Model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_access_requests_service_get_options_by_secret**
> SecretAccessOptionsModel secret_access_requests_service_get_options_by_secret(id)

Get Secret Access Options by Secret ID

Get Secret Access Options by Secret ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_access_requests_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.secret_access_options_model import SecretAccessOptionsModel
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
    api_instance = secret_access_requests_api.SecretAccessRequestsApi(api_client)
    id = 1 # int | Secret ID

    # example passing only required values which don't have defaults set
    try:
        # Get Secret Access Options by Secret ID
        api_response = api_instance.secret_access_requests_service_get_options_by_secret(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretAccessRequestsApi->secret_access_requests_service_get_options_by_secret: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Secret ID |

### Return type

[**SecretAccessOptionsModel**](SecretAccessOptionsModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Access Request Options |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_access_requests_service_get_pending_request**
> SecretAccessPendingRequestModel secret_access_requests_service_get_pending_request(id)

Get Secret Access Request with Current and Eligible Reviewers by ID

Get Secret Access Request by ID. Will also get a lists of current and eligible approvers if the request is in a Pending state

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_access_requests_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_access_pending_request_model import SecretAccessPendingRequestModel
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
    api_instance = secret_access_requests_api.SecretAccessRequestsApi(api_client)
    id = 1 # int | Secret Access ID

    # example passing only required values which don't have defaults set
    try:
        # Get Secret Access Request with Current and Eligible Reviewers by ID
        api_response = api_instance.secret_access_requests_service_get_pending_request(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretAccessRequestsApi->secret_access_requests_service_get_pending_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Secret Access ID |

### Return type

[**SecretAccessPendingRequestModel**](SecretAccessPendingRequestModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Access Model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_access_requests_service_get_request**
> SecretAccessModel secret_access_requests_service_get_request(id)

Get Secret Access Request by ID

Get Secret Access Request by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_access_requests_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_access_model import SecretAccessModel
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
    api_instance = secret_access_requests_api.SecretAccessRequestsApi(api_client)
    id = 1 # int | Secret Access ID

    # example passing only required values which don't have defaults set
    try:
        # Get Secret Access Request by ID
        api_response = api_instance.secret_access_requests_service_get_request(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretAccessRequestsApi->secret_access_requests_service_get_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Secret Access ID |

### Return type

[**SecretAccessModel**](SecretAccessModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Access Model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_access_requests_service_get_requests_for_secret**
> PagingOfSecretAccessModel secret_access_requests_service_get_requests_for_secret(id)

Get Secret Access Requests by Status for Current User.

Get Secret Access Requests by Status for Current User.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_access_requests_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_secret_access_model import PagingOfSecretAccessModel
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
    api_instance = secret_access_requests_api.SecretAccessRequestsApi(api_client)
    id = 1 # int | Secret ID
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Secret Access Requests by Status for Current User.
        api_response = api_instance.secret_access_requests_service_get_requests_for_secret(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretAccessRequestsApi->secret_access_requests_service_get_requests_for_secret: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Secret Access Requests by Status for Current User.
        api_response = api_instance.secret_access_requests_service_get_requests_for_secret(id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretAccessRequestsApi->secret_access_requests_service_get_requests_for_secret: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Secret ID |
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfSecretAccessModel**](PagingOfSecretAccessModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Access Model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_access_requests_service_search_requests**
> PagingOfSecretAccessModel secret_access_requests_service_search_requests()

Search Secret Access Requests by Status for Current User.

Search Secret Access Requests by Status for Current User.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_access_requests_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_secret_access_model import PagingOfSecretAccessModel
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
    api_instance = secret_access_requests_api.SecretAccessRequestsApi(api_client)
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
        # Search Secret Access Requests by Status for Current User.
        api_response = api_instance.secret_access_requests_service_search_requests(filter_is_my_request=filter_is_my_request, filter_status=filter_status, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretAccessRequestsApi->secret_access_requests_service_search_requests: %s\n" % e)
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

[**PagingOfSecretAccessModel**](PagingOfSecretAccessModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Access Model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_access_requests_service_update_request**
> SecretAccessActionResultModel secret_access_requests_service_update_request()

Update a Secret Access Request

Update the start date, end date, and status for a request.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_access_requests_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_access_action_result_model import SecretAccessActionResultModel
from plugins.model.secret_access_update_args import SecretAccessUpdateArgs
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
    api_instance = secret_access_requests_api.SecretAccessRequestsApi(api_client)
    secret_access_update_args = SecretAccessUpdateArgs(
        expiration_date=DateTimeOffset(
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
        secret_access_request_id=1,
        start_date=DateTimeOffset(
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
        status=SecretAccessModelStatus("Pending"),
    ) # SecretAccessUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Secret Access Request
        api_response = api_instance.secret_access_requests_service_update_request(secret_access_update_args=secret_access_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretAccessRequestsApi->secret_access_requests_service_update_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_access_update_args** | [**SecretAccessUpdateArgs**](SecretAccessUpdateArgs.md)| args | [optional]

### Return type

[**SecretAccessActionResultModel**](SecretAccessActionResultModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Access Action Result Model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

