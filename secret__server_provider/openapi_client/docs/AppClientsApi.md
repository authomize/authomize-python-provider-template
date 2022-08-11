# plugins.AppClientsApi

All URIs are relative to *https://integrations.secretservercloud.com//api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_clients_service_create_client**](AppClientsApi.md#app_clients_service_create_client) | **POST** /v1/app-clients | Create App Client
[**app_clients_service_delete_client**](AppClientsApi.md#app_clients_service_delete_client) | **DELETE** /v1/app-clients/{id} | Delete App Client
[**app_clients_service_get_client**](AppClientsApi.md#app_clients_service_get_client) | **GET** /v1/app-clients/{id} | Get App Client
[**app_clients_service_stub**](AppClientsApi.md#app_clients_service_stub) | **GET** /v1/app-clients/stub | Get App Client Stub
[**app_clients_service_update_client**](AppClientsApi.md#app_clients_service_update_client) | **PUT** /v1/app-clients/{id} | Update App Client


# **app_clients_service_create_client**
> AppClientModel app_clients_service_create_client()

Create App Client

Create a new app client

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import app_clients_api
from plugins.model.app_client_create_args import AppClientCreateArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.app_client_model import AppClientModel
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
    api_instance = app_clients_api.AppClientsApi(api_client)
    app_client_create_args = AppClientCreateArgs(
        redirect_uri=None,
    ) # AppClientCreateArgs | App client creation options (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create App Client
        api_response = api_instance.app_clients_service_create_client(app_client_create_args=app_client_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling AppClientsApi->app_clients_service_create_client: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_client_create_args** | [**AppClientCreateArgs**](AppClientCreateArgs.md)| App client creation options | [optional]

### Return type

[**AppClientModel**](AppClientModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App client object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_clients_service_delete_client**
> DeletedModel app_clients_service_delete_client(id)

Delete App Client

Delete an app client by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import app_clients_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.deleted_model import DeletedModel
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
    api_instance = app_clients_api.AppClientsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | App client ID

    # example passing only required values which don't have defaults set
    try:
        # Delete App Client
        api_response = api_instance.app_clients_service_delete_client(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling AppClientsApi->app_clients_service_delete_client: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| App client ID |

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

# **app_clients_service_get_client**
> AppClientModel app_clients_service_get_client(id)

Get App Client

Get a single app client by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import app_clients_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.app_client_model import AppClientModel
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
    api_instance = app_clients_api.AppClientsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | App client ID
    include_inactive = True # bool | Whether to include inactive app clients (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get App Client
        api_response = api_instance.app_clients_service_get_client(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling AppClientsApi->app_clients_service_get_client: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get App Client
        api_response = api_instance.app_clients_service_get_client(id, include_inactive=include_inactive)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling AppClientsApi->app_clients_service_get_client: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| App client ID |
 **include_inactive** | **bool**| Whether to include inactive app clients | [optional]

### Return type

[**AppClientModel**](AppClientModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App client object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_clients_service_stub**
> AppClientModel app_clients_service_stub()

Get App Client Stub

Return the default values for a new app client

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import app_clients_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.app_client_model import AppClientModel
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
    api_instance = app_clients_api.AppClientsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get App Client Stub
        api_response = api_instance.app_clients_service_stub()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling AppClientsApi->app_clients_service_stub: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AppClientModel**](AppClientModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App client object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_clients_service_update_client**
> AppClientModel app_clients_service_update_client(id)

Update App Client

Update a single app client by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import app_clients_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.app_client_model import AppClientModel
from plugins.model.app_client_update_args import AppClientUpdateArgs
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
    api_instance = app_clients_api.AppClientsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | App client ID
    app_client_update_args = AppClientUpdateArgs(
        id=None,
        redirect_uri=None,
    ) # AppClientUpdateArgs | App client update options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update App Client
        api_response = api_instance.app_clients_service_update_client(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling AppClientsApi->app_clients_service_update_client: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update App Client
        api_response = api_instance.app_clients_service_update_client(id, app_client_update_args=app_client_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling AppClientsApi->app_clients_service_update_client: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| App client ID |
 **app_client_update_args** | [**AppClientUpdateArgs**](AppClientUpdateArgs.md)| App client update options | [optional]

### Return type

[**AppClientModel**](AppClientModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App client object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

