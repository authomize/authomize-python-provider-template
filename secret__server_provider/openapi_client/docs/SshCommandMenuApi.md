# plugins.SshCommandMenuApi

All URIs are relative to *https://integrations.secretservercloud.com//api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ssh_command_menu_service_add_ssh_command_menu**](SshCommandMenuApi.md#ssh_command_menu_service_add_ssh_command_menu) | **POST** /v1/ssh-command-menu | Add an SSH Command Menu
[**ssh_command_menu_service_get_ssh_command_menu**](SshCommandMenuApi.md#ssh_command_menu_service_get_ssh_command_menu) | **GET** /v1/ssh-command-menu/{sshCommandMenuId} | Get SSH Command Menu
[**ssh_command_menu_service_get_ssh_command_state**](SshCommandMenuApi.md#ssh_command_menu_service_get_ssh_command_state) | **GET** /v1/ssh-command-menu/state | Get user actions for SSH Commands
[**ssh_command_menu_service_patch_ssh_command_menu**](SshCommandMenuApi.md#ssh_command_menu_service_patch_ssh_command_menu) | **PATCH** /v1/ssh-command-menu/{sshCommandMenuId} | Update an SSH Command Menu
[**ssh_command_menu_service_search_audits**](SshCommandMenuApi.md#ssh_command_menu_service_search_audits) | **GET** /v1/ssh-command-menu/audit/search | Search Menu Audits
[**ssh_command_menu_service_search_item_audits**](SshCommandMenuApi.md#ssh_command_menu_service_search_item_audits) | **GET** /v1/ssh-command-item/audit/search | Search SSH Command, Blocklist, and Menu Audits for audit item
[**ssh_command_menu_service_search_ssh_command_menu**](SshCommandMenuApi.md#ssh_command_menu_service_search_ssh_command_menu) | **GET** /v1/ssh-command-menu/search | Search SSH Commands


# **ssh_command_menu_service_add_ssh_command_menu**
> SshCommandMenuModel ssh_command_menu_service_add_ssh_command_menu()

Add an SSH Command Menu

Create a new SSH Command Menu item

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import ssh_command_menu_api
from plugins.model.ssh_command_menu_model import SshCommandMenuModel
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.ssh_command_menu_create_args import SshCommandMenuCreateArgs
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com//api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
    host = "https://integrations.secretservercloud.com//api"
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
    api_instance = ssh_command_menu_api.SshCommandMenuApi(api_client)
    ssh_command_menu_create_args = SshCommandMenuCreateArgs(
        data=SshCommandMenuCreateModel(
            active=True,
            description=None,
            name=None,
            ssh_commands=None,
        ),
    ) # SshCommandMenuCreateArgs | SSH Command create options (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add an SSH Command Menu
        api_response = api_instance.ssh_command_menu_service_add_ssh_command_menu(ssh_command_menu_create_args=ssh_command_menu_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SshCommandMenuApi->ssh_command_menu_service_add_ssh_command_menu: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_command_menu_create_args** | [**SshCommandMenuCreateArgs**](SshCommandMenuCreateArgs.md)| SSH Command create options | [optional]

### Return type

[**SshCommandMenuModel**](SshCommandMenuModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SSH Command Menu |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssh_command_menu_service_get_ssh_command_menu**
> SshCommandMenuModel ssh_command_menu_service_get_ssh_command_menu(ssh_command_menu_id)

Get SSH Command Menu

Return details for a specific SSH Command Menu item

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import ssh_command_menu_api
from plugins.model.ssh_command_menu_model import SshCommandMenuModel
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com//api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
    host = "https://integrations.secretservercloud.com//api"
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
    api_instance = ssh_command_menu_api.SshCommandMenuApi(api_client)
    ssh_command_menu_id = None # bool, date, datetime, dict, float, int, list, str, none_type | sshCommandMenuId

    # example passing only required values which don't have defaults set
    try:
        # Get SSH Command Menu
        api_response = api_instance.ssh_command_menu_service_get_ssh_command_menu(ssh_command_menu_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SshCommandMenuApi->ssh_command_menu_service_get_ssh_command_menu: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_command_menu_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| sshCommandMenuId |

### Return type

[**SshCommandMenuModel**](SshCommandMenuModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SSH Command Menu |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssh_command_menu_service_get_ssh_command_state**
> SshCommandMenuStateModel ssh_command_menu_service_get_ssh_command_state()

Get user actions for SSH Commands

Available user actions for commands

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import ssh_command_menu_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.ssh_command_menu_state_model import SshCommandMenuStateModel
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com//api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
    host = "https://integrations.secretservercloud.com//api"
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
    api_instance = ssh_command_menu_api.SshCommandMenuApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get user actions for SSH Commands
        api_response = api_instance.ssh_command_menu_service_get_ssh_command_state()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SshCommandMenuApi->ssh_command_menu_service_get_ssh_command_state: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SshCommandMenuStateModel**](SshCommandMenuStateModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of actions |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssh_command_menu_service_patch_ssh_command_menu**
> SshCommandMenuModel ssh_command_menu_service_patch_ssh_command_menu(ssh_command_menu_id)

Update an SSH Command Menu

Update an SSH Command Menu

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import ssh_command_menu_api
from plugins.model.ssh_command_menu_patch_args import SshCommandMenuPatchArgs
from plugins.model.ssh_command_menu_model import SshCommandMenuModel
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com//api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
    host = "https://integrations.secretservercloud.com//api"
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
    api_instance = ssh_command_menu_api.SshCommandMenuApi(api_client)
    ssh_command_menu_id = None # bool, date, datetime, dict, float, int, list, str, none_type | sshCommandMenuId
    ssh_command_menu_patch_args = SshCommandMenuPatchArgs(
        data=SshCommandMenuPatchModel(
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
            ssh_command_menu_guid=None,
            ssh_command_menu_id=None,
            ssh_commands=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
        ),
    ) # SshCommandMenuPatchArgs | SSH Command Menu Update Options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an SSH Command Menu
        api_response = api_instance.ssh_command_menu_service_patch_ssh_command_menu(ssh_command_menu_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SshCommandMenuApi->ssh_command_menu_service_patch_ssh_command_menu: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an SSH Command Menu
        api_response = api_instance.ssh_command_menu_service_patch_ssh_command_menu(ssh_command_menu_id, ssh_command_menu_patch_args=ssh_command_menu_patch_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SshCommandMenuApi->ssh_command_menu_service_patch_ssh_command_menu: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_command_menu_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| sshCommandMenuId |
 **ssh_command_menu_patch_args** | [**SshCommandMenuPatchArgs**](SshCommandMenuPatchArgs.md)| SSH Command Menu Update Options | [optional]

### Return type

[**SshCommandMenuModel**](SshCommandMenuModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SSH Command Menu |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssh_command_menu_service_search_audits**
> PagingOfSshCommandMenuAuditSummaryModel ssh_command_menu_service_search_audits()

Search Menu Audits

Search, filter, sort, and page audits

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import ssh_command_menu_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_ssh_command_menu_audit_summary_model import PagingOfSshCommandMenuAuditSummaryModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com//api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
    host = "https://integrations.secretservercloud.com//api"
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
    api_instance = ssh_command_menu_api.SshCommandMenuApi(api_client)
    is_exporting = True # bool | isExporting (optional)
    filter_ssh_command_menu_name = None # bool, date, datetime, dict, float, int, list, str, none_type | SshCommandMenuName (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Menu Audits
        api_response = api_instance.ssh_command_menu_service_search_audits(is_exporting=is_exporting, filter_ssh_command_menu_name=filter_ssh_command_menu_name, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SshCommandMenuApi->ssh_command_menu_service_search_audits: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_exporting** | **bool**| isExporting | [optional]
 **filter_ssh_command_menu_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| SshCommandMenuName | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfSshCommandMenuAuditSummaryModel**](PagingOfSshCommandMenuAuditSummaryModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Menu audit search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssh_command_menu_service_search_item_audits**
> PagingOfSshCommandItemAuditSummaryModel ssh_command_menu_service_search_item_audits()

Search SSH Command, Blocklist, and Menu Audits for audit item

Search, filter, sort, and page audits for audit item

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import ssh_command_menu_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.paging_of_ssh_command_item_audit_summary_model import PagingOfSshCommandItemAuditSummaryModel
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com//api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
    host = "https://integrations.secretservercloud.com//api"
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
    api_instance = ssh_command_menu_api.SshCommandMenuApi(api_client)
    is_exporting = True # bool | isExporting (optional)
    filter_ssh_command_item_name_or_notes = None # bool, date, datetime, dict, float, int, list, str, none_type | SshCommandItemNameOrNotes (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search SSH Command, Blocklist, and Menu Audits for audit item
        api_response = api_instance.ssh_command_menu_service_search_item_audits(is_exporting=is_exporting, filter_ssh_command_item_name_or_notes=filter_ssh_command_item_name_or_notes, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SshCommandMenuApi->ssh_command_menu_service_search_item_audits: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_exporting** | **bool**| isExporting | [optional]
 **filter_ssh_command_item_name_or_notes** | **bool, date, datetime, dict, float, int, list, str, none_type**| SshCommandItemNameOrNotes | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfSshCommandItemAuditSummaryModel**](PagingOfSshCommandItemAuditSummaryModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SSH Command, Blocklist, and Menu search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssh_command_menu_service_search_ssh_command_menu**
> PagingOfSshCommandMenuSummaryModel ssh_command_menu_service_search_ssh_command_menu()

Search SSH Commands

Search, filter, sort, and page SSH Commands

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import ssh_command_menu_api
from plugins.model.paging_of_ssh_command_menu_summary_model import PagingOfSshCommandMenuSummaryModel
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com//api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
    host = "https://integrations.secretservercloud.com//api"
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
    api_instance = ssh_command_menu_api.SshCommandMenuApi(api_client)
    filter_include_disabled = True # bool | IncludeDisabled (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search SSH Commands
        api_response = api_instance.ssh_command_menu_service_search_ssh_command_menu(filter_include_disabled=filter_include_disabled, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SshCommandMenuApi->ssh_command_menu_service_search_ssh_command_menu: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_include_disabled** | **bool**| IncludeDisabled | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfSshCommandMenuSummaryModel**](PagingOfSshCommandMenuSummaryModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SSH Command Menu search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

