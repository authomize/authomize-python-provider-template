# secret_server_openapiclient.EventSubscriptionsApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**event_subscriptions_service_create_event_subscription**](EventSubscriptionsApi.md#event_subscriptions_service_create_event_subscription) | **POST** /v1/event-subscriptions | Create event subscription
[**event_subscriptions_service_get_event_subscription**](EventSubscriptionsApi.md#event_subscriptions_service_get_event_subscription) | **GET** /v1/event-subscriptions/{eventSubscriptionId} | event subscription
[**event_subscriptions_service_get_subscription_entity_types**](EventSubscriptionsApi.md#event_subscriptions_service_get_subscription_entity_types) | **GET** /v1/event-subscriptions/event-types | Get an Event Subscription Types and Actions
[**event_subscriptions_service_get_subscription_stub**](EventSubscriptionsApi.md#event_subscriptions_service_get_subscription_stub) | **GET** /v1/event-subscriptions/stub | Get an empty event subscription
[**event_subscriptions_service_search_event_subscriptions**](EventSubscriptionsApi.md#event_subscriptions_service_search_event_subscriptions) | **GET** /v1/event-subscriptions | Search event subscriptions
[**event_subscriptions_service_update_event_subscription**](EventSubscriptionsApi.md#event_subscriptions_service_update_event_subscription) | **PATCH** /v1/event-subscriptions/{eventSubscriptionId} | Update event subscription


# **event_subscriptions_service_create_event_subscription**
> EventSubscriptionModel event_subscriptions_service_create_event_subscription()

Create event subscription

Create a new event subscription

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import event_subscriptions_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.event_subscription_model import EventSubscriptionModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.event_subscription_create_args import EventSubscriptionCreateArgs
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
    api_instance = event_subscriptions_api.EventSubscriptionsApi(api_client)
    event_subscription_create_args = EventSubscriptionCreateArgs(
        data=EventSubscriptionCreateModel(
            active=True,
            entity_actions=[
                EventSubscriptionEntityActionModel(
                    condition_type=EventSubscriptionConditionType("{}"),
                    container_id=None,
                    container_name=None,
                    event_action_display_name=None,
                    event_action_id=None,
                    event_entity_type=EventSubscriptionEntity("{}"),
                    event_entity_type_display_name=None,
                    id=None,
                    include_subcontainers=True,
                    item_id=None,
                    item_name=None,
                ),
            ],
            send_email=True,
            send_slack=True,
            subscription_name=None,
        ),
    ) # EventSubscriptionCreateArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create event subscription
        api_response = api_instance.event_subscriptions_service_create_event_subscription(event_subscription_create_args=event_subscription_create_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling EventSubscriptionsApi->event_subscriptions_service_create_event_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_subscription_create_args** | [**EventSubscriptionCreateArgs**](EventSubscriptionCreateArgs.md)| args | [optional]

### Return type

[**EventSubscriptionModel**](EventSubscriptionModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details for a specific event subscription |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_subscriptions_service_get_event_subscription**
> EventSubscriptionModel event_subscriptions_service_get_event_subscription(event_subscription_id)

event subscription

Details for a specific event subscription

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import event_subscriptions_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.event_subscription_model import EventSubscriptionModel
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
    api_instance = event_subscriptions_api.EventSubscriptionsApi(api_client)
    event_subscription_id = None # bool, date, datetime, dict, float, int, list, str, none_type | eventSubscriptionId

    # example passing only required values which don't have defaults set
    try:
        # event subscription
        api_response = api_instance.event_subscriptions_service_get_event_subscription(event_subscription_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling EventSubscriptionsApi->event_subscriptions_service_get_event_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_subscription_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| eventSubscriptionId |

### Return type

[**EventSubscriptionModel**](EventSubscriptionModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details for a specific event subscription |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_subscriptions_service_get_subscription_entity_types**
> [EntityTypeModel] event_subscriptions_service_get_subscription_entity_types()

Get an Event Subscription Types and Actions

Returns the array of Event Subscription Types and Actions

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import event_subscriptions_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.entity_type_model import EntityTypeModel
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
    api_instance = event_subscriptions_api.EventSubscriptionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get an Event Subscription Types and Actions
        api_response = api_instance.event_subscriptions_service_get_subscription_entity_types()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling EventSubscriptionsApi->event_subscriptions_service_get_subscription_entity_types: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[EntityTypeModel]**](EntityTypeModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Event Subscription Types and Actions View |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_subscriptions_service_get_subscription_stub**
> EventSubscriptionStubViewModel event_subscriptions_service_get_subscription_stub()

Get an empty event subscription

Returns the empty event subscription

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import event_subscriptions_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.event_subscription_stub_view_model import EventSubscriptionStubViewModel
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
    api_instance = event_subscriptions_api.EventSubscriptionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get an empty event subscription
        api_response = api_instance.event_subscriptions_service_get_subscription_stub()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling EventSubscriptionsApi->event_subscriptions_service_get_subscription_stub: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**EventSubscriptionStubViewModel**](EventSubscriptionStubViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An empty event subscription |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_subscriptions_service_search_event_subscriptions**
> PagingOfEventSubscriptionSummary event_subscriptions_service_search_event_subscriptions()

Search event subscriptions

Search, filter, sort, and page event subscriptions

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import event_subscriptions_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.paging_of_event_subscription_summary import PagingOfEventSubscriptionSummary
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
    api_instance = event_subscriptions_api.EventSubscriptionsApi(api_client)
    filter_include_inactive = True # bool | IncludeInactive (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search event subscriptions
        api_response = api_instance.event_subscriptions_service_search_event_subscriptions(filter_include_inactive=filter_include_inactive, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling EventSubscriptionsApi->event_subscriptions_service_search_event_subscriptions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_include_inactive** | **bool**| IncludeInactive | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfEventSubscriptionSummary**](PagingOfEventSubscriptionSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | event subscriptions results |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_subscriptions_service_update_event_subscription**
> EventSubscriptionModel event_subscriptions_service_update_event_subscription(event_subscription_id)

Update event subscription

Update an event subscription

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import event_subscriptions_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.event_subscription_update_args import EventSubscriptionUpdateArgs
from secret_server_openapiclient.model.event_subscription_model import EventSubscriptionModel
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
    api_instance = event_subscriptions_api.EventSubscriptionsApi(api_client)
    event_subscription_id = None # bool, date, datetime, dict, float, int, list, str, none_type | eventSubscriptionId
    event_subscription_update_args = EventSubscriptionUpdateArgs(
        data=EventSubscriptionUpdateModel(
            active=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            entity_actions=UpdateFieldValueOfEventSubscriptionEntityActionModelArray(
                dirty=True,
                value=[
                    EventSubscriptionEntityActionModel(
                        condition_type=EventSubscriptionConditionType("{}"),
                        container_id=None,
                        container_name=None,
                        event_action_display_name=None,
                        event_action_id=None,
                        event_entity_type=EventSubscriptionEntity("{}"),
                        event_entity_type_display_name=None,
                        id=None,
                        include_subcontainers=True,
                        item_id=None,
                        item_name=None,
                    ),
                ],
            ),
            inbox_expiration=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            subscribers=UpdateFieldValueOfInt32Array(
                dirty=True,
                value=[
                    None,
                ],
            ),
            subscription_name=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
        ),
    ) # EventSubscriptionUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update event subscription
        api_response = api_instance.event_subscriptions_service_update_event_subscription(event_subscription_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling EventSubscriptionsApi->event_subscriptions_service_update_event_subscription: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update event subscription
        api_response = api_instance.event_subscriptions_service_update_event_subscription(event_subscription_id, event_subscription_update_args=event_subscription_update_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling EventSubscriptionsApi->event_subscriptions_service_update_event_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_subscription_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| eventSubscriptionId |
 **event_subscription_update_args** | [**EventSubscriptionUpdateArgs**](EventSubscriptionUpdateArgs.md)| args | [optional]

### Return type

[**EventSubscriptionModel**](EventSubscriptionModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details for a specific event subscription |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

