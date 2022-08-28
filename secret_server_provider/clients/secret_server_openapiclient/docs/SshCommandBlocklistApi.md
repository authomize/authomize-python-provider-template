# secret_server_openapiclient.SshCommandBlocklistApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ssh_command_blocklist_service_create_ssh_command_blocklist**](SshCommandBlocklistApi.md#ssh_command_blocklist_service_create_ssh_command_blocklist) | **POST** /v1/ssh-command-blocklist | Add an SSH Command Blocklist
[**ssh_command_blocklist_service_get_ssh_command_blocklist**](SshCommandBlocklistApi.md#ssh_command_blocklist_service_get_ssh_command_blocklist) | **GET** /v1/ssh-command-blocklist/{id} | Get an SSH Command Blocklist
[**ssh_command_blocklist_service_get_ssh_command_blocklist_policies**](SshCommandBlocklistApi.md#ssh_command_blocklist_service_get_ssh_command_blocklist_policies) | **GET** /v1/ssh-command-blocklist/policies | Get a list of Secret Policies that use the given blocklist
[**ssh_command_blocklist_service_get_ssh_command_blocklist_stub**](SshCommandBlocklistApi.md#ssh_command_blocklist_service_get_ssh_command_blocklist_stub) | **GET** /v1/ssh-command-blocklist/stub | Stub an empty SSH Command Blocklist
[**ssh_command_blocklist_service_get_ssh_command_blocklists**](SshCommandBlocklistApi.md#ssh_command_blocklist_service_get_ssh_command_blocklists) | **GET** /v1/ssh-command-blocklist/list | Get a list of SSH Command Blocklist
[**ssh_command_blocklist_service_patch_ssh_command_blocklist**](SshCommandBlocklistApi.md#ssh_command_blocklist_service_patch_ssh_command_blocklist) | **PATCH** /v1/ssh-command-blocklist/{sshCommandBlocklistId} | Update an SSH Command Blocklist


# **ssh_command_blocklist_service_create_ssh_command_blocklist**
> SshCommandBlocklistModel ssh_command_blocklist_service_create_ssh_command_blocklist()

Add an SSH Command Blocklist

Add an SSH Command Blocklist

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import ssh_command_blocklist_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.ssh_command_blocklist_create_args import SshCommandBlocklistCreateArgs
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.ssh_command_blocklist_model import SshCommandBlocklistModel
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
    api_instance = ssh_command_blocklist_api.SshCommandBlocklistApi(api_client)
    ssh_command_blocklist_create_args = SshCommandBlocklistCreateArgs(
        data=SshCommandBlocklistCreateModel(
            active=True,
            description=None,
            name=None,
            ssh_command_blocklist_id=None,
            ssh_command_ids=[
                None,
            ],
        ),
    ) # SshCommandBlocklistCreateArgs | SSH Command Blocklist add options (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add an SSH Command Blocklist
        api_response = api_instance.ssh_command_blocklist_service_create_ssh_command_blocklist(ssh_command_blocklist_create_args=ssh_command_blocklist_create_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SshCommandBlocklistApi->ssh_command_blocklist_service_create_ssh_command_blocklist: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_command_blocklist_create_args** | [**SshCommandBlocklistCreateArgs**](SshCommandBlocklistCreateArgs.md)| SSH Command Blocklist add options | [optional]

### Return type

[**SshCommandBlocklistModel**](SshCommandBlocklistModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SSH Command Blocklist |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssh_command_blocklist_service_get_ssh_command_blocklist**
> SshCommandBlocklistModel ssh_command_blocklist_service_get_ssh_command_blocklist(id)

Get an SSH Command Blocklist

Returns the SSH Command Blocklist for the provided ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import ssh_command_blocklist_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.ssh_command_blocklist_model import SshCommandBlocklistModel
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
    api_instance = ssh_command_blocklist_api.SshCommandBlocklistApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | SSH Command Blocklist ID

    # example passing only required values which don't have defaults set
    try:
        # Get an SSH Command Blocklist
        api_response = api_instance.ssh_command_blocklist_service_get_ssh_command_blocklist(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SshCommandBlocklistApi->ssh_command_blocklist_service_get_ssh_command_blocklist: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| SSH Command Blocklist ID |

### Return type

[**SshCommandBlocklistModel**](SshCommandBlocklistModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The SSH Command Blocklist View |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssh_command_blocklist_service_get_ssh_command_blocklist_policies**
> PagingOfBlocklistSecretPolicySummaryModel ssh_command_blocklist_service_get_ssh_command_blocklist_policies()

Get a list of Secret Policies that use the given blocklist

Returns a list of Secret Policies that meet the paging/searching critera

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import ssh_command_blocklist_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.paging_of_blocklist_secret_policy_summary_model import PagingOfBlocklistSecretPolicySummaryModel
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
    api_instance = ssh_command_blocklist_api.SshCommandBlocklistApi(api_client)
    filter_ssh_command_blocklist_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Results will be associated to the provided blocklist id (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of Secret Policies that use the given blocklist
        api_response = api_instance.ssh_command_blocklist_service_get_ssh_command_blocklist_policies(filter_ssh_command_blocklist_id=filter_ssh_command_blocklist_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SshCommandBlocklistApi->ssh_command_blocklist_service_get_ssh_command_blocklist_policies: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_ssh_command_blocklist_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Results will be associated to the provided blocklist id | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfBlocklistSecretPolicySummaryModel**](PagingOfBlocklistSecretPolicySummaryModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of Secret Policies |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssh_command_blocklist_service_get_ssh_command_blocklist_stub**
> SshCommandBlocklistDto ssh_command_blocklist_service_get_ssh_command_blocklist_stub()

Stub an empty SSH Command Blocklist

Returns an empty SSH Command Blocklist to be filled out.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import ssh_command_blocklist_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.ssh_command_blocklist_dto import SshCommandBlocklistDto
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
    api_instance = ssh_command_blocklist_api.SshCommandBlocklistApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Stub an empty SSH Command Blocklist
        api_response = api_instance.ssh_command_blocklist_service_get_ssh_command_blocklist_stub()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SshCommandBlocklistApi->ssh_command_blocklist_service_get_ssh_command_blocklist_stub: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SshCommandBlocklistDto**](SshCommandBlocklistDto.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An empty SSH Command Blocklist |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssh_command_blocklist_service_get_ssh_command_blocklists**
> PagingOfSshCommandBlocklistSummaryModel ssh_command_blocklist_service_get_ssh_command_blocklists()

Get a list of SSH Command Blocklist

Returns a list of SSH Command Blocklists that meet the paging/searching critera

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import ssh_command_blocklist_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.paging_of_ssh_command_blocklist_summary_model import PagingOfSshCommandBlocklistSummaryModel
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
    api_instance = ssh_command_blocklist_api.SshCommandBlocklistApi(api_client)
    filter_include_active = True # bool | IncludeActive (optional)
    filter_include_inactive = True # bool | IncludeInactive (optional)
    filter_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Name (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of SSH Command Blocklist
        api_response = api_instance.ssh_command_blocklist_service_get_ssh_command_blocklists(filter_include_active=filter_include_active, filter_include_inactive=filter_include_inactive, filter_name=filter_name, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SshCommandBlocklistApi->ssh_command_blocklist_service_get_ssh_command_blocklists: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_include_active** | **bool**| IncludeActive | [optional]
 **filter_include_inactive** | **bool**| IncludeInactive | [optional]
 **filter_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Name | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfSshCommandBlocklistSummaryModel**](PagingOfSshCommandBlocklistSummaryModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of SSH Command Blocklists |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssh_command_blocklist_service_patch_ssh_command_blocklist**
> SshCommandBlocklistModel ssh_command_blocklist_service_patch_ssh_command_blocklist(ssh_command_blocklist_id)

Update an SSH Command Blocklist

Update an SSH Command Blocklist

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import ssh_command_blocklist_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.ssh_command_blocklist_patch_args import SshCommandBlocklistPatchArgs
from secret_server_openapiclient.model.ssh_command_blocklist_model import SshCommandBlocklistModel
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
    api_instance = ssh_command_blocklist_api.SshCommandBlocklistApi(api_client)
    ssh_command_blocklist_id = None # bool, date, datetime, dict, float, int, list, str, none_type | sshCommandBlocklistId
    ssh_command_blocklist_patch_args = SshCommandBlocklistPatchArgs(
        data=SshCommandBlocklistPatchModel(
            active=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            description=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            name=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            ssh_command_blocklist_id=None,
            ssh_command_ids=UpdateFieldValueOfGuidArray(
                dirty=True,
                value=[
                    None,
                ],
            ),
        ),
    ) # SshCommandBlocklistPatchArgs | SSH Command Blocklist Update Options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an SSH Command Blocklist
        api_response = api_instance.ssh_command_blocklist_service_patch_ssh_command_blocklist(ssh_command_blocklist_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SshCommandBlocklistApi->ssh_command_blocklist_service_patch_ssh_command_blocklist: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an SSH Command Blocklist
        api_response = api_instance.ssh_command_blocklist_service_patch_ssh_command_blocklist(ssh_command_blocklist_id, ssh_command_blocklist_patch_args=ssh_command_blocklist_patch_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SshCommandBlocklistApi->ssh_command_blocklist_service_patch_ssh_command_blocklist: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_command_blocklist_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| sshCommandBlocklistId |
 **ssh_command_blocklist_patch_args** | [**SshCommandBlocklistPatchArgs**](SshCommandBlocklistPatchArgs.md)| SSH Command Blocklist Update Options | [optional]

### Return type

[**SshCommandBlocklistModel**](SshCommandBlocklistModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SSH Command Blocklist |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

