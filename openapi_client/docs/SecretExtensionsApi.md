# plugins.SecretExtensionsApi

All URIs are relative to *https://integrations.secretservercloud.com//api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**secret_extensions_service_get_auto_fill_values**](SecretExtensionsApi.md#secret_extensions_service_get_auto_fill_values) | **POST** /v1/secret-extensions/autofill-values | Get AutoFill values for Url by SecretId
[**secret_extensions_service_get_web_secret_templates**](SecretExtensionsApi.md#secret_extensions_service_get_web_secret_templates) | **GET** /v1/secret-extensions/web-secret-templates | Get Secret Templates
[**secret_extensions_service_search**](SecretExtensionsApi.md#secret_extensions_service_search) | **POST** /v1/secret-extensions/search-by-url | Search Secrets by Url
[**secret_extensions_service_search_active_directory_secrets**](SecretExtensionsApi.md#secret_extensions_service_search_active_directory_secrets) | **POST** /v1/secret-extensions/search-ad-secrets-by-domain | Search Secrets by Domain
[**secret_extensions_service_search_windows_account_secrets**](SecretExtensionsApi.md#secret_extensions_service_search_windows_account_secrets) | **POST** /v1/secret-extensions/search-windows-account-secrets-by-computer-name | Search Secrets by Computer Name


# **secret_extensions_service_get_auto_fill_values**
> SecretExtensionAutoFillResult secret_extensions_service_get_auto_fill_values()

Get AutoFill values for Url by SecretId

Get AutoFill values (username and password) for Url by SecretId

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_extensions_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.secret_extension_auto_fill_result import SecretExtensionAutoFillResult
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.extension_auto_fill_value_args import ExtensionAutoFillValueArgs
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
    api_instance = secret_extensions_api.SecretExtensionsApi(api_client)
    extension_auto_fill_value_args = ExtensionAutoFillValueArgs(
        secret_id=None,
        url=None,
    ) # ExtensionAutoFillValueArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get AutoFill values for Url by SecretId
        api_response = api_instance.secret_extensions_service_get_auto_fill_values(extension_auto_fill_value_args=extension_auto_fill_value_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretExtensionsApi->secret_extensions_service_get_auto_fill_values: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extension_auto_fill_value_args** | [**ExtensionAutoFillValueArgs**](ExtensionAutoFillValueArgs.md)| args | [optional]

### Return type

[**SecretExtensionAutoFillResult**](SecretExtensionAutoFillResult.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Autofill values result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_extensions_service_get_web_secret_templates**
> [SecretTemplateModel] secret_extensions_service_get_web_secret_templates()

Get Secret Templates

Get Secret Templates valid for web passwords

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_extensions_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.secret_template_model import SecretTemplateModel
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
    api_instance = secret_extensions_api.SecretExtensionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Secret Templates
        api_response = api_instance.secret_extensions_service_get_web_secret_templates()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretExtensionsApi->secret_extensions_service_get_web_secret_templates: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[SecretTemplateModel]**](SecretTemplateModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Secret Templates |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_extensions_service_search**
> [SecretSearchByUrlSummary] secret_extensions_service_search()

Search Secrets by Url

Search for Secrets that match a URL

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_extensions_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_search_by_url_summary import SecretSearchByUrlSummary
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
    api_instance = secret_extensions_api.SecretExtensionsApi(api_client)
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | url (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Secrets by Url
        api_response = api_instance.secret_extensions_service_search(body=body)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretExtensionsApi->secret_extensions_service_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| url | [optional]

### Return type

[**[SecretSearchByUrlSummary]**](SecretSearchByUrlSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_extensions_service_search_active_directory_secrets**
> [SecretExtensionSearchSummary] secret_extensions_service_search_active_directory_secrets()

Search Secrets by Domain

Search for Secrets that match a domain

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_extensions_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.secret_extension_search_summary import SecretExtensionSearchSummary
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
    api_instance = secret_extensions_api.SecretExtensionsApi(api_client)
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | domain (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Secrets by Domain
        api_response = api_instance.secret_extensions_service_search_active_directory_secrets(body=body)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretExtensionsApi->secret_extensions_service_search_active_directory_secrets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| domain | [optional]

### Return type

[**[SecretExtensionSearchSummary]**](SecretExtensionSearchSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_extensions_service_search_windows_account_secrets**
> [SecretExtensionSearchSummary] secret_extensions_service_search_windows_account_secrets()

Search Secrets by Computer Name

Search for Secrets that match a computer name

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_extensions_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.secret_extension_search_summary import SecretExtensionSearchSummary
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
    api_instance = secret_extensions_api.SecretExtensionsApi(api_client)
    body = None # bool, date, datetime, dict, float, int, list, str, none_type | computerName (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Secrets by Computer Name
        api_response = api_instance.secret_extensions_service_search_windows_account_secrets(body=body)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretExtensionsApi->secret_extensions_service_search_windows_account_secrets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**| computerName | [optional]

### Return type

[**[SecretExtensionSearchSummary]**](SecretExtensionSearchSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

