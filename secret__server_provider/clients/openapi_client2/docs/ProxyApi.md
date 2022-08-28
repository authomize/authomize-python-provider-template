# plugins.ProxyApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**proxy_service_create_terminal_client_overrides**](ProxyApi.md#proxy_service_create_terminal_client_overrides) | **POST** /v1/proxy/ssh/client-overrides | Creates SSH Terminal client overrides
[**proxy_service_delete_terminal_client_overrides**](ProxyApi.md#proxy_service_delete_terminal_client_overrides) | **DELETE** /v1/proxy/ssh/client-overrides/{clientOverrideId} | Deletes SSH Terminal client overrides
[**proxy_service_generate_rdp_proxy_certificate**](ProxyApi.md#proxy_service_generate_rdp_proxy_certificate) | **POST** /v1/proxy/rdp/generate-certificate | Generate RDP server certificate
[**proxy_service_generate_ssh_host_key**](ProxyApi.md#proxy_service_generate_ssh_host_key) | **POST** /v1/proxy/ssh/generate-key | Generate SSH Host Key
[**proxy_service_get_audits**](ProxyApi.md#proxy_service_get_audits) | **GET** /v1/proxy/audit | Get the Proxy Audit List
[**proxy_service_get_endpoint_notification**](ProxyApi.md#proxy_service_get_endpoint_notification) | **GET** /v1/proxy/endpoints/notification | Get endpoint warnings
[**proxy_service_get_endpoints**](ProxyApi.md#proxy_service_get_endpoints) | **GET** /v1/proxy/endpoints | Get the proxy endpoints list
[**proxy_service_get_explanations**](ProxyApi.md#proxy_service_get_explanations) | **GET** /v1/proxy/explanation | Get Proxy Explanations
[**proxy_service_get_proxying_state**](ProxyApi.md#proxy_service_get_proxying_state) | **GET** /v1/proxy/state | Get proxy state
[**proxy_service_get_rdp_endpoint_notification**](ProxyApi.md#proxy_service_get_rdp_endpoint_notification) | **GET** /v1/proxy/rdp/notification | Get a notification of where the RDP proxy is running
[**proxy_service_get_rdp_proxy_configuration**](ProxyApi.md#proxy_service_get_rdp_proxy_configuration) | **GET** /v1/proxy/rdp/config | Get the RDP proxy configuration
[**proxy_service_get_ssh_endpoint_notification**](ProxyApi.md#proxy_service_get_ssh_endpoint_notification) | **GET** /v1/proxy/ssh/notification | Get a notification of where the SSH proxy is running
[**proxy_service_get_ssh_proxy_configuration**](ProxyApi.md#proxy_service_get_ssh_proxy_configuration) | **GET** /v1/proxy/ssh/config | Get the SSH proxy configuration
[**proxy_service_get_terminal_client_history**](ProxyApi.md#proxy_service_get_terminal_client_history) | **GET** /v1/proxy/ssh/clienthistory | Get SSH Terminal client history
[**proxy_service_get_terminal_client_overrides**](ProxyApi.md#proxy_service_get_terminal_client_overrides) | **GET** /v1/proxy/ssh/client-overrides | Get SSH Terminal client overrides
[**proxy_service_get_terminal_clients**](ProxyApi.md#proxy_service_get_terminal_clients) | **GET** /v1/proxy/ssh/clients | Get SSH Terminal clients
[**proxy_service_patch_engine**](ProxyApi.md#proxy_service_patch_engine) | **PATCH** /v1/proxy/endpoints/engines/{id} | Update an engine proxy configuration
[**proxy_service_patch_node**](ProxyApi.md#proxy_service_patch_node) | **PATCH** /v1/proxy/endpoints/nodes/{id} | Update a node proxy configuration
[**proxy_service_patch_rdp_proxy_configuration**](ProxyApi.md#proxy_service_patch_rdp_proxy_configuration) | **PATCH** /v1/proxy/rdp/config | Update the RDP proxy configuration
[**proxy_service_patch_site**](ProxyApi.md#proxy_service_patch_site) | **PATCH** /v1/proxy/endpoints/sites/{id} | Update a site proxy configuration
[**proxy_service_patch_ssh_proxy_configuration**](ProxyApi.md#proxy_service_patch_ssh_proxy_configuration) | **PATCH** /v1/proxy/ssh/config | Update the SSH proxy configuration
[**proxy_service_update_terminal_client_overrides**](ProxyApi.md#proxy_service_update_terminal_client_overrides) | **PATCH** /v1/proxy/ssh/client-overrides/{clientOverrideId} | Updates SSH Terminal client overrides
[**proxy_service_update_terminal_client_type**](ProxyApi.md#proxy_service_update_terminal_client_type) | **PATCH** /v1/proxy/ssh/clients/{clientId} | Updates a SSH Terminal client type


# **proxy_service_create_terminal_client_overrides**
> ProxyClientOverrideSummary proxy_service_create_terminal_client_overrides()

Creates SSH Terminal client overrides

Creates SSH Terminal client overrides

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import proxy_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.proxy_client_override_summary import ProxyClientOverrideSummary
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
    api_instance = proxy_api.ProxyApi(api_client)
    proxy_client_override_summary = ProxyClientOverrideSummary(
        client_override_id=1,
        ip_address_range="ip_address_range_example",
        terminal_client_type=ProxyClientType("{}"),
    ) # ProxyClientOverrideSummary | clientOverride (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates SSH Terminal client overrides
        api_response = api_instance.proxy_service_create_terminal_client_overrides(proxy_client_override_summary=proxy_client_override_summary)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_create_terminal_client_overrides: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proxy_client_override_summary** | [**ProxyClientOverrideSummary**](ProxyClientOverrideSummary.md)| clientOverride | [optional]

### Return type

[**ProxyClientOverrideSummary**](ProxyClientOverrideSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of SSH Terminal client overrides |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_service_delete_terminal_client_overrides**
> DeletedModel proxy_service_delete_terminal_client_overrides(client_override_id)

Deletes SSH Terminal client overrides

Deletes SSH Terminal client overrides

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import proxy_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.deleted_model import DeletedModel
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
    api_instance = proxy_api.ProxyApi(api_client)
    client_override_id = 1 # int | clientOverrideId

    # example passing only required values which don't have defaults set
    try:
        # Deletes SSH Terminal client overrides
        api_response = api_instance.proxy_service_delete_terminal_client_overrides(client_override_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_delete_terminal_client_overrides: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_override_id** | **int**| clientOverrideId |

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
**200** | A list of SSH Terminal client overrides |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_service_generate_rdp_proxy_certificate**
> RdpProxyConfigurationViewModel proxy_service_generate_rdp_proxy_certificate()

Generate RDP server certificate

Generates a new RDP server certificate and returns the RDP configuration with the updated server certificate

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import proxy_api
from plugins.model.rdp_proxy_configuration_view_model import RdpProxyConfigurationViewModel
from plugins.model.generate_rdp_certificate_args import GenerateRdpCertificateArgs
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
    api_instance = proxy_api.ProxyApi(api_client)
    generate_rdp_certificate_args = GenerateRdpCertificateArgs(
        dns_name="dns_name_example",
    ) # GenerateRdpCertificateArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generate RDP server certificate
        api_response = api_instance.proxy_service_generate_rdp_proxy_certificate(generate_rdp_certificate_args=generate_rdp_certificate_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_generate_rdp_proxy_certificate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_rdp_certificate_args** | [**GenerateRdpCertificateArgs**](GenerateRdpCertificateArgs.md)| args | [optional]

### Return type

[**RdpProxyConfigurationViewModel**](RdpProxyConfigurationViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RDP Proxy Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_service_generate_ssh_host_key**
> SshProxyConfigurationViewModel proxy_service_generate_ssh_host_key()

Generate SSH Host Key

Generates a new SSH host key and returns the SSH configuration with the updated host key

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import proxy_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.ssh_proxy_configuration_view_model import SshProxyConfigurationViewModel
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
    api_instance = proxy_api.ProxyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Generate SSH Host Key
        api_response = api_instance.proxy_service_generate_ssh_host_key()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_generate_ssh_host_key: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SshProxyConfigurationViewModel**](SshProxyConfigurationViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SSH Proxy Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_service_get_audits**
> PagingOfProxyAuditModel proxy_service_get_audits()

Get the Proxy Audit List

Search, filter, sort, and page Proxy Audits.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import proxy_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_proxy_audit_model import PagingOfProxyAuditModel
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
    api_instance = proxy_api.ProxyApi(api_client)
    is_exporting = True # bool | isExporting (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the Proxy Audit List
        api_response = api_instance.proxy_service_get_audits(is_exporting=is_exporting, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_get_audits: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_exporting** | **bool**| isExporting | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfProxyAuditModel**](PagingOfProxyAuditModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of Proxy Audits. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_service_get_endpoint_notification**
> str proxy_service_get_endpoint_notification()

Get endpoint warnings

Get endpoint warnings

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import proxy_api
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
    api_instance = proxy_api.ProxyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get endpoint warnings
        api_response = api_instance.proxy_service_get_endpoint_notification()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_get_endpoint_notification: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of nodes, sites, and engines with proxy configurations |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_service_get_endpoints**
> ProxyEndpointsViewModel proxy_service_get_endpoints()

Get the proxy endpoints list

Get the proxy endpoints list

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import proxy_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.proxy_endpoints_view_model import ProxyEndpointsViewModel
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
    api_instance = proxy_api.ProxyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the proxy endpoints list
        api_response = api_instance.proxy_service_get_endpoints()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_get_endpoints: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ProxyEndpointsViewModel**](ProxyEndpointsViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of nodes, sites, and engines with proxy configurations |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_service_get_explanations**
> ProxyExplanationsViewModel proxy_service_get_explanations()

Get Proxy Explanations

Get an explanation of the SSH proxy, SSH terminal, and RDP proxy features

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import proxy_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.proxy_explanations_view_model import ProxyExplanationsViewModel
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
    api_instance = proxy_api.ProxyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Proxy Explanations
        api_response = api_instance.proxy_service_get_explanations()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_get_explanations: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ProxyExplanationsViewModel**](ProxyExplanationsViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Explanations |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_service_get_proxying_state**
> ProxyingStateModel proxy_service_get_proxying_state()

Get proxy state

Get proxy state

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import proxy_api
from plugins.model.proxying_state_model import ProxyingStateModel
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
    api_instance = proxy_api.ProxyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get proxy state
        api_response = api_instance.proxy_service_get_proxying_state()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_get_proxying_state: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ProxyingStateModel**](ProxyingStateModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Proxy state |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_service_get_rdp_endpoint_notification**
> str proxy_service_get_rdp_endpoint_notification()

Get a notification of where the RDP proxy is running

Get a notification of where the RDP proxy is running

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import proxy_api
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
    api_instance = proxy_api.ProxyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get a notification of where the RDP proxy is running
        api_response = api_instance.proxy_service_get_rdp_endpoint_notification()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_get_rdp_endpoint_notification: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of nodes, sites, and engines with proxy configurations |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_service_get_rdp_proxy_configuration**
> RdpProxyConfigurationViewModel proxy_service_get_rdp_proxy_configuration()

Get the RDP proxy configuration

Get the RDP proxy configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import proxy_api
from plugins.model.rdp_proxy_configuration_view_model import RdpProxyConfigurationViewModel
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
    api_instance = proxy_api.ProxyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the RDP proxy configuration
        api_response = api_instance.proxy_service_get_rdp_proxy_configuration()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_get_rdp_proxy_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**RdpProxyConfigurationViewModel**](RdpProxyConfigurationViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RDP Proxy Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_service_get_ssh_endpoint_notification**
> str proxy_service_get_ssh_endpoint_notification()

Get a notification of where the SSH proxy is running

Get a notification of where the SSH proxy is running

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import proxy_api
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
    api_instance = proxy_api.ProxyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get a notification of where the SSH proxy is running
        api_response = api_instance.proxy_service_get_ssh_endpoint_notification()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_get_ssh_endpoint_notification: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of nodes, sites, and engines with proxy configurations |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_service_get_ssh_proxy_configuration**
> SshProxyConfigurationViewModel proxy_service_get_ssh_proxy_configuration()

Get the SSH proxy configuration

Get the SSH proxy configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import proxy_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.ssh_proxy_configuration_view_model import SshProxyConfigurationViewModel
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
    api_instance = proxy_api.ProxyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the SSH proxy configuration
        api_response = api_instance.proxy_service_get_ssh_proxy_configuration()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_get_ssh_proxy_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SshProxyConfigurationViewModel**](SshProxyConfigurationViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SSH Proxy Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_service_get_terminal_client_history**
> PagingOfProxyClientHistorySummaryAndSshProxyClientHistoryFilterQuery proxy_service_get_terminal_client_history()

Get SSH Terminal client history

Get SSH Terminal client history

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import proxy_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_proxy_client_history_summary_and_ssh_proxy_client_history_filter_query import PagingOfProxyClientHistorySummaryAndSshProxyClientHistoryFilterQuery
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
    api_instance = proxy_api.ProxyApi(api_client)
    filter_authenticate_result = "filter.authenticateResult_example" # str | AuthenticateResult (optional)
    filter_end_date = "filter.endDate_example" # str | EndDate (optional)
    filter_engine_identity_guid = "filter.engineIdentityGuid_example" # str | EngineIdentityGuid (optional)
    filter_ip_address = "filter.ipAddress_example" # str | IpAddress (optional)
    filter_start_date = "filter.startDate_example" # str | StartDate (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get SSH Terminal client history
        api_response = api_instance.proxy_service_get_terminal_client_history(filter_authenticate_result=filter_authenticate_result, filter_end_date=filter_end_date, filter_engine_identity_guid=filter_engine_identity_guid, filter_ip_address=filter_ip_address, filter_start_date=filter_start_date, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_get_terminal_client_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_authenticate_result** | **str**| AuthenticateResult | [optional]
 **filter_end_date** | **str**| EndDate | [optional]
 **filter_engine_identity_guid** | **str**| EngineIdentityGuid | [optional]
 **filter_ip_address** | **str**| IpAddress | [optional]
 **filter_start_date** | **str**| StartDate | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfProxyClientHistorySummaryAndSshProxyClientHistoryFilterQuery**](PagingOfProxyClientHistorySummaryAndSshProxyClientHistoryFilterQuery.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of SSH Terminal client history |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_service_get_terminal_client_overrides**
> [ProxyClientOverrideSummary] proxy_service_get_terminal_client_overrides()

Get SSH Terminal client overrides

Get SSH Terminal client overrides

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import proxy_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.proxy_client_override_summary import ProxyClientOverrideSummary
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
    api_instance = proxy_api.ProxyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get SSH Terminal client overrides
        api_response = api_instance.proxy_service_get_terminal_client_overrides()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_get_terminal_client_overrides: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[ProxyClientOverrideSummary]**](ProxyClientOverrideSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of SSH Terminal client overrides |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_service_get_terminal_clients**
> PagingOfProxyClientSummaryAndSshProxyClientsFilterQuery proxy_service_get_terminal_clients()

Get SSH Terminal clients

Get SSH Terminal clients

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import proxy_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.paging_of_proxy_client_summary_and_ssh_proxy_clients_filter_query import PagingOfProxyClientSummaryAndSshProxyClientsFilterQuery
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
    api_instance = proxy_api.ProxyApi(api_client)
    filter_ip_address = "filter.ipAddress_example" # str | IpAddress (optional)
    filter_terminal_client_type = "filter.terminalClientType_example" # str | TerminalClientType (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get SSH Terminal clients
        api_response = api_instance.proxy_service_get_terminal_clients(filter_ip_address=filter_ip_address, filter_terminal_client_type=filter_terminal_client_type, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_get_terminal_clients: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_ip_address** | **str**| IpAddress | [optional]
 **filter_terminal_client_type** | **str**| TerminalClientType | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfProxyClientSummaryAndSshProxyClientsFilterQuery**](PagingOfProxyClientSummaryAndSshProxyClientsFilterQuery.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of SSH Terminal clients |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_service_patch_engine**
> ProxyEndpointsViewModel proxy_service_patch_engine(id)

Update an engine proxy configuration

Update an engine proxy configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import proxy_api
from plugins.model.proxy_engine_view_model import ProxyEngineViewModel
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.proxy_endpoints_view_model import ProxyEndpointsViewModel
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
    api_instance = proxy_api.ProxyApi(api_client)
    id = 1 # int | id
    proxy_engine_view_model = ProxyEngineViewModel(
        bind_ip_address="bind_ip_address_example",
        engine_id=1,
        friendly_name="friendly_name_example",
        public_host="public_host_example",
        site_name="site_name_example",
    ) # ProxyEngineViewModel | engine (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an engine proxy configuration
        api_response = api_instance.proxy_service_patch_engine(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_patch_engine: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an engine proxy configuration
        api_response = api_instance.proxy_service_patch_engine(id, proxy_engine_view_model=proxy_engine_view_model)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_patch_engine: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id |
 **proxy_engine_view_model** | [**ProxyEngineViewModel**](ProxyEngineViewModel.md)| engine | [optional]

### Return type

[**ProxyEndpointsViewModel**](ProxyEndpointsViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of nodes, sites, and engines with proxy configurations |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_service_patch_node**
> ProxyEndpointsViewModel proxy_service_patch_node(id)

Update a node proxy configuration

Update a node proxy configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import proxy_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.proxy_node_view_model import ProxyNodeViewModel
from plugins.model.proxy_endpoints_view_model import ProxyEndpointsViewModel
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
    api_instance = proxy_api.ProxyApi(api_client)
    id = 1 # int | id
    proxy_node_view_model = ProxyNodeViewModel(
        bind_ip_address="bind_ip_address_example",
        jumpbox_available_port_range="jumpbox_available_port_range_example",
        machine_name="machine_name_example",
        node_id=1,
        public_host="public_host_example",
    ) # ProxyNodeViewModel | node (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a node proxy configuration
        api_response = api_instance.proxy_service_patch_node(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_patch_node: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a node proxy configuration
        api_response = api_instance.proxy_service_patch_node(id, proxy_node_view_model=proxy_node_view_model)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_patch_node: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id |
 **proxy_node_view_model** | [**ProxyNodeViewModel**](ProxyNodeViewModel.md)| node | [optional]

### Return type

[**ProxyEndpointsViewModel**](ProxyEndpointsViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of nodes, sites, and engines with proxy configurations |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_service_patch_rdp_proxy_configuration**
> RdpProxyConfigurationViewModel proxy_service_patch_rdp_proxy_configuration()

Update the RDP proxy configuration

Update the RDP proxy configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import proxy_api
from plugins.model.rdp_proxy_configuration_view_model import RdpProxyConfigurationViewModel
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
    api_instance = proxy_api.ProxyApi(api_client)
    rdp_proxy_configuration_view_model = RdpProxyConfigurationViewModel(
        allow_site_selection_for_active_directory_accounts=True,
        days_to_keep_operational_logs=1,
        enable_rdp_proxy=True,
        enable_remote_host_validation=True,
        is_cloud=True,
        proxy_new_secrets_by_default=True,
        rdp_proxy_port=1,
        rdp_server_certificate=RdpProxyCertificateViewModel(
            rdp_server_certificate=open('/path/to/file', 'rb'),
            rdp_server_certificate_file_name="rdp_server_certificate_file_name_example",
            rdp_server_certificate_password="rdp_server_certificate_password_example",
        ),
null,
        rdp_server_certificate_multipart_password="rdp_server_certificate_multipart_password_example",
    ) # RdpProxyConfigurationViewModel | viewModel (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the RDP proxy configuration
        api_response = api_instance.proxy_service_patch_rdp_proxy_configuration(rdp_proxy_configuration_view_model=rdp_proxy_configuration_view_model)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_patch_rdp_proxy_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rdp_proxy_configuration_view_model** | [**RdpProxyConfigurationViewModel**](RdpProxyConfigurationViewModel.md)| viewModel | [optional]

### Return type

[**RdpProxyConfigurationViewModel**](RdpProxyConfigurationViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RDP Proxy Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_service_patch_site**
> ProxyEndpointsViewModel proxy_service_patch_site(id)

Update a site proxy configuration

Update a site proxy configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import proxy_api
from plugins.model.proxy_site_view_model import ProxySiteViewModel
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.proxy_endpoints_view_model import ProxyEndpointsViewModel
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
    api_instance = proxy_api.ProxyApi(api_client)
    id = 1 # int | id
    proxy_site_view_model = ProxySiteViewModel(
        enable_rdp_proxy=True,
        enable_ssh_proxy=True,
        rdp_proxy_port=1,
        rdp_proxy_port_inherited=True,
        site_id=1,
        site_name="site_name_example",
        ssh_jumpbox_available_port_range="ssh_jumpbox_available_port_range_example",
        ssh_proxy_port=1,
        ssh_proxy_port_inherited=True,
    ) # ProxySiteViewModel | site (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a site proxy configuration
        api_response = api_instance.proxy_service_patch_site(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_patch_site: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a site proxy configuration
        api_response = api_instance.proxy_service_patch_site(id, proxy_site_view_model=proxy_site_view_model)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_patch_site: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id |
 **proxy_site_view_model** | [**ProxySiteViewModel**](ProxySiteViewModel.md)| site | [optional]

### Return type

[**ProxyEndpointsViewModel**](ProxyEndpointsViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of nodes, sites, and engines with proxy configurations |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_service_patch_ssh_proxy_configuration**
> SshProxyConfigurationViewModel proxy_service_patch_ssh_proxy_configuration()

Update the SSH proxy configuration

Update the SSH proxy configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import proxy_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.ssh_proxy_configuration_view_model import SshProxyConfigurationViewModel
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
    api_instance = proxy_api.ProxyApi(api_client)
    ssh_proxy_configuration_view_model = SshProxyConfigurationViewModel(
        available_port_range="available_port_range_example",
        days_to_keep_operational_logs=1,
        enable_password_hiding=True,
        enable_proxy_block_listing=True,
        enable_proxy_inactivity_timeout=True,
        enable_ssh_proxy=True,
        enable_ssh_public_key_auth=True,
        enable_ssh_terminal=True,
        enable_ssh_tunneling=True,
        enable_terminal_inactivity_timeout=True,
        enable_window_title_change_command=True,
        is_cloud=True,
        password_regex_filter="password_regex_filter_example",
        proxy_auto_block_listing_max_num=1,
        proxy_auto_block_listing_time_frame_minutes=1,
        proxy_inactivity_timeout_seconds=1,
        proxy_new_secrets_by_default=True,
        ssh_host_key="ssh_host_key_example",
        ssh_proxy_banner="ssh_proxy_banner_example",
        ssh_proxy_host_fingerprint="ssh_proxy_host_fingerprint_example",
        ssh_proxy_port=1,
        ssh_terminal_banner="ssh_terminal_banner_example",
        terminal_inactivity_timeout_seconds=1,
        tunnel_keep_alive_in_seconds=1,
    ) # SshProxyConfigurationViewModel | viewModel (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the SSH proxy configuration
        api_response = api_instance.proxy_service_patch_ssh_proxy_configuration(ssh_proxy_configuration_view_model=ssh_proxy_configuration_view_model)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_patch_ssh_proxy_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_proxy_configuration_view_model** | [**SshProxyConfigurationViewModel**](SshProxyConfigurationViewModel.md)| viewModel | [optional]

### Return type

[**SshProxyConfigurationViewModel**](SshProxyConfigurationViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SSH Proxy Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_service_update_terminal_client_overrides**
> ProxyClientOverrideSummary proxy_service_update_terminal_client_overrides(client_override_id)

Updates SSH Terminal client overrides

Updates SSH Terminal client overrides

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import proxy_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.proxy_client_override_summary import ProxyClientOverrideSummary
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
    api_instance = proxy_api.ProxyApi(api_client)
    client_override_id = 1 # int | clientOverrideId
    proxy_client_override_summary = ProxyClientOverrideSummary(
        client_override_id=1,
        ip_address_range="ip_address_range_example",
        terminal_client_type=ProxyClientType("{}"),
    ) # ProxyClientOverrideSummary | clientOverride (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates SSH Terminal client overrides
        api_response = api_instance.proxy_service_update_terminal_client_overrides(client_override_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_update_terminal_client_overrides: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates SSH Terminal client overrides
        api_response = api_instance.proxy_service_update_terminal_client_overrides(client_override_id, proxy_client_override_summary=proxy_client_override_summary)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_update_terminal_client_overrides: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_override_id** | **int**| clientOverrideId |
 **proxy_client_override_summary** | [**ProxyClientOverrideSummary**](ProxyClientOverrideSummary.md)| clientOverride | [optional]

### Return type

[**ProxyClientOverrideSummary**](ProxyClientOverrideSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of SSH Terminal client overrides |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_service_update_terminal_client_type**
> bool proxy_service_update_terminal_client_type(client_id)

Updates a SSH Terminal client type

Updates a SSH Terminal client type

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import proxy_api
from plugins.model.proxy_client_summary import ProxyClientSummary
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
    api_instance = proxy_api.ProxyApi(api_client)
    client_id = 1 # int | clientId
    proxy_client_summary = ProxyClientSummary(
        client_id=1,
        ip_address="ip_address_example",
        last_connection_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        terminal_client_type=ProxyClientType("{}"),
    ) # ProxyClientSummary | client (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates a SSH Terminal client type
        api_response = api_instance.proxy_service_update_terminal_client_type(client_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_update_terminal_client_type: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates a SSH Terminal client type
        api_response = api_instance.proxy_service_update_terminal_client_type(client_id, proxy_client_summary=proxy_client_summary)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_update_terminal_client_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| clientId |
 **proxy_client_summary** | [**ProxyClientSummary**](ProxyClientSummary.md)| client | [optional]

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
**200** | A list of SSH Terminal clients |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

