# plugins.ScriptApi

All URIs are relative to *https://integrations.secretservercloud.com//api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**script_service_load**](ScriptApi.md#script_service_load) | **GET** /v1/userscripts/{id} | Get Script
[**script_service_post**](ScriptApi.md#script_service_post) | **POST** /v1/userscripts | Create Script
[**script_service_search**](ScriptApi.md#script_service_search) | **GET** /v1/userscripts | Search scripts


# **script_service_load**
> ScriptModel script_service_load(id)

Get Script

Get a single script by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import script_api
from plugins.model.script_model import ScriptModel
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
    api_instance = script_api.ScriptApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Script ID

    # example passing only required values which don't have defaults set
    try:
        # Get Script
        api_response = api_instance.script_service_load(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ScriptApi->script_service_load: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Script ID |

### Return type

[**ScriptModel**](ScriptModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Script object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **script_service_post**
> ScriptModel script_service_post()

Create Script

Create a new Script

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import script_api
from plugins.model.script_model import ScriptModel
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.script_create_args import ScriptCreateArgs
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
    api_instance = script_api.ScriptApi(api_client)
    script_create_args = ScriptCreateArgs(
        active=True,
        additional_data=None,
        description=None,
        name=None,
        odbc_connection_string_args=[
            None,
        ],
        script=None,
        script_category_id=None,
        script_category_name=None,
        script_type=UserScriptType("{}"),
        usage_count=None,
    ) # ScriptCreateArgs | Script creation options (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Script
        api_response = api_instance.script_service_post(script_create_args=script_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ScriptApi->script_service_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **script_create_args** | [**ScriptCreateArgs**](ScriptCreateArgs.md)| Script creation options | [optional]

### Return type

[**ScriptModel**](ScriptModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Template object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **script_service_search**
> PagingOfScriptSummary script_service_search()

Search scripts

Search, filter, sort, and page scripts

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import script_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.paging_of_script_summary import PagingOfScriptSummary
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
    api_instance = script_api.ScriptApi(api_client)
    filter_include_inactive = True # bool | Whether to include inactive scripts in the results (optional)
    filter_search_text = None # bool, date, datetime, dict, float, int, list, str, none_type | Search Text (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search scripts
        api_response = api_instance.script_service_search(filter_include_inactive=filter_include_inactive, filter_search_text=filter_search_text, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ScriptApi->script_service_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_include_inactive** | **bool**| Whether to include inactive scripts in the results | [optional]
 **filter_search_text** | **bool, date, datetime, dict, float, int, list, str, none_type**| Search Text | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfScriptSummary**](PagingOfScriptSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | scripts search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

