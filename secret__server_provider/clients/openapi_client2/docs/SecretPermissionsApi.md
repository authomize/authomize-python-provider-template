# plugins.SecretPermissionsApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**secret_permissions_service_add_secret_permission**](SecretPermissionsApi.md#secret_permissions_service_add_secret_permission) | **POST** /v1/secret-permissions | Create Secret Permission
[**secret_permissions_service_delete**](SecretPermissionsApi.md#secret_permissions_service_delete) | **DELETE** /v1/secret-permissions/{id} | Delete Secret Permission
[**secret_permissions_service_get**](SecretPermissionsApi.md#secret_permissions_service_get) | **GET** /v1/secret-permissions/{id} | Get Secret Permission
[**secret_permissions_service_is_current_user_secret_owner**](SecretPermissionsApi.md#secret_permissions_service_is_current_user_secret_owner) | **POST** /v1/secret-permissions/is-current-user-secret-owner | Check Current User is Owner
[**secret_permissions_service_search_secret_permissions**](SecretPermissionsApi.md#secret_permissions_service_search_secret_permissions) | **GET** /v1/secret-permissions | Search Secret Permissions
[**secret_permissions_service_stub**](SecretPermissionsApi.md#secret_permissions_service_stub) | **GET** /v1/secret-permissions/stub | Get Secret Permission Stub
[**secret_permissions_service_update_secret_permission**](SecretPermissionsApi.md#secret_permissions_service_update_secret_permission) | **PUT** /v1/secret-permissions/{id} | Update Secret Permission
[**secret_permissions_service_update_secret_share**](SecretPermissionsApi.md#secret_permissions_service_update_secret_share) | **PATCH** /v1/secrets/{secretId}/share | Update Secret share inherit


# **secret_permissions_service_add_secret_permission**
> SecretPermissionModel secret_permissions_service_add_secret_permission()

Create Secret Permission

Create a new secret permission

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_permissions_api
from plugins.model.secret_permission_model import SecretPermissionModel
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_permission_create_args import SecretPermissionCreateArgs
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
    api_instance = secret_permissions_api.SecretPermissionsApi(api_client)
    secret_permission_create_args = SecretPermissionCreateArgs(
        domain_name="domain_name_example",
        group_id=1,
        group_name="group_name_example",
        secret_access_role_name="secret_access_role_name_example",
        secret_id=1,
        user_id=1,
        user_name="user_name_example",
    ) # SecretPermissionCreateArgs | Secret permission creation options (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Secret Permission
        api_response = api_instance.secret_permissions_service_add_secret_permission(secret_permission_create_args=secret_permission_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretPermissionsApi->secret_permissions_service_add_secret_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_permission_create_args** | [**SecretPermissionCreateArgs**](SecretPermissionCreateArgs.md)| Secret permission creation options | [optional]

### Return type

[**SecretPermissionModel**](SecretPermissionModel.md)

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

# **secret_permissions_service_delete**
> DeletedModel secret_permissions_service_delete(id)

Delete Secret Permission

Delete a secret permission by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_permissions_api
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
    api_instance = secret_permissions_api.SecretPermissionsApi(api_client)
    id = 1 # int | Secret permission ID

    # example passing only required values which don't have defaults set
    try:
        # Delete Secret Permission
        api_response = api_instance.secret_permissions_service_delete(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretPermissionsApi->secret_permissions_service_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Secret permission ID |

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

# **secret_permissions_service_get**
> SecretPermissionModel secret_permissions_service_get(id)

Get Secret Permission

Get a single secret permission by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_permissions_api
from plugins.model.secret_permission_model import SecretPermissionModel
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
    api_instance = secret_permissions_api.SecretPermissionsApi(api_client)
    id = 1 # int | Secret permission ID
    include_inactive = True # bool | Whether to include inactive permissions in the results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Secret Permission
        api_response = api_instance.secret_permissions_service_get(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretPermissionsApi->secret_permissions_service_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Secret Permission
        api_response = api_instance.secret_permissions_service_get(id, include_inactive=include_inactive)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretPermissionsApi->secret_permissions_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Secret permission ID |
 **include_inactive** | **bool**| Whether to include inactive permissions in the results | [optional]

### Return type

[**SecretPermissionModel**](SecretPermissionModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret permission object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_permissions_service_is_current_user_secret_owner**
> SecretPermissionsIsCurrentUserSecretOwnerResponseModel secret_permissions_service_is_current_user_secret_owner()

Check Current User is Owner

Check if the current user is a Secret Owner using the submitted Permissions.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_permissions_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.secret_permissions_is_current_user_secret_owner_response_model import SecretPermissionsIsCurrentUserSecretOwnerResponseModel
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_permissions_is_current_user_secret_owner_args import SecretPermissionsIsCurrentUserSecretOwnerArgs
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
    api_instance = secret_permissions_api.SecretPermissionsApi(api_client)
    secret_permissions_is_current_user_secret_owner_args = SecretPermissionsIsCurrentUserSecretOwnerArgs(
        data=SecretPermissionsIsCurrentUserSecretOwnerModel(
            group_secret_access_roles=[
                SecretPermissionsGroupSecretAccessRoleModel(
                    group_id=1,
                    secret_access_role_id=1,
                ),
            ],
        ),
    ) # SecretPermissionsIsCurrentUserSecretOwnerArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Check Current User is Owner
        api_response = api_instance.secret_permissions_service_is_current_user_secret_owner(secret_permissions_is_current_user_secret_owner_args=secret_permissions_is_current_user_secret_owner_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretPermissionsApi->secret_permissions_service_is_current_user_secret_owner: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_permissions_is_current_user_secret_owner_args** | [**SecretPermissionsIsCurrentUserSecretOwnerArgs**](SecretPermissionsIsCurrentUserSecretOwnerArgs.md)| args | [optional]

### Return type

[**SecretPermissionsIsCurrentUserSecretOwnerResponseModel**](SecretPermissionsIsCurrentUserSecretOwnerResponseModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SecretPermissionsCurrentUserIsOwnerModel object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_permissions_service_search_secret_permissions**
> PagingOfSecretPermissionSummary secret_permissions_service_search_secret_permissions()

Search Secret Permissions

Search, filter, sort, and page secret permissions

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_permissions_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_secret_permission_summary import PagingOfSecretPermissionSummary
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
    api_instance = secret_permissions_api.SecretPermissionsApi(api_client)
    filter_domain_name = "filter.domainName_example" # str | DomainName (optional)
    filter_group_id = 1 # int | Filter by group ID (optional)
    filter_group_name = "filter.groupName_example" # str | GroupName (optional)
    filter_secret_id = 1 # int | Filter by secret ID (optional)
    filter_user_id = 1 # int | Filter by user ID (optional)
    filter_user_name = "filter.userName_example" # str | UserName (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Secret Permissions
        api_response = api_instance.secret_permissions_service_search_secret_permissions(filter_domain_name=filter_domain_name, filter_group_id=filter_group_id, filter_group_name=filter_group_name, filter_secret_id=filter_secret_id, filter_user_id=filter_user_id, filter_user_name=filter_user_name, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretPermissionsApi->secret_permissions_service_search_secret_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_domain_name** | **str**| DomainName | [optional]
 **filter_group_id** | **int**| Filter by group ID | [optional]
 **filter_group_name** | **str**| GroupName | [optional]
 **filter_secret_id** | **int**| Filter by secret ID | [optional]
 **filter_user_id** | **int**| Filter by user ID | [optional]
 **filter_user_name** | **str**| UserName | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfSecretPermissionSummary**](PagingOfSecretPermissionSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret permissions search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_permissions_service_stub**
> SecretPermissionModel secret_permissions_service_stub(secret_id)

Get Secret Permission Stub

Return the default values for a new secret permission

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_permissions_api
from plugins.model.secret_permission_model import SecretPermissionModel
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
    api_instance = secret_permissions_api.SecretPermissionsApi(api_client)
    secret_id = 1 # int | Options for generating a secret permission stub

    # example passing only required values which don't have defaults set
    try:
        # Get Secret Permission Stub
        api_response = api_instance.secret_permissions_service_stub(secret_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretPermissionsApi->secret_permissions_service_stub: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_id** | **int**| Options for generating a secret permission stub |

### Return type

[**SecretPermissionModel**](SecretPermissionModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret permission object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_permissions_service_update_secret_permission**
> SecretPermissionModel secret_permissions_service_update_secret_permission(id)

Update Secret Permission

Update a single secret permission by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_permissions_api
from plugins.model.secret_permission_model import SecretPermissionModel
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_permission_update_args import SecretPermissionUpdateArgs
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
    api_instance = secret_permissions_api.SecretPermissionsApi(api_client)
    id = 1 # int | Secret permission ID
    secret_permission_update_args = SecretPermissionUpdateArgs(
        id=1,
        secret_access_role_name="secret_access_role_name_example",
        secret_id=1,
    ) # SecretPermissionUpdateArgs | Secret permission update options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Secret Permission
        api_response = api_instance.secret_permissions_service_update_secret_permission(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretPermissionsApi->secret_permissions_service_update_secret_permission: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Secret Permission
        api_response = api_instance.secret_permissions_service_update_secret_permission(id, secret_permission_update_args=secret_permission_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretPermissionsApi->secret_permissions_service_update_secret_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Secret permission ID |
 **secret_permission_update_args** | [**SecretPermissionUpdateArgs**](SecretPermissionUpdateArgs.md)| Secret permission update options | [optional]

### Return type

[**SecretPermissionModel**](SecretPermissionModel.md)

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

# **secret_permissions_service_update_secret_share**
> SecretShareModel secret_permissions_service_update_secret_share(secret_id)

Update Secret share inherit

Update a single secret for share inheritance

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_permissions_api
from plugins.model.secret_share_update_args import SecretShareUpdateArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.secret_share_model import SecretShareModel
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
    api_instance = secret_permissions_api.SecretPermissionsApi(api_client)
    secret_id = 1 # int | Secret ID
    secret_share_update_args = SecretShareUpdateArgs(
        data=SecretShareUpdateModel(
            inherit_permissions=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
        ),
    ) # SecretShareUpdateArgs | Secret share update options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Secret share inherit
        api_response = api_instance.secret_permissions_service_update_secret_share(secret_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretPermissionsApi->secret_permissions_service_update_secret_share: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Secret share inherit
        api_response = api_instance.secret_permissions_service_update_secret_share(secret_id, secret_share_update_args=secret_share_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretPermissionsApi->secret_permissions_service_update_secret_share: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_id** | **int**| Secret ID |
 **secret_share_update_args** | [**SecretShareUpdateArgs**](SecretShareUpdateArgs.md)| Secret share update options | [optional]

### Return type

[**SecretShareModel**](SecretShareModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret share inheritance result |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

