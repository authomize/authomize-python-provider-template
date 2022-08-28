# secret_server_openapiclient.SecretDependenciesApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**secret_dependencies_service_create_dependency**](SecretDependenciesApi.md#secret_dependencies_service_create_dependency) | **POST** /v1/secret-dependencies | Create Secret Dependency
[**secret_dependencies_service_create_dependency_group**](SecretDependenciesApi.md#secret_dependencies_service_create_dependency_group) | **POST** /v1/secret-dependencies/groups/{secretId} | Create Secret Dependency Group
[**secret_dependencies_service_delete**](SecretDependenciesApi.md#secret_dependencies_service_delete) | **DELETE** /v1/secret-dependencies/{id} | Delete Secret Dependency
[**secret_dependencies_service_execute**](SecretDependenciesApi.md#secret_dependencies_service_execute) | **POST** /v1/secret-dependencies/run | Run Dependencies
[**secret_dependencies_service_get_dependency**](SecretDependenciesApi.md#secret_dependencies_service_get_dependency) | **GET** /v1/secret-dependencies/{id} | Get Secret Dependency
[**secret_dependencies_service_get_dependency_run_task_status**](SecretDependenciesApi.md#secret_dependencies_service_get_dependency_run_task_status) | **GET** /v1/secret-dependencies/run/{identifier} | Get Secret Dependency run task status
[**secret_dependencies_service_get_groups**](SecretDependenciesApi.md#secret_dependencies_service_get_groups) | **GET** /v1/secret-dependencies/groups/{secretId} | Get Secret Dependency Groups for a Secret
[**secret_dependencies_service_get_scripts**](SecretDependenciesApi.md#secret_dependencies_service_get_scripts) | **GET** /v1/secret-dependencies/scripts | Get Scripts that are possible to use for Dependencies
[**secret_dependencies_service_get_templates**](SecretDependenciesApi.md#secret_dependencies_service_get_templates) | **GET** /v1/secret-dependencies/templates | Get Dependency Templates
[**secret_dependencies_service_search_dependency_summary**](SecretDependenciesApi.md#secret_dependencies_service_search_dependency_summary) | **GET** /v1/secret-dependencies | Search Secret Dependencies
[**secret_dependencies_service_stub**](SecretDependenciesApi.md#secret_dependencies_service_stub) | **GET** /v1/secret-dependencies/stub | Get Secret Dependency Stub
[**secret_dependencies_service_update_dependency**](SecretDependenciesApi.md#secret_dependencies_service_update_dependency) | **PUT** /v1/secret-dependencies/{id} | Update Secret Dependency
[**secret_dependencies_service_update_secret_dependency_group**](SecretDependenciesApi.md#secret_dependencies_service_update_secret_dependency_group) | **PUT** /v1/secret-dependencies/groups/{secretId} | Update Secret Dependency Group


# **secret_dependencies_service_create_dependency**
> SecretDependencyModel secret_dependencies_service_create_dependency()

Create Secret Dependency

Creates a new Secret Dependency and returns the model

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_dependencies_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.secret_dependency_create_args import SecretDependencyCreateArgs
from secret_server_openapiclient.model.secret_dependency_model import SecretDependencyModel
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
    api_instance = secret_dependencies_api.SecretDependenciesApi(api_client)
    secret_dependency_create_args = SecretDependencyCreateArgs(
        active=True,
        condition_dependency_id=None,
        condition_mode=None,
        dependency_template=SecretDependencyTemplate(
            changer_script_id=None,
            dependency_scan_item_fields=[
                SecretDependencyScanItemField(
                    id=None,
                    name=None,
                    parent_name=None,
                    value=None,
                ),
            ],
            script_name=None,
            secret_dependency_changer_id=None,
            secret_dependency_template_id=None,
        ),
        description=None,
        group_id=None,
        machine_name=None,
        privileged_account_secret_id=None,
        run_script=SecretDependencyRunScript(
            machine_name=None,
            odbc_connection_arguments=[
                SecretDependencyOdbcConnectionArg(
                    name=None,
                    value=None,
                ),
            ],
            script_arguments=[
                SecretDependencyUniversalScriptArgument(
                    name=None,
                    type=None,
                    value=None,
                ),
            ],
            script_id=None,
            script_name=None,
            service_name=None,
        ),
        secret_id=None,
        secret_name=None,
        service_name=None,
        settings=[
            SecretDependencySettingMapForDisplay(
                changer_setting_value=None,
                setting=SecretDependencySetting(
                    active=True,
                    can_edit=True,
                    can_edit_value=True,
                    child_settings=[
                        SecretDependencySetting(),
                    ],
                    default_value=None,
                    display_name=None,
                    id=None,
                    is_visibile=True,
                    parent_setting_id=None,
                    regex_validation=None,
                    setting_name=None,
                    setting_section_id=None,
                    setting_type=None,
                    sub_setting_section_id=None,
                ),
                setting_id=None,
                setting_name=None,
                setting_value=None,
            ),
        ],
        sort_order=None,
        ssh_key_secret_id=None,
        type_id=None,
        type_name=None,
    ) # SecretDependencyCreateArgs | Secret Dependency create options (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Secret Dependency
        api_response = api_instance.secret_dependencies_service_create_dependency(secret_dependency_create_args=secret_dependency_create_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretDependenciesApi->secret_dependencies_service_create_dependency: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_dependency_create_args** | [**SecretDependencyCreateArgs**](SecretDependencyCreateArgs.md)| Secret Dependency create options | [optional]

### Return type

[**SecretDependencyModel**](SecretDependencyModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Dependency object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_dependencies_service_create_dependency_group**
> SecretDependencyGroup secret_dependencies_service_create_dependency_group(secret_id)

Create Secret Dependency Group

Creates a new Secret Dependency Group and returns the model

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_dependencies_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.secret_dependency_group import SecretDependencyGroup
from secret_server_openapiclient.model.secret_dependency_group_create_args import SecretDependencyGroupCreateArgs
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
    api_instance = secret_dependencies_api.SecretDependenciesApi(api_client)
    secret_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret ID
    secret_dependency_group_create_args = SecretDependencyGroupCreateArgs(
        secret_dependency_group_name=None,
        site_id=None,
    ) # SecretDependencyGroupCreateArgs | Secret Dependency create options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Secret Dependency Group
        api_response = api_instance.secret_dependencies_service_create_dependency_group(secret_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretDependenciesApi->secret_dependencies_service_create_dependency_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Secret Dependency Group
        api_response = api_instance.secret_dependencies_service_create_dependency_group(secret_id, secret_dependency_group_create_args=secret_dependency_group_create_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretDependenciesApi->secret_dependencies_service_create_dependency_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret ID |
 **secret_dependency_group_create_args** | [**SecretDependencyGroupCreateArgs**](SecretDependencyGroupCreateArgs.md)| Secret Dependency create options | [optional]

### Return type

[**SecretDependencyGroup**](SecretDependencyGroup.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Dependency Group object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_dependencies_service_delete**
> DeletedModel secret_dependencies_service_delete(id)

Delete Secret Dependency

Delete a Secret Dependency by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_dependencies_api
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
    api_instance = secret_dependencies_api.SecretDependenciesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret Dependency ID

    # example passing only required values which don't have defaults set
    try:
        # Delete Secret Dependency
        api_response = api_instance.secret_dependencies_service_delete(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretDependenciesApi->secret_dependencies_service_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret Dependency ID |

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

# **secret_dependencies_service_execute**
> bool, date, datetime, dict, float, int, list, str, none_type secret_dependencies_service_execute()

Run Dependencies

Runs the list of dependencies and retruns an identifier that can be used to collect the status.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_dependencies_api
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
    api_instance = secret_dependencies_api.SecretDependenciesApi(api_client)
    request_body = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | Dependency Id array (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Run Dependencies
        api_response = api_instance.secret_dependencies_service_execute(request_body=request_body)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretDependenciesApi->secret_dependencies_service_execute: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | **[bool, date, datetime, dict, float, int, list, str, none_type]**| Dependency Id array | [optional]

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
**200** | Identifier of the task |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_dependencies_service_get_dependency**
> SecretDependencyModel secret_dependencies_service_get_dependency(id)

Get Secret Dependency

Gets a Secret Dependency and returns the Secret Dependency Model

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_dependencies_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.secret_dependency_model import SecretDependencyModel
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
    api_instance = secret_dependencies_api.SecretDependenciesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret Dependency ID

    # example passing only required values which don't have defaults set
    try:
        # Get Secret Dependency
        api_response = api_instance.secret_dependencies_service_get_dependency(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretDependenciesApi->secret_dependencies_service_get_dependency: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret Dependency ID |

### Return type

[**SecretDependencyModel**](SecretDependencyModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Dependency object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_dependencies_service_get_dependency_run_task_status**
> TaskProgress secret_dependencies_service_get_dependency_run_task_status(identifier)

Get Secret Dependency run task status

Gets a Secret Dependency run task status

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_dependencies_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.task_progress import TaskProgress
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
    api_instance = secret_dependencies_api.SecretDependenciesApi(api_client)
    identifier = None # bool, date, datetime, dict, float, int, list, str, none_type | Task identifier

    # example passing only required values which don't have defaults set
    try:
        # Get Secret Dependency run task status
        api_response = api_instance.secret_dependencies_service_get_dependency_run_task_status(identifier)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretDependenciesApi->secret_dependencies_service_get_dependency_run_task_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **bool, date, datetime, dict, float, int, list, str, none_type**| Task identifier |

### Return type

[**TaskProgress**](TaskProgress.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task Status |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_dependencies_service_get_groups**
> ILogicResultOfSecretDependencyGroupArray secret_dependencies_service_get_groups(secret_id)

Get Secret Dependency Groups for a Secret

Get Secret Dependency Groups for a Secret

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_dependencies_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.i_logic_result_of_secret_dependency_group_array import ILogicResultOfSecretDependencyGroupArray
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
    api_instance = secret_dependencies_api.SecretDependenciesApi(api_client)
    secret_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret ID

    # example passing only required values which don't have defaults set
    try:
        # Get Secret Dependency Groups for a Secret
        api_response = api_instance.secret_dependencies_service_get_groups(secret_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretDependenciesApi->secret_dependencies_service_get_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret ID |

### Return type

[**ILogicResultOfSecretDependencyGroupArray**](ILogicResultOfSecretDependencyGroupArray.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Dependency Group array |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_dependencies_service_get_scripts**
> [DependencyScript] secret_dependencies_service_get_scripts()

Get Scripts that are possible to use for Dependencies

Get Scripts that are possible to use for Dependencies

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_dependencies_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.dependency_script import DependencyScript
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
    api_instance = secret_dependencies_api.SecretDependenciesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Scripts that are possible to use for Dependencies
        api_response = api_instance.secret_dependencies_service_get_scripts()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretDependenciesApi->secret_dependencies_service_get_scripts: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[DependencyScript]**](DependencyScript.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dependency Script array |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_dependencies_service_get_templates**
> [DependencyTemplate] secret_dependencies_service_get_templates()

Get Dependency Templates

Get Dependency Templates

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_dependencies_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.dependency_template import DependencyTemplate
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
    api_instance = secret_dependencies_api.SecretDependenciesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Dependency Templates
        api_response = api_instance.secret_dependencies_service_get_templates()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretDependenciesApi->secret_dependencies_service_get_templates: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[DependencyTemplate]**](DependencyTemplate.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dependency Template array |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_dependencies_service_search_dependency_summary**
> PagingOfSecretDependencySummary secret_dependencies_service_search_dependency_summary(filter_secret_id)

Search Secret Dependencies

Search, filter, sort, and page Secret Dependencies on a Secret

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_dependencies_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.paging_of_secret_dependency_summary import PagingOfSecretDependencySummary
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
    api_instance = secret_dependencies_api.SecretDependenciesApi(api_client)
    filter_secret_id = None # bool, date, datetime, dict, float, int, list, str, none_type | The Secret Id to filter on
    filter_group_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Filter by group id (optional)
    filter_include_inactive = True # bool | Whether or not to include inactive Secret Depenencies (optional)
    filter_last_run_status = None # bool, date, datetime, dict, float, int, list, str, none_type | Filter by last dependency result status (optional)
    filter_search_text = None # bool, date, datetime, dict, float, int, list, str, none_type | Search in the title / name and machine fields (optional)
    filter_template_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Filter by dependency template id (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search Secret Dependencies
        api_response = api_instance.secret_dependencies_service_search_dependency_summary(filter_secret_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretDependenciesApi->secret_dependencies_service_search_dependency_summary: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Secret Dependencies
        api_response = api_instance.secret_dependencies_service_search_dependency_summary(filter_secret_id, filter_group_id=filter_group_id, filter_include_inactive=filter_include_inactive, filter_last_run_status=filter_last_run_status, filter_search_text=filter_search_text, filter_template_id=filter_template_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretDependenciesApi->secret_dependencies_service_search_dependency_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_secret_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| The Secret Id to filter on |
 **filter_group_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Filter by group id | [optional]
 **filter_include_inactive** | **bool**| Whether or not to include inactive Secret Depenencies | [optional]
 **filter_last_run_status** | **bool, date, datetime, dict, float, int, list, str, none_type**| Filter by last dependency result status | [optional]
 **filter_search_text** | **bool, date, datetime, dict, float, int, list, str, none_type**| Search in the title / name and machine fields | [optional]
 **filter_template_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Filter by dependency template id | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfSecretDependencySummary**](PagingOfSecretDependencySummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SecretDependency search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_dependencies_service_stub**
> SecretDependencyModel secret_dependencies_service_stub()

Get Secret Dependency Stub

Return the default values for a new Secret Dependency

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_dependencies_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.secret_dependency_model import SecretDependencyModel
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
    api_instance = secret_dependencies_api.SecretDependenciesApi(api_client)
    script_id = None # bool, date, datetime, dict, float, int, list, str, none_type | The Id of the Script that this Dependency will Run.  Only provide this value if the Dependency is running a script directly, and ensure that the type of the script matches the TypeId value passed in. (optional)
    secret_id = None # bool, date, datetime, dict, float, int, list, str, none_type | The Id of the Secret that this Dependency will appear on (optional)
    template_id = None # bool, date, datetime, dict, float, int, list, str, none_type | The Id of the Dependency Template that this Dependecy will be modeled on. Only provide this value if the Dependency is based on a Template. (optional)
    type_id = None # bool, date, datetime, dict, float, int, list, str, none_type | The Id of the Dependency Type that this Dependecy will be modeled on. Only provide this value if the Dependency is a running a script directly and is NOT based on a Dependency Template.  Valid Values: PowershellScript = 7, SshScript = 8, SqlScript = 9 (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Secret Dependency Stub
        api_response = api_instance.secret_dependencies_service_stub(script_id=script_id, secret_id=secret_id, template_id=template_id, type_id=type_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretDependenciesApi->secret_dependencies_service_stub: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **script_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| The Id of the Script that this Dependency will Run.  Only provide this value if the Dependency is running a script directly, and ensure that the type of the script matches the TypeId value passed in. | [optional]
 **secret_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| The Id of the Secret that this Dependency will appear on | [optional]
 **template_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| The Id of the Dependency Template that this Dependecy will be modeled on. Only provide this value if the Dependency is based on a Template. | [optional]
 **type_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| The Id of the Dependency Type that this Dependecy will be modeled on. Only provide this value if the Dependency is a running a script directly and is NOT based on a Dependency Template.  Valid Values: PowershellScript &#x3D; 7, SshScript &#x3D; 8, SqlScript &#x3D; 9 | [optional]

### Return type

[**SecretDependencyModel**](SecretDependencyModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SecretDependencyModel |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_dependencies_service_update_dependency**
> SecretDependencyUpdateArgs secret_dependencies_service_update_dependency(id)

Update Secret Dependency

Updates a Secret Dependency and returns the model

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_dependencies_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.secret_dependency_update_args import SecretDependencyUpdateArgs
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
    api_instance = secret_dependencies_api.SecretDependenciesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret Dependency ID
    secret_dependency_update_args = SecretDependencyUpdateArgs(
        active=True,
        condition_dependency_id=None,
        condition_mode=None,
        dependency_template=SecretDependencyTemplate(
            changer_script_id=None,
            dependency_scan_item_fields=[
                SecretDependencyScanItemField(
                    id=None,
                    name=None,
                    parent_name=None,
                    value=None,
                ),
            ],
            script_name=None,
            secret_dependency_changer_id=None,
            secret_dependency_template_id=None,
        ),
        description=None,
        group_id=None,
        id=None,
        machine_name=None,
        privileged_account_secret_id=None,
        run_script=SecretDependencyRunScript(
            machine_name=None,
            odbc_connection_arguments=[
                SecretDependencyOdbcConnectionArg(
                    name=None,
                    value=None,
                ),
            ],
            script_arguments=[
                SecretDependencyUniversalScriptArgument(
                    name=None,
                    type=None,
                    value=None,
                ),
            ],
            script_id=None,
            script_name=None,
            service_name=None,
        ),
        secret_id=None,
        secret_name=None,
        service_name=None,
        settings=[
            SecretDependencySettingMapForDisplay(
                changer_setting_value=None,
                setting=SecretDependencySetting(
                    active=True,
                    can_edit=True,
                    can_edit_value=True,
                    child_settings=[
                        SecretDependencySetting(),
                    ],
                    default_value=None,
                    display_name=None,
                    id=None,
                    is_visibile=True,
                    parent_setting_id=None,
                    regex_validation=None,
                    setting_name=None,
                    setting_section_id=None,
                    setting_type=None,
                    sub_setting_section_id=None,
                ),
                setting_id=None,
                setting_name=None,
                setting_value=None,
            ),
        ],
        sort_order=None,
        ssh_key_secret_id=None,
        type_id=None,
        type_name=None,
    ) # SecretDependencyUpdateArgs | Secret Dependency update options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Secret Dependency
        api_response = api_instance.secret_dependencies_service_update_dependency(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretDependenciesApi->secret_dependencies_service_update_dependency: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Secret Dependency
        api_response = api_instance.secret_dependencies_service_update_dependency(id, secret_dependency_update_args=secret_dependency_update_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretDependenciesApi->secret_dependencies_service_update_dependency: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret Dependency ID |
 **secret_dependency_update_args** | [**SecretDependencyUpdateArgs**](SecretDependencyUpdateArgs.md)| Secret Dependency update options | [optional]

### Return type

[**SecretDependencyUpdateArgs**](SecretDependencyUpdateArgs.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SecretDependencyModel object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_dependencies_service_update_secret_dependency_group**
> SecretDependencyGroupModel secret_dependencies_service_update_secret_dependency_group(secret_id)

Update Secret Dependency Group

Update a Secret Dependency Group

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import secret_dependencies_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.update_secret_dependency_group_args import UpdateSecretDependencyGroupArgs
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.secret_dependency_group_model import SecretDependencyGroupModel
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
    api_instance = secret_dependencies_api.SecretDependenciesApi(api_client)
    secret_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Id of Secret to assign to Dependency Group.
    update_secret_dependency_group_args = UpdateSecretDependencyGroupArgs(
        data=UpdateSecretDependencyGroupModel(
            secret_dependency_group_id=None,
            secret_dependency_group_name=None,
            site_id=None,
        ),
    ) # UpdateSecretDependencyGroupArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Secret Dependency Group
        api_response = api_instance.secret_dependencies_service_update_secret_dependency_group(secret_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretDependenciesApi->secret_dependencies_service_update_secret_dependency_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Secret Dependency Group
        api_response = api_instance.secret_dependencies_service_update_secret_dependency_group(secret_id, update_secret_dependency_group_args=update_secret_dependency_group_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SecretDependenciesApi->secret_dependencies_service_update_secret_dependency_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Id of Secret to assign to Dependency Group. |
 **update_secret_dependency_group_args** | [**UpdateSecretDependencyGroupArgs**](UpdateSecretDependencyGroupArgs.md)| args | [optional]

### Return type

[**SecretDependencyGroupModel**](SecretDependencyGroupModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SecretDependencyGroupModel object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

