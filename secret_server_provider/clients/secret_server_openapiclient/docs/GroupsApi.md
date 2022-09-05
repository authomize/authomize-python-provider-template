# secret_server_openapiclient.GroupsApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groups_service_add_user_to_group**](GroupsApi.md#groups_service_add_user_to_group) | **POST** /v1/groups/{id}/users | Add User To Group
[**groups_service_create**](GroupsApi.md#groups_service_create) | **POST** /v1/groups | Create Group
[**groups_service_create_user_roles**](GroupsApi.md#groups_service_create_user_roles) | **POST** /v1/groups/{id}/roles | Add roles to existing group
[**groups_service_delete**](GroupsApi.md#groups_service_delete) | **DELETE** /v1/groups/{id} | Delete Group
[**groups_service_delete_user_roles**](GroupsApi.md#groups_service_delete_user_roles) | **DELETE** /v1/groups/{id}/roles | Remove roles from existing group
[**groups_service_get**](GroupsApi.md#groups_service_get) | **GET** /v1/groups/{id} | Get Group
[**groups_service_get_audit_group_assignments**](GroupsApi.md#groups_service_get_audit_group_assignments) | **GET** /v1/groups/audit | Get group audits
[**groups_service_get_group_membership**](GroupsApi.md#groups_service_get_group_membership) | **GET** /v1/groups/{id}/users | Get Group Membership
[**groups_service_get_group_user**](GroupsApi.md#groups_service_get_group_user) | **GET** /v1/groups/{id}/users/{userId} | Get User In Group
[**groups_service_get_group_users_lookup**](GroupsApi.md#groups_service_get_group_users_lookup) | **GET** /v1/groups/{id}/users-lookup | Get Group Users for display
[**groups_service_get_roles**](GroupsApi.md#groups_service_get_roles) | **GET** /v1/groups/{id}/roles | Gets roles for group
[**groups_service_lookup**](GroupsApi.md#groups_service_lookup) | **GET** /v1/groups/lookup | Lookup Groups
[**groups_service_patch_group**](GroupsApi.md#groups_service_patch_group) | **PATCH** /v1/groups/{groupId} | Patch Group
[**groups_service_patch_group_membership**](GroupsApi.md#groups_service_patch_group_membership) | **PATCH** /v1/groups/{id}/users | Patch Group Membership
[**groups_service_remove_user_from_group**](GroupsApi.md#groups_service_remove_user_from_group) | **DELETE** /v1/groups/{id}/users/{userId} | Remove User From Group
[**groups_service_search**](GroupsApi.md#groups_service_search) | **GET** /v1/groups | Search Groups
[**groups_service_stub**](GroupsApi.md#groups_service_stub) | **GET** /v1/groups/stub | Get Group Stub
[**groups_service_update**](GroupsApi.md#groups_service_update) | **PUT** /v1/groups/{id} | Update Group
[**groups_service_update_group_members**](GroupsApi.md#groups_service_update_group_members) | **PUT** /v1/groups/{groupId}/users | Update all members of a group
[**groups_service_update_user_roles**](GroupsApi.md#groups_service_update_user_roles) | **PUT** /v1/groups/{id}/roles | Update all roles on group


# **groups_service_add_user_to_group**
> GroupUserModel groups_service_add_user_to_group(id)

Add User To Group

Add a user to a group

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import groups_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.group_user_model import GroupUserModel
from secret_server_openapiclient.model.group_user_create_args import GroupUserCreateArgs
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
    api_instance = groups_api.GroupsApi(api_client)
    id = 1 # int | Group ID
    group_user_create_args = GroupUserCreateArgs(
        user_id=1,
    ) # GroupUserCreateArgs | Group user add options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add User To Group
        api_response = api_instance.groups_service_add_user_to_group(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling GroupsApi->groups_service_add_user_to_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add User To Group
        api_response = api_instance.groups_service_add_user_to_group(id, group_user_create_args=group_user_create_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling GroupsApi->groups_service_add_user_to_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Group ID |
 **group_user_create_args** | [**GroupUserCreateArgs**](GroupUserCreateArgs.md)| Group user add options | [optional]

### Return type

[**GroupUserModel**](GroupUserModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User group membership object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_service_create**
> GroupModel groups_service_create()

Create Group

Create a new group

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import groups_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.group_model import GroupModel
from secret_server_openapiclient.model.group_create_args import GroupCreateArgs
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
    api_instance = groups_api.GroupsApi(api_client)
    group_create_args = GroupCreateArgs(
        ad_guid="ad_guid_example",
        domain_id=1,
        enabled=True,
        has_group_owners=True,
        is_platform=True,
        name="name_example",
        owner_group_ids=[
            1,
        ],
        owner_group_names=[
            "owner_group_names_example",
        ],
        owner_user_ids=[
            1,
        ],
        owner_user_names=[
            "owner_user_names_example",
        ],
        synchronized=True,
        synchronize_now=True,
    ) # GroupCreateArgs | Group creation options (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Group
        api_response = api_instance.groups_service_create(group_create_args=group_create_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling GroupsApi->groups_service_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_create_args** | [**GroupCreateArgs**](GroupCreateArgs.md)| Group creation options | [optional]

### Return type

[**GroupModel**](GroupModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_service_create_user_roles**
> RoleChangeStatusModel groups_service_create_user_roles(id)

Add roles to existing group

Add roles to existing group

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import groups_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.role_change_status_model import RoleChangeStatusModel
from secret_server_openapiclient.model.role_assignments import RoleAssignments
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
    api_instance = groups_api.GroupsApi(api_client)
    id = 1 # int | id
    role_assignments = RoleAssignments(
        role_ids=[
            1,
        ],
    ) # RoleAssignments | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add roles to existing group
        api_response = api_instance.groups_service_create_user_roles(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling GroupsApi->groups_service_create_user_roles: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add roles to existing group
        api_response = api_instance.groups_service_create_user_roles(id, role_assignments=role_assignments)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling GroupsApi->groups_service_create_user_roles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id |
 **role_assignments** | [**RoleAssignments**](RoleAssignments.md)| args | [optional]

### Return type

[**RoleChangeStatusModel**](RoleChangeStatusModel.md)

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

# **groups_service_delete**
> DeletedModel groups_service_delete(id)

Delete Group

Delete a group by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import groups_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.deleted_model import DeletedModel
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
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
    api_instance = groups_api.GroupsApi(api_client)
    id = 1 # int | Group ID

    # example passing only required values which don't have defaults set
    try:
        # Delete Group
        api_response = api_instance.groups_service_delete(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling GroupsApi->groups_service_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Group ID |

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

# **groups_service_delete_user_roles**
> RoleChangeStatusModel groups_service_delete_user_roles(id)

Remove roles from existing group

Remove roles from existing group

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import groups_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.role_removals import RoleRemovals
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.role_change_status_model import RoleChangeStatusModel
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
    api_instance = groups_api.GroupsApi(api_client)
    id = 1 # int | id
    role_removals = RoleRemovals(
        role_ids=[
            1,
        ],
    ) # RoleRemovals | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove roles from existing group
        api_response = api_instance.groups_service_delete_user_roles(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling GroupsApi->groups_service_delete_user_roles: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove roles from existing group
        api_response = api_instance.groups_service_delete_user_roles(id, role_removals=role_removals)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling GroupsApi->groups_service_delete_user_roles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id |
 **role_removals** | [**RoleRemovals**](RoleRemovals.md)| args | [optional]

### Return type

[**RoleChangeStatusModel**](RoleChangeStatusModel.md)

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

# **groups_service_get**
> GroupModel groups_service_get(id)

Get Group

Get a single group by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import groups_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.group_model import GroupModel
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
    api_instance = groups_api.GroupsApi(api_client)
    id = 1 # int | Group ID

    # example passing only required values which don't have defaults set
    try:
        # Get Group
        api_response = api_instance.groups_service_get(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling GroupsApi->groups_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Group ID |

### Return type

[**GroupModel**](GroupModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_service_get_audit_group_assignments**
> PagingOfAdminAuditItem groups_service_get_audit_group_assignments()

Get group audits

Audit records for group assignments

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import groups_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.paging_of_admin_audit_item import PagingOfAdminAuditItem
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
    api_instance = groups_api.GroupsApi(api_client)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get group audits
        api_response = api_instance.groups_service_get_audit_group_assignments(skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling GroupsApi->groups_service_get_audit_group_assignments: %s\n" % e)
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

[**PagingOfAdminAuditItem**](PagingOfAdminAuditItem.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Audit records for group assignments |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_service_get_group_membership**
> PagingOfGroupUserSummary groups_service_get_group_membership(id)

Get Group Membership

Get group membership will return all of the users that are assigned as members of the group

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import groups_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.paging_of_group_user_summary import PagingOfGroupUserSummary
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
    api_instance = groups_api.GroupsApi(api_client)
    id = 1 # int | Group ID
    filter_include_inactive_users_for_group = True # bool | Whether to include inactive users in the results (optional)
    filter_user_domain_id = 1 # int | Filter only users in a specific domain (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Group Membership
        api_response = api_instance.groups_service_get_group_membership(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling GroupsApi->groups_service_get_group_membership: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Group Membership
        api_response = api_instance.groups_service_get_group_membership(id, filter_include_inactive_users_for_group=filter_include_inactive_users_for_group, filter_user_domain_id=filter_user_domain_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling GroupsApi->groups_service_get_group_membership: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Group ID |
 **filter_include_inactive_users_for_group** | **bool**| Whether to include inactive users in the results | [optional]
 **filter_user_domain_id** | **int**| Filter only users in a specific domain | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfGroupUserSummary**](PagingOfGroupUserSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group membership results |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_service_get_group_user**
> GroupUserModel groups_service_get_group_user(id, user_id)

Get User In Group

Get a user in a group

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import groups_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.group_user_model import GroupUserModel
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
    api_instance = groups_api.GroupsApi(api_client)
    id = 1 # int | Group ID
    user_id = 1 # int | User ID

    # example passing only required values which don't have defaults set
    try:
        # Get User In Group
        api_response = api_instance.groups_service_get_group_user(id, user_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling GroupsApi->groups_service_get_group_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Group ID |
 **user_id** | **int**| User ID |

### Return type

[**GroupUserModel**](GroupUserModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User group membership object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_service_get_group_users_lookup**
> GroupUsersLookupViewModel groups_service_get_group_users_lookup(id)

Get Group Users for display

Get Group Users for display by group id

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import groups_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.group_users_lookup_view_model import GroupUsersLookupViewModel
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
    api_instance = groups_api.GroupsApi(api_client)
    id = 1 # int | Group ID

    # example passing only required values which don't have defaults set
    try:
        # Get Group Users for display
        api_response = api_instance.groups_service_get_group_users_lookup(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling GroupsApi->groups_service_get_group_users_lookup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Group ID |

### Return type

[**GroupUsersLookupViewModel**](GroupUsersLookupViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GroupUsersLookupViewModel object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_service_get_roles**
> PagingOfRoleSummary groups_service_get_roles(id)

Gets roles for group

Gets roles for group

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import groups_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.paging_of_role_summary import PagingOfRoleSummary
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
    api_instance = groups_api.GroupsApi(api_client)
    id = 1 # int | id
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets roles for group
        api_response = api_instance.groups_service_get_roles(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling GroupsApi->groups_service_get_roles: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets roles for group
        api_response = api_instance.groups_service_get_roles(id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling GroupsApi->groups_service_get_roles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id |
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfRoleSummary**](PagingOfRoleSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success / Fail |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_service_lookup**
> PagingOfGroupLookup groups_service_lookup()

Lookup Groups

Search, filter, sort, and page groups, returning only group ID and name

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import groups_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.paging_of_group_lookup import PagingOfGroupLookup
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
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
    api_instance = groups_api.GroupsApi(api_client)
    filter_domain_id = 1 # int | Active Directory domain ID (optional)
    filter_exclude_inbox_rule_id_subscribers = 1 # int | Do not include any groups already subscribed this inbox notification rule (optional)
    filter_include_inactive = True # bool | Whether to include inactive groups in the results (optional)
    filter_limit_to_viewable_groups = True # bool | Limit groups to groups that current user can view details of (optional)
    filter_platform_only = True # bool | Limit groups to only Platform groups (optional)
    filter_search_text = "filter.searchText_example" # str | Search text (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Lookup Groups
        api_response = api_instance.groups_service_lookup(filter_domain_id=filter_domain_id, filter_exclude_inbox_rule_id_subscribers=filter_exclude_inbox_rule_id_subscribers, filter_include_inactive=filter_include_inactive, filter_limit_to_viewable_groups=filter_limit_to_viewable_groups, filter_platform_only=filter_platform_only, filter_search_text=filter_search_text, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling GroupsApi->groups_service_lookup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_domain_id** | **int**| Active Directory domain ID | [optional]
 **filter_exclude_inbox_rule_id_subscribers** | **int**| Do not include any groups already subscribed this inbox notification rule | [optional]
 **filter_include_inactive** | **bool**| Whether to include inactive groups in the results | [optional]
 **filter_limit_to_viewable_groups** | **bool**| Limit groups to groups that current user can view details of | [optional]
 **filter_platform_only** | **bool**| Limit groups to only Platform groups | [optional]
 **filter_search_text** | **str**| Search text | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfGroupLookup**](PagingOfGroupLookup.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_service_patch_group**
> GroupModel groups_service_patch_group(group_id)

Patch Group

Patch a single group by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import groups_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.group_patch_args import GroupPatchArgs
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.group_model import GroupModel
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
    api_instance = groups_api.GroupsApi(api_client)
    group_id = 1 # int | Group ID
    group_patch_args = GroupPatchArgs(
        data=GroupPatchModel(
            added_owner_group_ids=[
                1,
            ],
            enabled=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            ip_address_restriction_ids=UpdateFieldValueOfInt32Array(
                dirty=True,
                value=[
                    1,
                ],
            ),
            name=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            owner_group_ids=UpdateFieldValueOfInt32Array(
                dirty=True,
                value=[
                    1,
                ],
            ),
            removed_owner_group_ids=[
                1,
            ],
        ),
    ) # GroupPatchArgs | Group update options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Patch Group
        api_response = api_instance.groups_service_patch_group(group_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling GroupsApi->groups_service_patch_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Patch Group
        api_response = api_instance.groups_service_patch_group(group_id, group_patch_args=group_patch_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling GroupsApi->groups_service_patch_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Group ID |
 **group_patch_args** | [**GroupPatchArgs**](GroupPatchArgs.md)| Group update options | [optional]

### Return type

[**GroupModel**](GroupModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_service_patch_group_membership**
> GroupMembershipPatchResult groups_service_patch_group_membership(id)

Patch Group Membership

Update group memberships by sending a list of add and remove IDs

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import groups_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.group_membership_patch_model import GroupMembershipPatchModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.group_membership_patch_result import GroupMembershipPatchResult
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
    api_instance = groups_api.GroupsApi(api_client)
    id = 1 # int | Group ID
    group_membership_patch_model = GroupMembershipPatchModel(
        added_user_ids=[
            1,
        ],
        remove_user_ids=[
            1,
        ],
    ) # GroupMembershipPatchModel | Group update options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Patch Group Membership
        api_response = api_instance.groups_service_patch_group_membership(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling GroupsApi->groups_service_patch_group_membership: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Patch Group Membership
        api_response = api_instance.groups_service_patch_group_membership(id, group_membership_patch_model=group_membership_patch_model)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling GroupsApi->groups_service_patch_group_membership: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Group ID |
 **group_membership_patch_model** | [**GroupMembershipPatchModel**](GroupMembershipPatchModel.md)| Group update options | [optional]

### Return type

[**GroupMembershipPatchResult**](GroupMembershipPatchResult.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_service_remove_user_from_group**
> DeletedModel groups_service_remove_user_from_group(id, user_id)

Remove User From Group

Remove a user from a group

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import groups_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.deleted_model import DeletedModel
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
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
    api_instance = groups_api.GroupsApi(api_client)
    id = 1 # int | Group ID
    user_id = 1 # int | User ID

    # example passing only required values which don't have defaults set
    try:
        # Remove User From Group
        api_response = api_instance.groups_service_remove_user_from_group(id, user_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling GroupsApi->groups_service_remove_user_from_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Group ID |
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

# **groups_service_search**
> PagingOfGroupSummary groups_service_search()

Search Groups

Search, filter, sort, and page groups

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import groups_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.paging_of_group_summary import PagingOfGroupSummary
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
    api_instance = groups_api.GroupsApi(api_client)
    filter_domain_id = 1 # int | Active Directory domain ID (optional)
    filter_exclude_inbox_rule_id_subscribers = 1 # int | Do not include any groups already subscribed this inbox notification rule (optional)
    filter_include_inactive = True # bool | Whether to include inactive groups in the results (optional)
    filter_limit_to_viewable_groups = True # bool | Limit groups to groups that current user can view details of (optional)
    filter_platform_only = True # bool | Limit groups to only Platform groups (optional)
    filter_search_text = "filter.searchText_example" # str | Search text (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Groups
        api_response = api_instance.groups_service_search(filter_domain_id=filter_domain_id, filter_exclude_inbox_rule_id_subscribers=filter_exclude_inbox_rule_id_subscribers, filter_include_inactive=filter_include_inactive, filter_limit_to_viewable_groups=filter_limit_to_viewable_groups, filter_platform_only=filter_platform_only, filter_search_text=filter_search_text, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling GroupsApi->groups_service_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_domain_id** | **int**| Active Directory domain ID | [optional]
 **filter_exclude_inbox_rule_id_subscribers** | **int**| Do not include any groups already subscribed this inbox notification rule | [optional]
 **filter_include_inactive** | **bool**| Whether to include inactive groups in the results | [optional]
 **filter_limit_to_viewable_groups** | **bool**| Limit groups to groups that current user can view details of | [optional]
 **filter_platform_only** | **bool**| Limit groups to only Platform groups | [optional]
 **filter_search_text** | **str**| Search text | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfGroupSummary**](PagingOfGroupSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_service_stub**
> GroupModel groups_service_stub()

Get Group Stub

Return the default values for a new group

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import groups_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.group_model import GroupModel
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
    api_instance = groups_api.GroupsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Group Stub
        api_response = api_instance.groups_service_stub()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling GroupsApi->groups_service_stub: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GroupModel**](GroupModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_service_update**
> GroupModel groups_service_update(id)

Update Group

Update a single group by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import groups_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.group_update_args import GroupUpdateArgs
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.group_model import GroupModel
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
    api_instance = groups_api.GroupsApi(api_client)
    id = 1 # int | Group ID
    group_update_args = GroupUpdateArgs(
        ad_guid="ad_guid_example",
        domain_id=1,
        enabled=True,
        has_group_owners=True,
        id=1,
        is_platform=True,
        name="name_example",
        owner_group_ids=[
            1,
        ],
        owner_group_names=[
            "owner_group_names_example",
        ],
        owner_user_ids=[
            1,
        ],
        owner_user_names=[
            "owner_user_names_example",
        ],
        synchronized=True,
        synchronize_now=True,
    ) # GroupUpdateArgs | Group update options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Group
        api_response = api_instance.groups_service_update(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling GroupsApi->groups_service_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Group
        api_response = api_instance.groups_service_update(id, group_update_args=group_update_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling GroupsApi->groups_service_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Group ID |
 **group_update_args** | [**GroupUpdateArgs**](GroupUpdateArgs.md)| Group update options | [optional]

### Return type

[**GroupModel**](GroupModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_service_update_group_members**
> GroupMembershipAssignmentResponse groups_service_update_group_members(group_id)

Update all members of a group

Update all members of a group

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import groups_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.group_membership_assignment_response import GroupMembershipAssignmentResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.group_member_assignment_request import GroupMemberAssignmentRequest
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
    api_instance = groups_api.GroupsApi(api_client)
    group_id = 1 # int | groupId
    group_member_assignment_request = GroupMemberAssignmentRequest(
        user_ids=[
            1,
        ],
    ) # GroupMemberAssignmentRequest | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update all members of a group
        api_response = api_instance.groups_service_update_group_members(group_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling GroupsApi->groups_service_update_group_members: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update all members of a group
        api_response = api_instance.groups_service_update_group_members(group_id, group_member_assignment_request=group_member_assignment_request)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling GroupsApi->groups_service_update_group_members: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| groupId |
 **group_member_assignment_request** | [**GroupMemberAssignmentRequest**](GroupMemberAssignmentRequest.md)| args | [optional]

### Return type

[**GroupMembershipAssignmentResponse**](GroupMembershipAssignmentResponse.md)

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

# **groups_service_update_user_roles**
> RoleChangeStatusModel groups_service_update_user_roles(id)

Update all roles on group

Update all roles on group

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import groups_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.role_change_status_model import RoleChangeStatusModel
from secret_server_openapiclient.model.role_assignments import RoleAssignments
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
    api_instance = groups_api.GroupsApi(api_client)
    id = 1 # int | id
    role_assignments = RoleAssignments(
        role_ids=[
            1,
        ],
    ) # RoleAssignments | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update all roles on group
        api_response = api_instance.groups_service_update_user_roles(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling GroupsApi->groups_service_update_user_roles: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update all roles on group
        api_response = api_instance.groups_service_update_user_roles(id, role_assignments=role_assignments)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling GroupsApi->groups_service_update_user_roles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id |
 **role_assignments** | [**RoleAssignments**](RoleAssignments.md)| args | [optional]

### Return type

[**RoleChangeStatusModel**](RoleChangeStatusModel.md)

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

