# plugins.ScheduleApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schedule_service_create_schedule**](ScheduleApi.md#schedule_service_create_schedule) | **POST** /v1/schedules | Create a Recurring Schedule
[**schedule_service_get_schedule**](ScheduleApi.md#schedule_service_get_schedule) | **GET** /v1/schedules/{scheduleId} | Recurring schedule
[**schedule_service_update_schedule**](ScheduleApi.md#schedule_service_update_schedule) | **PATCH** /v1/schedules/{scheduleId} | Update a Recurring Schedule


# **schedule_service_create_schedule**
> RecurringScheduleModel schedule_service_create_schedule()

Create a Recurring Schedule

Create a recurring schedule and all constraints

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import schedule_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.recurring_schedule_create_args import RecurringScheduleCreateArgs
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.recurring_schedule_model import RecurringScheduleModel
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
    api_instance = schedule_api.ScheduleApi(api_client)
    recurring_schedule_create_args = RecurringScheduleCreateArgs(
        data=RecurringScheduleCreateModel(
            active=True,
            duration=None,
            duration_start_date=None,
            entity=RecurringScheduleEntityModel(
                entity_id=None,
                entity_type=RecurringScheduleEntityType("{}"),
                id=None,
            ),
            notes=None,
            recurring_schedule_type=RecurringScheduleType("{}"),
            schedule_constraints=[
                RecurringScheduleValueModel(
                    recurrence_value=None,
                    recurrence_value_type=RecurringScheduleValueType("{}"),
                ),
            ],
            time_zone_id=None,
        ),
    ) # RecurringScheduleCreateArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a Recurring Schedule
        api_response = api_instance.schedule_service_create_schedule(recurring_schedule_create_args=recurring_schedule_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ScheduleApi->schedule_service_create_schedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recurring_schedule_create_args** | [**RecurringScheduleCreateArgs**](RecurringScheduleCreateArgs.md)| args | [optional]

### Return type

[**RecurringScheduleModel**](RecurringScheduleModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The saved recurring schedule details |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule_service_get_schedule**
> RecurringScheduleModel schedule_service_get_schedule(schedule_id)

Recurring schedule

Get all the details for a recurring schedule by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import schedule_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.recurring_schedule_model import RecurringScheduleModel
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
    api_instance = schedule_api.ScheduleApi(api_client)
    schedule_id = None # bool, date, datetime, dict, float, int, list, str, none_type | scheduleId

    # example passing only required values which don't have defaults set
    try:
        # Recurring schedule
        api_response = api_instance.schedule_service_get_schedule(schedule_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ScheduleApi->schedule_service_get_schedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| scheduleId |

### Return type

[**RecurringScheduleModel**](RecurringScheduleModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The recurring schedule details |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule_service_update_schedule**
> RecurringScheduleModel schedule_service_update_schedule(schedule_id)

Update a Recurring Schedule

Update partial details for a recurring schedule or all constraints

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import schedule_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.recurring_schedule_model import RecurringScheduleModel
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.recurring_schedule_update_args import RecurringScheduleUpdateArgs
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
    api_instance = schedule_api.ScheduleApi(api_client)
    schedule_id = None # bool, date, datetime, dict, float, int, list, str, none_type | scheduleId
    recurring_schedule_update_args = RecurringScheduleUpdateArgs(
        data=RecurringScheduleUpdateModel(
            active=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            duration=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            duration_start_date=UpdateFieldValueOfDateTime(
                dirty=True,
                value=None,
            ),
            notes=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            recurring_schedule_id=None,
            recurring_schedule_type=UpdateFieldValueOfRecurringScheduleType(
                dirty=True,
                value=RecurringScheduleType("{}"),
            ),
            schedule_constraints=UpdateFieldValueOfRecurringScheduleValueModelArray(
                dirty=True,
                value=[
                    RecurringScheduleValueModel(
                        recurrence_value=None,
                        recurrence_value_type=RecurringScheduleValueType("{}"),
                    ),
                ],
            ),
            time_zone_id=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
        ),
    ) # RecurringScheduleUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a Recurring Schedule
        api_response = api_instance.schedule_service_update_schedule(schedule_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ScheduleApi->schedule_service_update_schedule: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Recurring Schedule
        api_response = api_instance.schedule_service_update_schedule(schedule_id, recurring_schedule_update_args=recurring_schedule_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ScheduleApi->schedule_service_update_schedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| scheduleId |
 **recurring_schedule_update_args** | [**RecurringScheduleUpdateArgs**](RecurringScheduleUpdateArgs.md)| args | [optional]

### Return type

[**RecurringScheduleModel**](RecurringScheduleModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated recurring schedule details |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

