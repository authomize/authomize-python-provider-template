# secret_server_openapiclient.SshCommandApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ssh_command_service_create_ssh_command**](SshCommandApi.md#ssh_command_service_create_ssh_command) | **POST** /v1/ssh-command | Add an SSH Command
[**ssh_command_service_get_ssh_command**](SshCommandApi.md#ssh_command_service_get_ssh_command) | **GET** /v1/ssh-command/{id} | Get an SSH Command
[**ssh_command_service_get_ssh_command_stub**](SshCommandApi.md#ssh_command_service_get_ssh_command_stub) | **GET** /v1/ssh-command/stub | Stub an empty SSH Command
[**ssh_command_service_get_ssh_commands**](SshCommandApi.md#ssh_command_service_get_ssh_commands) | **GET** /v1/ssh-command/list | Get a list of SSH Commands
[**ssh_command_service_update_ssh_command**](SshCommandApi.md#ssh_command_service_update_ssh_command) | **PATCH** /v1/ssh-command/{sshCommandId} | Update an SSH Command


# **ssh_command_service_create_ssh_command**
> SshCommandModel ssh_command_service_create_ssh_command()

Add an SSH Command

Add an SSH Command

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import ssh_command_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.ssh_command_create_args import SshCommandCreateArgs
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.ssh_command_model import SshCommandModel
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
    api_instance = ssh_command_api.SshCommandApi(api_client)
    ssh_command_create_args = SshCommandCreateArgs(
        data=SshCommandCreateModel(
            command=None,
            command_permission_type=CommandPermissionType("{}"),
            name=None,
            ssh_command_guid=None,
        ),
    ) # SshCommandCreateArgs | SSH Command add options (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add an SSH Command
        api_response = api_instance.ssh_command_service_create_ssh_command(ssh_command_create_args=ssh_command_create_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SshCommandApi->ssh_command_service_create_ssh_command: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_command_create_args** | [**SshCommandCreateArgs**](SshCommandCreateArgs.md)| SSH Command add options | [optional]

### Return type

[**SshCommandModel**](SshCommandModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SSH Command |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssh_command_service_get_ssh_command**
> SshCommandModel ssh_command_service_get_ssh_command(id)

Get an SSH Command

Returns the SSH Command for the provided ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import ssh_command_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.ssh_command_model import SshCommandModel
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
    api_instance = ssh_command_api.SshCommandApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | SSH Command ID

    # example passing only required values which don't have defaults set
    try:
        # Get an SSH Command
        api_response = api_instance.ssh_command_service_get_ssh_command(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SshCommandApi->ssh_command_service_get_ssh_command: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| SSH Command ID |

### Return type

[**SshCommandModel**](SshCommandModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The SSH Command View |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssh_command_service_get_ssh_command_stub**
> SshCommandDto ssh_command_service_get_ssh_command_stub()

Stub an empty SSH Command

Returns an empty SSH Command to be filled out.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import ssh_command_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.ssh_command_dto import SshCommandDto
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
    api_instance = ssh_command_api.SshCommandApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Stub an empty SSH Command
        api_response = api_instance.ssh_command_service_get_ssh_command_stub()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SshCommandApi->ssh_command_service_get_ssh_command_stub: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SshCommandDto**](SshCommandDto.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An empty SSH Command |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssh_command_service_get_ssh_commands**
> PagingOfSshCommandSummaryModel ssh_command_service_get_ssh_commands()

Get a list of SSH Commands

Returns a list of SSH Commands that meet the paging/searching critera

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import ssh_command_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.paging_of_ssh_command_summary_model import PagingOfSshCommandSummaryModel
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
    api_instance = ssh_command_api.SshCommandApi(api_client)
    filter_command_permission_type = None # bool, date, datetime, dict, float, int, list, str, none_type | CommandPermissionType (optional)
    filter_name_or_command = None # bool, date, datetime, dict, float, int, list, str, none_type | NameOrCommand (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of SSH Commands
        api_response = api_instance.ssh_command_service_get_ssh_commands(filter_command_permission_type=filter_command_permission_type, filter_name_or_command=filter_name_or_command, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SshCommandApi->ssh_command_service_get_ssh_commands: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_command_permission_type** | **bool, date, datetime, dict, float, int, list, str, none_type**| CommandPermissionType | [optional]
 **filter_name_or_command** | **bool, date, datetime, dict, float, int, list, str, none_type**| NameOrCommand | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfSshCommandSummaryModel**](PagingOfSshCommandSummaryModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of SSH Commands |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssh_command_service_update_ssh_command**
> SshCommandModel ssh_command_service_update_ssh_command(ssh_command_id)

Update an SSH Command

Update an SSH Command

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import ssh_command_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.ssh_command_patch_args import SshCommandPatchArgs
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.ssh_command_model import SshCommandModel
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
    api_instance = ssh_command_api.SshCommandApi(api_client)
    ssh_command_id = None # bool, date, datetime, dict, float, int, list, str, none_type | sshCommandId
    ssh_command_patch_args = SshCommandPatchArgs(
        data=SshCommandPatchModel(
            command=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            name=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            sort_order=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            ssh_command_guid=None,
            ssh_command_id=None,
        ),
    ) # SshCommandPatchArgs | SSH Command Update Options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an SSH Command
        api_response = api_instance.ssh_command_service_update_ssh_command(ssh_command_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SshCommandApi->ssh_command_service_update_ssh_command: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an SSH Command
        api_response = api_instance.ssh_command_service_update_ssh_command(ssh_command_id, ssh_command_patch_args=ssh_command_patch_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SshCommandApi->ssh_command_service_update_ssh_command: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_command_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| sshCommandId |
 **ssh_command_patch_args** | [**SshCommandPatchArgs**](SshCommandPatchArgs.md)| SSH Command Update Options | [optional]

### Return type

[**SshCommandModel**](SshCommandModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SSH Command |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

