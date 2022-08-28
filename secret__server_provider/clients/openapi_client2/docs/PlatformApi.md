# plugins.PlatformApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**platform_service_get_synchronization_status**](PlatformApi.md#platform_service_get_synchronization_status) | **GET** /v1/platform/synchronization | Platform Sync Status
[**platform_service_link_platform_group**](PlatformApi.md#platform_service_link_platform_group) | **POST** /v1/platform/group | Link a group from Platform
[**platform_service_search_platform_for_groups**](PlatformApi.md#platform_service_search_platform_for_groups) | **GET** /v1/platform/groups/search-directory | Search in Platform for groups
[**platform_service_synchronize_now**](PlatformApi.md#platform_service_synchronize_now) | **POST** /v1/platform/synchronization-now | Synchronize Platform user properties and group memberships
[**platform_service_unlink_domain_group**](PlatformApi.md#platform_service_unlink_domain_group) | **DELETE** /v1/platform/group/{groupId} | Unlink a group from Platform


# **platform_service_get_synchronization_status**
> PlatformSynchronizationStatus platform_service_get_synchronization_status()

Platform Sync Status

Return status of platform synchronization

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import platform_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.platform_synchronization_status import PlatformSynchronizationStatus
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
    api_instance = platform_api.PlatformApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Platform Sync Status
        api_response = api_instance.platform_service_get_synchronization_status()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling PlatformApi->platform_service_get_synchronization_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**PlatformSynchronizationStatus**](PlatformSynchronizationStatus.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Whether or not the sync has started |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_service_link_platform_group**
> bool platform_service_link_platform_group()

Link a group from Platform

Linking or adding a group with Platform will allow permissions to be added before those members log in.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import platform_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.link_external_group_args import LinkExternalGroupArgs
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
    api_instance = platform_api.PlatformApi(api_client)
    link_external_group_args = LinkExternalGroupArgs(
        data=LinkExternalGroupSettings(
            domain_identifier="domain_identifier_example",
            name="name_example",
        ),
    ) # LinkExternalGroupArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Link a group from Platform
        api_response = api_instance.platform_service_link_platform_group(link_external_group_args=link_external_group_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling PlatformApi->platform_service_link_platform_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_external_group_args** | [**LinkExternalGroupArgs**](LinkExternalGroupArgs.md)| args | [optional]

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
**200** | Success status |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_service_search_platform_for_groups**
> ExternalGroupViewModel platform_service_search_platform_for_groups()

Search in Platform for groups

Search in Platform for external groups using Platform credentials

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import platform_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.external_group_view_model import ExternalGroupViewModel
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
    api_instance = platform_api.PlatformApi(api_client)
    search_text = "searchText_example" # str | Search text. Use * for wildcards, ex: Admin*. Leave empty to return all. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search in Platform for groups
        api_response = api_instance.platform_service_search_platform_for_groups(search_text=search_text)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling PlatformApi->platform_service_search_platform_for_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_text** | **str**| Search text. Use * for wildcards, ex: Admin*. Leave empty to return all. | [optional]

### Return type

[**ExternalGroupViewModel**](ExternalGroupViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of groups matching search criteria |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_service_synchronize_now**
> bool platform_service_synchronize_now()

Synchronize Platform user properties and group memberships

Run synchronize to update groups and user properties for Platform users

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import platform_api
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
    api_instance = platform_api.PlatformApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Synchronize Platform user properties and group memberships
        api_response = api_instance.platform_service_synchronize_now()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling PlatformApi->platform_service_synchronize_now: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**200** | True if the command was initiated successfully |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_service_unlink_domain_group**
> bool platform_service_unlink_domain_group(group_id)

Unlink a group from Platform

Unlinking a group from Platform will disable the group.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import platform_api
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
    api_instance = platform_api.PlatformApi(api_client)
    group_id = 1 # int | groupId

    # example passing only required values which don't have defaults set
    try:
        # Unlink a group from Platform
        api_response = api_instance.platform_service_unlink_domain_group(group_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling PlatformApi->platform_service_unlink_domain_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| groupId |

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
**200** | Success status |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

