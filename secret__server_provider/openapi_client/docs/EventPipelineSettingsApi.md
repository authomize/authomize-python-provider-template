# plugins.EventPipelineSettingsApi

All URIs are relative to *https://integrations.secretservercloud.com//api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**event_pipeline_settings_service_get_event_pipeline_filter_settings**](EventPipelineSettingsApi.md#event_pipeline_settings_service_get_event_pipeline_filter_settings) | **GET** /v1/event-pipeline-settings/filter-settings/list/{id} | Get Event Pipeline Filter Settings
[**event_pipeline_settings_service_get_event_pipeline_task_settings**](EventPipelineSettingsApi.md#event_pipeline_settings_service_get_event_pipeline_task_settings) | **GET** /v1/event-pipeline-settings/task-settings/list/{id} | Get Event Pipeline Task Settings
[**event_pipeline_settings_service_get_event_pipeline_tasks**](EventPipelineSettingsApi.md#event_pipeline_settings_service_get_event_pipeline_tasks) | **GET** /v1/event-pipeline-settings/task/list | Get Event Pipeline Tasks
[**event_pipeline_settings_service_get_pipeline_filter_options**](EventPipelineSettingsApi.md#event_pipeline_settings_service_get_pipeline_filter_options) | **GET** /v1/event-pipeline-settings/filter/options | Get Pipeline Filter Options
[**event_pipeline_settings_service_get_pipeline_task_options**](EventPipelineSettingsApi.md#event_pipeline_settings_service_get_pipeline_task_options) | **GET** /v1/event-pipeline-settings/tasks/options | Get Pipeline Task Options


# **event_pipeline_settings_service_get_event_pipeline_filter_settings**
> [EventPipelineFilterSettingMapSummary] event_pipeline_settings_service_get_event_pipeline_filter_settings(id)

Get Event Pipeline Filter Settings

Get all filter settings for a specific pipeline

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import event_pipeline_settings_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.event_pipeline_filter_setting_map_summary import EventPipelineFilterSettingMapSummary
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
    api_instance = event_pipeline_settings_api.EventPipelineSettingsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Event Pipeline Filter ID

    # example passing only required values which don't have defaults set
    try:
        # Get Event Pipeline Filter Settings
        api_response = api_instance.event_pipeline_settings_service_get_event_pipeline_filter_settings(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling EventPipelineSettingsApi->event_pipeline_settings_service_get_event_pipeline_filter_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Event Pipeline Filter ID |

### Return type

[**[EventPipelineFilterSettingMapSummary]**](EventPipelineFilterSettingMapSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | filter settings |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_pipeline_settings_service_get_event_pipeline_task_settings**
> [EventPipelineTaskSettingMapSummary] event_pipeline_settings_service_get_event_pipeline_task_settings(id)

Get Event Pipeline Task Settings

Returns a list of all pipeline task settings

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import event_pipeline_settings_api
from plugins.model.event_pipeline_task_setting_map_summary import EventPipelineTaskSettingMapSummary
from plugins.model.internal_server_error_response import InternalServerErrorResponse
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
    api_instance = event_pipeline_settings_api.EventPipelineSettingsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Event Pipeline Task ID

    # example passing only required values which don't have defaults set
    try:
        # Get Event Pipeline Task Settings
        api_response = api_instance.event_pipeline_settings_service_get_event_pipeline_task_settings(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling EventPipelineSettingsApi->event_pipeline_settings_service_get_event_pipeline_task_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Event Pipeline Task ID |

### Return type

[**[EventPipelineTaskSettingMapSummary]**](EventPipelineTaskSettingMapSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pipeline task settings |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_pipeline_settings_service_get_event_pipeline_tasks**
> PagingOfEventPipelineTask event_pipeline_settings_service_get_event_pipeline_tasks()

Get Event Pipeline Tasks

Get all tasks

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import event_pipeline_settings_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_event_pipeline_task import PagingOfEventPipelineTask
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
    api_instance = event_pipeline_settings_api.EventPipelineSettingsApi(api_client)
    filter_event_action_id = None # bool, date, datetime, dict, float, int, list, str, none_type | EventActionId (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Event Pipeline Tasks
        api_response = api_instance.event_pipeline_settings_service_get_event_pipeline_tasks(filter_event_action_id=filter_event_action_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling EventPipelineSettingsApi->event_pipeline_settings_service_get_event_pipeline_tasks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_event_action_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| EventActionId | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfEventPipelineTask**](PagingOfEventPipelineTask.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paged list of tasks |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_pipeline_settings_service_get_pipeline_filter_options**
> [EventPipelineFilterSummary] event_pipeline_settings_service_get_pipeline_filter_options()

Get Pipeline Filter Options

Get all the available filter options

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import event_pipeline_settings_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.event_pipeline_filter_summary import EventPipelineFilterSummary
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
    api_instance = event_pipeline_settings_api.EventPipelineSettingsApi(api_client)
    event_entity_type_id = None # bool, date, datetime, dict, float, int, list, str, none_type | eventEntityTypeId (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Pipeline Filter Options
        api_response = api_instance.event_pipeline_settings_service_get_pipeline_filter_options(event_entity_type_id=event_entity_type_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling EventPipelineSettingsApi->event_pipeline_settings_service_get_pipeline_filter_options: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_entity_type_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| eventEntityTypeId | [optional]

### Return type

[**[EventPipelineFilterSummary]**](EventPipelineFilterSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of filter options |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_pipeline_settings_service_get_pipeline_task_options**
> [EventPipelineTaskSummary] event_pipeline_settings_service_get_pipeline_task_options()

Get Pipeline Task Options

Get all available options for tasks

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import event_pipeline_settings_api
from plugins.model.event_pipeline_task_summary import EventPipelineTaskSummary
from plugins.model.internal_server_error_response import InternalServerErrorResponse
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
    api_instance = event_pipeline_settings_api.EventPipelineSettingsApi(api_client)
    event_entity_type_id = None # bool, date, datetime, dict, float, int, list, str, none_type | eventEntityTypeId (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Pipeline Task Options
        api_response = api_instance.event_pipeline_settings_service_get_pipeline_task_options(event_entity_type_id=event_entity_type_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling EventPipelineSettingsApi->event_pipeline_settings_service_get_pipeline_task_options: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_entity_type_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| eventEntityTypeId | [optional]

### Return type

[**[EventPipelineTaskSummary]**](EventPipelineTaskSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of task options |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

