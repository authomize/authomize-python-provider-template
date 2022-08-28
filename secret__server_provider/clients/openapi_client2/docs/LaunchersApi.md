# plugins.LaunchersApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**launchers_service_create**](LaunchersApi.md#launchers_service_create) | **POST** /v1/launchers/secret | Launch a secret.
[**launchers_service_get**](LaunchersApi.md#launchers_service_get) | **GET** /v1/launchers/{id} | Get Launcher
[**launchers_service_launcher_succeeded**](LaunchersApi.md#launchers_service_launcher_succeeded) | **GET** /v1/launchers/prepare/{id}/result | Get Prepare Launcher Result
[**launchers_service_lookup**](LaunchersApi.md#launchers_service_lookup) | **GET** /v1/launchers/lookup | Lookup Launchers
[**launchers_service_prepare_launcher**](LaunchersApi.md#launchers_service_prepare_launcher) | **POST** /v1/launchers/prepare | Prepare Launcher Session
[**launchers_service_search_launcher_details_v2**](LaunchersApi.md#launchers_service_search_launcher_details_v2) | **GET** /v2/launchers/secret | Get secret launcher details.
[**launchers_service_search_launchers**](LaunchersApi.md#launchers_service_search_launchers) | **GET** /v1/launchers | Search Launchers
[**launchers_service_trigger_download**](LaunchersApi.md#launchers_service_trigger_download) | **GET** /v1/launchers/protocol-handler | Triggers a download of the Protocol Handler


# **launchers_service_create**
> LaunchedSecretModel launchers_service_create()

Launch a secret.

Launch a the secret using the provided secret id, and required fields.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import launchers_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.launch_secret_args import LaunchSecretArgs
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.launched_secret_model import LaunchedSecretModel
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
    api_instance = launchers_api.LaunchersApi(api_client)
    launch_secret_args = LaunchSecretArgs(
        launcher_id=1,
        prompt_field_value="prompt_field_value_example",
        secret_id=1,
        site_id=1,
    ) # LaunchSecretArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Launch a secret.
        api_response = api_instance.launchers_service_create(launch_secret_args=launch_secret_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling LaunchersApi->launchers_service_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **launch_secret_args** | [**LaunchSecretArgs**](LaunchSecretArgs.md)| args | [optional]

### Return type

[**LaunchedSecretModel**](LaunchedSecretModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Launched Secret details |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **launchers_service_get**
> LauncherModel launchers_service_get(id)

Get Launcher

Get a single launcher by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import launchers_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.launcher_model import LauncherModel
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
    api_instance = launchers_api.LaunchersApi(api_client)
    id = 1 # int | Launcher ID

    # example passing only required values which don't have defaults set
    try:
        # Get Launcher
        api_response = api_instance.launchers_service_get(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling LaunchersApi->launchers_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Launcher ID |

### Return type

[**LauncherModel**](LauncherModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Launcher object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **launchers_service_launcher_succeeded**
> PrepareLauncherQueryResultModel launchers_service_launcher_succeeded(id)

Get Prepare Launcher Result

Get result of prepare Launcher Session request.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import launchers_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.prepare_launcher_query_result_model import PrepareLauncherQueryResultModel
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
    api_instance = launchers_api.LaunchersApi(api_client)
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get Prepare Launcher Result
        api_response = api_instance.launchers_service_launcher_succeeded(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling LaunchersApi->launchers_service_launcher_succeeded: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id |

### Return type

[**PrepareLauncherQueryResultModel**](PrepareLauncherQueryResultModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Prepare Launcher Query Result |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **launchers_service_lookup**
> PagingOfLauncherLookup launchers_service_lookup()

Lookup Launchers

Search, filter, sort, and page launchers, returning only launcher ID and name

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import launchers_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_launcher_lookup import PagingOfLauncherLookup
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
    api_instance = launchers_api.LaunchersApi(api_client)
    filter_application = "filter.application_example" # str | Associated application (optional)
    filter_include_inactive = True # bool | Whether to include inactive launchers (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Lookup Launchers
        api_response = api_instance.launchers_service_lookup(filter_application=filter_application, filter_include_inactive=filter_include_inactive, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling LaunchersApi->launchers_service_lookup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_application** | **str**| Associated application | [optional]
 **filter_include_inactive** | **bool**| Whether to include inactive launchers | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfLauncherLookup**](PagingOfLauncherLookup.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Launcher search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **launchers_service_prepare_launcher**
> PrepareLauncherResult launchers_service_prepare_launcher()

Prepare Launcher Session

Prepare a Launcher Session.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import launchers_api
from plugins.model.prepare_launcher_result import PrepareLauncherResult
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.prepare_launcher_args import PrepareLauncherArgs
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
    api_instance = launchers_api.LaunchersApi(api_client)
    prepare_launcher_args = PrepareLauncherArgs(
        launcher_type_id=1,
        prompt_field_value="prompt_field_value_example",
        secret_id=1,
        site_id=1,
    ) # PrepareLauncherArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Prepare Launcher Session
        api_response = api_instance.launchers_service_prepare_launcher(prepare_launcher_args=prepare_launcher_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling LaunchersApi->launchers_service_prepare_launcher: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prepare_launcher_args** | [**PrepareLauncherArgs**](PrepareLauncherArgs.md)| args | [optional]

### Return type

[**PrepareLauncherResult**](PrepareLauncherResult.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PrepareLauncherResult |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **launchers_service_search_launcher_details_v2**
> PagingOfLauncherDetailsV2 launchers_service_search_launcher_details_v2()

Get secret launcher details.

Get the details and fields needed for the launchers a secret can use.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import launchers_api
from plugins.model.paging_of_launcher_details_v2 import PagingOfLauncherDetailsV2
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
    api_instance = launchers_api.LaunchersApi(api_client)
    filter_secret_id = 1 # int | The secret to get launch information about (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get secret launcher details.
        api_response = api_instance.launchers_service_search_launcher_details_v2(filter_secret_id=filter_secret_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling LaunchersApi->launchers_service_search_launcher_details_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_secret_id** | **int**| The secret to get launch information about | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfLauncherDetailsV2**](PagingOfLauncherDetailsV2.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret&#39;s Launcher details |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **launchers_service_search_launchers**
> PagingOfLauncherSummary launchers_service_search_launchers()

Search Launchers

Search, filter, sort, and page launchers

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import launchers_api
from plugins.model.paging_of_launcher_summary import PagingOfLauncherSummary
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
    api_instance = launchers_api.LaunchersApi(api_client)
    filter_application = "filter.application_example" # str | Associated application (optional)
    filter_include_inactive = True # bool | Whether to include inactive launchers (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Launchers
        api_response = api_instance.launchers_service_search_launchers(filter_application=filter_application, filter_include_inactive=filter_include_inactive, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling LaunchersApi->launchers_service_search_launchers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_application** | **str**| Associated application | [optional]
 **filter_include_inactive** | **bool**| Whether to include inactive launchers | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfLauncherSummary**](PagingOfLauncherSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Launcher search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **launchers_service_trigger_download**
> launchers_service_trigger_download()

Triggers a download of the Protocol Handler

Triggers a download of the Protocol Handler

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import launchers_api
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
    api_instance = launchers_api.LaunchersApi(api_client)
    force_msi = True # bool | forceMsi (optional)
    is32_bit = True # bool | is32Bit (optional)
    is_rds = True # bool | isRDS (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Triggers a download of the Protocol Handler
        api_instance.launchers_service_trigger_download(force_msi=force_msi, is32_bit=is32_bit, is_rds=is_rds)
    except plugins.ApiException as e:
        print("Exception when calling LaunchersApi->launchers_service_trigger_download: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **force_msi** | **bool**| forceMsi | [optional]
 **is32_bit** | **bool**| is32Bit | [optional]
 **is_rds** | **bool**| isRDS | [optional]

### Return type

void (empty response body)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Unknown or empty response |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

