# secret_server_openapiclient.ProxyApi

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
import secret_server_openapiclient
from secret_server_openapiclient.api import proxy_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.proxy_client_override_summary import ProxyClientOverrideSummary
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
    api_instance = proxy_api.ProxyApi(api_client)
    proxy_client_override_summary = ProxyClientOverrideSummary(
        client_override_id=None,
        ip_address_range=None,
        terminal_client_type=ProxyClientType("{}"),
    ) # ProxyClientOverrideSummary | clientOverride (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates SSH Terminal client overrides
        api_response = api_instance.proxy_service_create_terminal_client_overrides(proxy_client_override_summary=proxy_client_override_summary)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
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
import secret_server_openapiclient
from secret_server_openapiclient.api import proxy_api
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
    api_instance = proxy_api.ProxyApi(api_client)
    client_override_id = None # bool, date, datetime, dict, float, int, list, str, none_type | clientOverrideId

    # example passing only required values which don't have defaults set
    try:
        # Deletes SSH Terminal client overrides
        api_response = api_instance.proxy_service_delete_terminal_client_overrides(client_override_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_delete_terminal_client_overrides: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_override_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| clientOverrideId |

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
import secret_server_openapiclient
from secret_server_openapiclient.api import proxy_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.rdp_proxy_configuration_view_model import RdpProxyConfigurationViewModel
from secret_server_openapiclient.model.generate_rdp_certificate_args import GenerateRdpCertificateArgs
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
    api_instance = proxy_api.ProxyApi(api_client)
    generate_rdp_certificate_args = GenerateRdpCertificateArgs(
        dns_name=None,
    ) # GenerateRdpCertificateArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generate RDP server certificate
        api_response = api_instance.proxy_service_generate_rdp_proxy_certificate(generate_rdp_certificate_args=generate_rdp_certificate_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
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
import secret_server_openapiclient
from secret_server_openapiclient.api import proxy_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.ssh_proxy_configuration_view_model import SshProxyConfigurationViewModel
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
    api_instance = proxy_api.ProxyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Generate SSH Host Key
        api_response = api_instance.proxy_service_generate_ssh_host_key()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
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
import secret_server_openapiclient
from secret_server_openapiclient.api import proxy_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.paging_of_proxy_audit_model import PagingOfProxyAuditModel
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
    api_instance = proxy_api.ProxyApi(api_client)
    is_exporting = True # bool | isExporting (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the Proxy Audit List
        api_response = api_instance.proxy_service_get_audits(is_exporting=is_exporting, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_get_audits: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_exporting** | **bool**| isExporting | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

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
> bool, date, datetime, dict, float, int, list, str, none_type proxy_service_get_endpoint_notification()

Get endpoint warnings

Get endpoint warnings

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import proxy_api
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
    api_instance = proxy_api.ProxyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get endpoint warnings
        api_response = api_instance.proxy_service_get_endpoint_notification()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_get_endpoint_notification: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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
import secret_server_openapiclient
from secret_server_openapiclient.api import proxy_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.proxy_endpoints_view_model import ProxyEndpointsViewModel
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
    api_instance = proxy_api.ProxyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the proxy endpoints list
        api_response = api_instance.proxy_service_get_endpoints()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
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
import secret_server_openapiclient
from secret_server_openapiclient.api import proxy_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.proxy_explanations_view_model import ProxyExplanationsViewModel
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
    api_instance = proxy_api.ProxyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Proxy Explanations
        api_response = api_instance.proxy_service_get_explanations()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
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
import secret_server_openapiclient
from secret_server_openapiclient.api import proxy_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.proxying_state_model import ProxyingStateModel
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
    api_instance = proxy_api.ProxyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get proxy state
        api_response = api_instance.proxy_service_get_proxying_state()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
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
> bool, date, datetime, dict, float, int, list, str, none_type proxy_service_get_rdp_endpoint_notification()

Get a notification of where the RDP proxy is running

Get a notification of where the RDP proxy is running

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import proxy_api
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
    api_instance = proxy_api.ProxyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get a notification of where the RDP proxy is running
        api_response = api_instance.proxy_service_get_rdp_endpoint_notification()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_get_rdp_endpoint_notification: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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
import secret_server_openapiclient
from secret_server_openapiclient.api import proxy_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.rdp_proxy_configuration_view_model import RdpProxyConfigurationViewModel
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
    api_instance = proxy_api.ProxyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the RDP proxy configuration
        api_response = api_instance.proxy_service_get_rdp_proxy_configuration()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
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
> bool, date, datetime, dict, float, int, list, str, none_type proxy_service_get_ssh_endpoint_notification()

Get a notification of where the SSH proxy is running

Get a notification of where the SSH proxy is running

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import proxy_api
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
    api_instance = proxy_api.ProxyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get a notification of where the SSH proxy is running
        api_response = api_instance.proxy_service_get_ssh_endpoint_notification()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_get_ssh_endpoint_notification: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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
import secret_server_openapiclient
from secret_server_openapiclient.api import proxy_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.ssh_proxy_configuration_view_model import SshProxyConfigurationViewModel
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
    api_instance = proxy_api.ProxyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the SSH proxy configuration
        api_response = api_instance.proxy_service_get_ssh_proxy_configuration()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
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
import secret_server_openapiclient
from secret_server_openapiclient.api import proxy_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.paging_of_proxy_client_history_summary_and_ssh_proxy_client_history_filter_query import PagingOfProxyClientHistorySummaryAndSshProxyClientHistoryFilterQuery
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
    api_instance = proxy_api.ProxyApi(api_client)
    filter_authenticate_result = None # bool, date, datetime, dict, float, int, list, str, none_type | AuthenticateResult (optional)
    filter_end_date = None # bool, date, datetime, dict, float, int, list, str, none_type | EndDate (optional)
    filter_engine_identity_guid = None # bool, date, datetime, dict, float, int, list, str, none_type | EngineIdentityGuid (optional)
    filter_ip_address = None # bool, date, datetime, dict, float, int, list, str, none_type | IpAddress (optional)
    filter_start_date = None # bool, date, datetime, dict, float, int, list, str, none_type | StartDate (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get SSH Terminal client history
        api_response = api_instance.proxy_service_get_terminal_client_history(filter_authenticate_result=filter_authenticate_result, filter_end_date=filter_end_date, filter_engine_identity_guid=filter_engine_identity_guid, filter_ip_address=filter_ip_address, filter_start_date=filter_start_date, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_get_terminal_client_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_authenticate_result** | **bool, date, datetime, dict, float, int, list, str, none_type**| AuthenticateResult | [optional]
 **filter_end_date** | **bool, date, datetime, dict, float, int, list, str, none_type**| EndDate | [optional]
 **filter_engine_identity_guid** | **bool, date, datetime, dict, float, int, list, str, none_type**| EngineIdentityGuid | [optional]
 **filter_ip_address** | **bool, date, datetime, dict, float, int, list, str, none_type**| IpAddress | [optional]
 **filter_start_date** | **bool, date, datetime, dict, float, int, list, str, none_type**| StartDate | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

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
import secret_server_openapiclient
from secret_server_openapiclient.api import proxy_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.proxy_client_override_summary import ProxyClientOverrideSummary
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
    api_instance = proxy_api.ProxyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get SSH Terminal client overrides
        api_response = api_instance.proxy_service_get_terminal_client_overrides()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
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
import secret_server_openapiclient
from secret_server_openapiclient.api import proxy_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.paging_of_proxy_client_summary_and_ssh_proxy_clients_filter_query import PagingOfProxyClientSummaryAndSshProxyClientsFilterQuery
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
    api_instance = proxy_api.ProxyApi(api_client)
    filter_ip_address = None # bool, date, datetime, dict, float, int, list, str, none_type | IpAddress (optional)
    filter_terminal_client_type = None # bool, date, datetime, dict, float, int, list, str, none_type | TerminalClientType (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get SSH Terminal clients
        api_response = api_instance.proxy_service_get_terminal_clients(filter_ip_address=filter_ip_address, filter_terminal_client_type=filter_terminal_client_type, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_get_terminal_clients: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_ip_address** | **bool, date, datetime, dict, float, int, list, str, none_type**| IpAddress | [optional]
 **filter_terminal_client_type** | **bool, date, datetime, dict, float, int, list, str, none_type**| TerminalClientType | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

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
import secret_server_openapiclient
from secret_server_openapiclient.api import proxy_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.proxy_endpoints_view_model import ProxyEndpointsViewModel
from secret_server_openapiclient.model.proxy_engine_view_model import ProxyEngineViewModel
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
    api_instance = proxy_api.ProxyApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    proxy_engine_view_model = ProxyEngineViewModel(
        bind_ip_address=None,
        engine_id=None,
        friendly_name=None,
        public_host=None,
        site_name=None,
    ) # ProxyEngineViewModel | engine (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an engine proxy configuration
        api_response = api_instance.proxy_service_patch_engine(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_patch_engine: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an engine proxy configuration
        api_response = api_instance.proxy_service_patch_engine(id, proxy_engine_view_model=proxy_engine_view_model)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_patch_engine: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
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
import secret_server_openapiclient
from secret_server_openapiclient.api import proxy_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.proxy_endpoints_view_model import ProxyEndpointsViewModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.proxy_node_view_model import ProxyNodeViewModel
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
    api_instance = proxy_api.ProxyApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    proxy_node_view_model = ProxyNodeViewModel(
        bind_ip_address=None,
        jumpbox_available_port_range=None,
        machine_name=None,
        node_id=None,
        public_host=None,
    ) # ProxyNodeViewModel | node (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a node proxy configuration
        api_response = api_instance.proxy_service_patch_node(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_patch_node: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a node proxy configuration
        api_response = api_instance.proxy_service_patch_node(id, proxy_node_view_model=proxy_node_view_model)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_patch_node: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
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
import secret_server_openapiclient
from secret_server_openapiclient.api import proxy_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.rdp_proxy_configuration_view_model import RdpProxyConfigurationViewModel
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
    api_instance = proxy_api.ProxyApi(api_client)
    rdp_proxy_configuration_view_model = RdpProxyConfigurationViewModel(
        allow_site_selection_for_active_directory_accounts=True,
        days_to_keep_operational_logs=None,
        enable_rdp_proxy=True,
        enable_remote_host_validation=True,
        is_cloud=True,
        proxy_new_secrets_by_default=True,
        rdp_proxy_port=None,
        rdp_server_certificate=RdpProxyCertificateViewModel(
            rdp_server_certificate=None,
            rdp_server_certificate_file_name=None,
            rdp_server_certificate_password=None,
        ),
null,
        rdp_server_certificate_multipart_password=None,
    ) # RdpProxyConfigurationViewModel | viewModel (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the RDP proxy configuration
        api_response = api_instance.proxy_service_patch_rdp_proxy_configuration(rdp_proxy_configuration_view_model=rdp_proxy_configuration_view_model)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
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
import secret_server_openapiclient
from secret_server_openapiclient.api import proxy_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.proxy_endpoints_view_model import ProxyEndpointsViewModel
from secret_server_openapiclient.model.proxy_site_view_model import ProxySiteViewModel
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
    api_instance = proxy_api.ProxyApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    proxy_site_view_model = ProxySiteViewModel(
        enable_rdp_proxy=True,
        enable_ssh_proxy=True,
        rdp_proxy_port=None,
        rdp_proxy_port_inherited=True,
        site_id=None,
        site_name=None,
        ssh_jumpbox_available_port_range=None,
        ssh_proxy_port=None,
        ssh_proxy_port_inherited=True,
    ) # ProxySiteViewModel | site (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a site proxy configuration
        api_response = api_instance.proxy_service_patch_site(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_patch_site: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a site proxy configuration
        api_response = api_instance.proxy_service_patch_site(id, proxy_site_view_model=proxy_site_view_model)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_patch_site: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
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
import secret_server_openapiclient
from secret_server_openapiclient.api import proxy_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.ssh_proxy_configuration_view_model import SshProxyConfigurationViewModel
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
    api_instance = proxy_api.ProxyApi(api_client)
    ssh_proxy_configuration_view_model = SshProxyConfigurationViewModel(
        available_port_range=None,
        days_to_keep_operational_logs=None,
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
        password_regex_filter=None,
        proxy_auto_block_listing_max_num=None,
        proxy_auto_block_listing_time_frame_minutes=None,
        proxy_inactivity_timeout_seconds=None,
        proxy_new_secrets_by_default=True,
        ssh_host_key=None,
        ssh_proxy_banner=None,
        ssh_proxy_host_fingerprint=None,
        ssh_proxy_port=None,
        ssh_terminal_banner=None,
        terminal_inactivity_timeout_seconds=None,
        tunnel_keep_alive_in_seconds=None,
    ) # SshProxyConfigurationViewModel | viewModel (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the SSH proxy configuration
        api_response = api_instance.proxy_service_patch_ssh_proxy_configuration(ssh_proxy_configuration_view_model=ssh_proxy_configuration_view_model)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
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
import secret_server_openapiclient
from secret_server_openapiclient.api import proxy_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.proxy_client_override_summary import ProxyClientOverrideSummary
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
    api_instance = proxy_api.ProxyApi(api_client)
    client_override_id = None # bool, date, datetime, dict, float, int, list, str, none_type | clientOverrideId
    proxy_client_override_summary = ProxyClientOverrideSummary(
        client_override_id=None,
        ip_address_range=None,
        terminal_client_type=ProxyClientType("{}"),
    ) # ProxyClientOverrideSummary | clientOverride (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates SSH Terminal client overrides
        api_response = api_instance.proxy_service_update_terminal_client_overrides(client_override_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_update_terminal_client_overrides: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates SSH Terminal client overrides
        api_response = api_instance.proxy_service_update_terminal_client_overrides(client_override_id, proxy_client_override_summary=proxy_client_override_summary)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_update_terminal_client_overrides: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_override_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| clientOverrideId |
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
import secret_server_openapiclient
from secret_server_openapiclient.api import proxy_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.proxy_client_summary import ProxyClientSummary
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
    api_instance = proxy_api.ProxyApi(api_client)
    client_id = None # bool, date, datetime, dict, float, int, list, str, none_type | clientId
    proxy_client_summary = ProxyClientSummary(
        client_id=None,
        ip_address=None,
        last_connection_date=None,
        terminal_client_type=ProxyClientType("{}"),
    ) # ProxyClientSummary | client (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates a SSH Terminal client type
        api_response = api_instance.proxy_service_update_terminal_client_type(client_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_update_terminal_client_type: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates a SSH Terminal client type
        api_response = api_instance.proxy_service_update_terminal_client_type(client_id, proxy_client_summary=proxy_client_summary)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ProxyApi->proxy_service_update_terminal_client_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| clientId |
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

