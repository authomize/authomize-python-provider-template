# plugins.TicketSystemsApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ticket_systems_service_create_ticket_system**](TicketSystemsApi.md#ticket_systems_service_create_ticket_system) | **POST** /v1/ticket-systems | Creates a Ticket System
[**ticket_systems_service_get_ticket_system**](TicketSystemsApi.md#ticket_systems_service_get_ticket_system) | **GET** /v1/ticket-systems/{id} | Gets a ticket system by ID
[**ticket_systems_service_get_ticket_system_v2**](TicketSystemsApi.md#ticket_systems_service_get_ticket_system_v2) | **GET** /v2/ticket-systems/{id} | Gets a ticket system by ID
[**ticket_systems_service_get_ticket_systems**](TicketSystemsApi.md#ticket_systems_service_get_ticket_systems) | **GET** /v1/ticket-systems | Gets all ticket systems
[**ticket_systems_service_get_ticket_systems_v2**](TicketSystemsApi.md#ticket_systems_service_get_ticket_systems_v2) | **GET** /v2/ticket-systems | Gets all ticket systems
[**ticket_systems_service_update_ticket_system**](TicketSystemsApi.md#ticket_systems_service_update_ticket_system) | **PATCH** /v1/ticket-systems/{id} | Updates a Ticket System


# **ticket_systems_service_create_ticket_system**
> TicketSystemModelV2 ticket_systems_service_create_ticket_system()

Creates a Ticket System

Creates a Ticket System

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import ticket_systems_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.ticket_system_model_v2 import TicketSystemModelV2
from plugins.model.ticket_system_create_args import TicketSystemCreateArgs
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
    api_instance = ticket_systems_api.TicketSystemsApi(api_client)
    ticket_system_create_args = TicketSystemCreateArgs(
        data=TicketSystemCreateModel(
            active=True,
            add_comments_to_ticket=True,
            bmc_change_management_comment_work_type="bmc_change_management_comment_work_type_example",
            bmc_incident_management_comment_work_type="bmc_incident_management_comment_work_type_example",
            bmc_remedy_authentication="bmc_remedy_authentication_example",
            bmc_remedy_url_endpoint="bmc_remedy_url_endpoint_example",
            description="description_example",
            display_message="display_message_example",
            force_require_ticket_number=ForceRequireTicketSystemOptions("{}"),
            is_default=True,
            name="name_example",
            power_shell_add_comment_script_arguments="power_shell_add_comment_script_arguments_example",
            power_shell_add_comment_script_id=1,
            power_shell_add_ticket_comment_script_arguments="power_shell_add_ticket_comment_script_arguments_example",
            power_shell_add_ticket_comment_script_id=1,
            power_shell_run_as_account_secret_id=1,
            power_shell_ticket_status_script_arguments="power_shell_ticket_status_script_arguments_example",
            power_shell_ticket_status_script_id=1,
            service_now_allowed_statuses="service_now_allowed_statuses_example",
            service_now_domain_name="service_now_domain_name_example",
            site_id=1,
            system_credential_secret_id=1,
            ticket_number_error_message="ticket_number_error_message_example",
            ticket_number_validation="ticket_number_validation_example",
            ticket_system_type=TicketSystemTypes("{}"),
            view_ticket_url="view_ticket_url_example",
        ),
    ) # TicketSystemCreateArgs | Ticket System Create Args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates a Ticket System
        api_response = api_instance.ticket_systems_service_create_ticket_system(ticket_system_create_args=ticket_system_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling TicketSystemsApi->ticket_systems_service_create_ticket_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_system_create_args** | [**TicketSystemCreateArgs**](TicketSystemCreateArgs.md)| Ticket System Create Args | [optional]

### Return type

[**TicketSystemModelV2**](TicketSystemModelV2.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ticket System Model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_systems_service_get_ticket_system**
> TicketSystemModel ticket_systems_service_get_ticket_system(id)

Gets a ticket system by ID

Gets a ticket system by ID.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import ticket_systems_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.ticket_system_model import TicketSystemModel
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
    api_instance = ticket_systems_api.TicketSystemsApi(api_client)
    id = 1 # int | Ticket System ID

    # example passing only required values which don't have defaults set
    try:
        # Gets a ticket system by ID
        api_response = api_instance.ticket_systems_service_get_ticket_system(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling TicketSystemsApi->ticket_systems_service_get_ticket_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Ticket System ID |

### Return type

[**TicketSystemModel**](TicketSystemModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ticket System Model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_systems_service_get_ticket_system_v2**
> TicketSystemModelV2 ticket_systems_service_get_ticket_system_v2(id)

Gets a ticket system by ID

Gets a ticket system by ID.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import ticket_systems_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.ticket_system_model_v2 import TicketSystemModelV2
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
    api_instance = ticket_systems_api.TicketSystemsApi(api_client)
    id = 1 # int | Ticket System ID

    # example passing only required values which don't have defaults set
    try:
        # Gets a ticket system by ID
        api_response = api_instance.ticket_systems_service_get_ticket_system_v2(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling TicketSystemsApi->ticket_systems_service_get_ticket_system_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Ticket System ID |

### Return type

[**TicketSystemModelV2**](TicketSystemModelV2.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ticket System Model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_systems_service_get_ticket_systems**
> [TicketSystemModel] ticket_systems_service_get_ticket_systems()

Gets all ticket systems

Gets all ticket systems.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import ticket_systems_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.ticket_system_model import TicketSystemModel
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
    api_instance = ticket_systems_api.TicketSystemsApi(api_client)
    include_inactive = True # bool | includeInactive (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets all ticket systems
        api_response = api_instance.ticket_systems_service_get_ticket_systems(include_inactive=include_inactive)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling TicketSystemsApi->ticket_systems_service_get_ticket_systems: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_inactive** | **bool**| includeInactive | [optional]

### Return type

[**[TicketSystemModel]**](TicketSystemModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ticket System Models |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_systems_service_get_ticket_systems_v2**
> PagingOfTicketSystemSummary ticket_systems_service_get_ticket_systems_v2()

Gets all ticket systems

Gets all ticket systems.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import ticket_systems_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_ticket_system_summary import PagingOfTicketSystemSummary
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
    api_instance = ticket_systems_api.TicketSystemsApi(api_client)
    include_inactive = True # bool | includeInactive (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets all ticket systems
        api_response = api_instance.ticket_systems_service_get_ticket_systems_v2(include_inactive=include_inactive, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling TicketSystemsApi->ticket_systems_service_get_ticket_systems_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_inactive** | **bool**| includeInactive | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfTicketSystemSummary**](PagingOfTicketSystemSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ticket System Summaries |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_systems_service_update_ticket_system**
> TicketSystemModelV2 ticket_systems_service_update_ticket_system(id)

Updates a Ticket System

Updates a Ticket System

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import ticket_systems_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.ticket_system_patch_args import TicketSystemPatchArgs
from plugins.model.ticket_system_model_v2 import TicketSystemModelV2
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
    api_instance = ticket_systems_api.TicketSystemsApi(api_client)
    id = 1 # int | id
    ticket_system_patch_args = TicketSystemPatchArgs(
        data=TicketSystemPatchModel(
            active=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            add_comments_to_ticket=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            bmc_change_management_comment_work_type=UpdateFieldValueOfOptionalBmcChangeManagementCommentWorkType(
                dirty=True,
                value="value_example",
            ),
            bmc_incident_management_comment_work_type=UpdateFieldValueOfOptionalBmcIncidentManagementCommentWorkType(
                dirty=True,
                value="value_example",
            ),
            bmc_remedy_authentication=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            bmc_remedy_url_endpoint=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            description=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            display_message=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            force_require_ticket_number=UpdateFieldValueOfForceRequireTicketSystemOptions(
                dirty=True,
                value=ForceRequireTicketSystemOptions("{}"),
            ),
            is_default=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            name=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            power_shell_add_comment_script_arguments=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            power_shell_add_comment_script_id=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=1,
            ),
            power_shell_add_ticket_comment_script_arguments=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            power_shell_add_ticket_comment_script_id=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=1,
            ),
            power_shell_run_as_account_secret_id=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=1,
            ),
            power_shell_ticket_status_script_arguments=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            power_shell_ticket_status_script_id=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=1,
            ),
            service_now_allowed_statuses=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            service_now_domain_name=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            site_id=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=1,
            ),
            system_credential_secret_id=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=1,
            ),
            ticket_number_error_message=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            ticket_number_validation=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            ticket_system_id=1,
            ticket_system_type=UpdateFieldValueOfTicketSystemTypes(
                dirty=True,
                value=TicketSystemTypes("{}"),
            ),
            view_ticket_url=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
        ),
    ) # TicketSystemPatchArgs | Ticket System Patch Args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates a Ticket System
        api_response = api_instance.ticket_systems_service_update_ticket_system(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling TicketSystemsApi->ticket_systems_service_update_ticket_system: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates a Ticket System
        api_response = api_instance.ticket_systems_service_update_ticket_system(id, ticket_system_patch_args=ticket_system_patch_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling TicketSystemsApi->ticket_systems_service_update_ticket_system: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id |
 **ticket_system_patch_args** | [**TicketSystemPatchArgs**](TicketSystemPatchArgs.md)| Ticket System Patch Args | [optional]

### Return type

[**TicketSystemModelV2**](TicketSystemModelV2.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ticket System Model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

