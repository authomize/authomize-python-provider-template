# plugins.ServerNodesApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**server_nodes_service_get**](ServerNodesApi.md#server_nodes_service_get) | **GET** /v1/nodes/{nodeId} | Get Server Node
[**server_nodes_service_get_list**](ServerNodesApi.md#server_nodes_service_get_list) | **GET** /v1/nodes | Get Server Nodes
[**server_nodes_service_update_node_configuration**](ServerNodesApi.md#server_nodes_service_update_node_configuration) | **POST** /v1/nodes/{nodeId}/configuration | Update Server Node Configuration


# **server_nodes_service_get**
> ServerNodeModel server_nodes_service_get(node_id)

Get Server Node

Get Server Node

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import server_nodes_api
from plugins.model.server_node_model import ServerNodeModel
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
    api_instance = server_nodes_api.ServerNodesApi(api_client)
    node_id = None # bool, date, datetime, dict, float, int, list, str, none_type | nodeId

    # example passing only required values which don't have defaults set
    try:
        # Get Server Node
        api_response = api_instance.server_nodes_service_get(node_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ServerNodesApi->server_nodes_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| nodeId |

### Return type

[**ServerNodeModel**](ServerNodeModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Server Node List |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **server_nodes_service_get_list**
> [ServerNodeModel] server_nodes_service_get_list()

Get Server Nodes

Get Server Nodes

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import server_nodes_api
from plugins.model.server_node_model import ServerNodeModel
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
    api_instance = server_nodes_api.ServerNodesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Server Nodes
        api_response = api_instance.server_nodes_service_get_list()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ServerNodesApi->server_nodes_service_get_list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[ServerNodeModel]**](ServerNodeModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Server Node List |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **server_nodes_service_update_node_configuration**
> server_nodes_service_update_node_configuration(node_id)

Update Server Node Configuration

Update Server Node Configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import server_nodes_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.server_node_configuration_model import ServerNodeConfigurationModel
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
    api_instance = server_nodes_api.ServerNodesApi(api_client)
    node_id = None # bool, date, datetime, dict, float, int, list, str, none_type | nodeId
    server_node_configuration_model = ServerNodeConfigurationModel(
        enable_background_worker=True,
        enable_engine_worker=True,
        enable_session_recording_worker=True,
        in_cluster=True,
        log_level=None,
        readonly_mode_enabled=True,
    ) # ServerNodeConfigurationModel | nodeConfiguration (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Server Node Configuration
        api_instance.server_nodes_service_update_node_configuration(node_id)
    except plugins.ApiException as e:
        print("Exception when calling ServerNodesApi->server_nodes_service_update_node_configuration: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Server Node Configuration
        api_instance.server_nodes_service_update_node_configuration(node_id, server_node_configuration_model=server_node_configuration_model)
    except plugins.ApiException as e:
        print("Exception when calling ServerNodesApi->server_nodes_service_update_node_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| nodeId |
 **server_node_configuration_model** | [**ServerNodeConfigurationModel**](ServerNodeConfigurationModel.md)| nodeConfiguration | [optional]

### Return type

void (empty response body)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Unknown or empty response |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

