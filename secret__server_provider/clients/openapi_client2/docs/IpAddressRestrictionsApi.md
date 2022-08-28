# plugins.IpAddressRestrictionsApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ip_address_restrictions_service_create**](IpAddressRestrictionsApi.md#ip_address_restrictions_service_create) | **POST** /v1/ipaddress-restrictions | Create IP Address restriction
[**ip_address_restrictions_service_create_group_ip_restriction**](IpAddressRestrictionsApi.md#ip_address_restrictions_service_create_group_ip_restriction) | **POST** /v1/ipaddress-restrictions/{id}/groups | Create Group IP Address restriction
[**ip_address_restrictions_service_create_user_ip_restriction**](IpAddressRestrictionsApi.md#ip_address_restrictions_service_create_user_ip_restriction) | **POST** /v1/ipaddress-restrictions/{id}/users | Create User IP Address restriction
[**ip_address_restrictions_service_delete**](IpAddressRestrictionsApi.md#ip_address_restrictions_service_delete) | **DELETE** /v1/ipaddress-restrictions/{id} | Delete IP Address restriction
[**ip_address_restrictions_service_delete_group_ip_restriction**](IpAddressRestrictionsApi.md#ip_address_restrictions_service_delete_group_ip_restriction) | **DELETE** /v1/ipaddress-restrictions/{id}/groups/{groupId} | Delete Group IP Address restriction
[**ip_address_restrictions_service_delete_user_ip_restriction**](IpAddressRestrictionsApi.md#ip_address_restrictions_service_delete_user_ip_restriction) | **DELETE** /v1/ipaddress-restrictions/{id}/users/{userId} | Delete User IP Address restriction
[**ip_address_restrictions_service_get**](IpAddressRestrictionsApi.md#ip_address_restrictions_service_get) | **GET** /v1/ipaddress-restrictions/{id} | Get IP Address restriction
[**ip_address_restrictions_service_get_all_by_group**](IpAddressRestrictionsApi.md#ip_address_restrictions_service_get_all_by_group) | **GET** /v1/groups/{id}/ipaddress-restrictions | Search IP Address restrictions assigned to a group
[**ip_address_restrictions_service_get_all_by_user**](IpAddressRestrictionsApi.md#ip_address_restrictions_service_get_all_by_user) | **GET** /v1/users/{id}/ipaddress-restrictions | Search IP Address restrictions assigned to a user
[**ip_address_restrictions_service_get_group**](IpAddressRestrictionsApi.md#ip_address_restrictions_service_get_group) | **GET** /v1/ipaddress-restrictions/{id}/groups/{groupId} | Get Group IP Address restriction
[**ip_address_restrictions_service_get_user_ip_restriction**](IpAddressRestrictionsApi.md#ip_address_restrictions_service_get_user_ip_restriction) | **GET** /v1/ipaddress-restrictions/{id}/users/{userId} | Get User IP Address restriction
[**ip_address_restrictions_service_search**](IpAddressRestrictionsApi.md#ip_address_restrictions_service_search) | **GET** /v1/ipaddress-restrictions | Search IP Address restrictions
[**ip_address_restrictions_service_search_groups**](IpAddressRestrictionsApi.md#ip_address_restrictions_service_search_groups) | **GET** /v1/ipaddress-restrictions/{id}/groups | Search groups assigned to an IP Address restriction
[**ip_address_restrictions_service_search_users**](IpAddressRestrictionsApi.md#ip_address_restrictions_service_search_users) | **GET** /v1/ipaddress-restrictions/{id}/users | Search users assigned to an IP Address restriction
[**ip_address_restrictions_service_update**](IpAddressRestrictionsApi.md#ip_address_restrictions_service_update) | **PUT** /v1/ipaddress-restrictions/{id} | Update IP Address restriction


# **ip_address_restrictions_service_create**
> IpAddressRestrictionModel ip_address_restrictions_service_create()

Create IP Address restriction

Create a new IP Address restriction

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import ip_address_restrictions_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.ip_address_restriction_create_args import IpAddressRestrictionCreateArgs
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.ip_address_restriction_model import IpAddressRestrictionModel
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
    api_instance = ip_address_restrictions_api.IpAddressRestrictionsApi(api_client)
    ip_address_restriction_create_args = IpAddressRestrictionCreateArgs(
        name="name_example",
        range="range_example",
    ) # IpAddressRestrictionCreateArgs | IP Address restriction (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create IP Address restriction
        api_response = api_instance.ip_address_restrictions_service_create(ip_address_restriction_create_args=ip_address_restriction_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling IpAddressRestrictionsApi->ip_address_restrictions_service_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_address_restriction_create_args** | [**IpAddressRestrictionCreateArgs**](IpAddressRestrictionCreateArgs.md)| IP Address restriction | [optional]

### Return type

[**IpAddressRestrictionModel**](IpAddressRestrictionModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IP Address restriction object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_address_restrictions_service_create_group_ip_restriction**
> GroupIpAddressRestrictionModel ip_address_restrictions_service_create_group_ip_restriction(id)

Create Group IP Address restriction

Create a new Group IP Address restriction

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import ip_address_restrictions_api
from plugins.model.group_ip_address_restriction_model import GroupIpAddressRestrictionModel
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.group_ip_address_restriction_create_args import GroupIpAddressRestrictionCreateArgs
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
    api_instance = ip_address_restrictions_api.IpAddressRestrictionsApi(api_client)
    id = 1 # int | IP Address restriction ID
    group_ip_address_restriction_create_args = GroupIpAddressRestrictionCreateArgs(
        group_id=1,
        ip_address_restriction_id=1,
    ) # GroupIpAddressRestrictionCreateArgs | Group IP Address restriction (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Group IP Address restriction
        api_response = api_instance.ip_address_restrictions_service_create_group_ip_restriction(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling IpAddressRestrictionsApi->ip_address_restrictions_service_create_group_ip_restriction: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Group IP Address restriction
        api_response = api_instance.ip_address_restrictions_service_create_group_ip_restriction(id, group_ip_address_restriction_create_args=group_ip_address_restriction_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling IpAddressRestrictionsApi->ip_address_restrictions_service_create_group_ip_restriction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| IP Address restriction ID |
 **group_ip_address_restriction_create_args** | [**GroupIpAddressRestrictionCreateArgs**](GroupIpAddressRestrictionCreateArgs.md)| Group IP Address restriction | [optional]

### Return type

[**GroupIpAddressRestrictionModel**](GroupIpAddressRestrictionModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group IP Address restriction object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_address_restrictions_service_create_user_ip_restriction**
> UserIpAddressRestrictionModel ip_address_restrictions_service_create_user_ip_restriction(id)

Create User IP Address restriction

Create a new User IP Address restriction

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import ip_address_restrictions_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.user_ip_address_restriction_model import UserIpAddressRestrictionModel
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.user_ip_address_restriction_create_args import UserIpAddressRestrictionCreateArgs
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
    api_instance = ip_address_restrictions_api.IpAddressRestrictionsApi(api_client)
    id = 1 # int | IP Address restriction ID
    user_ip_address_restriction_create_args = UserIpAddressRestrictionCreateArgs(
        ip_address_restriction_id=1,
        user_id=1,
    ) # UserIpAddressRestrictionCreateArgs | User IP Address restriction (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create User IP Address restriction
        api_response = api_instance.ip_address_restrictions_service_create_user_ip_restriction(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling IpAddressRestrictionsApi->ip_address_restrictions_service_create_user_ip_restriction: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create User IP Address restriction
        api_response = api_instance.ip_address_restrictions_service_create_user_ip_restriction(id, user_ip_address_restriction_create_args=user_ip_address_restriction_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling IpAddressRestrictionsApi->ip_address_restrictions_service_create_user_ip_restriction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| IP Address restriction ID |
 **user_ip_address_restriction_create_args** | [**UserIpAddressRestrictionCreateArgs**](UserIpAddressRestrictionCreateArgs.md)| User IP Address restriction | [optional]

### Return type

[**UserIpAddressRestrictionModel**](UserIpAddressRestrictionModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User IP Address restriction object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_address_restrictions_service_delete**
> DeletedModel ip_address_restrictions_service_delete(id)

Delete IP Address restriction

Delete an IP Address restriction by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import ip_address_restrictions_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.deleted_model import DeletedModel
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
    api_instance = ip_address_restrictions_api.IpAddressRestrictionsApi(api_client)
    id = 1 # int | IP Address restriction Id

    # example passing only required values which don't have defaults set
    try:
        # Delete IP Address restriction
        api_response = api_instance.ip_address_restrictions_service_delete(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling IpAddressRestrictionsApi->ip_address_restrictions_service_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| IP Address restriction Id |

### Return type

[**DeletedModel**](DeletedModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Object deletion result |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_address_restrictions_service_delete_group_ip_restriction**
> DeletedModel ip_address_restrictions_service_delete_group_ip_restriction(group_id, id)

Delete Group IP Address restriction

Delete a Group IP Address restriction by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import ip_address_restrictions_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.deleted_model import DeletedModel
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
    api_instance = ip_address_restrictions_api.IpAddressRestrictionsApi(api_client)
    group_id = 1 # int | Group ID
    id = 1 # int | IP Address restriction Id

    # example passing only required values which don't have defaults set
    try:
        # Delete Group IP Address restriction
        api_response = api_instance.ip_address_restrictions_service_delete_group_ip_restriction(group_id, id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling IpAddressRestrictionsApi->ip_address_restrictions_service_delete_group_ip_restriction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Group ID |
 **id** | **int**| IP Address restriction Id |

### Return type

[**DeletedModel**](DeletedModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Object deletion result |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_address_restrictions_service_delete_user_ip_restriction**
> DeletedModel ip_address_restrictions_service_delete_user_ip_restriction(id, user_id)

Delete User IP Address restriction

Delete a User IP Address restriction by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import ip_address_restrictions_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.deleted_model import DeletedModel
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
    api_instance = ip_address_restrictions_api.IpAddressRestrictionsApi(api_client)
    id = 1 # int | IP Address restriction Id
    user_id = 1 # int | User ID

    # example passing only required values which don't have defaults set
    try:
        # Delete User IP Address restriction
        api_response = api_instance.ip_address_restrictions_service_delete_user_ip_restriction(id, user_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling IpAddressRestrictionsApi->ip_address_restrictions_service_delete_user_ip_restriction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| IP Address restriction Id |
 **user_id** | **int**| User ID |

### Return type

[**DeletedModel**](DeletedModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Object deletion result |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_address_restrictions_service_get**
> IpAddressRestrictionModel ip_address_restrictions_service_get(id)

Get IP Address restriction

Get a single IP Address restriction by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import ip_address_restrictions_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.ip_address_restriction_model import IpAddressRestrictionModel
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
    api_instance = ip_address_restrictions_api.IpAddressRestrictionsApi(api_client)
    id = 1 # int | IP Address restriction ID

    # example passing only required values which don't have defaults set
    try:
        # Get IP Address restriction
        api_response = api_instance.ip_address_restrictions_service_get(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling IpAddressRestrictionsApi->ip_address_restrictions_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| IP Address restriction ID |

### Return type

[**IpAddressRestrictionModel**](IpAddressRestrictionModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IP Address restriction object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_address_restrictions_service_get_all_by_group**
> PagingOfGroupIpAddressRestrictionModel ip_address_restrictions_service_get_all_by_group(id)

Search IP Address restrictions assigned to a group

Search, filter, sort, and page IP Address restriction assigned to a group

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import ip_address_restrictions_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.paging_of_group_ip_address_restriction_model import PagingOfGroupIpAddressRestrictionModel
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
    api_instance = ip_address_restrictions_api.IpAddressRestrictionsApi(api_client)
    id = 1 # int | Group ID
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search IP Address restrictions assigned to a group
        api_response = api_instance.ip_address_restrictions_service_get_all_by_group(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling IpAddressRestrictionsApi->ip_address_restrictions_service_get_all_by_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search IP Address restrictions assigned to a group
        api_response = api_instance.ip_address_restrictions_service_get_all_by_group(id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling IpAddressRestrictionsApi->ip_address_restrictions_service_get_all_by_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Group ID |
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfGroupIpAddressRestrictionModel**](PagingOfGroupIpAddressRestrictionModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group and IP Address restriction search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_address_restrictions_service_get_all_by_user**
> PagingOfUserIpAddressRestrictionModel ip_address_restrictions_service_get_all_by_user(id)

Search IP Address restrictions assigned to a user

Search, filter, sort, and page IP Address restriction assigned to a user

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import ip_address_restrictions_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.paging_of_user_ip_address_restriction_model import PagingOfUserIpAddressRestrictionModel
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
    api_instance = ip_address_restrictions_api.IpAddressRestrictionsApi(api_client)
    id = 1 # int | User ID
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search IP Address restrictions assigned to a user
        api_response = api_instance.ip_address_restrictions_service_get_all_by_user(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling IpAddressRestrictionsApi->ip_address_restrictions_service_get_all_by_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search IP Address restrictions assigned to a user
        api_response = api_instance.ip_address_restrictions_service_get_all_by_user(id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling IpAddressRestrictionsApi->ip_address_restrictions_service_get_all_by_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User ID |
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfUserIpAddressRestrictionModel**](PagingOfUserIpAddressRestrictionModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User and IP Address restriction search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_address_restrictions_service_get_group**
> GroupIpAddressRestrictionModel ip_address_restrictions_service_get_group(group_id, id)

Get Group IP Address restriction

Get a single Group IP Address restriction by restriction and group ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import ip_address_restrictions_api
from plugins.model.group_ip_address_restriction_model import GroupIpAddressRestrictionModel
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
    api_instance = ip_address_restrictions_api.IpAddressRestrictionsApi(api_client)
    group_id = 1 # int | Group ID
    id = 1 # int | IP Address restriction ID

    # example passing only required values which don't have defaults set
    try:
        # Get Group IP Address restriction
        api_response = api_instance.ip_address_restrictions_service_get_group(group_id, id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling IpAddressRestrictionsApi->ip_address_restrictions_service_get_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Group ID |
 **id** | **int**| IP Address restriction ID |

### Return type

[**GroupIpAddressRestrictionModel**](GroupIpAddressRestrictionModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group and IP Address restriction object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_address_restrictions_service_get_user_ip_restriction**
> UserIpAddressRestrictionModel ip_address_restrictions_service_get_user_ip_restriction(id, user_id)

Get User IP Address restriction

Get a single User IP Address restriction by restriction and user ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import ip_address_restrictions_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.user_ip_address_restriction_model import UserIpAddressRestrictionModel
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
    api_instance = ip_address_restrictions_api.IpAddressRestrictionsApi(api_client)
    id = 1 # int | IP Address restriction ID
    user_id = 1 # int | User ID

    # example passing only required values which don't have defaults set
    try:
        # Get User IP Address restriction
        api_response = api_instance.ip_address_restrictions_service_get_user_ip_restriction(id, user_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling IpAddressRestrictionsApi->ip_address_restrictions_service_get_user_ip_restriction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| IP Address restriction ID |
 **user_id** | **int**| User ID |

### Return type

[**UserIpAddressRestrictionModel**](UserIpAddressRestrictionModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User and IP Address restriction object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_address_restrictions_service_search**
> PagingOfIpAddressRestrictionSummary ip_address_restrictions_service_search()

Search IP Address restrictions

Search, filter, sort, and page IP Address restrictions

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import ip_address_restrictions_api
from plugins.model.paging_of_ip_address_restriction_summary import PagingOfIpAddressRestrictionSummary
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
    api_instance = ip_address_restrictions_api.IpAddressRestrictionsApi(api_client)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search IP Address restrictions
        api_response = api_instance.ip_address_restrictions_service_search(skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling IpAddressRestrictionsApi->ip_address_restrictions_service_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfIpAddressRestrictionSummary**](PagingOfIpAddressRestrictionSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IP Address restriction search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_address_restrictions_service_search_groups**
> PagingOfGroupIpAddressRestrictionModel ip_address_restrictions_service_search_groups(id)

Search groups assigned to an IP Address restriction

Search, filter, sort, and page groups assigned to an IP Address restriction

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import ip_address_restrictions_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.paging_of_group_ip_address_restriction_model import PagingOfGroupIpAddressRestrictionModel
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
    api_instance = ip_address_restrictions_api.IpAddressRestrictionsApi(api_client)
    id = 1 # int | IP Address restriction ID
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search groups assigned to an IP Address restriction
        api_response = api_instance.ip_address_restrictions_service_search_groups(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling IpAddressRestrictionsApi->ip_address_restrictions_service_search_groups: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search groups assigned to an IP Address restriction
        api_response = api_instance.ip_address_restrictions_service_search_groups(id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling IpAddressRestrictionsApi->ip_address_restrictions_service_search_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| IP Address restriction ID |
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfGroupIpAddressRestrictionModel**](PagingOfGroupIpAddressRestrictionModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group and IP Address restriction search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_address_restrictions_service_search_users**
> PagingOfUserIpAddressRestrictionModel ip_address_restrictions_service_search_users(id)

Search users assigned to an IP Address restriction

Search, filter, sort, and page users assigned to an IP Address restriction

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import ip_address_restrictions_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.paging_of_user_ip_address_restriction_model import PagingOfUserIpAddressRestrictionModel
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
    api_instance = ip_address_restrictions_api.IpAddressRestrictionsApi(api_client)
    id = 1 # int | IP Address restriction ID
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search users assigned to an IP Address restriction
        api_response = api_instance.ip_address_restrictions_service_search_users(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling IpAddressRestrictionsApi->ip_address_restrictions_service_search_users: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search users assigned to an IP Address restriction
        api_response = api_instance.ip_address_restrictions_service_search_users(id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling IpAddressRestrictionsApi->ip_address_restrictions_service_search_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| IP Address restriction ID |
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfUserIpAddressRestrictionModel**](PagingOfUserIpAddressRestrictionModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User and IP Address restriction search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_address_restrictions_service_update**
> IpAddressRestrictionModel ip_address_restrictions_service_update(id)

Update IP Address restriction

Update a new IP Address restriction

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import ip_address_restrictions_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.ip_address_restriction_update_args import IpAddressRestrictionUpdateArgs
from plugins.model.ip_address_restriction_model import IpAddressRestrictionModel
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
    api_instance = ip_address_restrictions_api.IpAddressRestrictionsApi(api_client)
    id = 1 # int | IP Address restriction Id
    ip_address_restriction_update_args = IpAddressRestrictionUpdateArgs(
        id=1,
        name="name_example",
        range="range_example",
    ) # IpAddressRestrictionUpdateArgs | IP Address restriction (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update IP Address restriction
        api_response = api_instance.ip_address_restrictions_service_update(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling IpAddressRestrictionsApi->ip_address_restrictions_service_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update IP Address restriction
        api_response = api_instance.ip_address_restrictions_service_update(id, ip_address_restriction_update_args=ip_address_restriction_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling IpAddressRestrictionsApi->ip_address_restrictions_service_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| IP Address restriction Id |
 **ip_address_restriction_update_args** | [**IpAddressRestrictionUpdateArgs**](IpAddressRestrictionUpdateArgs.md)| IP Address restriction | [optional]

### Return type

[**IpAddressRestrictionModel**](IpAddressRestrictionModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IP Address restriction object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

