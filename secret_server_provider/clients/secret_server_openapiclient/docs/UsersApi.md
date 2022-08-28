# secret_server_openapiclient.UsersApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_service_add_user_owner**](UsersApi.md#users_service_add_user_owner) | **POST** /v1/users/{id}/owners | Add User Owner
[**users_service_add_user_to_groups**](UsersApi.md#users_service_add_user_to_groups) | **POST** /v1/users/{id}/groups | Add groups to existing user
[**users_service_change_password**](UsersApi.md#users_service_change_password) | **POST** /v1/users/change-password | Change User Password
[**users_service_create_user**](UsersApi.md#users_service_create_user) | **POST** /v1/users | Create User
[**users_service_create_user_public_ssh_key**](UsersApi.md#users_service_create_user_public_ssh_key) | **POST** /v1/users/public-ssh-keys | Create a User Ssh Key
[**users_service_create_user_roles**](UsersApi.md#users_service_create_user_roles) | **POST** /v1/users/{id}/roles | Add roles to existing user
[**users_service_deactivate_user_public_ssh_key**](UsersApi.md#users_service_deactivate_user_public_ssh_key) | **PATCH** /v1/users/public-ssh-keys/{id} | Deactivate SSH Key
[**users_service_delete**](UsersApi.md#users_service_delete) | **DELETE** /v1/users/{id} | Delete User
[**users_service_delete_user_owner**](UsersApi.md#users_service_delete_user_owner) | **DELETE** /v1/users/{id}/owners/{ownerId} | Remove User Owner
[**users_service_delete_user_roles**](UsersApi.md#users_service_delete_user_roles) | **DELETE** /v1/users/{id}/roles | Remove roles from existing user
[**users_service_get**](UsersApi.md#users_service_get) | **GET** /v1/users/{id} | Get User
[**users_service_get_current_user**](UsersApi.md#users_service_get_current_user) | **GET** /v1/users/current | Current User
[**users_service_get_current_user_sessions**](UsersApi.md#users_service_get_current_user_sessions) | **GET** /v1/users/sessions | User Sessions
[**users_service_get_domains**](UsersApi.md#users_service_get_domains) | **GET** /v1/domains | Get Domains
[**users_service_get_preference**](UsersApi.md#users_service_get_preference) | **GET** /v1/users/preference | Get Preference
[**users_service_get_roles**](UsersApi.md#users_service_get_roles) | **GET** /v1/users/{id}/roles | Gets roles for user
[**users_service_get_site_audits**](UsersApi.md#users_service_get_site_audits) | **GET** /v1/users/{userId}/audit | User Audits
[**users_service_get_user_action_audits**](UsersApi.md#users_service_get_user_action_audits) | **GET** /v1/users/action/audit | User Audits by Action
[**users_service_get_user_groups**](UsersApi.md#users_service_get_user_groups) | **GET** /v1/users/{id}/groups | Get User Groups
[**users_service_get_user_owner**](UsersApi.md#users_service_get_user_owner) | **GET** /v1/users/{id}/owners/{ownerId} | Get User Owner
[**users_service_get_user_public_ssh_keys**](UsersApi.md#users_service_get_user_public_ssh_keys) | **GET** /v1/users/public-ssh-keys | Get User Public Ssh Keys
[**users_service_get_user_roles**](UsersApi.md#users_service_get_user_roles) | **GET** /v1/users/{userId}/roles-assigned | Get User Roles
[**users_service_get_user_teams**](UsersApi.md#users_service_get_user_teams) | **GET** /v1/users/{userId}/teams | User Teams
[**users_service_lock_out**](UsersApi.md#users_service_lock_out) | **POST** /v1/users/{userId}/lock-out | Lock Out
[**users_service_lookup**](UsersApi.md#users_service_lookup) | **GET** /v1/users/lookup | Lookup Users
[**users_service_patch_user**](UsersApi.md#users_service_patch_user) | **PATCH** /v1/users/{id} | Update included properties for user by Id
[**users_service_patch_user_owners**](UsersApi.md#users_service_patch_user_owners) | **PATCH** /v1/users/{id}/owners | Add and remove the owners on the user
[**users_service_remove_user_groups**](UsersApi.md#users_service_remove_user_groups) | **DELETE** /v1/users/{id}/groups | Remove groups from existing user
[**users_service_reset_two_factor**](UsersApi.md#users_service_reset_two_factor) | **POST** /v1/users/{userId}/reset-two-factor | Reset 2FA
[**users_service_reset_user_password**](UsersApi.md#users_service_reset_user_password) | **POST** /v1/users/{userId}/password-reset | Reset a user password as an admin
[**users_service_search_user_owners**](UsersApi.md#users_service_search_user_owners) | **GET** /v1/users/{id}/owners | Get User Owners
[**users_service_search_users**](UsersApi.md#users_service_search_users) | **GET** /v1/users | Search Users
[**users_service_set_user_double_lock_password**](UsersApi.md#users_service_set_user_double_lock_password) | **PUT** /v1/users/doublelock-password | Update Users Doublelock Password
[**users_service_stub**](UsersApi.md#users_service_stub) | **GET** /v1/users/stub | Get User Stub
[**users_service_terminate_current_user_sessions**](UsersApi.md#users_service_terminate_current_user_sessions) | **POST** /v1/users/sessions/terminate | Terminate Current User Sessions
[**users_service_update_preference**](UsersApi.md#users_service_update_preference) | **POST** /v1/users/preference | Update Preference
[**users_service_update_user**](UsersApi.md#users_service_update_user) | **PUT** /v1/users/{id} | Update User
[**users_service_update_user_groups**](UsersApi.md#users_service_update_user_groups) | **PUT** /v1/users/{id}/groups | Update all groups on user
[**users_service_update_user_roles**](UsersApi.md#users_service_update_user_roles) | **PUT** /v1/users/{id}/roles | Update all roles on user
[**users_service_user_personal_info_delete_command**](UsersApi.md#users_service_user_personal_info_delete_command) | **POST** /v1/users/delete-pii/{id} | Delete a user&#39;s personally identifiable info
[**users_service_verify_password**](UsersApi.md#users_service_verify_password) | **POST** /v1/users/verify-password | Verify the Current User Password


# **users_service_add_user_owner**
> UserOwnerModel users_service_add_user_owner(id)

Add User Owner

Add an owner to a single user

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.user_owner_create_args import UserOwnerCreateArgs
from secret_server_openapiclient.model.user_owner_model import UserOwnerModel
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
    api_instance = users_api.UsersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | User ID
    user_owner_create_args = UserOwnerCreateArgs(
        group_id=None,
        group_name=None,
        user_id=None,
        user_name=None,
    ) # UserOwnerCreateArgs | User owner add options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add User Owner
        api_response = api_instance.users_service_add_user_owner(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_add_user_owner: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add User Owner
        api_response = api_instance.users_service_add_user_owner(id, user_owner_create_args=user_owner_create_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_add_user_owner: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| User ID |
 **user_owner_create_args** | [**UserOwnerCreateArgs**](UserOwnerCreateArgs.md)| User owner add options | [optional]

### Return type

[**UserOwnerModel**](UserOwnerModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User owner object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_service_add_user_to_groups**
> GroupChangeStatusModel users_service_add_user_to_groups(id)

Add groups to existing user

Add groups to existing user

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.group_change_status_model import GroupChangeStatusModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.group_assignments import GroupAssignments
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
    api_instance = users_api.UsersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    group_assignments = GroupAssignments(
        group_ids=[
            None,
        ],
    ) # GroupAssignments | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add groups to existing user
        api_response = api_instance.users_service_add_user_to_groups(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_add_user_to_groups: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add groups to existing user
        api_response = api_instance.users_service_add_user_to_groups(id, group_assignments=group_assignments)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_add_user_to_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **group_assignments** | [**GroupAssignments**](GroupAssignments.md)| args | [optional]

### Return type

[**GroupChangeStatusModel**](GroupChangeStatusModel.md)

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

# **users_service_change_password**
> UserModel users_service_change_password()

Change User Password

Change a user's password

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.user_model import UserModel
from secret_server_openapiclient.model.user_change_password_args import UserChangePasswordArgs
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
    api_instance = users_api.UsersApi(api_client)
    user_change_password_args = UserChangePasswordArgs(
        current_password=None,
        new_password=None,
    ) # UserChangePasswordArgs | User password change options (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Change User Password
        api_response = api_instance.users_service_change_password(user_change_password_args=user_change_password_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_change_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_change_password_args** | [**UserChangePasswordArgs**](UserChangePasswordArgs.md)| User password change options | [optional]

### Return type

[**UserModel**](UserModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_service_create_user**
> UserModel users_service_create_user()

Create User

Create a new user

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.user_model import UserModel
from secret_server_openapiclient.model.user_create_args import UserCreateArgs
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
    api_instance = users_api.UsersApi(api_client)
    user_create_args = UserCreateArgs(
        ad_guid=None,
        display_name=None,
        domain_id=None,
        duo_two_factor=True,
        email_address=None,
        enabled=True,
        fido2_two_factor=True,
        is_application_account=True,
        oath_two_factor=True,
        password=None,
        radius_two_factor=True,
        radius_user_name=None,
        two_factor=True,
        unix_authentication_method=UnixAuthenticationMethodType("{}"),
        user_name=None,
    ) # UserCreateArgs | User creation options (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create User
        api_response = api_instance.users_service_create_user(user_create_args=user_create_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_create_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create_args** | [**UserCreateArgs**](UserCreateArgs.md)| User creation options | [optional]

### Return type

[**UserModel**](UserModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_service_create_user_public_ssh_key**
> bool, date, datetime, dict, float, int, list, str, none_type users_service_create_user_public_ssh_key()

Create a User Ssh Key

Create the public ssh keys for the current user

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.user_public_ssh_key_create_args import UserPublicSshKeyCreateArgs
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
    api_instance = users_api.UsersApi(api_client)
    user_public_ssh_key_create_args = UserPublicSshKeyCreateArgs(
        description=None,
        format=None,
        passphrase=None,
    ) # UserPublicSshKeyCreateArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a User Ssh Key
        api_response = api_instance.users_service_create_user_public_ssh_key(user_public_ssh_key_create_args=user_public_ssh_key_create_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_create_user_public_ssh_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_public_ssh_key_create_args** | [**UserPublicSshKeyCreateArgs**](UserPublicSshKeyCreateArgs.md)| args | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Private ssh key result |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_service_create_user_roles**
> RoleChangeStatusModel users_service_create_user_roles(id)

Add roles to existing user

Add roles to existing user

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    role_assignments = RoleAssignments(
        role_ids=[
            None,
        ],
    ) # RoleAssignments | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add roles to existing user
        api_response = api_instance.users_service_create_user_roles(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_create_user_roles: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add roles to existing user
        api_response = api_instance.users_service_create_user_roles(id, role_assignments=role_assignments)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_create_user_roles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
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

# **users_service_deactivate_user_public_ssh_key**
> bool, date, datetime, dict, float, int, list, str, none_type users_service_deactivate_user_public_ssh_key(id)

Deactivate SSH Key

Deactivate a User's Public SSH Key by specifying the key's ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
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
    api_instance = users_api.UsersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Public SSH Key ID

    # example passing only required values which don't have defaults set
    try:
        # Deactivate SSH Key
        api_response = api_instance.users_service_deactivate_user_public_ssh_key(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_deactivate_user_public_ssh_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Public SSH Key ID |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The ID if the key deactivated |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_service_delete**
> DeletedModel users_service_delete(id)

Delete User

Delete a user by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | User ID

    # example passing only required values which don't have defaults set
    try:
        # Delete User
        api_response = api_instance.users_service_delete(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| User ID |

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

# **users_service_delete_user_owner**
> DeletedModel users_service_delete_user_owner(id, owner_id)

Remove User Owner

Remove an owner from a single user

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | User ID
    owner_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Owner ID is the unique sequence for this specific owner.  This is returned as ID on UserOwnerModel

    # example passing only required values which don't have defaults set
    try:
        # Remove User Owner
        api_response = api_instance.users_service_delete_user_owner(id, owner_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_delete_user_owner: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| User ID |
 **owner_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Owner ID is the unique sequence for this specific owner.  This is returned as ID on UserOwnerModel |

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

# **users_service_delete_user_roles**
> RoleChangeStatusModel users_service_delete_user_roles(id)

Remove roles from existing user

Remove roles from existing user

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    role_removals = RoleRemovals(
        role_ids=[
            None,
        ],
    ) # RoleRemovals | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove roles from existing user
        api_response = api_instance.users_service_delete_user_roles(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_delete_user_roles: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove roles from existing user
        api_response = api_instance.users_service_delete_user_roles(id, role_removals=role_removals)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_delete_user_roles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
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

# **users_service_get**
> UserModel users_service_get(id)

Get User

Get a single user by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.user_model import UserModel
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
    api_instance = users_api.UsersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | User ID
    include_inactive = True # bool | Whether to include inactive users in the results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get User
        api_response = api_instance.users_service_get(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get User
        api_response = api_instance.users_service_get(id, include_inactive=include_inactive)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| User ID |
 **include_inactive** | **bool**| Whether to include inactive users in the results | [optional]

### Return type

[**UserModel**](UserModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_service_get_current_user**
> CurrentUserModel users_service_get_current_user()

Current User

Gets the current user

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.current_user_model import CurrentUserModel
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
    api_instance = users_api.UsersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Current User
        api_response = api_instance.users_service_get_current_user()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_get_current_user: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CurrentUserModel**](CurrentUserModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current user result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_service_get_current_user_sessions**
> PagingOfSessionSummaryModel users_service_get_current_user_sessions()

User Sessions

Get sessions for current user

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.paging_of_session_summary_model import PagingOfSessionSummaryModel
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
    api_instance = users_api.UsersApi(api_client)
    is_exporting = True # bool | isExporting (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # User Sessions
        api_response = api_instance.users_service_get_current_user_sessions(is_exporting=is_exporting, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_get_current_user_sessions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_exporting** | **bool**| isExporting | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfSessionSummaryModel**](PagingOfSessionSummaryModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paged List of Sessions |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_service_get_domains**
> PagingOfDomainSummary users_service_get_domains()

Get Domains

Get Domains

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.paging_of_domain_summary import PagingOfDomainSummary
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
    api_instance = users_api.UsersApi(api_client)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Domains
        api_response = api_instance.users_service_get_domains(skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_get_domains: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfDomainSummary**](PagingOfDomainSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Domain summary list |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_service_get_preference**
> PreferenceModel users_service_get_preference()

Get Preference

Get a Preference for the current user

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.preference_model import PreferenceModel
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
    api_instance = users_api.UsersApi(api_client)
    is_legacy = True # bool | Is Legacy (optional)
    setting_code = None # bool, date, datetime, dict, float, int, list, str, none_type | Setting Code (optional)
    setting_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Setting Name (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Preference
        api_response = api_instance.users_service_get_preference(is_legacy=is_legacy, setting_code=setting_code, setting_name=setting_name)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_get_preference: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_legacy** | **bool**| Is Legacy | [optional]
 **setting_code** | **bool, date, datetime, dict, float, int, list, str, none_type**| Setting Code | [optional]
 **setting_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Setting Name | [optional]

### Return type

[**PreferenceModel**](PreferenceModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Preference |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_service_get_roles**
> PagingOfRoleSummary users_service_get_roles(id)

Gets roles for user

Gets roles for user

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets roles for user
        api_response = api_instance.users_service_get_roles(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_get_roles: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets roles for user
        api_response = api_instance.users_service_get_roles(id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_get_roles: %s\n" % e)
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

# **users_service_get_site_audits**
> PagingOfUserAuditSummary users_service_get_site_audits(user_id)

User Audits

Get all of the audits for a user

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.paging_of_user_audit_summary import PagingOfUserAuditSummary
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
    api_instance = users_api.UsersApi(api_client)
    user_id = None # bool, date, datetime, dict, float, int, list, str, none_type | userId
    is_exporting = True # bool | isExporting (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # User Audits
        api_response = api_instance.users_service_get_site_audits(user_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_get_site_audits: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # User Audits
        api_response = api_instance.users_service_get_site_audits(user_id, is_exporting=is_exporting, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_get_site_audits: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| userId |
 **is_exporting** | **bool**| isExporting | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfUserAuditSummary**](PagingOfUserAuditSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paged List of Audits |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_service_get_user_action_audits**
> PagingOfUserAuditSummary users_service_get_user_action_audits()

User Audits by Action

Get all of the audits for users who performed the specified action

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.paging_of_user_audit_summary import PagingOfUserAuditSummary
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
    api_instance = users_api.UsersApi(api_client)
    actions = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | actions (optional)
    is_exporting = True # bool | isExporting (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # User Audits by Action
        api_response = api_instance.users_service_get_user_action_audits(actions=actions, is_exporting=is_exporting, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_get_user_action_audits: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actions** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| actions | [optional]
 **is_exporting** | **bool**| isExporting | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfUserAuditSummary**](PagingOfUserAuditSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paged List of Audits |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_service_get_user_groups**
> PagingOfGroupUserSummary users_service_get_user_groups(id)

Get User Groups

Get the groups for a user by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | User ID
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get User Groups
        api_response = api_instance.users_service_get_user_groups(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_get_user_groups: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get User Groups
        api_response = api_instance.users_service_get_user_groups(id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_get_user_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| User ID |
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

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

# **users_service_get_user_owner**
> UserOwnerModel users_service_get_user_owner(id, owner_id)

Get User Owner

Get a single owner for a user

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.user_owner_model import UserOwnerModel
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
    api_instance = users_api.UsersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | User ID
    owner_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Owner ID

    # example passing only required values which don't have defaults set
    try:
        # Get User Owner
        api_response = api_instance.users_service_get_user_owner(id, owner_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_get_user_owner: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| User ID |
 **owner_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Owner ID |

### Return type

[**UserOwnerModel**](UserOwnerModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User owner object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_service_get_user_public_ssh_keys**
> PagingOfUserPublicSshKeySummary users_service_get_user_public_ssh_keys()

Get User Public Ssh Keys

Get the public ssh keys for a user by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.paging_of_user_public_ssh_key_summary import PagingOfUserPublicSshKeySummary
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
    api_instance = users_api.UsersApi(api_client)
    filter_include_expired = True # bool | Whether to include expired user public ssh keys in the results (optional)
    filter_include_inactive = True # bool | Whether to include inactive user public ssh keys in the results (optional)
    filter_search_text = None # bool, date, datetime, dict, float, int, list, str, none_type | Search text (optional)
    filter_user_id = None # bool, date, datetime, dict, float, int, list, str, none_type | An optional ID for a specific user's public ssh keys (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get User Public Ssh Keys
        api_response = api_instance.users_service_get_user_public_ssh_keys(filter_include_expired=filter_include_expired, filter_include_inactive=filter_include_inactive, filter_search_text=filter_search_text, filter_user_id=filter_user_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_get_user_public_ssh_keys: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_include_expired** | **bool**| Whether to include expired user public ssh keys in the results | [optional]
 **filter_include_inactive** | **bool**| Whether to include inactive user public ssh keys in the results | [optional]
 **filter_search_text** | **bool, date, datetime, dict, float, int, list, str, none_type**| Search text | [optional]
 **filter_user_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| An optional ID for a specific user&#39;s public ssh keys | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfUserPublicSshKeySummary**](PagingOfUserPublicSshKeySummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Public ssh key results |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_service_get_user_roles**
> PagingOfUserRoleSummary users_service_get_user_roles(user_id)

Get User Roles

Get the roles for a user by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.paging_of_user_role_summary import PagingOfUserRoleSummary
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
    api_instance = users_api.UsersApi(api_client)
    user_id = None # bool, date, datetime, dict, float, int, list, str, none_type | User ID
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get User Roles
        api_response = api_instance.users_service_get_user_roles(user_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_get_user_roles: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get User Roles
        api_response = api_instance.users_service_get_user_roles(user_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_get_user_roles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| User ID |
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfUserRoleSummary**](PagingOfUserRoleSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User role summary |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_service_get_user_teams**
> PagingOfUserTeamSummary users_service_get_user_teams(user_id)

User Teams

Get all of the teams for a user

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.paging_of_user_team_summary import PagingOfUserTeamSummary
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
    api_instance = users_api.UsersApi(api_client)
    user_id = None # bool, date, datetime, dict, float, int, list, str, none_type | userId
    filter_include_group_memberships = True # bool | Include Group Memberships (optional)
    filter_include_inactive = True # bool | Include Inactive (optional)
    filter_search_term = None # bool, date, datetime, dict, float, int, list, str, none_type | Search Term (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # User Teams
        api_response = api_instance.users_service_get_user_teams(user_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_get_user_teams: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # User Teams
        api_response = api_instance.users_service_get_user_teams(user_id, filter_include_group_memberships=filter_include_group_memberships, filter_include_inactive=filter_include_inactive, filter_search_term=filter_search_term, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_get_user_teams: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| userId |
 **filter_include_group_memberships** | **bool**| Include Group Memberships | [optional]
 **filter_include_inactive** | **bool**| Include Inactive | [optional]
 **filter_search_term** | **bool, date, datetime, dict, float, int, list, str, none_type**| Search Term | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfUserTeamSummary**](PagingOfUserTeamSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paged List of Team Summaries |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_service_lock_out**
> LockOutResponseModel users_service_lock_out(user_id)

Lock Out

Lock Out a specific user.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.lock_out_response_model import LockOutResponseModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.lock_out_args import LockOutArgs
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
    api_instance = users_api.UsersApi(api_client)
    user_id = None # bool, date, datetime, dict, float, int, list, str, none_type | userId
    lock_out_args = LockOutArgs(
        data=LockOutRequestModel(
            description=None,
            reason_type=LockOutReasonType("SuspiciousActivity"),
        ),
    ) # LockOutArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Lock Out
        api_response = api_instance.users_service_lock_out(user_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_lock_out: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Lock Out
        api_response = api_instance.users_service_lock_out(user_id, lock_out_args=lock_out_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_lock_out: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| userId |
 **lock_out_args** | [**LockOutArgs**](LockOutArgs.md)| args | [optional]

### Return type

[**LockOutResponseModel**](LockOutResponseModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of Lock Out |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_service_lookup**
> PagingOfUserLookup users_service_lookup()

Lookup Users

Search, filter, sort, and page users, returning only user ID and name

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.paging_of_user_lookup import PagingOfUserLookup
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
    api_instance = users_api.UsersApi(api_client)
    filter_domain_id = None # bool, date, datetime, dict, float, int, list, str, none_type | If not null, filters users by Active Directory domain. (optional)
    filter_exclude_inbox_rule_id_subscribers = None # bool, date, datetime, dict, float, int, list, str, none_type | When set all subscribers not subscribed directly to this inbox notification rule will be excluded. (optional)
    filter_include_inactive = True # bool | Whether to include inactive users in the results. (optional)
    filter_search_fields = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | User fields to search. (optional)
    filter_search_text = None # bool, date, datetime, dict, float, int, list, str, none_type | The text to match in the username, display name, or email address. (optional)
    filter_user_ids = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | User Ids to search. (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Lookup Users
        api_response = api_instance.users_service_lookup(filter_domain_id=filter_domain_id, filter_exclude_inbox_rule_id_subscribers=filter_exclude_inbox_rule_id_subscribers, filter_include_inactive=filter_include_inactive, filter_search_fields=filter_search_fields, filter_search_text=filter_search_text, filter_user_ids=filter_user_ids, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_lookup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_domain_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| If not null, filters users by Active Directory domain. | [optional]
 **filter_exclude_inbox_rule_id_subscribers** | **bool, date, datetime, dict, float, int, list, str, none_type**| When set all subscribers not subscribed directly to this inbox notification rule will be excluded. | [optional]
 **filter_include_inactive** | **bool**| Whether to include inactive users in the results. | [optional]
 **filter_search_fields** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| User fields to search. | [optional]
 **filter_search_text** | **bool, date, datetime, dict, float, int, list, str, none_type**| The text to match in the username, display name, or email address. | [optional]
 **filter_user_ids** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| User Ids to search. | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfUserLookup**](PagingOfUserLookup.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_service_patch_user**
> UserModel users_service_patch_user(id)

Update included properties for user by Id

Update included properties for user by Id

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.user_model import UserModel
from secret_server_openapiclient.model.patch_user_model import PatchUserModel
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
    api_instance = users_api.UsersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    patch_user_model = PatchUserModel(
        date_option_id=UpdateFieldValueOfInt32(
            dirty=True,
            value=None,
        ),
        display_name=UpdateFieldValueOfString(
            dirty=True,
            value=None,
        ),
        duo_two_factor=UpdateFieldValueOfBoolean(
            dirty=True,
            value=True,
        ),
        email_address=UpdateFieldValueOfString(
            dirty=True,
            value=None,
        ),
        enabled=UpdateFieldValueOfBoolean(
            dirty=True,
            value=True,
        ),
        fido2_two_factor=UpdateFieldValueOfBoolean(
            dirty=True,
            value=True,
        ),
        group_owners=[
            None,
        ],
        id=None,
        ip_address_restriction_ids=UpdateFieldValueOfInt32Array(
            dirty=True,
            value=[
                None,
            ],
        ),
        is_application_account=UpdateFieldValueOfBoolean(
            dirty=True,
            value=True,
        ),
        is_group_owner_update=True,
        is_locked_out=UpdateFieldValueOfBoolean(
            dirty=True,
            value=True,
        ),
        login_failures=UpdateFieldValueOfInt32(
            dirty=True,
            value=None,
        ),
        oath_two_factor=UpdateFieldValueOfBoolean(
            dirty=True,
            value=True,
        ),
        password=UpdateFieldValueOfString(
            dirty=True,
            value=None,
        ),
        radius_two_factor=UpdateFieldValueOfBoolean(
            dirty=True,
            value=True,
        ),
        radius_user_name=UpdateFieldValueOfString(
            dirty=True,
            value=None,
        ),
        slack_id=UpdateFieldValueOfString(
            dirty=True,
            value=None,
        ),
        time_option_id=UpdateFieldValueOfInt32(
            dirty=True,
            value=None,
        ),
        two_factor=UpdateFieldValueOfBoolean(
            dirty=True,
            value=True,
        ),
        unix_authentication_method=UpdateFieldValueOfUnixAuthenticationMethodType(
            dirty=True,
            value=UnixAuthenticationMethodType("{}"),
        ),
    ) # PatchUserModel | patchModel (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update included properties for user by Id
        api_response = api_instance.users_service_patch_user(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_patch_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update included properties for user by Id
        api_response = api_instance.users_service_patch_user(id, patch_user_model=patch_user_model)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_patch_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **patch_user_model** | [**PatchUserModel**](PatchUserModel.md)| patchModel | [optional]

### Return type

[**UserModel**](UserModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_service_patch_user_owners**
> UserOwnerPatchResult users_service_patch_user_owners(id)

Add and remove the owners on the user

Add and remove the owners on the user

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.user_owner_patch_result import UserOwnerPatchResult
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.user_owner_patch_user_model import UserOwnerPatchUserModel
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
    api_instance = users_api.UsersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    user_owner_patch_user_model = UserOwnerPatchUserModel(
        added_group_ids=[
            None,
        ],
        remove_all_owners=True,
        remove_group_ids=[
            None,
        ],
    ) # UserOwnerPatchUserModel | patchModel (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add and remove the owners on the user
        api_response = api_instance.users_service_patch_user_owners(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_patch_user_owners: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add and remove the owners on the user
        api_response = api_instance.users_service_patch_user_owners(id, user_owner_patch_user_model=user_owner_patch_user_model)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_patch_user_owners: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **user_owner_patch_user_model** | [**UserOwnerPatchUserModel**](UserOwnerPatchUserModel.md)| patchModel | [optional]

### Return type

[**UserOwnerPatchResult**](UserOwnerPatchResult.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of all user owner objects for the user |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_service_remove_user_groups**
> GroupChangeStatusModel users_service_remove_user_groups(id)

Remove groups from existing user

Remove groups from existing user

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.group_change_status_model import GroupChangeStatusModel
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
    api_instance = users_api.UsersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    group_ids = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | groupIds (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove groups from existing user
        api_response = api_instance.users_service_remove_user_groups(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_remove_user_groups: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove groups from existing user
        api_response = api_instance.users_service_remove_user_groups(id, group_ids=group_ids)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_remove_user_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **group_ids** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| groupIds | [optional]

### Return type

[**GroupChangeStatusModel**](GroupChangeStatusModel.md)

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

# **users_service_reset_two_factor**
> ResetTwoFactorResponseModel users_service_reset_two_factor(user_id)

Reset 2FA

Reset 2FA for a specific user.  After the reset they will need to update their 2FA on next login

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.reset_two_factor_args import ResetTwoFactorArgs
from secret_server_openapiclient.model.reset_two_factor_response_model import ResetTwoFactorResponseModel
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
    api_instance = users_api.UsersApi(api_client)
    user_id = None # bool, date, datetime, dict, float, int, list, str, none_type | userId
    reset_two_factor_args = ResetTwoFactorArgs(
        data=ResetTwoFactorRequestModel(
            two_factor_type=TwoFactorResetType("Oath"),
        ),
    ) # ResetTwoFactorArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Reset 2FA
        api_response = api_instance.users_service_reset_two_factor(user_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_reset_two_factor: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Reset 2FA
        api_response = api_instance.users_service_reset_two_factor(user_id, reset_two_factor_args=reset_two_factor_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_reset_two_factor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| userId |
 **reset_two_factor_args** | [**ResetTwoFactorArgs**](ResetTwoFactorArgs.md)| args | [optional]

### Return type

[**ResetTwoFactorResponseModel**](ResetTwoFactorResponseModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of 2FA reset |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_service_reset_user_password**
> PasswordResetResultModel users_service_reset_user_password(user_id)

Reset a user password as an admin

The password reset command

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.password_reset_result_model import PasswordResetResultModel
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.password_reset_args import PasswordResetArgs
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
    api_instance = users_api.UsersApi(api_client)
    user_id = None # bool, date, datetime, dict, float, int, list, str, none_type | userId
    password_reset_args = PasswordResetArgs(
        data=PasswordResetRequestModel(
            password=None,
            user_id=None,
        ),
    ) # PasswordResetArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Reset a user password as an admin
        api_response = api_instance.users_service_reset_user_password(user_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_reset_user_password: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Reset a user password as an admin
        api_response = api_instance.users_service_reset_user_password(user_id, password_reset_args=password_reset_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_reset_user_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| userId |
 **password_reset_args** | [**PasswordResetArgs**](PasswordResetArgs.md)| args | [optional]

### Return type

[**PasswordResetResultModel**](PasswordResetResultModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Password Reset Result |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_service_search_user_owners**
> PagingOfUserOwnerSummary users_service_search_user_owners(id)

Get User Owners

Get the owners for a user by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.paging_of_user_owner_summary import PagingOfUserOwnerSummary
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
    api_instance = users_api.UsersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | User ID
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get User Owners
        api_response = api_instance.users_service_search_user_owners(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_search_user_owners: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get User Owners
        api_response = api_instance.users_service_search_user_owners(id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_search_user_owners: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| User ID |
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfUserOwnerSummary**](PagingOfUserOwnerSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User owner results |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_service_search_users**
> PagingOfUserSummary users_service_search_users()

Search Users

Search, filter, sort, and page users

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.paging_of_user_summary import PagingOfUserSummary
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
    api_instance = users_api.UsersApi(api_client)
    filter_domain_id = None # bool, date, datetime, dict, float, int, list, str, none_type | If not null, filters users by Active Directory domain. (optional)
    filter_exclude_inbox_rule_id_subscribers = None # bool, date, datetime, dict, float, int, list, str, none_type | When set all subscribers not subscribed directly to this inbox notification rule will be excluded. (optional)
    filter_include_inactive = True # bool | Whether to include inactive users in the results. (optional)
    filter_search_fields = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | User fields to search. (optional)
    filter_search_text = None # bool, date, datetime, dict, float, int, list, str, none_type | The text to match in the username, display name, or email address. (optional)
    filter_user_ids = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | User Ids to search. (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Users
        api_response = api_instance.users_service_search_users(filter_domain_id=filter_domain_id, filter_exclude_inbox_rule_id_subscribers=filter_exclude_inbox_rule_id_subscribers, filter_include_inactive=filter_include_inactive, filter_search_fields=filter_search_fields, filter_search_text=filter_search_text, filter_user_ids=filter_user_ids, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_search_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_domain_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| If not null, filters users by Active Directory domain. | [optional]
 **filter_exclude_inbox_rule_id_subscribers** | **bool, date, datetime, dict, float, int, list, str, none_type**| When set all subscribers not subscribed directly to this inbox notification rule will be excluded. | [optional]
 **filter_include_inactive** | **bool**| Whether to include inactive users in the results. | [optional]
 **filter_search_fields** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| User fields to search. | [optional]
 **filter_search_text** | **bool, date, datetime, dict, float, int, list, str, none_type**| The text to match in the username, display name, or email address. | [optional]
 **filter_user_ids** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| User Ids to search. | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfUserSummary**](PagingOfUserSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_service_set_user_double_lock_password**
> bool users_service_set_user_double_lock_password()

Update Users Doublelock Password

Update the doublelock password of a user

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.double_lock_set_user_password_args import DoubleLockSetUserPasswordArgs
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
    api_instance = users_api.UsersApi(api_client)
    double_lock_set_user_password_args = DoubleLockSetUserPasswordArgs(
        password=None,
    ) # DoubleLockSetUserPasswordArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Users Doublelock Password
        api_response = api_instance.users_service_set_user_double_lock_password(double_lock_set_user_password_args=double_lock_set_user_password_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_set_user_double_lock_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **double_lock_set_user_password_args** | [**DoubleLockSetUserPasswordArgs**](DoubleLockSetUserPasswordArgs.md)| args | [optional]

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
**200** | Result of the doublelock password change |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_service_stub**
> UserModel users_service_stub()

Get User Stub

Return the default values for a new user

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.user_model import UserModel
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
    api_instance = users_api.UsersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get User Stub
        api_response = api_instance.users_service_stub()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_stub: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**UserModel**](UserModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default User |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_service_terminate_current_user_sessions**
> SessionTerminateResponseModel users_service_terminate_current_user_sessions()

Terminate Current User Sessions

Terminate sessions of the current user

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.session_terminate_response_model import SessionTerminateResponseModel
from secret_server_openapiclient.model.session_terminate_args import SessionTerminateArgs
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
    api_instance = users_api.UsersApi(api_client)
    session_terminate_args = SessionTerminateArgs(
        data=SessionTerminateModel(
            user_session_ids=[
                None,
            ],
        ),
    ) # SessionTerminateArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Terminate Current User Sessions
        api_response = api_instance.users_service_terminate_current_user_sessions(session_terminate_args=session_terminate_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_terminate_current_user_sessions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_terminate_args** | [**SessionTerminateArgs**](SessionTerminateArgs.md)| args | [optional]

### Return type

[**SessionTerminateResponseModel**](SessionTerminateResponseModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of Session Termination |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_service_update_preference**
> PreferenceModel users_service_update_preference()

Update Preference

Update a Preference for the current user

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.rest_preference_update_args import RestPreferenceUpdateArgs
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.preference_model import PreferenceModel
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
    api_instance = users_api.UsersApi(api_client)
    rest_preference_update_args = RestPreferenceUpdateArgs(
        setting_code=None,
        setting_name=None,
        value={},
    ) # RestPreferenceUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Preference
        api_response = api_instance.users_service_update_preference(rest_preference_update_args=rest_preference_update_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_update_preference: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rest_preference_update_args** | [**RestPreferenceUpdateArgs**](RestPreferenceUpdateArgs.md)| args | [optional]

### Return type

[**PreferenceModel**](PreferenceModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Preference |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_service_update_user**
> UserModel users_service_update_user(id)

Update User

Update a single user by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.user_model import UserModel
from secret_server_openapiclient.model.user_update_args import UserUpdateArgs
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
    api_instance = users_api.UsersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | User ID
    user_update_args = UserUpdateArgs(
        date_option_id=None,
        display_name=None,
        duo_two_factor=True,
        email_address=None,
        enabled=True,
        fido2_two_factor=True,
        group_owners=[
            None,
        ],
        id=None,
        is_application_account=True,
        is_group_owner_update=True,
        is_locked_out=True,
        login_failures=None,
        oath_two_factor=True,
        password=None,
        radius_two_factor=True,
        radius_user_name=None,
        time_option_id=None,
        two_factor=True,
        unix_authentication_method=UnixAuthenticationMethodType("{}"),
    ) # UserUpdateArgs | User update options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update User
        api_response = api_instance.users_service_update_user(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_update_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update User
        api_response = api_instance.users_service_update_user(id, user_update_args=user_update_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_update_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| User ID |
 **user_update_args** | [**UserUpdateArgs**](UserUpdateArgs.md)| User update options | [optional]

### Return type

[**UserModel**](UserModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_service_update_user_groups**
> GroupChangeStatusModel users_service_update_user_groups(id)

Update all groups on user

Update all groups on user

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.group_change_status_model import GroupChangeStatusModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.group_assignments import GroupAssignments
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
    api_instance = users_api.UsersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    group_assignments = GroupAssignments(
        group_ids=[
            None,
        ],
    ) # GroupAssignments | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update all groups on user
        api_response = api_instance.users_service_update_user_groups(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_update_user_groups: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update all groups on user
        api_response = api_instance.users_service_update_user_groups(id, group_assignments=group_assignments)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_update_user_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **group_assignments** | [**GroupAssignments**](GroupAssignments.md)| args | [optional]

### Return type

[**GroupChangeStatusModel**](GroupChangeStatusModel.md)

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

# **users_service_update_user_roles**
> RoleChangeStatusModel users_service_update_user_roles(id)

Update all roles on user

Update all roles on user

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    role_assignments = RoleAssignments(
        role_ids=[
            None,
        ],
    ) # RoleAssignments | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update all roles on user
        api_response = api_instance.users_service_update_user_roles(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_update_user_roles: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update all roles on user
        api_response = api_instance.users_service_update_user_roles(id, role_assignments=role_assignments)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_update_user_roles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
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

# **users_service_user_personal_info_delete_command**
> bool users_service_user_personal_info_delete_command(id)

Delete a user's personally identifiable info

Delete a user's personally identifiable info

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
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
    api_instance = users_api.UsersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id

    # example passing only required values which don't have defaults set
    try:
        # Delete a user's personally identifiable info
        api_response = api_instance.users_service_user_personal_info_delete_command(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_user_personal_info_delete_command: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |

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
**200** | Success / Fail |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_service_verify_password**
> bool users_service_verify_password()

Verify the Current User Password

Verify the current user's password

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import users_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.user_password_verify_args import UserPasswordVerifyArgs
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
    api_instance = users_api.UsersApi(api_client)
    user_password_verify_args = UserPasswordVerifyArgs(
        password=None,
    ) # UserPasswordVerifyArgs | User password verification options (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Verify the Current User Password
        api_response = api_instance.users_service_verify_password(user_password_verify_args=user_password_verify_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling UsersApi->users_service_verify_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_password_verify_args** | [**UserPasswordVerifyArgs**](UserPasswordVerifyArgs.md)| User password verification options | [optional]

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
**200** | Success / Fail |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

