# secret_server_openapiclient.LauncherAgentsApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**launcher_agents_service_create_collection**](LauncherAgentsApi.md#launcher_agents_service_create_collection) | **POST** /v1/launcheragents/collections | Create Launcher Agent Collection
[**launcher_agents_service_get**](LauncherAgentsApi.md#launcher_agents_service_get) | **GET** /v1/launcheragents/{id} | Get Launcher Agent 
[**launcher_agents_service_get_by_collection_id**](LauncherAgentsApi.md#launcher_agents_service_get_by_collection_id) | **GET** /v1/launcheragents/collections/{id} | Get Launcher Agent Collection
[**launcher_agents_service_search**](LauncherAgentsApi.md#launcher_agents_service_search) | **GET** /v1/launcheragents | Search Launcher Agents
[**launcher_agents_service_search_agents_with_issues**](LauncherAgentsApi.md#launcher_agents_service_search_agents_with_issues) | **GET** /v1/launcheragents/issues | Search Launcher Agents with Issues
[**launcher_agents_service_search_collections**](LauncherAgentsApi.md#launcher_agents_service_search_collections) | **GET** /v1/launcheragents/collections | Search Launcher Agent Collections
[**launcher_agents_service_stub**](LauncherAgentsApi.md#launcher_agents_service_stub) | **GET** /v1/launcheragents/collections/stub | Get Launcher Agent Collection Stub
[**launcher_agents_service_update**](LauncherAgentsApi.md#launcher_agents_service_update) | **PUT** /v1/launcheragents/{id} | Update Launcher Agent 
[**launcher_agents_service_update_collection**](LauncherAgentsApi.md#launcher_agents_service_update_collection) | **PUT** /v1/launcheragents/collections/{id} | Update Launcher Agent Collection


# **launcher_agents_service_create_collection**
> LauncherAgentCollectionModel launcher_agents_service_create_collection()

Create Launcher Agent Collection

Create a new Launcher Agent Collection

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import launcher_agents_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.launcher_agent_collection_create_args import LauncherAgentCollectionCreateArgs
from secret_server_openapiclient.model.launcher_agent_collection_model import LauncherAgentCollectionModel
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
    api_instance = launcher_agents_api.LauncherAgentsApi(api_client)
    launcher_agent_collection_create_args = LauncherAgentCollectionCreateArgs(
        name="name_example",
        record_keystrokes=True,
        record_standalone_sessions=True,
    ) # LauncherAgentCollectionCreateArgs | Launcher Agent Collection creation options (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Launcher Agent Collection
        api_response = api_instance.launcher_agents_service_create_collection(launcher_agent_collection_create_args=launcher_agent_collection_create_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling LauncherAgentsApi->launcher_agents_service_create_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **launcher_agent_collection_create_args** | [**LauncherAgentCollectionCreateArgs**](LauncherAgentCollectionCreateArgs.md)| Launcher Agent Collection creation options | [optional]

### Return type

[**LauncherAgentCollectionModel**](LauncherAgentCollectionModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Launcher Agent Collection object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **launcher_agents_service_get**
> LauncherAgentModel launcher_agents_service_get(id)

Get Launcher Agent 

Get a single Launcher Agent  by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import launcher_agents_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.launcher_agent_model import LauncherAgentModel
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
    api_instance = launcher_agents_api.LauncherAgentsApi(api_client)
    id = 1 # int | Launcher Agent ID
    include_inactive = True # bool | Whether to include inactive Launcher Agents in the results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Launcher Agent 
        api_response = api_instance.launcher_agents_service_get(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling LauncherAgentsApi->launcher_agents_service_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Launcher Agent 
        api_response = api_instance.launcher_agents_service_get(id, include_inactive=include_inactive)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling LauncherAgentsApi->launcher_agents_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Launcher Agent ID |
 **include_inactive** | **bool**| Whether to include inactive Launcher Agents in the results | [optional]

### Return type

[**LauncherAgentModel**](LauncherAgentModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LauncherAgent object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **launcher_agents_service_get_by_collection_id**
> LauncherAgentCollectionModel launcher_agents_service_get_by_collection_id(id)

Get Launcher Agent Collection

Get a single Launcher Agent Collection by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import launcher_agents_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.launcher_agent_collection_model import LauncherAgentCollectionModel
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
    api_instance = launcher_agents_api.LauncherAgentsApi(api_client)
    id = 1 # int | Launcher Agent Collection ID
    include_inactive = True # bool | Whether to include inactive Launcher Agent Collections in the results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Launcher Agent Collection
        api_response = api_instance.launcher_agents_service_get_by_collection_id(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling LauncherAgentsApi->launcher_agents_service_get_by_collection_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Launcher Agent Collection
        api_response = api_instance.launcher_agents_service_get_by_collection_id(id, include_inactive=include_inactive)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling LauncherAgentsApi->launcher_agents_service_get_by_collection_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Launcher Agent Collection ID |
 **include_inactive** | **bool**| Whether to include inactive Launcher Agent Collections in the results | [optional]

### Return type

[**LauncherAgentCollectionModel**](LauncherAgentCollectionModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LauncherAgentCollection object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **launcher_agents_service_search**
> PagingOfLauncherAgentSummary launcher_agents_service_search()

Search Launcher Agents

Search, filter, sort, and page Launcher Agent s

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import launcher_agents_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.paging_of_launcher_agent_summary import PagingOfLauncherAgentSummary
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
    api_instance = launcher_agents_api.LauncherAgentsApi(api_client)
    filter_include_inactive = True # bool | IncludeInactive (optional)
    filter_launcher_agent_collection_id = 1 # int | LauncherAgentCollectionId (optional)
    filter_out_of_date = True # bool | OutOfDate (optional)
    filter_search_text = "filter.searchText_example" # str | SearchText (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Launcher Agents
        api_response = api_instance.launcher_agents_service_search(filter_include_inactive=filter_include_inactive, filter_launcher_agent_collection_id=filter_launcher_agent_collection_id, filter_out_of_date=filter_out_of_date, filter_search_text=filter_search_text, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling LauncherAgentsApi->launcher_agents_service_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_include_inactive** | **bool**| IncludeInactive | [optional]
 **filter_launcher_agent_collection_id** | **int**| LauncherAgentCollectionId | [optional]
 **filter_out_of_date** | **bool**| OutOfDate | [optional]
 **filter_search_text** | **str**| SearchText | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfLauncherAgentSummary**](PagingOfLauncherAgentSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Launcher Agent  search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **launcher_agents_service_search_agents_with_issues**
> PagingOfLauncherAgentSummary launcher_agents_service_search_agents_with_issues()

Search Launcher Agents with Issues

Search, filter, sort, and page Launcher Agent with issues

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import launcher_agents_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.paging_of_launcher_agent_summary import PagingOfLauncherAgentSummary
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
    api_instance = launcher_agents_api.LauncherAgentsApi(api_client)
    filter_launcher_agent_collection_id = 1 # int | LauncherAgentCollectionId (optional)
    filter_search_text = "filter.searchText_example" # str | SearchText (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Launcher Agents with Issues
        api_response = api_instance.launcher_agents_service_search_agents_with_issues(filter_launcher_agent_collection_id=filter_launcher_agent_collection_id, filter_search_text=filter_search_text, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling LauncherAgentsApi->launcher_agents_service_search_agents_with_issues: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_launcher_agent_collection_id** | **int**| LauncherAgentCollectionId | [optional]
 **filter_search_text** | **str**| SearchText | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfLauncherAgentSummary**](PagingOfLauncherAgentSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Launcher Agent search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **launcher_agents_service_search_collections**
> PagingOfLauncherAgentCollectionSummary launcher_agents_service_search_collections()

Search Launcher Agent Collections

Search, filter, sort, and page Launcher Agent Collections

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import launcher_agents_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.paging_of_launcher_agent_collection_summary import PagingOfLauncherAgentCollectionSummary
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
    api_instance = launcher_agents_api.LauncherAgentsApi(api_client)
    filter_include_inactive = True # bool | Whether to include inactive Launcher Agent Collections in the results (optional)
    filter_search_text = "filter.searchText_example" # str | Search text (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Launcher Agent Collections
        api_response = api_instance.launcher_agents_service_search_collections(filter_include_inactive=filter_include_inactive, filter_search_text=filter_search_text, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling LauncherAgentsApi->launcher_agents_service_search_collections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_include_inactive** | **bool**| Whether to include inactive Launcher Agent Collections in the results | [optional]
 **filter_search_text** | **str**| Search text | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfLauncherAgentCollectionSummary**](PagingOfLauncherAgentCollectionSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Launcher Agent Collection search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **launcher_agents_service_stub**
> LauncherAgentCollectionModel launcher_agents_service_stub()

Get Launcher Agent Collection Stub

Return the default values for a new Launcher Agent Collection

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import launcher_agents_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.launcher_agent_collection_model import LauncherAgentCollectionModel
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
    api_instance = launcher_agents_api.LauncherAgentsApi(api_client)
    include_inactive = True # bool | IncludeInactive (optional)
    search_text = "searchText_example" # str | SearchText (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Launcher Agent Collection Stub
        api_response = api_instance.launcher_agents_service_stub(include_inactive=include_inactive, search_text=search_text)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling LauncherAgentsApi->launcher_agents_service_stub: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_inactive** | **bool**| IncludeInactive | [optional]
 **search_text** | **str**| SearchText | [optional]

### Return type

[**LauncherAgentCollectionModel**](LauncherAgentCollectionModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Launcher Agent Collection object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **launcher_agents_service_update**
> LauncherAgentModel launcher_agents_service_update(id)

Update Launcher Agent 

Update a single Launcher Agent by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import launcher_agents_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.launcher_agent_update_args import LauncherAgentUpdateArgs
from secret_server_openapiclient.model.launcher_agent_model import LauncherAgentModel
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
    api_instance = launcher_agents_api.LauncherAgentsApi(api_client)
    id = 1 # int | Launcher Agent ID
    launcher_agent_update_args = LauncherAgentUpdateArgs(
        active=True,
        id=1,
        record_keystrokes=True,
        record_standalone_sessions=True,
    ) # LauncherAgentUpdateArgs | Launcher Agent update options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Launcher Agent 
        api_response = api_instance.launcher_agents_service_update(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling LauncherAgentsApi->launcher_agents_service_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Launcher Agent 
        api_response = api_instance.launcher_agents_service_update(id, launcher_agent_update_args=launcher_agent_update_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling LauncherAgentsApi->launcher_agents_service_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Launcher Agent ID |
 **launcher_agent_update_args** | [**LauncherAgentUpdateArgs**](LauncherAgentUpdateArgs.md)| Launcher Agent update options | [optional]

### Return type

[**LauncherAgentModel**](LauncherAgentModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Launcher Agent object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **launcher_agents_service_update_collection**
> LauncherAgentCollectionModel launcher_agents_service_update_collection(id)

Update Launcher Agent Collection

Update a single Launcher Agent Collection by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import launcher_agents_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.launcher_agent_collection_model import LauncherAgentCollectionModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.launcher_agent_collection_update_args import LauncherAgentCollectionUpdateArgs
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
    api_instance = launcher_agents_api.LauncherAgentsApi(api_client)
    id = 1 # int | Launcher Agent Collection ID
    launcher_agent_collection_update_args = LauncherAgentCollectionUpdateArgs(
        active=True,
        id=1,
        name="name_example",
        record_keystrokes=True,
        record_standalone_sessions=True,
    ) # LauncherAgentCollectionUpdateArgs | Launcher Agent Collection update options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Launcher Agent Collection
        api_response = api_instance.launcher_agents_service_update_collection(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling LauncherAgentsApi->launcher_agents_service_update_collection: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Launcher Agent Collection
        api_response = api_instance.launcher_agents_service_update_collection(id, launcher_agent_collection_update_args=launcher_agent_collection_update_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling LauncherAgentsApi->launcher_agents_service_update_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Launcher Agent Collection ID |
 **launcher_agent_collection_update_args** | [**LauncherAgentCollectionUpdateArgs**](LauncherAgentCollectionUpdateArgs.md)| Launcher Agent Collection update options | [optional]

### Return type

[**LauncherAgentCollectionModel**](LauncherAgentCollectionModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Launcher Agent Collection object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

