# plugins.JumpboxRouteApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jumpbox_route_service_add_jumpbox_route_level**](JumpboxRouteApi.md#jumpbox_route_service_add_jumpbox_route_level) | **POST** /v1/jumpbox-route/{id}/level | Create JumpboxRoute Level
[**jumpbox_route_service_createjumpbox_route**](JumpboxRouteApi.md#jumpbox_route_service_createjumpbox_route) | **POST** /v1/jumpbox-route | Create JumpboxRoute
[**jumpbox_route_service_delete_jumpbox_route_level**](JumpboxRouteApi.md#jumpbox_route_service_delete_jumpbox_route_level) | **DELETE** /v1/jumpbox-route/{id}/level/{order} | Delete JumpboxRoute Level
[**jumpbox_route_service_get**](JumpboxRouteApi.md#jumpbox_route_service_get) | **GET** /v1/jumpbox-route/{id} | Find JumpboxRoute
[**jumpbox_route_service_get_all_levels**](JumpboxRouteApi.md#jumpbox_route_service_get_all_levels) | **GET** /v1/jumpbox-route/{id}/level | Find Levels for a Jumpbox Route
[**jumpbox_route_service_get_all_routes_for_user**](JumpboxRouteApi.md#jumpbox_route_service_get_all_routes_for_user) | **GET** /v1/jumpbox-route/user | Get Jumpbox Routes visible to a user
[**jumpbox_route_service_get_jumpbox_audits**](JumpboxRouteApi.md#jumpbox_route_service_get_jumpbox_audits) | **GET** /v1/jumpbox-route/{id}/audit | Get Jumpbox Route Audits
[**jumpbox_route_service_patch_jumpbox_route_level**](JumpboxRouteApi.md#jumpbox_route_service_patch_jumpbox_route_level) | **PATCH** /v1/jumpbox-route/{id}/level/{order} | Edit JumpboxRoute Level
[**jumpbox_route_service_search**](JumpboxRouteApi.md#jumpbox_route_service_search) | **GET** /v1/jumpbox-route/search | Search JumpboxRoutes
[**jumpbox_route_service_update_jumpbox_route**](JumpboxRouteApi.md#jumpbox_route_service_update_jumpbox_route) | **PATCH** /v1/jumpbox-route/{id} | Udpate a Jumpbox Route


# **jumpbox_route_service_add_jumpbox_route_level**
> JumpboxRouteLevelSummaryModel jumpbox_route_service_add_jumpbox_route_level(id)

Create JumpboxRoute Level

Create a new Jumpbox Route Level

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import jumpbox_route_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.jumpbox_route_level_summary_model import JumpboxRouteLevelSummaryModel
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.jumpbox_route_level_create_args import JumpboxRouteLevelCreateArgs
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
    api_instance = jumpbox_route_api.JumpboxRouteApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    jumpbox_route_level_create_args = JumpboxRouteLevelCreateArgs(
        data=JumpboxRouteLevelCreateModel(
            port=None,
            secret_id=None,
        ),
    ) # JumpboxRouteLevelCreateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create JumpboxRoute Level
        api_response = api_instance.jumpbox_route_service_add_jumpbox_route_level(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling JumpboxRouteApi->jumpbox_route_service_add_jumpbox_route_level: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create JumpboxRoute Level
        api_response = api_instance.jumpbox_route_service_add_jumpbox_route_level(id, jumpbox_route_level_create_args=jumpbox_route_level_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling JumpboxRouteApi->jumpbox_route_service_add_jumpbox_route_level: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **jumpbox_route_level_create_args** | [**JumpboxRouteLevelCreateArgs**](JumpboxRouteLevelCreateArgs.md)| args | [optional]

### Return type

[**JumpboxRouteLevelSummaryModel**](JumpboxRouteLevelSummaryModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JumpboxRouteLevel Summary Object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jumpbox_route_service_createjumpbox_route**
> JumpboxRouteSummaryModel jumpbox_route_service_createjumpbox_route()

Create JumpboxRoute

Create a new Jumpbox Route

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import jumpbox_route_api
from plugins.model.jumpbox_route_create_args import JumpboxRouteCreateArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.jumpbox_route_summary_model import JumpboxRouteSummaryModel
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
    api_instance = jumpbox_route_api.JumpboxRouteApi(api_client)
    jumpbox_route_create_args = JumpboxRouteCreateArgs(
        data=JumpboxRouteCreateModel(
            active=True,
            description=None,
            name=None,
        ),
    ) # JumpboxRouteCreateArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create JumpboxRoute
        api_response = api_instance.jumpbox_route_service_createjumpbox_route(jumpbox_route_create_args=jumpbox_route_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling JumpboxRouteApi->jumpbox_route_service_createjumpbox_route: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jumpbox_route_create_args** | [**JumpboxRouteCreateArgs**](JumpboxRouteCreateArgs.md)| args | [optional]

### Return type

[**JumpboxRouteSummaryModel**](JumpboxRouteSummaryModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JumpboxRoute Summary Object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jumpbox_route_service_delete_jumpbox_route_level**
> bool jumpbox_route_service_delete_jumpbox_route_level(id, order)

Delete JumpboxRoute Level

Delete a Jumpbox Route Level on a Jumpbox Route

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import jumpbox_route_api
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
    api_instance = jumpbox_route_api.JumpboxRouteApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    order = None # bool, date, datetime, dict, float, int, list, str, none_type | order

    # example passing only required values which don't have defaults set
    try:
        # Delete JumpboxRoute Level
        api_response = api_instance.jumpbox_route_service_delete_jumpbox_route_level(id, order)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling JumpboxRouteApi->jumpbox_route_service_delete_jumpbox_route_level: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **order** | **bool, date, datetime, dict, float, int, list, str, none_type**| order |

### Return type

**bool**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jumpbox_route_service_get**
> JumpboxRouteModel jumpbox_route_service_get(id)

Find JumpboxRoute

Find a Jumpbox Route by Id

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import jumpbox_route_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.jumpbox_route_model import JumpboxRouteModel
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
    api_instance = jumpbox_route_api.JumpboxRouteApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Jumpbox Route Id

    # example passing only required values which don't have defaults set
    try:
        # Find JumpboxRoute
        api_response = api_instance.jumpbox_route_service_get(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling JumpboxRouteApi->jumpbox_route_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Jumpbox Route Id |

### Return type

[**JumpboxRouteModel**](JumpboxRouteModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JumpboxRoute detail object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jumpbox_route_service_get_all_levels**
> PagingOfJumpboxRouteLevelViewModel jumpbox_route_service_get_all_levels(id)

Find Levels for a Jumpbox Route

Find all Levels for a Jumpbox Route by Jumpbox Route Id

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import jumpbox_route_api
from plugins.model.paging_of_jumpbox_route_level_view_model import PagingOfJumpboxRouteLevelViewModel
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
    api_instance = jumpbox_route_api.JumpboxRouteApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Jumpbox Route Id

    # example passing only required values which don't have defaults set
    try:
        # Find Levels for a Jumpbox Route
        api_response = api_instance.jumpbox_route_service_get_all_levels(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling JumpboxRouteApi->jumpbox_route_service_get_all_levels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Jumpbox Route Id |

### Return type

[**PagingOfJumpboxRouteLevelViewModel**](PagingOfJumpboxRouteLevelViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Jumpbox route Level View Model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jumpbox_route_service_get_all_routes_for_user**
> PagingOfJumpboxRouteSummaryModel jumpbox_route_service_get_all_routes_for_user()

Get Jumpbox Routes visible to a user

Get an array of Jumpbox Routes that are visible to a specific user

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import jumpbox_route_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.paging_of_jumpbox_route_summary_model import PagingOfJumpboxRouteSummaryModel
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
    api_instance = jumpbox_route_api.JumpboxRouteApi(api_client)
    filter_include_active = True # bool | IncludeActive (optional)
    filter_include_inactive = True # bool | IncludeInactive (optional)
    filter_search_term = None # bool, date, datetime, dict, float, int, list, str, none_type | SearchTerm (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Jumpbox Routes visible to a user
        api_response = api_instance.jumpbox_route_service_get_all_routes_for_user(filter_include_active=filter_include_active, filter_include_inactive=filter_include_inactive, filter_search_term=filter_search_term, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling JumpboxRouteApi->jumpbox_route_service_get_all_routes_for_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_include_active** | **bool**| IncludeActive | [optional]
 **filter_include_inactive** | **bool**| IncludeInactive | [optional]
 **filter_search_term** | **bool, date, datetime, dict, float, int, list, str, none_type**| SearchTerm | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfJumpboxRouteSummaryModel**](PagingOfJumpboxRouteSummaryModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Jumpbox Route Summary Model paging object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jumpbox_route_service_get_jumpbox_audits**
> PagingOfJumpboxRouteAuditModel jumpbox_route_service_get_jumpbox_audits(id)

Get Jumpbox Route Audits

Retrieve audits for the Jumpbox Routes

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import jumpbox_route_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_jumpbox_route_audit_model import PagingOfJumpboxRouteAuditModel
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
    api_instance = jumpbox_route_api.JumpboxRouteApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    is_exporting = True # bool | isExporting (optional)
    filter_search_term = None # bool, date, datetime, dict, float, int, list, str, none_type | SearchTerm (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Jumpbox Route Audits
        api_response = api_instance.jumpbox_route_service_get_jumpbox_audits(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling JumpboxRouteApi->jumpbox_route_service_get_jumpbox_audits: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Jumpbox Route Audits
        api_response = api_instance.jumpbox_route_service_get_jumpbox_audits(id, is_exporting=is_exporting, filter_search_term=filter_search_term, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling JumpboxRouteApi->jumpbox_route_service_get_jumpbox_audits: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **is_exporting** | **bool**| isExporting | [optional]
 **filter_search_term** | **bool, date, datetime, dict, float, int, list, str, none_type**| SearchTerm | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfJumpboxRouteAuditModel**](PagingOfJumpboxRouteAuditModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paged list of audit entries |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jumpbox_route_service_patch_jumpbox_route_level**
> JumpboxRouteLevelSummaryModel jumpbox_route_service_patch_jumpbox_route_level(id, order)

Edit JumpboxRoute Level

Edit a Jumpbox Route Level

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import jumpbox_route_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.jumpbox_route_level_summary_model import JumpboxRouteLevelSummaryModel
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.jumpbox_route_level_patch_args import JumpboxRouteLevelPatchArgs
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
    api_instance = jumpbox_route_api.JumpboxRouteApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    order = None # bool, date, datetime, dict, float, int, list, str, none_type | order
    jumpbox_route_level_patch_args = JumpboxRouteLevelPatchArgs(
        data=JumpboxRouteLevelPatchModel(
            order=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            port=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            secret_id=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
        ),
    ) # JumpboxRouteLevelPatchArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit JumpboxRoute Level
        api_response = api_instance.jumpbox_route_service_patch_jumpbox_route_level(id, order)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling JumpboxRouteApi->jumpbox_route_service_patch_jumpbox_route_level: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit JumpboxRoute Level
        api_response = api_instance.jumpbox_route_service_patch_jumpbox_route_level(id, order, jumpbox_route_level_patch_args=jumpbox_route_level_patch_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling JumpboxRouteApi->jumpbox_route_service_patch_jumpbox_route_level: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **order** | **bool, date, datetime, dict, float, int, list, str, none_type**| order |
 **jumpbox_route_level_patch_args** | [**JumpboxRouteLevelPatchArgs**](JumpboxRouteLevelPatchArgs.md)| args | [optional]

### Return type

[**JumpboxRouteLevelSummaryModel**](JumpboxRouteLevelSummaryModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JumpboxRouteLevel Summary Object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jumpbox_route_service_search**
> PagingOfJumpboxRouteSummaryModel jumpbox_route_service_search()

Search JumpboxRoutes

Search, filter, sort, and page Jumpbox routes

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import jumpbox_route_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.paging_of_jumpbox_route_summary_model import PagingOfJumpboxRouteSummaryModel
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
    api_instance = jumpbox_route_api.JumpboxRouteApi(api_client)
    filter_include_active = True # bool | IncludeActive (optional)
    filter_include_inactive = True # bool | IncludeInactive (optional)
    filter_search_term = None # bool, date, datetime, dict, float, int, list, str, none_type | SearchTerm (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search JumpboxRoutes
        api_response = api_instance.jumpbox_route_service_search(filter_include_active=filter_include_active, filter_include_inactive=filter_include_inactive, filter_search_term=filter_search_term, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling JumpboxRouteApi->jumpbox_route_service_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_include_active** | **bool**| IncludeActive | [optional]
 **filter_include_inactive** | **bool**| IncludeInactive | [optional]
 **filter_search_term** | **bool, date, datetime, dict, float, int, list, str, none_type**| SearchTerm | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfJumpboxRouteSummaryModel**](PagingOfJumpboxRouteSummaryModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JumpboxRoute search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jumpbox_route_service_update_jumpbox_route**
> JumpboxRouteSummaryModel jumpbox_route_service_update_jumpbox_route(id)

Udpate a Jumpbox Route

Update an existing Jumpbox Route using the existing Jumpbox Route's ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import jumpbox_route_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.jumpbox_route_summary_model import JumpboxRouteSummaryModel
from plugins.model.jumpbox_route_patch_args import JumpboxRoutePatchArgs
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
    api_instance = jumpbox_route_api.JumpboxRouteApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    jumpbox_route_patch_args = JumpboxRoutePatchArgs(
        data=JumpboxRoutePatchModel(
            active=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            description=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            jumpbox_route_id=None,
            name=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
        ),
    ) # JumpboxRoutePatchArgs | jumpboxRouteUpdateArgs (optional)

    # example passing only required values which don't have defaults set
    try:
        # Udpate a Jumpbox Route
        api_response = api_instance.jumpbox_route_service_update_jumpbox_route(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling JumpboxRouteApi->jumpbox_route_service_update_jumpbox_route: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Udpate a Jumpbox Route
        api_response = api_instance.jumpbox_route_service_update_jumpbox_route(id, jumpbox_route_patch_args=jumpbox_route_patch_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling JumpboxRouteApi->jumpbox_route_service_update_jumpbox_route: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **jumpbox_route_patch_args** | [**JumpboxRoutePatchArgs**](JumpboxRoutePatchArgs.md)| jumpboxRouteUpdateArgs | [optional]

### Return type

[**JumpboxRouteSummaryModel**](JumpboxRouteSummaryModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JumpboxRoute Summary Object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

