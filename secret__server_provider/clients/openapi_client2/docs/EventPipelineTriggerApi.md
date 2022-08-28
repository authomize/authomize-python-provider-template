# plugins.EventPipelineTriggerApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**event_pipeline_trigger_service_get_event_pipeline_stub**](EventPipelineTriggerApi.md#event_pipeline_trigger_service_get_event_pipeline_stub) | **GET** /v1/event-pipeline/trigger/stub | Stub an Event Pipeline Trigger
[**event_pipeline_trigger_service_get_event_pipeline_trigger_options**](EventPipelineTriggerApi.md#event_pipeline_trigger_service_get_event_pipeline_trigger_options) | **GET** /v1/event-pipeline/trigger/options | Get Pipeline Trigger Options
[**event_pipeline_trigger_service_get_event_pipeline_triggers**](EventPipelineTriggerApi.md#event_pipeline_trigger_service_get_event_pipeline_triggers) | **GET** /v1/event-pipeline/{id}/trigger | Get the triggers for an Event Pipeline


# **event_pipeline_trigger_service_get_event_pipeline_stub**
> EventPipelineTrigger event_pipeline_trigger_service_get_event_pipeline_stub()

Stub an Event Pipeline Trigger

Creates an empty Event Pipeline Trigger to be populated

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import event_pipeline_trigger_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.event_pipeline_trigger import EventPipelineTrigger
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
    api_instance = event_pipeline_trigger_api.EventPipelineTriggerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Stub an Event Pipeline Trigger
        api_response = api_instance.event_pipeline_trigger_service_get_event_pipeline_stub()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling EventPipelineTriggerApi->event_pipeline_trigger_service_get_event_pipeline_stub: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**EventPipelineTrigger**](EventPipelineTrigger.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The empty Event Pipeline Trigger |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_pipeline_trigger_service_get_event_pipeline_trigger_options**
> [EventPipelineTriggerSummary] event_pipeline_trigger_service_get_event_pipeline_trigger_options()

Get Pipeline Trigger Options

returns all available pipeline trigger options for a specific entity type

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import event_pipeline_trigger_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.event_pipeline_trigger_summary import EventPipelineTriggerSummary
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
    api_instance = event_pipeline_trigger_api.EventPipelineTriggerApi(api_client)
    event_entity_type_id = 1 # int | eventEntityTypeId (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Pipeline Trigger Options
        api_response = api_instance.event_pipeline_trigger_service_get_event_pipeline_trigger_options(event_entity_type_id=event_entity_type_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling EventPipelineTriggerApi->event_pipeline_trigger_service_get_event_pipeline_trigger_options: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_entity_type_id** | **int**| eventEntityTypeId | [optional]

### Return type

[**[EventPipelineTriggerSummary]**](EventPipelineTriggerSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of triggers |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_pipeline_trigger_service_get_event_pipeline_triggers**
> [EventPipelineTriggerSummary] event_pipeline_trigger_service_get_event_pipeline_triggers(id)

Get the triggers for an Event Pipeline

Returns the triggers for the Event Pipeline that has the provided ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import event_pipeline_trigger_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.event_pipeline_trigger_summary import EventPipelineTriggerSummary
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
    api_instance = event_pipeline_trigger_api.EventPipelineTriggerApi(api_client)
    id = 1 # int | Event Pipeline ID

    # example passing only required values which don't have defaults set
    try:
        # Get the triggers for an Event Pipeline
        api_response = api_instance.event_pipeline_trigger_service_get_event_pipeline_triggers(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling EventPipelineTriggerApi->event_pipeline_trigger_service_get_event_pipeline_triggers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Event Pipeline ID |

### Return type

[**[EventPipelineTriggerSummary]**](EventPipelineTriggerSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of Event Pipeline Triggers |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

