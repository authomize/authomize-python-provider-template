# secret_server_openapiclient.SecretTemplatePermissionsApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**secret_template_permissions_service_get_template_permission_roles**](SecretTemplatePermissionsApi.md#secret_template_permissions_service_get_template_permission_roles) | **GET** /v1/secret-template-permissions/roles | Get Secret Template Permission Roles
[**secret_template_permissions_service_search**](SecretTemplatePermissionsApi.md#secret_template_permissions_service_search) | **GET** /v1/secret-template-permissions | Search Secret Template Permissions
[**secret_template_permissions_service_search_template_permissions**](SecretTemplatePermissionsApi.md#secret_template_permissions_service_search_template_permissions) | **GET** /v1/secret-template-permissions/grouped | Get Secret Template Permissions
[**secret_template_permissions_service_update**](SecretTemplatePermissionsApi.md#secret_template_permissions_service_update) | **PUT** /v1/secret-template-permissions | Update Secret Templates Permissions
[**secret_template_permissions_service_update_template_permissions**](SecretTemplatePermissionsApi.md#secret_template_permissions_service_update_template_permissions) | **PUT** /v1/secret-template-permissions/{secretTypeId} | Update Secret Template Type Permissions


# **secret_template_permissions_service_get_template_permission_roles**
> [SecretTemplatePermissionRole] secret_template_permissions_service_get_template_permission_roles()

Get Secret Template Permission Roles

Get Secret Template Permission Roles

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_template_permissions_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.secret_template_permission_role import SecretTemplatePermissionRole
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
    api_instance = secret_template_permissions_api.SecretTemplatePermissionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Secret Template Permission Roles
        api_response = api_instance.secret_template_permissions_service_get_template_permission_roles()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretTemplatePermissionsApi->secret_template_permissions_service_get_template_permission_roles: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[SecretTemplatePermissionRole]**](SecretTemplatePermissionRole.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Template Permission Role |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_template_permissions_service_search**
> PagingOfSecretTemplateGroupSummary secret_template_permissions_service_search()

Search Secret Template Permissions

Search, filter, sort, and page secret template permissions

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_template_permissions_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.paging_of_secret_template_group_summary import PagingOfSecretTemplateGroupSummary
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
    api_instance = secret_template_permissions_api.SecretTemplatePermissionsApi(api_client)
    filter_group_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Group Id (optional)
    filter_search_text = None # bool, date, datetime, dict, float, int, list, str, none_type | Search text (optional)
    filter_secret_type_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret type (template) Id (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Secret Template Permissions
        api_response = api_instance.secret_template_permissions_service_search(filter_group_id=filter_group_id, filter_search_text=filter_search_text, filter_secret_type_id=filter_secret_type_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretTemplatePermissionsApi->secret_template_permissions_service_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_group_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Group Id | [optional]
 **filter_search_text** | **bool, date, datetime, dict, float, int, list, str, none_type**| Search text | [optional]
 **filter_secret_type_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret type (template) Id | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfSecretTemplateGroupSummary**](PagingOfSecretTemplateGroupSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret template permission search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_template_permissions_service_search_template_permissions**
> PagingOfSecretTemplateGroupedPermissionSummary secret_template_permissions_service_search_template_permissions()

Get Secret Template Permissions

Get Secret Template Permissions

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_template_permissions_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.paging_of_secret_template_grouped_permission_summary import PagingOfSecretTemplateGroupedPermissionSummary
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
    api_instance = secret_template_permissions_api.SecretTemplatePermissionsApi(api_client)
    filter_group_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Will only return permissions that apply to this group (optional)
    filter_template_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Will only return permissions that apply to this template (optional)
    filter_user_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Will only return permissions that apply to this user (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Secret Template Permissions
        api_response = api_instance.secret_template_permissions_service_search_template_permissions(filter_group_id=filter_group_id, filter_template_id=filter_template_id, filter_user_id=filter_user_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretTemplatePermissionsApi->secret_template_permissions_service_search_template_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_group_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Will only return permissions that apply to this group | [optional]
 **filter_template_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Will only return permissions that apply to this template | [optional]
 **filter_user_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Will only return permissions that apply to this user | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfSecretTemplateGroupedPermissionSummary**](PagingOfSecretTemplateGroupedPermissionSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Template Permissions |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_template_permissions_service_update**
> SecretTemplatePermissionModel secret_template_permissions_service_update()

Update Secret Templates Permissions

Change permissions

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_template_permissions_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.secret_template_permission_model import SecretTemplatePermissionModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.secret_template_permissions_update_args import SecretTemplatePermissionsUpdateArgs
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
    api_instance = secret_template_permissions_api.SecretTemplatePermissionsApi(api_client)
    secret_template_permissions_update_args = SecretTemplatePermissionsUpdateArgs(
        group_id=None,
        permissions=[
            PermissionModel(
                role_id=None,
                secret_type_id=None,
            ),
        ],
    ) # SecretTemplatePermissionsUpdateArgs | Secret permission creation options (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Secret Templates Permissions
        api_response = api_instance.secret_template_permissions_service_update(secret_template_permissions_update_args=secret_template_permissions_update_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretTemplatePermissionsApi->secret_template_permissions_service_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_template_permissions_update_args** | [**SecretTemplatePermissionsUpdateArgs**](SecretTemplatePermissionsUpdateArgs.md)| Secret permission creation options | [optional]

### Return type

[**SecretTemplatePermissionModel**](SecretTemplatePermissionModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret permission object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_template_permissions_service_update_template_permissions**
> SecretTemplateTypePermissionsUpdateResponse secret_template_permissions_service_update_template_permissions(secret_type_id)

Update Secret Template Type Permissions

Update all the permissions for a single Secret template

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_template_permissions_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.secret_template_type_permissions_update_response import SecretTemplateTypePermissionsUpdateResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.secret_template_type_permissions_update_args import SecretTemplateTypePermissionsUpdateArgs
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
    api_instance = secret_template_permissions_api.SecretTemplatePermissionsApi(api_client)
    secret_type_id = None # bool, date, datetime, dict, float, int, list, str, none_type | secretTypeId
    secret_template_type_permissions_update_args = SecretTemplateTypePermissionsUpdateArgs(
        data=SecretTemplateTypePermissionsUpdateModel(
            permissions=[
                SecretTemplateTypePermissionsUpdateGroup(
                    group_id=None,
                    role_id=None,
                ),
            ],
        ),
    ) # SecretTemplateTypePermissionsUpdateArgs | Secret permission update options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Secret Template Type Permissions
        api_response = api_instance.secret_template_permissions_service_update_template_permissions(secret_type_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretTemplatePermissionsApi->secret_template_permissions_service_update_template_permissions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Secret Template Type Permissions
        api_response = api_instance.secret_template_permissions_service_update_template_permissions(secret_type_id, secret_template_type_permissions_update_args=secret_template_type_permissions_update_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretTemplatePermissionsApi->secret_template_permissions_service_update_template_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_type_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| secretTypeId |
 **secret_template_type_permissions_update_args** | [**SecretTemplateTypePermissionsUpdateArgs**](SecretTemplateTypePermissionsUpdateArgs.md)| Secret permission update options | [optional]

### Return type

[**SecretTemplateTypePermissionsUpdateResponse**](SecretTemplateTypePermissionsUpdateResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update permissions status response |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

