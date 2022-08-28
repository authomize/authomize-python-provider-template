# secret_server_openapiclient.SecretAccessRequestsApi

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
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_access_requests_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.secret_access_create_args import SecretAccessCreateArgs
from secret_server_openapiclient.model.secret_access_model import SecretAccessModel
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
    api_instance = secret_access_requests_api.SecretAccessRequestsApi(api_client)
    secret_access_create_args = SecretAccessCreateArgs(
        expiration_date=None,
        request_comment=None,
        secret_id=None,
        start_date=None,
        ticket_number=None,
        ticket_system_id=None,
    ) # SecretAccessCreateArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new Secret Access Request
        api_response = api_instance.secret_access_requests_service_create_request(secret_access_create_args=secret_access_create_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
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
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_access_requests_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.secret_access_view_comment_args import SecretAccessViewCommentArgs
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
    api_instance = secret_access_requests_api.SecretAccessRequestsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret ID
    secret_access_view_comment_args = SecretAccessViewCommentArgs(
        comment=None,
        ticket_number=None,
        ticket_system_id=None,
    ) # SecretAccessViewCommentArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new View Comment on a secret.
        api_response = api_instance.secret_access_requests_service_create_view_comment(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretAccessRequestsApi->secret_access_requests_service_create_view_comment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new View Comment on a secret.
        api_response = api_instance.secret_access_requests_service_create_view_comment(id, secret_access_view_comment_args=secret_access_view_comment_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretAccessRequestsApi->secret_access_requests_service_create_view_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret ID |
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
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_access_requests_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.paging_of_secret_access_request_history_model import PagingOfSecretAccessRequestHistoryModel
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
    api_instance = secret_access_requests_api.SecretAccessRequestsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret Access Request Id
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Secret access request history for the user that created the request.
        api_response = api_instance.secret_access_requests_service_get_history(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretAccessRequestsApi->secret_access_requests_service_get_history: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Secret access request history for the user that created the request.
        api_response = api_instance.secret_access_requests_service_get_history(id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretAccessRequestsApi->secret_access_requests_service_get_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret Access Request Id |
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

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
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_access_requests_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.secret_access_options_model import SecretAccessOptionsModel
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
    api_instance = secret_access_requests_api.SecretAccessRequestsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret ID

    # example passing only required values which don't have defaults set
    try:
        # Get Secret Access Options by Secret ID
        api_response = api_instance.secret_access_requests_service_get_options_by_secret(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretAccessRequestsApi->secret_access_requests_service_get_options_by_secret: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret ID |

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
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_access_requests_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.secret_access_pending_request_model import SecretAccessPendingRequestModel
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
    api_instance = secret_access_requests_api.SecretAccessRequestsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret Access ID

    # example passing only required values which don't have defaults set
    try:
        # Get Secret Access Request with Current and Eligible Reviewers by ID
        api_response = api_instance.secret_access_requests_service_get_pending_request(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretAccessRequestsApi->secret_access_requests_service_get_pending_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret Access ID |

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
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_access_requests_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.secret_access_model import SecretAccessModel
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
    api_instance = secret_access_requests_api.SecretAccessRequestsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret Access ID

    # example passing only required values which don't have defaults set
    try:
        # Get Secret Access Request by ID
        api_response = api_instance.secret_access_requests_service_get_request(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretAccessRequestsApi->secret_access_requests_service_get_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret Access ID |

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
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_access_requests_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.paging_of_secret_access_model import PagingOfSecretAccessModel
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
    api_instance = secret_access_requests_api.SecretAccessRequestsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret ID
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Secret Access Requests by Status for Current User.
        api_response = api_instance.secret_access_requests_service_get_requests_for_secret(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretAccessRequestsApi->secret_access_requests_service_get_requests_for_secret: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Secret Access Requests by Status for Current User.
        api_response = api_instance.secret_access_requests_service_get_requests_for_secret(id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretAccessRequestsApi->secret_access_requests_service_get_requests_for_secret: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret ID |
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

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
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_access_requests_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.paging_of_secret_access_model import PagingOfSecretAccessModel
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
    api_instance = secret_access_requests_api.SecretAccessRequestsApi(api_client)
    filter_is_my_request = True # bool | IsMyRequest (optional)
    filter_status = None # bool, date, datetime, dict, float, int, list, str, none_type | Status (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Secret Access Requests by Status for Current User.
        api_response = api_instance.secret_access_requests_service_search_requests(filter_is_my_request=filter_is_my_request, filter_status=filter_status, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretAccessRequestsApi->secret_access_requests_service_search_requests: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_is_my_request** | **bool**| IsMyRequest | [optional]
 **filter_status** | **bool, date, datetime, dict, float, int, list, str, none_type**| Status | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

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
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_access_requests_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.secret_access_update_args import SecretAccessUpdateArgs
from secret_server_openapiclient.model.secret_access_action_result_model import SecretAccessActionResultModel
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
    api_instance = secret_access_requests_api.SecretAccessRequestsApi(api_client)
    secret_access_update_args = SecretAccessUpdateArgs(
        expiration_date=DateTimeOffset(
            date=None,
            date_time=None,
            day=None,
            day_of_week=DayOfWeek("{}"),
            day_of_year=None,
            hour=None,
            local_date_time=None,
            millisecond=None,
            minute=None,
            month=None,
            offset=None,
            second=None,
            ticks=None,
            time_of_day=None,
            utc_date_time=None,
            utc_ticks=None,
            year=None,
        ),
        response_comment=None,
        secret_access_request_id=None,
        start_date=DateTimeOffset(
            date=None,
            date_time=None,
            day=None,
            day_of_week=DayOfWeek("{}"),
            day_of_year=None,
            hour=None,
            local_date_time=None,
            millisecond=None,
            minute=None,
            month=None,
            offset=None,
            second=None,
            ticks=None,
            time_of_day=None,
            utc_date_time=None,
            utc_ticks=None,
            year=None,
        ),
        status=SecretAccessModelStatus("Pending"),
    ) # SecretAccessUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Secret Access Request
        api_response = api_instance.secret_access_requests_service_update_request(secret_access_update_args=secret_access_update_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
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

