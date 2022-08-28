# plugins.RolesApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**roles_service_create**](RolesApi.md#roles_service_create) | **POST** /v1/roles | Create Role
[**roles_service_get**](RolesApi.md#roles_service_get) | **GET** /v1/roles/{id} | Get Role
[**roles_service_get_all**](RolesApi.md#roles_service_get_all) | **GET** /v1/roles | Search Roles
[**roles_service_get_all_role_permissions_by_type**](RolesApi.md#roles_service_get_all_role_permissions_by_type) | **GET** /v1/roles/{id}/permissions/unassigned | Get Unassigned Role Permissions
[**roles_service_get_role_groups**](RolesApi.md#roles_service_get_role_groups) | **GET** /v1/roles/{id}/groups | Get Role Groups
[**roles_service_get_role_permissions**](RolesApi.md#roles_service_get_role_permissions) | **GET** /v1/roles/{id}/permissions | Get Assigned Role Permissions
[**roles_service_patch_groups**](RolesApi.md#roles_service_patch_groups) | **PATCH** /v1/roles/{roleId}/groups | Patch Role Group Assignments
[**roles_service_stub**](RolesApi.md#roles_service_stub) | **GET** /v1/roles/stub | Get Role Stub
[**roles_service_update**](RolesApi.md#roles_service_update) | **PATCH** /v1/roles/{id} | Update Role
[**roles_service_update_permissions**](RolesApi.md#roles_service_update_permissions) | **PUT** /v1/roles/{id}/permissions | Update Role Permission Assignments


# **roles_service_create**
> RoleModel roles_service_create()

Create Role

Create a new Role

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import roles_api
from plugins.model.role_create_args import RoleCreateArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.role_model import RoleModel
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
    api_instance = roles_api.RolesApi(api_client)
    role_create_args = RoleCreateArgs(
        enabled=True,
        name=None,
    ) # RoleCreateArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Role
        api_response = api_instance.roles_service_create(role_create_args=role_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling RolesApi->roles_service_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_create_args** | [**RoleCreateArgs**](RoleCreateArgs.md)| args | [optional]

### Return type

[**RoleModel**](RoleModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Role object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_service_get**
> RoleModel roles_service_get(id)

Get Role

Get Role by Role ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import roles_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.role_model import RoleModel
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
    api_instance = roles_api.RolesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id

    # example passing only required values which don't have defaults set
    try:
        # Get Role
        api_response = api_instance.roles_service_get(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling RolesApi->roles_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |

### Return type

[**RoleModel**](RoleModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Role model result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_service_get_all**
> PagingOfRoleModel roles_service_get_all()

Search Roles

Search, filter, sort, and page Roles

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import roles_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_role_model import PagingOfRoleModel
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
    api_instance = roles_api.RolesApi(api_client)
    filter_group_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Only return roles assigned to this group id.  Will be ignored if UserId is set (optional)
    filter_include_inactive = True # bool | Whether to include inactive Roles in the results (optional)
    filter_user_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Only return roles assigned to this user id.  Will supercede GroupId if set (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Roles
        api_response = api_instance.roles_service_get_all(filter_group_id=filter_group_id, filter_include_inactive=filter_include_inactive, filter_user_id=filter_user_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling RolesApi->roles_service_get_all: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_group_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Only return roles assigned to this group id.  Will be ignored if UserId is set | [optional]
 **filter_include_inactive** | **bool**| Whether to include inactive Roles in the results | [optional]
 **filter_user_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Only return roles assigned to this user id.  Will supercede GroupId if set | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfRoleModel**](PagingOfRoleModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Role search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_service_get_all_role_permissions_by_type**
> PagingOfRolePermissionModel roles_service_get_all_role_permissions_by_type(id)

Get Unassigned Role Permissions

Get unassigned Role Permissions matching the type of a specific Role by Role ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import roles_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_role_permission_model import PagingOfRolePermissionModel
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
    api_instance = roles_api.RolesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Unassigned Role Permissions
        api_response = api_instance.roles_service_get_all_role_permissions_by_type(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling RolesApi->roles_service_get_all_role_permissions_by_type: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Unassigned Role Permissions
        api_response = api_instance.roles_service_get_all_role_permissions_by_type(id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling RolesApi->roles_service_get_all_role_permissions_by_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfRolePermissionModel**](PagingOfRolePermissionModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Role model result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_service_get_role_groups**
> PagingOfRoleGroupSummaryAndGroupMembershipFilter roles_service_get_role_groups(id)

Get Role Groups

Get assigned Groups by RoleId

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import roles_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.paging_of_role_group_summary_and_group_membership_filter import PagingOfRoleGroupSummaryAndGroupMembershipFilter
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
    api_instance = roles_api.RolesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    filter_include_inactive_users_for_group = True # bool | Whether to include inactive users in the results (optional)
    filter_user_domain_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Filter only users in a specific domain (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Role Groups
        api_response = api_instance.roles_service_get_role_groups(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling RolesApi->roles_service_get_role_groups: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Role Groups
        api_response = api_instance.roles_service_get_role_groups(id, filter_include_inactive_users_for_group=filter_include_inactive_users_for_group, filter_user_domain_id=filter_user_domain_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling RolesApi->roles_service_get_role_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **filter_include_inactive_users_for_group** | **bool**| Whether to include inactive users in the results | [optional]
 **filter_user_domain_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Filter only users in a specific domain | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfRoleGroupSummaryAndGroupMembershipFilter**](PagingOfRoleGroupSummaryAndGroupMembershipFilter.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Role Group summary result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_service_get_role_permissions**
> PagingOfRolePermissionModel roles_service_get_role_permissions(id)

Get Assigned Role Permissions

Get Permissions assigned to a single Role by Role ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import roles_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_role_permission_model import PagingOfRolePermissionModel
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
    api_instance = roles_api.RolesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Assigned Role Permissions
        api_response = api_instance.roles_service_get_role_permissions(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling RolesApi->roles_service_get_role_permissions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Assigned Role Permissions
        api_response = api_instance.roles_service_get_role_permissions(id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling RolesApi->roles_service_get_role_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfRolePermissionModel**](PagingOfRolePermissionModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Role Permission model result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_service_patch_groups**
> RoleGroupsPatchResult roles_service_patch_groups(role_id)

Patch Role Group Assignments

Update Groups assigned to a Role by sending list(s) of Group IDs to add/remove

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import roles_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.role_groups_patch_args import RoleGroupsPatchArgs
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.role_groups_patch_result import RoleGroupsPatchResult
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
    api_instance = roles_api.RolesApi(api_client)
    role_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Role ID
    role_groups_patch_args = RoleGroupsPatchArgs(
        data=RoleGroupsPatchModel(
            group_ids_to_add=UpdateFieldValueOfInt32Array(
                dirty=True,
                value=[
                    None,
                ],
            ),
            group_ids_to_remove=UpdateFieldValueOfInt32Array(
                dirty=True,
                value=[
                    None,
                ],
            ),
        ),
    ) # RoleGroupsPatchArgs | Role Groups update options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Patch Role Group Assignments
        api_response = api_instance.roles_service_patch_groups(role_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling RolesApi->roles_service_patch_groups: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Patch Role Group Assignments
        api_response = api_instance.roles_service_patch_groups(role_id, role_groups_patch_args=role_groups_patch_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling RolesApi->roles_service_patch_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Role ID |
 **role_groups_patch_args** | [**RoleGroupsPatchArgs**](RoleGroupsPatchArgs.md)| Role Groups update options | [optional]

### Return type

[**RoleGroupsPatchResult**](RoleGroupsPatchResult.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Role object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_service_stub**
> RoleModel roles_service_stub()

Get Role Stub

Return the default values for a new Role

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import roles_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.role_model import RoleModel
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
    api_instance = roles_api.RolesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Role Stub
        api_response = api_instance.roles_service_stub()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling RolesApi->roles_service_stub: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**RoleModel**](RoleModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Role object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_service_update**
> RoleModel roles_service_update(id)

Update Role

Update a single Role by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import roles_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.role_model import RoleModel
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.role_patch_args import RolePatchArgs
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
    api_instance = roles_api.RolesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Role ID
    role_patch_args = RolePatchArgs(
        data=RolePatchModel(
            enabled=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            name=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
        ),
    ) # RolePatchArgs | Role update options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Role
        api_response = api_instance.roles_service_update(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling RolesApi->roles_service_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Role
        api_response = api_instance.roles_service_update(id, role_patch_args=role_patch_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling RolesApi->roles_service_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Role ID |
 **role_patch_args** | [**RolePatchArgs**](RolePatchArgs.md)| Role update options | [optional]

### Return type

[**RoleModel**](RoleModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Role object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_service_update_permissions**
> RolePermissionsAssignmentResponse roles_service_update_permissions(id)

Update Role Permission Assignments

Update all Permissions assigned to Role

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import roles_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.role_permissions_assignment_request import RolePermissionsAssignmentRequest
from plugins.model.role_permissions_assignment_response import RolePermissionsAssignmentResponse
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
    api_instance = roles_api.RolesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    role_permissions_assignment_request = RolePermissionsAssignmentRequest(
        role_permission_ids=[
            None,
        ],
    ) # RolePermissionsAssignmentRequest | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Role Permission Assignments
        api_response = api_instance.roles_service_update_permissions(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling RolesApi->roles_service_update_permissions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Role Permission Assignments
        api_response = api_instance.roles_service_update_permissions(id, role_permissions_assignment_request=role_permissions_assignment_request)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling RolesApi->roles_service_update_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **role_permissions_assignment_request** | [**RolePermissionsAssignmentRequest**](RolePermissionsAssignmentRequest.md)| args | [optional]

### Return type

[**RolePermissionsAssignmentResponse**](RolePermissionsAssignmentResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success / Fail |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

