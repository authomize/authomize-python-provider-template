# plugins.DiscoveryApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**discovery_service_create_discovery_source**](DiscoveryApi.md#discovery_service_create_discovery_source) | **POST** /v1/discovery/source | Create a new discovery source
[**discovery_service_create_discovery_source_scanner_settings**](DiscoveryApi.md#discovery_service_create_discovery_source_scanner_settings) | **POST** /v1/discovery/source/{discoverySourceId}/scanner-settings | Create scanner setting
[**discovery_service_get_available_discovery_source_scanners**](DiscoveryApi.md#discovery_service_get_available_discovery_source_scanners) | **GET** /v1/discovery/source/{discoverySourceId}/available-scanners | Get Discovery Source Available Scanners
[**discovery_service_get_discovery_configuration**](DiscoveryApi.md#discovery_service_get_discovery_configuration) | **GET** /v1/discovery/configuration | Get Discovery Configuration
[**discovery_service_get_discovery_source**](DiscoveryApi.md#discovery_service_get_discovery_source) | **GET** /v1/discovery/source/{id} | Get discovery source
[**discovery_service_get_discovery_source_audits**](DiscoveryApi.md#discovery_service_get_discovery_source_audits) | **GET** /v1/discovery-source/audit | Get Discovery Source Audits
[**discovery_service_get_discovery_source_filter**](DiscoveryApi.md#discovery_service_get_discovery_source_filter) | **GET** /v1/discovery/source/{id}/filter | Get the source filter for a discovery source
[**discovery_service_get_discovery_source_stub**](DiscoveryApi.md#discovery_service_get_discovery_source_stub) | **GET** /v1/discovery/source/stub/{typeId} | Get a Discovery Source Stub
[**discovery_service_get_discovery_status**](DiscoveryApi.md#discovery_service_get_discovery_status) | **GET** /v1/discovery/status | Get Discovery Status
[**discovery_service_get_scan_types**](DiscoveryApi.md#discovery_service_get_scan_types) | **GET** /v1/discovery/scan-types | Get Discovery Scan Types
[**discovery_service_patch_discovery_source_filter**](DiscoveryApi.md#discovery_service_patch_discovery_source_filter) | **PATCH** /v1/discovery/source/{discoverySourceId}/filter/{memberId} | Patches discovery source filter
[**discovery_service_run_discovery_now**](DiscoveryApi.md#discovery_service_run_discovery_now) | **POST** /v1/discovery/run | Run a discovery command
[**discovery_service_search_discovery_source_scanner_settings**](DiscoveryApi.md#discovery_service_search_discovery_source_scanner_settings) | **GET** /v1/discovery/source/{discoverySourceId}/scanner-settings/search | Get Scanner Settings
[**discovery_service_search_discovery_sources**](DiscoveryApi.md#discovery_service_search_discovery_sources) | **GET** /v1/discovery/sources | Get discovery sources
[**discovery_service_search_for_domain_ou**](DiscoveryApi.md#discovery_service_search_for_domain_ou) | **GET** /v1/discovery/source/{discoverySourceId}/ou | Get and include or exclude for discovery
[**discovery_service_update_discovery_configuration**](DiscoveryApi.md#discovery_service_update_discovery_configuration) | **PATCH** /v1/discovery/configuration | Update discovery configuration
[**discovery_service_update_discovery_source**](DiscoveryApi.md#discovery_service_update_discovery_source) | **PATCH** /v1/discovery/source/{id} | Update a discovery source
[**discovery_service_update_discovery_source_filters**](DiscoveryApi.md#discovery_service_update_discovery_source_filters) | **PUT** /v1/discovery/source/{discoverySourceId}/filters | Updates discovery source filters


# **discovery_service_create_discovery_source**
> DiscoverySourceModel discovery_service_create_discovery_source()

Create a new discovery source

Creates a new discovery source

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import discovery_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.discovery_source_create_args import DiscoverySourceCreateArgs
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.discovery_source_model import DiscoverySourceModel
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
    api_instance = discovery_api.DiscoveryApi(api_client)
    discovery_source_create_args = DiscoverySourceCreateArgs(
        data=DiscoverySourceCreateModel(
            active=True,
            discover_specific_ous=True,
            discovery_scanner_id=None,
            discovery_source_settings=DiscoverySourceSettingsCreateModel(
                domain_type=DomainType("{}"),
                friendly_name=None,
                fully_qualified_domain_name=None,
                use_secure_ldap=True,
            ),
            last_discovery_run_date=None,
            machine_name_resolution_type=MachineNameResolutionType("{}"),
            name=None,
            secret_id=None,
            site_id=None,
        ),
    ) # DiscoverySourceCreateArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new discovery source
        api_response = api_instance.discovery_service_create_discovery_source(discovery_source_create_args=discovery_source_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DiscoveryApi->discovery_service_create_discovery_source: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **discovery_source_create_args** | [**DiscoverySourceCreateArgs**](DiscoverySourceCreateArgs.md)| args | [optional]

### Return type

[**DiscoverySourceModel**](DiscoverySourceModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new discovery source |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discovery_service_create_discovery_source_scanner_settings**
> DiscoveryScannerSettingViewModel discovery_service_create_discovery_source_scanner_settings(discovery_source_id)

Create scanner setting

Create a scanner setting on a discovery source

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import discovery_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.discovery_scanner_setting_view_model import DiscoveryScannerSettingViewModel
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.discovery_scanner_setting_create_args import DiscoveryScannerSettingCreateArgs
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
    api_instance = discovery_api.DiscoveryApi(api_client)
    discovery_source_id = None # bool, date, datetime, dict, float, int, list, str, none_type | discoverySourceId
    discovery_scanner_setting_create_args = DiscoveryScannerSettingCreateArgs(
        data=DiscoveryScannerSettingCreateData(
            discovery_scan_type_id=None,
        ),
    ) # DiscoveryScannerSettingCreateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create scanner setting
        api_response = api_instance.discovery_service_create_discovery_source_scanner_settings(discovery_source_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DiscoveryApi->discovery_service_create_discovery_source_scanner_settings: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create scanner setting
        api_response = api_instance.discovery_service_create_discovery_source_scanner_settings(discovery_source_id, discovery_scanner_setting_create_args=discovery_scanner_setting_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DiscoveryApi->discovery_service_create_discovery_source_scanner_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **discovery_source_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| discoverySourceId |
 **discovery_scanner_setting_create_args** | [**DiscoveryScannerSettingCreateArgs**](DiscoveryScannerSettingCreateArgs.md)| args | [optional]

### Return type

[**DiscoveryScannerSettingViewModel**](DiscoveryScannerSettingViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New scanner setting |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discovery_service_get_available_discovery_source_scanners**
> [DiscoveryScannerSettingTypeSummary] discovery_service_get_available_discovery_source_scanners(discovery_source_id)

Get Discovery Source Available Scanners

Get all of the scanners that can be created for this specific discovery source

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import discovery_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.discovery_scanner_setting_type_summary import DiscoveryScannerSettingTypeSummary
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
    api_instance = discovery_api.DiscoveryApi(api_client)
    discovery_source_id = None # bool, date, datetime, dict, float, int, list, str, none_type | discoverySourceId

    # example passing only required values which don't have defaults set
    try:
        # Get Discovery Source Available Scanners
        api_response = api_instance.discovery_service_get_available_discovery_source_scanners(discovery_source_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DiscoveryApi->discovery_service_get_available_discovery_source_scanners: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **discovery_source_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| discoverySourceId |

### Return type

[**[DiscoveryScannerSettingTypeSummary]**](DiscoveryScannerSettingTypeSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Discovery Scanner Types |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discovery_service_get_discovery_configuration**
> DiscoveryConfigurationModel discovery_service_get_discovery_configuration()

Get Discovery Configuration

Get Discovery Configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import discovery_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.discovery_configuration_model import DiscoveryConfigurationModel
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
    api_instance = discovery_api.DiscoveryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Discovery Configuration
        api_response = api_instance.discovery_service_get_discovery_configuration()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DiscoveryApi->discovery_service_get_discovery_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**DiscoveryConfigurationModel**](DiscoveryConfigurationModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Discovery Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discovery_service_get_discovery_source**
> DiscoverySourceModel discovery_service_get_discovery_source(id)

Get discovery source

Returns the discovery source

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import discovery_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.discovery_source_model import DiscoverySourceModel
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
    api_instance = discovery_api.DiscoveryApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Discovery Source ID

    # example passing only required values which don't have defaults set
    try:
        # Get discovery source
        api_response = api_instance.discovery_service_get_discovery_source(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DiscoveryApi->discovery_service_get_discovery_source: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Discovery Source ID |

### Return type

[**DiscoverySourceModel**](DiscoverySourceModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Discovery Source View |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discovery_service_get_discovery_source_audits**
> IPagingOfDiscoverySourceAuditModel discovery_service_get_discovery_source_audits()

Get Discovery Source Audits

Get Discovery Source Audits

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import discovery_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.i_paging_of_discovery_source_audit_model import IPagingOfDiscoverySourceAuditModel
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
    api_instance = discovery_api.DiscoveryApi(api_client)
    is_exporting = True # bool | isExporting (optional)
    filter_discovery_source_id = None # bool, date, datetime, dict, float, int, list, str, none_type | DiscoverySourceId (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Discovery Source Audits
        api_response = api_instance.discovery_service_get_discovery_source_audits(is_exporting=is_exporting, filter_discovery_source_id=filter_discovery_source_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DiscoveryApi->discovery_service_get_discovery_source_audits: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_exporting** | **bool**| isExporting | [optional]
 **filter_discovery_source_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| DiscoverySourceId | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**IPagingOfDiscoverySourceAuditModel**](IPagingOfDiscoverySourceAuditModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Discovery Source Audits |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discovery_service_get_discovery_source_filter**
> DomainDiscoveryScopeModel discovery_service_get_discovery_source_filter(id)

Get the source filter for a discovery source

Get the source filter for a discovery source

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import discovery_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.domain_discovery_scope_model import DomainDiscoveryScopeModel
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
    api_instance = discovery_api.DiscoveryApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id

    # example passing only required values which don't have defaults set
    try:
        # Get the source filter for a discovery source
        api_response = api_instance.discovery_service_get_discovery_source_filter(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DiscoveryApi->discovery_service_get_discovery_source_filter: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |

### Return type

[**DomainDiscoveryScopeModel**](DomainDiscoveryScopeModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The source filter for a discovery source |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discovery_service_get_discovery_source_stub**
> DiscoverySourceModel discovery_service_get_discovery_source_stub(type_id)

Get a Discovery Source Stub

Get a Discovery Source Stub

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import discovery_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.discovery_source_model import DiscoverySourceModel
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
    api_instance = discovery_api.DiscoveryApi(api_client)
    type_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Discovery Source Type ID

    # example passing only required values which don't have defaults set
    try:
        # Get a Discovery Source Stub
        api_response = api_instance.discovery_service_get_discovery_source_stub(type_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DiscoveryApi->discovery_service_get_discovery_source_stub: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Discovery Source Type ID |

### Return type

[**DiscoverySourceModel**](DiscoverySourceModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Discovery Source Stub |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discovery_service_get_discovery_status**
> DiscoveryStatusModel discovery_service_get_discovery_status()

Get Discovery Status

Get Discovery Status

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import discovery_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.discovery_status_model import DiscoveryStatusModel
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
    api_instance = discovery_api.DiscoveryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Discovery Status
        api_response = api_instance.discovery_service_get_discovery_status()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DiscoveryApi->discovery_service_get_discovery_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**DiscoveryStatusModel**](DiscoveryStatusModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Discovery Status |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discovery_service_get_scan_types**
> [DiscoveryScanTypeSummary] discovery_service_get_scan_types()

Get Discovery Scan Types

Get all of the scan types

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import discovery_api
from plugins.model.discovery_scan_type_summary import DiscoveryScanTypeSummary
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
    api_instance = discovery_api.DiscoveryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Discovery Scan Types
        api_response = api_instance.discovery_service_get_scan_types()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DiscoveryApi->discovery_service_get_scan_types: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[DiscoveryScanTypeSummary]**](DiscoveryScanTypeSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Discovery Scan Types |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discovery_service_patch_discovery_source_filter**
> DomainDiscoveryScopeFilterModel discovery_service_patch_discovery_source_filter(discovery_source_id, member_id)

Patches discovery source filter

Patches the properties on a single discovery source filter

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import discovery_api
from plugins.model.discovery_source_filter_patch_args import DiscoverySourceFilterPatchArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.domain_discovery_scope_filter_model import DomainDiscoveryScopeFilterModel
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
    api_instance = discovery_api.DiscoveryApi(api_client)
    discovery_source_id = None # bool, date, datetime, dict, float, int, list, str, none_type | discoverySourceId
    member_id = None # bool, date, datetime, dict, float, int, list, str, none_type | memberId
    discovery_source_filter_patch_args = DiscoverySourceFilterPatchArgs(
        data=DomainDiscoveryScopeFilterPatchModel(
            scan_target_type=UpdateFieldValueOfScanTargetType(
                dirty=True,
                value=ScanTargetType("{}"),
            ),
            secret_id=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=None,
            ),
            site_id=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=None,
            ),
        ),
    ) # DiscoverySourceFilterPatchArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Patches discovery source filter
        api_response = api_instance.discovery_service_patch_discovery_source_filter(discovery_source_id, member_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DiscoveryApi->discovery_service_patch_discovery_source_filter: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Patches discovery source filter
        api_response = api_instance.discovery_service_patch_discovery_source_filter(discovery_source_id, member_id, discovery_source_filter_patch_args=discovery_source_filter_patch_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DiscoveryApi->discovery_service_patch_discovery_source_filter: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **discovery_source_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| discoverySourceId |
 **member_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| memberId |
 **discovery_source_filter_patch_args** | [**DiscoverySourceFilterPatchArgs**](DiscoverySourceFilterPatchArgs.md)| args | [optional]

### Return type

[**DomainDiscoveryScopeFilterModel**](DomainDiscoveryScopeFilterModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | True |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discovery_service_run_discovery_now**
> bool discovery_service_run_discovery_now()

Run a discovery command

Run a discovery command

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import discovery_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.discovery_run_args import DiscoveryRunArgs
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
    api_instance = discovery_api.DiscoveryApi(api_client)
    discovery_run_args = DiscoveryRunArgs(
        data=DiscoveryRunModel(
            command_type=DiscoveryCommandType("Discovery"),
        ),
    ) # DiscoveryRunArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Run a discovery command
        api_response = api_instance.discovery_service_run_discovery_now(discovery_run_args=discovery_run_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DiscoveryApi->discovery_service_run_discovery_now: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **discovery_run_args** | [**DiscoveryRunArgs**](DiscoveryRunArgs.md)| args | [optional]

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
**200** | true to indicate the command was triggered |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discovery_service_search_discovery_source_scanner_settings**
> [DiscoveryScannerSettingSummaryModel] discovery_service_search_discovery_source_scanner_settings(discovery_source_id)

Get Scanner Settings

Get all of the scanner settings for a specific discovery source

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import discovery_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.discovery_scanner_setting_summary_model import DiscoveryScannerSettingSummaryModel
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
    api_instance = discovery_api.DiscoveryApi(api_client)
    discovery_source_id = None # bool, date, datetime, dict, float, int, list, str, none_type | discoverySourceId

    # example passing only required values which don't have defaults set
    try:
        # Get Scanner Settings
        api_response = api_instance.discovery_service_search_discovery_source_scanner_settings(discovery_source_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DiscoveryApi->discovery_service_search_discovery_source_scanner_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **discovery_source_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| discoverySourceId |

### Return type

[**[DiscoveryScannerSettingSummaryModel]**](DiscoveryScannerSettingSummaryModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Collection of scanner settings |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discovery_service_search_discovery_sources**
> PagingOfDiscoverySourceSummaryModel discovery_service_search_discovery_sources()

Get discovery sources

Returns discovery sources

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import discovery_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.paging_of_discovery_source_summary_model import PagingOfDiscoverySourceSummaryModel
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
    api_instance = discovery_api.DiscoveryApi(api_client)
    filter_discovery_source_name = None # bool, date, datetime, dict, float, int, list, str, none_type | DiscoverySourceName (optional)
    filter_discovery_source_type = None # bool, date, datetime, dict, float, int, list, str, none_type | DiscoverySourceType (optional)
    filter_include_active = True # bool | IncludeActive (optional)
    filter_include_inactive = True # bool | IncludeInactive (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get discovery sources
        api_response = api_instance.discovery_service_search_discovery_sources(filter_discovery_source_name=filter_discovery_source_name, filter_discovery_source_type=filter_discovery_source_type, filter_include_active=filter_include_active, filter_include_inactive=filter_include_inactive, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DiscoveryApi->discovery_service_search_discovery_sources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_discovery_source_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| DiscoverySourceName | [optional]
 **filter_discovery_source_type** | **bool, date, datetime, dict, float, int, list, str, none_type**| DiscoverySourceType | [optional]
 **filter_include_active** | **bool**| IncludeActive | [optional]
 **filter_include_inactive** | **bool**| IncludeInactive | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfDiscoverySourceSummaryModel**](PagingOfDiscoverySourceSummaryModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Discovery Source Views |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discovery_service_search_for_domain_ou**
> [OUModel] discovery_service_search_for_domain_ou(discovery_source_id)

Get and include or exclude for discovery

Returns the discovery source OU

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import discovery_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.ou_model import OUModel
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
    api_instance = discovery_api.DiscoveryApi(api_client)
    discovery_source_id = None # bool, date, datetime, dict, float, int, list, str, none_type | discoverySourceId
    include = True # bool | Only return items that can be included (optional)
    search_text = None # bool, date, datetime, dict, float, int, list, str, none_type | Search for OU items containing this text (optional)
    selected_ids = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | When include is false only include items within these exisitng IDs (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | The number of items to return (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get and include or exclude for discovery
        api_response = api_instance.discovery_service_search_for_domain_ou(discovery_source_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DiscoveryApi->discovery_service_search_for_domain_ou: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get and include or exclude for discovery
        api_response = api_instance.discovery_service_search_for_domain_ou(discovery_source_id, include=include, search_text=search_text, selected_ids=selected_ids, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DiscoveryApi->discovery_service_search_for_domain_ou: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **discovery_source_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| discoverySourceId |
 **include** | **bool**| Only return items that can be included | [optional]
 **search_text** | **bool, date, datetime, dict, float, int, list, str, none_type**| Search for OU items containing this text | [optional]
 **selected_ids** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| When include is false only include items within these exisitng IDs | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| The number of items to return | [optional]

### Return type

[**[OUModel]**](OUModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Discovery OU |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discovery_service_update_discovery_configuration**
> DiscoveryConfigurationModel discovery_service_update_discovery_configuration()

Update discovery configuration

Update discovery configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import discovery_api
from plugins.model.discovery_configuration_update_args import DiscoveryConfigurationUpdateArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.discovery_configuration_model import DiscoveryConfigurationModel
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
    api_instance = discovery_api.DiscoveryApi(api_client)
    discovery_configuration_update_args = DiscoveryConfigurationUpdateArgs(
        data=DiscoveryConfigurationUpdateModel(
            dependency_not_found_threshold=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            discovery_interval_days=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            discovery_interval_hours=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            discovery_scan_offset_hours=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            enable_discovery=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            engine_ad_discovery_batch_size=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            ignore_cluster_node_objects=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            max_log_age_days=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
        ),
    ) # DiscoveryConfigurationUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update discovery configuration
        api_response = api_instance.discovery_service_update_discovery_configuration(discovery_configuration_update_args=discovery_configuration_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DiscoveryApi->discovery_service_update_discovery_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **discovery_configuration_update_args** | [**DiscoveryConfigurationUpdateArgs**](DiscoveryConfigurationUpdateArgs.md)| args | [optional]

### Return type

[**DiscoveryConfigurationModel**](DiscoveryConfigurationModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated discovery configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discovery_service_update_discovery_source**
> DiscoverySourceModel discovery_service_update_discovery_source(id)

Update a discovery source

Update an existing discovery source using the existing discovery source ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import discovery_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.discovery_source_update_args import DiscoverySourceUpdateArgs
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.discovery_source_model import DiscoverySourceModel
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
    api_instance = discovery_api.DiscoveryApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Discovery Source ID
    discovery_source_update_args = DiscoverySourceUpdateArgs(
        data=DiscoverySourceUpdateModel(
            active=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            days_to_keep_machines=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            discover_specific_ous=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            discovery_source_settings=UpdateFieldValueOfDiscoverySourceSettingsUpdateModel(
                dirty=True,
                value=DiscoverySourceSettingsUpdateModel(
                    friendly_name=UpdateFieldValueOfString(
                        dirty=True,
                        value=None,
                    ),
                    fully_qualified_domain_name=UpdateFieldValueOfString(
                        dirty=True,
                        value=None,
                    ),
                    use_secure_ldap=UpdateFieldValueOfBoolean(
                        dirty=True,
                        value=True,
                    ),
                ),
            ),
            machine_name_resolution_type=UpdateFieldValueOfMachineNameResolutionType(
                dirty=True,
                value=MachineNameResolutionType("{}"),
            ),
            name=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            secret_id=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=None,
            ),
            site_id=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
        ),
    ) # DiscoverySourceUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a discovery source
        api_response = api_instance.discovery_service_update_discovery_source(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DiscoveryApi->discovery_service_update_discovery_source: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a discovery source
        api_response = api_instance.discovery_service_update_discovery_source(id, discovery_source_update_args=discovery_source_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DiscoveryApi->discovery_service_update_discovery_source: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Discovery Source ID |
 **discovery_source_update_args** | [**DiscoverySourceUpdateArgs**](DiscoverySourceUpdateArgs.md)| args | [optional]

### Return type

[**DiscoverySourceModel**](DiscoverySourceModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated discovery source |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discovery_service_update_discovery_source_filters**
> DomainDiscoveryScopeModel discovery_service_update_discovery_source_filters(discovery_source_id)

Updates discovery source filters

Updates the full collection of discovery source filters for a discovery source

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import discovery_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.domain_discovery_scope_model import DomainDiscoveryScopeModel
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.discovery_source_filters_update_args import DiscoverySourceFiltersUpdateArgs
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
    api_instance = discovery_api.DiscoveryApi(api_client)
    discovery_source_id = None # bool, date, datetime, dict, float, int, list, str, none_type | discoverySourceId
    discovery_source_filters_update_args = DiscoverySourceFiltersUpdateArgs(
        data=DiscoverySourceFiltersUpdateModel(
            filters=[
                DomainDiscoveryScopeFilterUpdateModel(
                    discovery_filter_id=None,
                    filter_type=DiscoveryFilterType("{}"),
                    guid=None,
                    scan_target_type=ScanTargetType("{}"),
                    secret_id=None,
                    site_id=None,
                ),
            ],
        ),
    ) # DiscoverySourceFiltersUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates discovery source filters
        api_response = api_instance.discovery_service_update_discovery_source_filters(discovery_source_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DiscoveryApi->discovery_service_update_discovery_source_filters: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates discovery source filters
        api_response = api_instance.discovery_service_update_discovery_source_filters(discovery_source_id, discovery_source_filters_update_args=discovery_source_filters_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DiscoveryApi->discovery_service_update_discovery_source_filters: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **discovery_source_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| discoverySourceId |
 **discovery_source_filters_update_args** | [**DiscoverySourceFiltersUpdateArgs**](DiscoverySourceFiltersUpdateArgs.md)| args | [optional]

### Return type

[**DomainDiscoveryScopeModel**](DomainDiscoveryScopeModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The source filter for a discovery source |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

