# plugins.EventPipelineApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**event_pipeline_service_create_event_pipelines**](EventPipelineApi.md#event_pipeline_service_create_event_pipelines) | **POST** /v1/event-pipeline | Create a new Event Pipeline
[**event_pipeline_service_get_event_pipeline**](EventPipelineApi.md#event_pipeline_service_get_event_pipeline) | **GET** /v1/event-pipeline/{id} | Get an Event Pipeline
[**event_pipeline_service_get_event_pipeline_runs**](EventPipelineApi.md#event_pipeline_service_get_event_pipeline_runs) | **GET** /v1/event-pipeline/runs | Get Event Pipeline Runs
[**event_pipeline_service_get_event_pipeline_stub**](EventPipelineApi.md#event_pipeline_service_get_event_pipeline_stub) | **GET** /v1/event-pipeline/stub | Stub an empty Event Pipeline
[**event_pipeline_service_get_event_pipeline_summaries**](EventPipelineApi.md#event_pipeline_service_get_event_pipeline_summaries) | **GET** /v1/event-pipeline/summaries | Get summaries of Event Pipelines
[**event_pipeline_service_get_event_pipelines**](EventPipelineApi.md#event_pipeline_service_get_event_pipelines) | **GET** /v1/event-pipeline/list | Get a list of Event Pipelines
[**event_pipeline_service_reorder_pipeline**](EventPipelineApi.md#event_pipeline_service_reorder_pipeline) | **PUT** /v1/event-pipeline/{id}/order | Reorder an Event Pipeline
[**event_pipeline_service_toggle_pipeline_active**](EventPipelineApi.md#event_pipeline_service_toggle_pipeline_active) | **PUT** /v1/event-pipeline/{id}/activate | Update an Event Pipeline active value
[**event_pipeline_service_update_event_pipelines**](EventPipelineApi.md#event_pipeline_service_update_event_pipelines) | **PUT** /v1/event-pipeline/{id} | Update an Event Pipeline


# **event_pipeline_service_create_event_pipelines**
> EventPipelineModel event_pipeline_service_create_event_pipelines()

Create a new Event Pipeline

Creates a new Event Pipeline with the provided object.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import event_pipeline_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.event_pipeline_create_args import EventPipelineCreateArgs
from plugins.model.event_pipeline_model import EventPipelineModel
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
    api_instance = event_pipeline_api.EventPipelineApi(api_client)
    event_pipeline_create_args = EventPipelineCreateArgs(
        data=EventPipelineUpdateModel(
            active=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            event_pipeline_description=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            event_pipeline_name=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            filters=UpdateFieldValueOfEventPipelineFilterMapUpdateModelArray(
                dirty=True,
                value=[
                    EventPipelineFilterMapUpdateModel(
                        event_pipeline_filter_id=UpdateFieldValueOfInt32(
                            dirty=True,
                            value=None,
                        ),
                        event_pipeline_filter_map_id=UpdateFieldValueOfOptionalInt32(
                            dirty=True,
                            value=None,
                        ),
                        event_pipeline_filter_name=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        settings=UpdateFieldValueOfSettingUpdateModelArray(
                            dirty=True,
                            value=[
                                SettingUpdateModel(
                                    setting_name=UpdateFieldValueOfString(
                                        dirty=True,
                                        value=None,
                                    ),
                                    setting_value=UpdateFieldValueOfString(
                                        dirty=True,
                                        value=None,
                                    ),
                                ),
                            ],
                        ),
                        sort_order=UpdateFieldValueOfInt32(
                            dirty=True,
                            value=None,
                        ),
                    ),
                ],
            ),
            tasks=UpdateFieldValueOfEventPipelineTaskMapUpdateModelArray(
                dirty=True,
                value=[
                    EventPipelineTaskMapUpdateModel(
                        event_pipeline_task_id=UpdateFieldValueOfInt32(
                            dirty=True,
                            value=None,
                        ),
                        event_pipeline_task_map_id=UpdateFieldValueOfOptionalInt32(
                            dirty=True,
                            value=None,
                        ),
                        event_pipeline_task_name=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        settings=UpdateFieldValueOfSettingUpdateModelArray(
                            dirty=True,
                            value=[
                                SettingUpdateModel(
                                    setting_name=UpdateFieldValueOfString(
                                        dirty=True,
                                        value=None,
                                    ),
                                    setting_value=UpdateFieldValueOfString(
                                        dirty=True,
                                        value=None,
                                    ),
                                ),
                            ],
                        ),
                        sort_order=UpdateFieldValueOfInt32(
                            dirty=True,
                            value=None,
                        ),
                    ),
                ],
            ),
            triggers=UpdateFieldValueOfEventPipelineTriggerUpdateModelArray(
                dirty=True,
                value=[
                    EventPipelineTriggerUpdateModel(
                        event_action_id=UpdateFieldValueOfInt32(
                            dirty=True,
                            value=None,
                        ),
                    ),
                ],
            ),
        ),
        event_entity_type_id=None,
        event_pipeline_policy_id=None,
    ) # EventPipelineCreateArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new Event Pipeline
        api_response = api_instance.event_pipeline_service_create_event_pipelines(event_pipeline_create_args=event_pipeline_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling EventPipelineApi->event_pipeline_service_create_event_pipelines: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_pipeline_create_args** | [**EventPipelineCreateArgs**](EventPipelineCreateArgs.md)| args | [optional]

### Return type

[**EventPipelineModel**](EventPipelineModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new Event Pipeline |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_pipeline_service_get_event_pipeline**
> EventPipelineModel event_pipeline_service_get_event_pipeline(id)

Get an Event Pipeline

Returns the Event Pipeline for the provided ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import event_pipeline_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.event_pipeline_model import EventPipelineModel
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
    api_instance = event_pipeline_api.EventPipelineApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Event Pipeline ID

    # example passing only required values which don't have defaults set
    try:
        # Get an Event Pipeline
        api_response = api_instance.event_pipeline_service_get_event_pipeline(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling EventPipelineApi->event_pipeline_service_get_event_pipeline: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Event Pipeline ID |

### Return type

[**EventPipelineModel**](EventPipelineModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Event Pipeline View |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_pipeline_service_get_event_pipeline_runs**
> PagingOfEventPipelineRunViewModel event_pipeline_service_get_event_pipeline_runs()

Get Event Pipeline Runs

Get all of the runs for a specific pipeline

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import event_pipeline_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.paging_of_event_pipeline_run_view_model import PagingOfEventPipelineRunViewModel
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
    api_instance = event_pipeline_api.EventPipelineApi(api_client)
    filter_event_pipeline_id = None # bool, date, datetime, dict, float, int, list, str, none_type | EventPipelineId (optional)
    filter_event_pipeline_policy_run_id = None # bool, date, datetime, dict, float, int, list, str, none_type | EventPipelinePolicyRunId (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Event Pipeline Runs
        api_response = api_instance.event_pipeline_service_get_event_pipeline_runs(filter_event_pipeline_id=filter_event_pipeline_id, filter_event_pipeline_policy_run_id=filter_event_pipeline_policy_run_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling EventPipelineApi->event_pipeline_service_get_event_pipeline_runs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_event_pipeline_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| EventPipelineId | [optional]
 **filter_event_pipeline_policy_run_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| EventPipelinePolicyRunId | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfEventPipelineRunViewModel**](PagingOfEventPipelineRunViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paged list of pipeline runs |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_pipeline_service_get_event_pipeline_stub**
> EventPipeline event_pipeline_service_get_event_pipeline_stub()

Stub an empty Event Pipeline

Returns an empty Event Pipeline to be filled out.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import event_pipeline_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.event_pipeline import EventPipeline
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
    api_instance = event_pipeline_api.EventPipelineApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Stub an empty Event Pipeline
        api_response = api_instance.event_pipeline_service_get_event_pipeline_stub()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling EventPipelineApi->event_pipeline_service_get_event_pipeline_stub: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**EventPipeline**](EventPipeline.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An empty Event Pipeline |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_pipeline_service_get_event_pipeline_summaries**
> PagingOfEventPipelineSummaryModel event_pipeline_service_get_event_pipeline_summaries()

Get summaries of Event Pipelines

Returns a list of Event Pipeline summaries that meet the searching criterea

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import event_pipeline_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.paging_of_event_pipeline_summary_model import PagingOfEventPipelineSummaryModel
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
    api_instance = event_pipeline_api.EventPipelineApi(api_client)
    filter_event_entity_type_id = None # bool, date, datetime, dict, float, int, list, str, none_type | EventEntityTypeId (optional)
    filter_event_pipeline_name = None # bool, date, datetime, dict, float, int, list, str, none_type | EventPipelineName (optional)
    filter_event_pipeline_policy_id = None # bool, date, datetime, dict, float, int, list, str, none_type | EventPipelinePolicyId (optional)
    filter_include_active = True # bool | IncludeActive (optional)
    filter_include_inactive = True # bool | IncludeInactive (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get summaries of Event Pipelines
        api_response = api_instance.event_pipeline_service_get_event_pipeline_summaries(filter_event_entity_type_id=filter_event_entity_type_id, filter_event_pipeline_name=filter_event_pipeline_name, filter_event_pipeline_policy_id=filter_event_pipeline_policy_id, filter_include_active=filter_include_active, filter_include_inactive=filter_include_inactive, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling EventPipelineApi->event_pipeline_service_get_event_pipeline_summaries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_event_entity_type_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| EventEntityTypeId | [optional]
 **filter_event_pipeline_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| EventPipelineName | [optional]
 **filter_event_pipeline_policy_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| EventPipelinePolicyId | [optional]
 **filter_include_active** | **bool**| IncludeActive | [optional]
 **filter_include_inactive** | **bool**| IncludeInactive | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfEventPipelineSummaryModel**](PagingOfEventPipelineSummaryModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The summaries of Event Pipelines |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_pipeline_service_get_event_pipelines**
> PagingOfEventPipelineViewModel event_pipeline_service_get_event_pipelines()

Get a list of Event Pipelines

Returns a list of Event Pipelines that meet the paging/searching criterea

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import event_pipeline_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.paging_of_event_pipeline_view_model import PagingOfEventPipelineViewModel
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
    api_instance = event_pipeline_api.EventPipelineApi(api_client)
    filter_event_entity_type_id = None # bool, date, datetime, dict, float, int, list, str, none_type | EventEntityTypeId (optional)
    filter_event_pipeline_name = None # bool, date, datetime, dict, float, int, list, str, none_type | EventPipelineName (optional)
    filter_event_pipeline_policy_id = None # bool, date, datetime, dict, float, int, list, str, none_type | EventPipelinePolicyId (optional)
    filter_include_active = True # bool | IncludeActive (optional)
    filter_include_inactive = True # bool | IncludeInactive (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of Event Pipelines
        api_response = api_instance.event_pipeline_service_get_event_pipelines(filter_event_entity_type_id=filter_event_entity_type_id, filter_event_pipeline_name=filter_event_pipeline_name, filter_event_pipeline_policy_id=filter_event_pipeline_policy_id, filter_include_active=filter_include_active, filter_include_inactive=filter_include_inactive, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling EventPipelineApi->event_pipeline_service_get_event_pipelines: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_event_entity_type_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| EventEntityTypeId | [optional]
 **filter_event_pipeline_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| EventPipelineName | [optional]
 **filter_event_pipeline_policy_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| EventPipelinePolicyId | [optional]
 **filter_include_active** | **bool**| IncludeActive | [optional]
 **filter_include_inactive** | **bool**| IncludeInactive | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfEventPipelineViewModel**](PagingOfEventPipelineViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of Event Pipelines |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_pipeline_service_reorder_pipeline**
> [EventPipelinePolicyMap] event_pipeline_service_reorder_pipeline(id)

Reorder an Event Pipeline

Reorder an existing Event Pipeline in a policy

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import event_pipeline_api
from plugins.model.event_pipeline_policy_map import EventPipelinePolicyMap
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.event_pipeline_order_update_args import EventPipelineOrderUpdateArgs
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
    api_instance = event_pipeline_api.EventPipelineApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Event Pipeline Id
    event_pipeline_order_update_args = EventPipelineOrderUpdateArgs(
        data=EventPipelineOrderUpdateModel(
            event_pipeline_policy_id=None,
            sort_order=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
        ),
    ) # EventPipelineOrderUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Reorder an Event Pipeline
        api_response = api_instance.event_pipeline_service_reorder_pipeline(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling EventPipelineApi->event_pipeline_service_reorder_pipeline: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Reorder an Event Pipeline
        api_response = api_instance.event_pipeline_service_reorder_pipeline(id, event_pipeline_order_update_args=event_pipeline_order_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling EventPipelineApi->event_pipeline_service_reorder_pipeline: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Event Pipeline Id |
 **event_pipeline_order_update_args** | [**EventPipelineOrderUpdateArgs**](EventPipelineOrderUpdateArgs.md)| args | [optional]

### Return type

[**[EventPipelinePolicyMap]**](EventPipelinePolicyMap.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Event Pipeline Policy Map |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_pipeline_service_toggle_pipeline_active**
> bool event_pipeline_service_toggle_pipeline_active(id)

Update an Event Pipeline active value

Sets if an Event Pipeline is active or not

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import event_pipeline_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.event_pipeline_activate_update_args import EventPipelineActivateUpdateArgs
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
    api_instance = event_pipeline_api.EventPipelineApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Event Pipeline Id
    event_pipeline_activate_update_args = EventPipelineActivateUpdateArgs(
        activate=True,
    ) # EventPipelineActivateUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an Event Pipeline active value
        api_response = api_instance.event_pipeline_service_toggle_pipeline_active(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling EventPipelineApi->event_pipeline_service_toggle_pipeline_active: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an Event Pipeline active value
        api_response = api_instance.event_pipeline_service_toggle_pipeline_active(id, event_pipeline_activate_update_args=event_pipeline_activate_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling EventPipelineApi->event_pipeline_service_toggle_pipeline_active: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Event Pipeline Id |
 **event_pipeline_activate_update_args** | [**EventPipelineActivateUpdateArgs**](EventPipelineActivateUpdateArgs.md)| args | [optional]

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
**200** | The Active value |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_pipeline_service_update_event_pipelines**
> EventPipelineModel event_pipeline_service_update_event_pipelines(id)

Update an Event Pipeline

Update an existing Event Pipeline using the existing Event Pipeline's ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import event_pipeline_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.event_pipeline_update_args import EventPipelineUpdateArgs
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.event_pipeline_model import EventPipelineModel
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
    api_instance = event_pipeline_api.EventPipelineApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Event Pipeline ID
    event_pipeline_update_args = EventPipelineUpdateArgs(
        data=EventPipelineUpdateModel(
            active=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            event_pipeline_description=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            event_pipeline_name=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            filters=UpdateFieldValueOfEventPipelineFilterMapUpdateModelArray(
                dirty=True,
                value=[
                    EventPipelineFilterMapUpdateModel(
                        event_pipeline_filter_id=UpdateFieldValueOfInt32(
                            dirty=True,
                            value=None,
                        ),
                        event_pipeline_filter_map_id=UpdateFieldValueOfOptionalInt32(
                            dirty=True,
                            value=None,
                        ),
                        event_pipeline_filter_name=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        settings=UpdateFieldValueOfSettingUpdateModelArray(
                            dirty=True,
                            value=[
                                SettingUpdateModel(
                                    setting_name=UpdateFieldValueOfString(
                                        dirty=True,
                                        value=None,
                                    ),
                                    setting_value=UpdateFieldValueOfString(
                                        dirty=True,
                                        value=None,
                                    ),
                                ),
                            ],
                        ),
                        sort_order=UpdateFieldValueOfInt32(
                            dirty=True,
                            value=None,
                        ),
                    ),
                ],
            ),
            tasks=UpdateFieldValueOfEventPipelineTaskMapUpdateModelArray(
                dirty=True,
                value=[
                    EventPipelineTaskMapUpdateModel(
                        event_pipeline_task_id=UpdateFieldValueOfInt32(
                            dirty=True,
                            value=None,
                        ),
                        event_pipeline_task_map_id=UpdateFieldValueOfOptionalInt32(
                            dirty=True,
                            value=None,
                        ),
                        event_pipeline_task_name=UpdateFieldValueOfString(
                            dirty=True,
                            value=None,
                        ),
                        settings=UpdateFieldValueOfSettingUpdateModelArray(
                            dirty=True,
                            value=[
                                SettingUpdateModel(
                                    setting_name=UpdateFieldValueOfString(
                                        dirty=True,
                                        value=None,
                                    ),
                                    setting_value=UpdateFieldValueOfString(
                                        dirty=True,
                                        value=None,
                                    ),
                                ),
                            ],
                        ),
                        sort_order=UpdateFieldValueOfInt32(
                            dirty=True,
                            value=None,
                        ),
                    ),
                ],
            ),
            triggers=UpdateFieldValueOfEventPipelineTriggerUpdateModelArray(
                dirty=True,
                value=[
                    EventPipelineTriggerUpdateModel(
                        event_action_id=UpdateFieldValueOfInt32(
                            dirty=True,
                            value=None,
                        ),
                    ),
                ],
            ),
        ),
    ) # EventPipelineUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an Event Pipeline
        api_response = api_instance.event_pipeline_service_update_event_pipelines(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling EventPipelineApi->event_pipeline_service_update_event_pipelines: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an Event Pipeline
        api_response = api_instance.event_pipeline_service_update_event_pipelines(id, event_pipeline_update_args=event_pipeline_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling EventPipelineApi->event_pipeline_service_update_event_pipelines: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Event Pipeline ID |
 **event_pipeline_update_args** | [**EventPipelineUpdateArgs**](EventPipelineUpdateArgs.md)| args | [optional]

### Return type

[**EventPipelineModel**](EventPipelineModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Event Pipeline |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

