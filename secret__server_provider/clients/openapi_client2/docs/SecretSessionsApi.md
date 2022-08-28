# plugins.SecretSessionsApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**secret_sessions_service_get**](SecretSessionsApi.md#secret_sessions_service_get) | **GET** /v1/recorded-sessions/{id} | Get Recorded Session
[**secret_sessions_service_get_session_recording**](SecretSessionsApi.md#secret_sessions_service_get_session_recording) | **GET** /v1/recorded-sessions/{id}/session-recordings | Recorded Session Video Stream
[**secret_sessions_service_get_summary**](SecretSessionsApi.md#secret_sessions_service_get_summary) | **GET** /v1/recorded-sessions/{id}/summary | Recorded Session Summary
[**secret_sessions_service_process_session**](SecretSessionsApi.md#secret_sessions_service_process_session) | **POST** /v1/recorded-sessions/{id}/request-processing | Request Immediate Session Processing
[**secret_sessions_service_search_points_of_interest**](SecretSessionsApi.md#secret_sessions_service_search_points_of_interest) | **GET** /v1/recorded-sessions/{id}/points-of-interest | Recorded Session Points of Interest
[**secret_sessions_service_search_points_of_interest_summary**](SecretSessionsApi.md#secret_sessions_service_search_points_of_interest_summary) | **GET** /v1/recorded-sessions/{id}/points-of-interest-summary | Recorded Session Points of Interest Summary
[**secret_sessions_service_search_sessions**](SecretSessionsApi.md#secret_sessions_service_search_sessions) | **GET** /v1/recorded-sessions | Search Recorded Sessions


# **secret_sessions_service_get**
> SecretSessionModel secret_sessions_service_get(id)

Get Recorded Session

Get a single recorded session by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_sessions_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_session_model import SecretSessionModel
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
    api_instance = secret_sessions_api.SecretSessionsApi(api_client)
    id = "id_example" # str | Recorded session ID

    # example passing only required values which don't have defaults set
    try:
        # Get Recorded Session
        api_response = api_instance.secret_sessions_service_get(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretSessionsApi->secret_sessions_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Recorded session ID |

### Return type

[**SecretSessionModel**](SecretSessionModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recorded session object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_sessions_service_get_session_recording**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} secret_sessions_service_get_session_recording(id)

Recorded Session Video Stream

Get the video stream for a recorded session

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_sessions_api
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
    api_instance = secret_sessions_api.SecretSessionsApi(api_client)
    id = "id_example" # str | Recorded session ID

    # example passing only required values which don't have defaults set
    try:
        # Recorded Session Video Stream
        api_response = api_instance.secret_sessions_service_get_session_recording(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretSessionsApi->secret_sessions_service_get_session_recording: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Recorded session ID |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recorded session video stream |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_sessions_service_get_summary**
> SecretSessionSummary secret_sessions_service_get_summary(id)

Recorded Session Summary

Get the summary for a recorded session

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_sessions_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_session_summary import SecretSessionSummary
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
    api_instance = secret_sessions_api.SecretSessionsApi(api_client)
    id = "id_example" # str | Recorded session ID

    # example passing only required values which don't have defaults set
    try:
        # Recorded Session Summary
        api_response = api_instance.secret_sessions_service_get_summary(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretSessionsApi->secret_sessions_service_get_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Recorded session ID |

### Return type

[**SecretSessionSummary**](SecretSessionSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recorded session summary |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_sessions_service_process_session**
> secret_sessions_service_process_session(id)

Request Immediate Session Processing

Issues a request for the immediate processing of a session video

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_sessions_api
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
    api_instance = secret_sessions_api.SecretSessionsApi(api_client)
    id = "id_example" # str | Recorded session ID

    # example passing only required values which don't have defaults set
    try:
        # Request Immediate Session Processing
        api_instance.secret_sessions_service_process_session(id)
    except plugins.ApiException as e:
        print("Exception when calling SecretSessionsApi->secret_sessions_service_process_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Recorded session ID |

### Return type

void (empty response body)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Unknown or empty response |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_sessions_service_search_points_of_interest**
> PagingOfSecretSessionPointOfInterestModel secret_sessions_service_search_points_of_interest(id)

Recorded Session Points of Interest

Get the points of interest for a recorded session

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_sessions_api
from plugins.model.paging_of_secret_session_point_of_interest_model import PagingOfSecretSessionPointOfInterestModel
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
    api_instance = secret_sessions_api.SecretSessionsApi(api_client)
    id = "id_example" # str | Recorded session ID
    filter_search_text = "filter.searchText_example" # str | Search text (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Recorded Session Points of Interest
        api_response = api_instance.secret_sessions_service_search_points_of_interest(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretSessionsApi->secret_sessions_service_search_points_of_interest: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Recorded Session Points of Interest
        api_response = api_instance.secret_sessions_service_search_points_of_interest(id, filter_search_text=filter_search_text, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretSessionsApi->secret_sessions_service_search_points_of_interest: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Recorded session ID |
 **filter_search_text** | **str**| Search text | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfSecretSessionPointOfInterestModel**](PagingOfSecretSessionPointOfInterestModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recorded session points of interest |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_sessions_service_search_points_of_interest_summary**
> PagingOfISecretSessionPointOfInterestSummaryModel secret_sessions_service_search_points_of_interest_summary(id)

Recorded Session Points of Interest Summary

Get the points of interest summary for a recorded session

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_sessions_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.paging_of_i_secret_session_point_of_interest_summary_model import PagingOfISecretSessionPointOfInterestSummaryModel
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
    api_instance = secret_sessions_api.SecretSessionsApi(api_client)
    id = "id_example" # str | Recorded session ID
    filter_search_text = "filter.searchText_example" # str | Search text (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Recorded Session Points of Interest Summary
        api_response = api_instance.secret_sessions_service_search_points_of_interest_summary(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretSessionsApi->secret_sessions_service_search_points_of_interest_summary: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Recorded Session Points of Interest Summary
        api_response = api_instance.secret_sessions_service_search_points_of_interest_summary(id, filter_search_text=filter_search_text, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretSessionsApi->secret_sessions_service_search_points_of_interest_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Recorded session ID |
 **filter_search_text** | **str**| Search text | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfISecretSessionPointOfInterestSummaryModel**](PagingOfISecretSessionPointOfInterestSummaryModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recorded session points of interest summary |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_sessions_service_search_sessions**
> PagingOfSecretSessionSummary secret_sessions_service_search_sessions()

Search Recorded Sessions

Search, filter, sort, and page recorded sessions

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_sessions_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.paging_of_secret_session_summary import PagingOfSecretSessionSummary
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
    api_instance = secret_sessions_api.SecretSessionsApi(api_client)
    filter_active = True # bool | Filter by active or inactive status (optional)
    filter_date_range = "filter.dateRange_example" # str | Return sessions within a certain number of days (optional)
    filter_end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | EndDate (optional)
    filter_end_time = "filter.endTime_example" # str | EndTime (optional)
    filter_folder_id = 1 # int | Filter by folder (optional)
    filter_group_ids = [
        1,
    ] # [int] | Return sessions for specific groups (optional)
    filter_include_non_secret_server_sessions = True # bool | IncludeNonSecretServerSessions (optional)
    filter_include_only_launched_successfully = True # bool | Return only sessions that launched successfully (optional)
    filter_include_restricted = True # bool | Whether to include restricted secret sessions (optional)
    filter_include_sub_folders = True # bool | Whether to include subfolders in a folder search (optional)
    filter_launcher_type_id = 1 # int | Filter by launcher type (optional)
    filter_search_text = "filter.searchText_example" # str | Search text (optional)
    filter_search_types = [
        "filter.searchTypes_example",
    ] # [str] | Specifies the sources of information you want to search across, can be many of (SecretItems, Username, Hostname, Domain, RdpKeystroke, RdpApplication, ProxyClient) (optional)
    filter_secret_ids = [
        1,
    ] # [int] | Return sessions for specific secrets (optional)
    filter_site_id = 1 # int | SiteId (optional)
    filter_start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | StartDate (optional)
    filter_start_time = "filter.startTime_example" # str | StartTime (optional)
    filter_user_ids = [
        1,
    ] # [int] | Return sessions for specific users (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Recorded Sessions
        api_response = api_instance.secret_sessions_service_search_sessions(filter_active=filter_active, filter_date_range=filter_date_range, filter_end_date=filter_end_date, filter_end_time=filter_end_time, filter_folder_id=filter_folder_id, filter_group_ids=filter_group_ids, filter_include_non_secret_server_sessions=filter_include_non_secret_server_sessions, filter_include_only_launched_successfully=filter_include_only_launched_successfully, filter_include_restricted=filter_include_restricted, filter_include_sub_folders=filter_include_sub_folders, filter_launcher_type_id=filter_launcher_type_id, filter_search_text=filter_search_text, filter_search_types=filter_search_types, filter_secret_ids=filter_secret_ids, filter_site_id=filter_site_id, filter_start_date=filter_start_date, filter_start_time=filter_start_time, filter_user_ids=filter_user_ids, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretSessionsApi->secret_sessions_service_search_sessions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_active** | **bool**| Filter by active or inactive status | [optional]
 **filter_date_range** | **str**| Return sessions within a certain number of days | [optional]
 **filter_end_date** | **datetime**| EndDate | [optional]
 **filter_end_time** | **str**| EndTime | [optional]
 **filter_folder_id** | **int**| Filter by folder | [optional]
 **filter_group_ids** | **[int]**| Return sessions for specific groups | [optional]
 **filter_include_non_secret_server_sessions** | **bool**| IncludeNonSecretServerSessions | [optional]
 **filter_include_only_launched_successfully** | **bool**| Return only sessions that launched successfully | [optional]
 **filter_include_restricted** | **bool**| Whether to include restricted secret sessions | [optional]
 **filter_include_sub_folders** | **bool**| Whether to include subfolders in a folder search | [optional]
 **filter_launcher_type_id** | **int**| Filter by launcher type | [optional]
 **filter_search_text** | **str**| Search text | [optional]
 **filter_search_types** | **[str]**| Specifies the sources of information you want to search across, can be many of (SecretItems, Username, Hostname, Domain, RdpKeystroke, RdpApplication, ProxyClient) | [optional]
 **filter_secret_ids** | **[int]**| Return sessions for specific secrets | [optional]
 **filter_site_id** | **int**| SiteId | [optional]
 **filter_start_date** | **datetime**| StartDate | [optional]
 **filter_start_time** | **str**| StartTime | [optional]
 **filter_user_ids** | **[int]**| Return sessions for specific users | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfSecretSessionSummary**](PagingOfSecretSessionSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recorded session search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

