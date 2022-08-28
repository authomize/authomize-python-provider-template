# plugins.FolderPermissionsApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**folder_permissions_service_create**](FolderPermissionsApi.md#folder_permissions_service_create) | **POST** /v1/folder-permissions | Create Folder Permission
[**folder_permissions_service_delete**](FolderPermissionsApi.md#folder_permissions_service_delete) | **DELETE** /v1/folder-permissions/{id} | Delete Folder Permission
[**folder_permissions_service_get**](FolderPermissionsApi.md#folder_permissions_service_get) | **GET** /v1/folder-permissions/{id} | Get Folder Permission
[**folder_permissions_service_search**](FolderPermissionsApi.md#folder_permissions_service_search) | **GET** /v1/folder-permissions | Search Folder Permissions
[**folder_permissions_service_stub**](FolderPermissionsApi.md#folder_permissions_service_stub) | **GET** /v1/folder-permissions/stub | Get Folder Permission Stub
[**folder_permissions_service_update**](FolderPermissionsApi.md#folder_permissions_service_update) | **PUT** /v1/folder-permissions/{id} | Update Folder Permission


# **folder_permissions_service_create**
> FolderPermissionModel folder_permissions_service_create()

Create Folder Permission

Create a new folder permission

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import folder_permissions_api
from plugins.model.folder_permission_create_args import FolderPermissionCreateArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.folder_permission_model import FolderPermissionModel
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
    api_instance = folder_permissions_api.FolderPermissionsApi(api_client)
    folder_permission_create_args = FolderPermissionCreateArgs(
        break_inheritance=True,
        folder_access_role_name="folder_access_role_name_example",
        folder_id=1,
        group_id=1,
        secret_access_role_name="secret_access_role_name_example",
        user_id=1,
    ) # FolderPermissionCreateArgs | Folder permission creation options (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Folder Permission
        api_response = api_instance.folder_permissions_service_create(folder_permission_create_args=folder_permission_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling FolderPermissionsApi->folder_permissions_service_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_permission_create_args** | [**FolderPermissionCreateArgs**](FolderPermissionCreateArgs.md)| Folder permission creation options | [optional]

### Return type

[**FolderPermissionModel**](FolderPermissionModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folder permission object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folder_permissions_service_delete**
> DeletedModel folder_permissions_service_delete(id)

Delete Folder Permission

Delete a folder permission by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import folder_permissions_api
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
    api_instance = folder_permissions_api.FolderPermissionsApi(api_client)
    id = 1 # int | Folder permission ID
    break_inheritance = True # bool | Include to remove permission inheritance (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete Folder Permission
        api_response = api_instance.folder_permissions_service_delete(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling FolderPermissionsApi->folder_permissions_service_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Folder Permission
        api_response = api_instance.folder_permissions_service_delete(id, break_inheritance=break_inheritance)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling FolderPermissionsApi->folder_permissions_service_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Folder permission ID |
 **break_inheritance** | **bool**| Include to remove permission inheritance | [optional]

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

# **folder_permissions_service_get**
> FolderPermissionModel folder_permissions_service_get(id)

Get Folder Permission

Get a single folder permission by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import folder_permissions_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.folder_permission_model import FolderPermissionModel
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
    api_instance = folder_permissions_api.FolderPermissionsApi(api_client)
    id = 1 # int | Folder permission ID
    include_inactive = True # bool | Whether to include inactive folder permissions in the results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Folder Permission
        api_response = api_instance.folder_permissions_service_get(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling FolderPermissionsApi->folder_permissions_service_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Folder Permission
        api_response = api_instance.folder_permissions_service_get(id, include_inactive=include_inactive)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling FolderPermissionsApi->folder_permissions_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Folder permission ID |
 **include_inactive** | **bool**| Whether to include inactive folder permissions in the results | [optional]

### Return type

[**FolderPermissionModel**](FolderPermissionModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folder permission object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folder_permissions_service_search**
> PagingOfFolderPermissionSummary folder_permissions_service_search()

Search Folder Permissions

Search, filter, sort, and page folder permissions

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import folder_permissions_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_folder_permission_summary import PagingOfFolderPermissionSummary
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
    api_instance = folder_permissions_api.FolderPermissionsApi(api_client)
    filter_exclude_editors = True # bool | If populated with true, will filter editors from results. Will default to false (optional)
    filter_exclude_owners = True # bool | If populated with true, will filter owners from results. Will default to false (optional)
    filter_exclude_viewers = True # bool | If populated with true, will filter viewers from results. Will default to false (optional)
    filter_folder_id = 1 # int | Limit results to a certain folder (optional)
    filter_group_id = 1 # int | Limit results to a certain group (optional)
    filter_user_id = 1 # int | Limit results to a certain user (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Folder Permissions
        api_response = api_instance.folder_permissions_service_search(filter_exclude_editors=filter_exclude_editors, filter_exclude_owners=filter_exclude_owners, filter_exclude_viewers=filter_exclude_viewers, filter_folder_id=filter_folder_id, filter_group_id=filter_group_id, filter_user_id=filter_user_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling FolderPermissionsApi->folder_permissions_service_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_exclude_editors** | **bool**| If populated with true, will filter editors from results. Will default to false | [optional]
 **filter_exclude_owners** | **bool**| If populated with true, will filter owners from results. Will default to false | [optional]
 **filter_exclude_viewers** | **bool**| If populated with true, will filter viewers from results. Will default to false | [optional]
 **filter_folder_id** | **int**| Limit results to a certain folder | [optional]
 **filter_group_id** | **int**| Limit results to a certain group | [optional]
 **filter_user_id** | **int**| Limit results to a certain user | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfFolderPermissionSummary**](PagingOfFolderPermissionSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folder permission search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folder_permissions_service_stub**
> FolderPermissionModel folder_permissions_service_stub(folder_id)

Get Folder Permission Stub

Return the default values for a new folder permission

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import folder_permissions_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.folder_permission_model import FolderPermissionModel
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
    api_instance = folder_permissions_api.FolderPermissionsApi(api_client)
    folder_id = 1 # int | Folder for which to generate a permission stub

    # example passing only required values which don't have defaults set
    try:
        # Get Folder Permission Stub
        api_response = api_instance.folder_permissions_service_stub(folder_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling FolderPermissionsApi->folder_permissions_service_stub: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| Folder for which to generate a permission stub |

### Return type

[**FolderPermissionModel**](FolderPermissionModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folder permission object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folder_permissions_service_update**
> FolderPermissionModel folder_permissions_service_update(id)

Update Folder Permission

Update a single folder permission by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import folder_permissions_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.folder_permission_update_args import FolderPermissionUpdateArgs
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.folder_permission_model import FolderPermissionModel
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
    api_instance = folder_permissions_api.FolderPermissionsApi(api_client)
    id = 1 # int | Folder permission ID
    folder_permission_update_args = FolderPermissionUpdateArgs(
        break_inheritance=True,
        folder_access_role_name="folder_access_role_name_example",
        folder_id=1,
        id=1,
        secret_access_role_name="secret_access_role_name_example",
    ) # FolderPermissionUpdateArgs | Folder permission update options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Folder Permission
        api_response = api_instance.folder_permissions_service_update(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling FolderPermissionsApi->folder_permissions_service_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Folder Permission
        api_response = api_instance.folder_permissions_service_update(id, folder_permission_update_args=folder_permission_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling FolderPermissionsApi->folder_permissions_service_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Folder permission ID |
 **folder_permission_update_args** | [**FolderPermissionUpdateArgs**](FolderPermissionUpdateArgs.md)| Folder permission update options | [optional]

### Return type

[**FolderPermissionModel**](FolderPermissionModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folder permission object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

