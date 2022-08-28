# plugins.DistributedEngineApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**distributed_engine_service_create_site**](DistributedEngineApi.md#distributed_engine_service_create_site) | **POST** /v1/distributed-engine/site | Create Site
[**distributed_engine_service_create_site_connector**](DistributedEngineApi.md#distributed_engine_service_create_site_connector) | **POST** /v1/distributed-engine/site-connector | Create Site Connector
[**distributed_engine_service_download_distributed_engine**](DistributedEngineApi.md#distributed_engine_service_download_distributed_engine) | **GET** /v1/distributed-engine/download-distributed-engine | Download Distributed Engine
[**distributed_engine_service_download_memory_mq**](DistributedEngineApi.md#distributed_engine_service_download_memory_mq) | **GET** /v1/distributed-engine/site-connector/{id}/download-memorymq | Download Memory MQ
[**distributed_engine_service_get_distributed_engine_configuration**](DistributedEngineApi.md#distributed_engine_service_get_distributed_engine_configuration) | **GET** /v1/distributed-engine/configuration | Distributed Engine Configuration
[**distributed_engine_service_get_engine_audits_for_site**](DistributedEngineApi.md#distributed_engine_service_get_engine_audits_for_site) | **GET** /v1/distributed-engine/site/{siteId}/engine-audits | Get Engine Audits for Site
[**distributed_engine_service_get_engine_settings**](DistributedEngineApi.md#distributed_engine_service_get_engine_settings) | **GET** /v1/distributed-engine/engine-settings/{engineId} | Get Engine Settings
[**distributed_engine_service_get_engine_settings_for_site**](DistributedEngineApi.md#distributed_engine_service_get_engine_settings_for_site) | **GET** /v1/distributed-engine/engine-settings/site/{siteId} | Get Default Engine Settings for Site
[**distributed_engine_service_get_server_capabilities**](DistributedEngineApi.md#distributed_engine_service_get_server_capabilities) | **GET** /v1/distributed-engine/{id}/server-capabilities | Get Server Capabilities
[**distributed_engine_service_get_site**](DistributedEngineApi.md#distributed_engine_service_get_site) | **GET** /v1/distributed-engine/site/{id} | Get Site
[**distributed_engine_service_get_site_audits**](DistributedEngineApi.md#distributed_engine_service_get_site_audits) | **GET** /v1/distributed-engine/site/{id}/audit | GetSiteAudits
[**distributed_engine_service_get_site_connector**](DistributedEngineApi.md#distributed_engine_service_get_site_connector) | **GET** /v1/distributed-engine/site-connector/{id} | Get Site Connector
[**distributed_engine_service_get_site_connector_credentials**](DistributedEngineApi.md#distributed_engine_service_get_site_connector_credentials) | **GET** /v1/distributed-engine/site-connector/{siteConnectorId}/credentials | Get Site Connector Credentials
[**distributed_engine_service_get_site_connector_stub**](DistributedEngineApi.md#distributed_engine_service_get_site_connector_stub) | **GET** /v1/distributed-engine/site-connector/stub | Get Site Connector Stub
[**distributed_engine_service_get_site_stub**](DistributedEngineApi.md#distributed_engine_service_get_site_stub) | **GET** /v1/distributed-engine/site/stub | Get Site Stub
[**distributed_engine_service_patch_distributed_engine_configuration**](DistributedEngineApi.md#distributed_engine_service_patch_distributed_engine_configuration) | **PATCH** /v1/distributed-engine/configuration | Update Distributed Engine Configuration
[**distributed_engine_service_patch_engine_settings**](DistributedEngineApi.md#distributed_engine_service_patch_engine_settings) | **PATCH** /v1/distributed-engine/engine-settings/{engineSettingsId} | Patch Engine Settings
[**distributed_engine_service_patch_engine_settings_for_engine**](DistributedEngineApi.md#distributed_engine_service_patch_engine_settings_for_engine) | **PATCH** /v1/distributed-engine/engine-settings/engine/{engineId} | Patch Engine Settings For Engine
[**distributed_engine_service_patch_site**](DistributedEngineApi.md#distributed_engine_service_patch_site) | **PATCH** /v1/distributed-engine/site/{id} | Patch Site
[**distributed_engine_service_reassign_secrets**](DistributedEngineApi.md#distributed_engine_service_reassign_secrets) | **POST** /v1/distributed-engine/site/{id}/reassign | Reassign Secrets From the Site
[**distributed_engine_service_search_engines**](DistributedEngineApi.md#distributed_engine_service_search_engines) | **GET** /v1/distributed-engine/engines | Search Engines
[**distributed_engine_service_search_site_connectors**](DistributedEngineApi.md#distributed_engine_service_search_site_connectors) | **GET** /v1/distributed-engine/site-connectors | Search Site Connectors
[**distributed_engine_service_search_site_logs**](DistributedEngineApi.md#distributed_engine_service_search_site_logs) | **GET** /v1/distributed-engine/site/{id}/logs | SearchSiteLogs
[**distributed_engine_service_search_sites**](DistributedEngineApi.md#distributed_engine_service_search_sites) | **GET** /v1/distributed-engine/sites | Search Sites
[**distributed_engine_service_update_engine_status**](DistributedEngineApi.md#distributed_engine_service_update_engine_status) | **POST** /v1/distributed-engine/update-engine-status | Activate Engine
[**distributed_engine_service_update_site_connector**](DistributedEngineApi.md#distributed_engine_service_update_site_connector) | **PATCH** /v1/distributed-engine/site-connector/{id} | Update Site Connector
[**distributed_engine_service_validate_site_connectivity**](DistributedEngineApi.md#distributed_engine_service_validate_site_connectivity) | **POST** /v1/distributed-engine/site/{siteId}/validate-connectivity | Validate Site Connectivity
[**distributed_engine_service_validate_site_connector**](DistributedEngineApi.md#distributed_engine_service_validate_site_connector) | **POST** /v1/distributed-engine/site-connector/{siteConnectorId}/validate | Validate Site Connector


# **distributed_engine_service_create_site**
> SiteBasicModel distributed_engine_service_create_site()

Create Site

Create Site and returns model

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import distributed_engine_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.site_basic_model import SiteBasicModel
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.site_create_args import SiteCreateArgs
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
    api_instance = distributed_engine_api.DistributedEngineApi(api_client)
    site_create_args = SiteCreateArgs(
        data=SiteCreateModel(
            active=True,
            enable_cred_ssp_for_win_rm=True,
            enable_rdp_proxy=True,
            enable_ssh_proxy=True,
            heartbeat_interval=1,
            powershell_secret_id=1,
            rdp_proxy_port=1,
            site_connector_id=1,
            site_name="site_name_example",
            ssh_proxy_port=1,
            win_rm_end_point_url="win_rm_end_point_url_example",
        ),
    ) # SiteCreateArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Site
        api_response = api_instance.distributed_engine_service_create_site(site_create_args=site_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_create_site: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_create_args** | [**SiteCreateArgs**](SiteCreateArgs.md)| args | [optional]

### Return type

[**SiteBasicModel**](SiteBasicModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Site object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_engine_service_create_site_connector**
> SiteConnectorViewModel distributed_engine_service_create_site_connector()

Create Site Connector

Create Site Connector and returns model

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import distributed_engine_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.site_connector_view_model import SiteConnectorViewModel
from plugins.model.site_connector_create_args import SiteConnectorCreateArgs
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
    api_instance = distributed_engine_api.DistributedEngineApi(api_client)
    site_connector_create_args = SiteConnectorCreateArgs(
        data=SiteConnectorCreateModel(
            active=True,
            host_name="host_name_example",
            port=1,
            queue_type=MessageQueueType("{}"),
            shared_access_key_name="shared_access_key_name_example",
            shared_access_key_value="shared_access_key_value_example",
            site_connector_name="site_connector_name_example",
            ssl_certificate_thumbprint="ssl_certificate_thumbprint_example",
            use_ssl=True,
        ),
    ) # SiteConnectorCreateArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Site Connector
        api_response = api_instance.distributed_engine_service_create_site_connector(site_connector_create_args=site_connector_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_create_site_connector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_connector_create_args** | [**SiteConnectorCreateArgs**](SiteConnectorCreateArgs.md)| args | [optional]

### Return type

[**SiteConnectorViewModel**](SiteConnectorViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Site Connector object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_engine_service_download_distributed_engine**
> FileStream distributed_engine_service_download_distributed_engine()

Download Distributed Engine

Downloads Distributed Engine

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import distributed_engine_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.file_stream import FileStream
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
    api_instance = distributed_engine_api.DistributedEngineApi(api_client)
    is64_bit = True # bool | is64Bit (optional)
    site_id = 1 # int | siteId (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Download Distributed Engine
        api_response = api_instance.distributed_engine_service_download_distributed_engine(is64_bit=is64_bit, site_id=site_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_download_distributed_engine: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is64_bit** | **bool**| is64Bit | [optional]
 **site_id** | **int**| siteId | [optional]

### Return type

[**FileStream**](FileStream.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DistributedEngine File Download |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_engine_service_download_memory_mq**
> FileStream distributed_engine_service_download_memory_mq(id)

Download Memory MQ

Downloads MemoryMQ

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import distributed_engine_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.file_stream import FileStream
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
    api_instance = distributed_engine_api.DistributedEngineApi(api_client)
    id = 1 # int | id

    # example passing only required values which don't have defaults set
    try:
        # Download Memory MQ
        api_response = api_instance.distributed_engine_service_download_memory_mq(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_download_memory_mq: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id |

### Return type

[**FileStream**](FileStream.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MemoryMQ File Download |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_engine_service_get_distributed_engine_configuration**
> DistributedEngineConfigurationModel distributed_engine_service_get_distributed_engine_configuration()

Distributed Engine Configuration

Retrieve the current settings for Distributed Engine configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import distributed_engine_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.distributed_engine_configuration_model import DistributedEngineConfigurationModel
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
    api_instance = distributed_engine_api.DistributedEngineApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Distributed Engine Configuration
        api_response = api_instance.distributed_engine_service_get_distributed_engine_configuration()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_get_distributed_engine_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**DistributedEngineConfigurationModel**](DistributedEngineConfigurationModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Distributed Engines Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_engine_service_get_engine_audits_for_site**
> PagingOfEngineAuditSummary distributed_engine_service_get_engine_audits_for_site(site_id)

Get Engine Audits for Site

Get Engine Audits having passed in Site Id

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import distributed_engine_api
from plugins.model.paging_of_engine_audit_summary import PagingOfEngineAuditSummary
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
    api_instance = distributed_engine_api.DistributedEngineApi(api_client)
    site_id = 1 # int | siteId
    is_exporting = True # bool | isExporting (optional)
    filter_engine_id = 1 # int | EngineId (optional)
    filter_search_term = "filter.searchTerm_example" # str | SearchTerm (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Engine Audits for Site
        api_response = api_instance.distributed_engine_service_get_engine_audits_for_site(site_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_get_engine_audits_for_site: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Engine Audits for Site
        api_response = api_instance.distributed_engine_service_get_engine_audits_for_site(site_id, is_exporting=is_exporting, filter_engine_id=filter_engine_id, filter_search_term=filter_search_term, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_get_engine_audits_for_site: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| siteId |
 **is_exporting** | **bool**| isExporting | [optional]
 **filter_engine_id** | **int**| EngineId | [optional]
 **filter_search_term** | **str**| SearchTerm | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfEngineAuditSummary**](PagingOfEngineAuditSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Engine Audit Summary object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_engine_service_get_engine_settings**
> EngineSettingsModel distributed_engine_service_get_engine_settings(engine_id)

Get Engine Settings

Get Engine Settings object having passed in Engine Id

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import distributed_engine_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.engine_settings_model import EngineSettingsModel
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
    api_instance = distributed_engine_api.DistributedEngineApi(api_client)
    engine_id = 1 # int | engineId

    # example passing only required values which don't have defaults set
    try:
        # Get Engine Settings
        api_response = api_instance.distributed_engine_service_get_engine_settings(engine_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_get_engine_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_id** | **int**| engineId |

### Return type

[**EngineSettingsModel**](EngineSettingsModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Engine Settings object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_engine_service_get_engine_settings_for_site**
> EngineSettingsModel distributed_engine_service_get_engine_settings_for_site(site_id)

Get Default Engine Settings for Site

Get Default Engine Settings object having passed in Site Id

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import distributed_engine_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.engine_settings_model import EngineSettingsModel
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
    api_instance = distributed_engine_api.DistributedEngineApi(api_client)
    site_id = 1 # int | siteId

    # example passing only required values which don't have defaults set
    try:
        # Get Default Engine Settings for Site
        api_response = api_instance.distributed_engine_service_get_engine_settings_for_site(site_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_get_engine_settings_for_site: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| siteId |

### Return type

[**EngineSettingsModel**](EngineSettingsModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Engine Settings object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_engine_service_get_server_capabilities**
> [EngineServerCapabilitiesSummary] distributed_engine_service_get_server_capabilities(id)

Get Server Capabilities

Gets the server capabilities of an engine's server

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import distributed_engine_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.engine_server_capabilities_summary import EngineServerCapabilitiesSummary
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
    api_instance = distributed_engine_api.DistributedEngineApi(api_client)
    id = 1 # int | id

    # example passing only required values which don't have defaults set
    try:
        # Get Server Capabilities
        api_response = api_instance.distributed_engine_service_get_server_capabilities(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_get_server_capabilities: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id |

### Return type

[**[EngineServerCapabilitiesSummary]**](EngineServerCapabilitiesSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the server capabilities of an engine&#39;s server |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_engine_service_get_site**
> SiteBasicModel distributed_engine_service_get_site(id)

Get Site

Get Site for passed in Id

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import distributed_engine_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.site_basic_model import SiteBasicModel
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
    api_instance = distributed_engine_api.DistributedEngineApi(api_client)
    id = 1 # int | id

    # example passing only required values which don't have defaults set
    try:
        # Get Site
        api_response = api_instance.distributed_engine_service_get_site(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_get_site: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id |

### Return type

[**SiteBasicModel**](SiteBasicModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Site if found |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_engine_service_get_site_audits**
> PagingOfSiteAuditSummary distributed_engine_service_get_site_audits(id)

GetSiteAudits

Get audits by Site Id

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import distributed_engine_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_site_audit_summary import PagingOfSiteAuditSummary
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
    api_instance = distributed_engine_api.DistributedEngineApi(api_client)
    id = 1 # int | id
    is_exporting = True # bool | isExporting (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # GetSiteAudits
        api_response = api_instance.distributed_engine_service_get_site_audits(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_get_site_audits: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GetSiteAudits
        api_response = api_instance.distributed_engine_service_get_site_audits(id, is_exporting=is_exporting, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_get_site_audits: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id |
 **is_exporting** | **bool**| isExporting | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfSiteAuditSummary**](PagingOfSiteAuditSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paged List of Audits |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_engine_service_get_site_connector**
> SiteConnectorViewModel distributed_engine_service_get_site_connector(id)

Get Site Connector

Get Site Connector for passed in Id

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import distributed_engine_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.site_connector_view_model import SiteConnectorViewModel
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
    api_instance = distributed_engine_api.DistributedEngineApi(api_client)
    id = 1 # int | id

    # example passing only required values which don't have defaults set
    try:
        # Get Site Connector
        api_response = api_instance.distributed_engine_service_get_site_connector(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_get_site_connector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id |

### Return type

[**SiteConnectorViewModel**](SiteConnectorViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Site Connector if found |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_engine_service_get_site_connector_credentials**
> SiteConnectorCredentialsModel distributed_engine_service_get_site_connector_credentials(site_connector_id)

Get Site Connector Credentials

Get Site Connector Credentials

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import distributed_engine_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.site_connector_credentials_model import SiteConnectorCredentialsModel
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
    api_instance = distributed_engine_api.DistributedEngineApi(api_client)
    site_connector_id = 1 # int | siteConnectorId

    # example passing only required values which don't have defaults set
    try:
        # Get Site Connector Credentials
        api_response = api_instance.distributed_engine_service_get_site_connector_credentials(site_connector_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_get_site_connector_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_connector_id** | **int**| siteConnectorId |

### Return type

[**SiteConnectorCredentialsModel**](SiteConnectorCredentialsModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Site Connector Credentials |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_engine_service_get_site_connector_stub**
> SiteConnectorViewModel distributed_engine_service_get_site_connector_stub()

Get Site Connector Stub

Get Site Connector for passed in args

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import distributed_engine_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.site_connector_view_model import SiteConnectorViewModel
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
    api_instance = distributed_engine_api.DistributedEngineApi(api_client)
    queue_type = "queueType_example" # str | QueueType (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Site Connector Stub
        api_response = api_instance.distributed_engine_service_get_site_connector_stub(queue_type=queue_type)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_get_site_connector_stub: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queue_type** | **str**| QueueType | [optional]

### Return type

[**SiteConnectorViewModel**](SiteConnectorViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stub of a Site Connector model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_engine_service_get_site_stub**
> SiteBasicModel distributed_engine_service_get_site_stub()

Get Site Stub

Get Site for passed in args

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import distributed_engine_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.site_basic_model import SiteBasicModel
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
    api_instance = distributed_engine_api.DistributedEngineApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Site Stub
        api_response = api_instance.distributed_engine_service_get_site_stub()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_get_site_stub: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SiteBasicModel**](SiteBasicModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stub of a Site model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_engine_service_patch_distributed_engine_configuration**
> DistributedEngineConfigurationModel distributed_engine_service_patch_distributed_engine_configuration()

Update Distributed Engine Configuration

Update the current settings for Distributed Engine configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import distributed_engine_api
from plugins.model.distributed_engine_configuration_update_args import DistributedEngineConfigurationUpdateArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.distributed_engine_configuration_model import DistributedEngineConfigurationModel
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
    api_instance = distributed_engine_api.DistributedEngineApi(api_client)
    distributed_engine_configuration_update_args = DistributedEngineConfigurationUpdateArgs(
        data=DistributedEngineConfigurationUpdateModel(
            azure_service_bus_transport_type=UpdateFieldValueOfAzureServiceBusTransportType(
                dirty=True,
                value=AzureServiceBusTransportType("{}"),
            ),
            callback_port=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=1,
            ),
            callback_url=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            default_callback_interval_seconds=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            enable_distributed_engines=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            protocol=UpdateFieldValueOfDistributedEngineProtocol(
                dirty=True,
                value=DistributedEngineProtocol("{}"),
            ),
            response_bus_site_connector_id=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=1,
            ),
            secret_heartbeat_message_minutes_to_live=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            secret_heartbeat_message_retry_minutes=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            secret_password_change_message_minutes_to_live=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            secret_password_change_message_retry_minutes=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
        ),
    ) # DistributedEngineConfigurationUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Distributed Engine Configuration
        api_response = api_instance.distributed_engine_service_patch_distributed_engine_configuration(distributed_engine_configuration_update_args=distributed_engine_configuration_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_patch_distributed_engine_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distributed_engine_configuration_update_args** | [**DistributedEngineConfigurationUpdateArgs**](DistributedEngineConfigurationUpdateArgs.md)| args | [optional]

### Return type

[**DistributedEngineConfigurationModel**](DistributedEngineConfigurationModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Distributed Engine Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_engine_service_patch_engine_settings**
> EngineSettingsModel distributed_engine_service_patch_engine_settings(engine_settings_id)

Patch Engine Settings

Patch Engine Settings object having passed in the Id

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import distributed_engine_api
from plugins.model.engine_settings_update_args import EngineSettingsUpdateArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.engine_settings_model import EngineSettingsModel
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
    api_instance = distributed_engine_api.DistributedEngineApi(api_client)
    engine_settings_id = 1 # int | engineSettingsId
    engine_settings_update_args = EngineSettingsUpdateArgs(
        data=EngineSettingsUpdateModel(
            ad_sync_enabled=UpdateFieldValueOfOptionalBoolean(
                dirty=True,
                value=True,
            ),
            advanced_auditing_enabled=UpdateFieldValueOfOptionalBoolean(
                dirty=True,
                value=True,
            ),
            local_account_discovery_enabled=UpdateFieldValueOfOptionalBoolean(
                dirty=True,
                value=True,
            ),
            log_level=UpdateFieldValueOfOptionalLog4NetLevel(
                dirty=True,
                value="value_example",
            ),
            password_changing_enabled=UpdateFieldValueOfOptionalBoolean(
                dirty=True,
                value=True,
            ),
            rdp_proxy_enabled=UpdateFieldValueOfOptionalBoolean(
                dirty=True,
                value=True,
            ),
            secret_workflow_enabled=UpdateFieldValueOfOptionalBoolean(
                dirty=True,
                value=True,
            ),
            security_analytics_enabled=UpdateFieldValueOfOptionalBoolean(
                dirty=True,
                value=True,
            ),
            service_account_management_enabled=UpdateFieldValueOfOptionalBoolean(
                dirty=True,
                value=True,
            ),
            ssh_proxy_enabled=UpdateFieldValueOfOptionalBoolean(
                dirty=True,
                value=True,
            ),
            ssh_terminal_enabled=UpdateFieldValueOfOptionalBoolean(
                dirty=True,
                value=True,
            ),
        ),
    ) # EngineSettingsUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Patch Engine Settings
        api_response = api_instance.distributed_engine_service_patch_engine_settings(engine_settings_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_patch_engine_settings: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Patch Engine Settings
        api_response = api_instance.distributed_engine_service_patch_engine_settings(engine_settings_id, engine_settings_update_args=engine_settings_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_patch_engine_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_settings_id** | **int**| engineSettingsId |
 **engine_settings_update_args** | [**EngineSettingsUpdateArgs**](EngineSettingsUpdateArgs.md)| args | [optional]

### Return type

[**EngineSettingsModel**](EngineSettingsModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Patch Engine Settings object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_engine_service_patch_engine_settings_for_engine**
> EngineSettingsModel distributed_engine_service_patch_engine_settings_for_engine(engine_id)

Patch Engine Settings For Engine

Patch Engine Settings object having passed in the Engine Id

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import distributed_engine_api
from plugins.model.engine_settings_update_args import EngineSettingsUpdateArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.engine_settings_model import EngineSettingsModel
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
    api_instance = distributed_engine_api.DistributedEngineApi(api_client)
    engine_id = 1 # int | engineId
    engine_settings_update_args = EngineSettingsUpdateArgs(
        data=EngineSettingsUpdateModel(
            ad_sync_enabled=UpdateFieldValueOfOptionalBoolean(
                dirty=True,
                value=True,
            ),
            advanced_auditing_enabled=UpdateFieldValueOfOptionalBoolean(
                dirty=True,
                value=True,
            ),
            local_account_discovery_enabled=UpdateFieldValueOfOptionalBoolean(
                dirty=True,
                value=True,
            ),
            log_level=UpdateFieldValueOfOptionalLog4NetLevel(
                dirty=True,
                value="value_example",
            ),
            password_changing_enabled=UpdateFieldValueOfOptionalBoolean(
                dirty=True,
                value=True,
            ),
            rdp_proxy_enabled=UpdateFieldValueOfOptionalBoolean(
                dirty=True,
                value=True,
            ),
            secret_workflow_enabled=UpdateFieldValueOfOptionalBoolean(
                dirty=True,
                value=True,
            ),
            security_analytics_enabled=UpdateFieldValueOfOptionalBoolean(
                dirty=True,
                value=True,
            ),
            service_account_management_enabled=UpdateFieldValueOfOptionalBoolean(
                dirty=True,
                value=True,
            ),
            ssh_proxy_enabled=UpdateFieldValueOfOptionalBoolean(
                dirty=True,
                value=True,
            ),
            ssh_terminal_enabled=UpdateFieldValueOfOptionalBoolean(
                dirty=True,
                value=True,
            ),
        ),
    ) # EngineSettingsUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Patch Engine Settings For Engine
        api_response = api_instance.distributed_engine_service_patch_engine_settings_for_engine(engine_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_patch_engine_settings_for_engine: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Patch Engine Settings For Engine
        api_response = api_instance.distributed_engine_service_patch_engine_settings_for_engine(engine_id, engine_settings_update_args=engine_settings_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_patch_engine_settings_for_engine: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_id** | **int**| engineId |
 **engine_settings_update_args** | [**EngineSettingsUpdateArgs**](EngineSettingsUpdateArgs.md)| args | [optional]

### Return type

[**EngineSettingsModel**](EngineSettingsModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Patch Engine Settings object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_engine_service_patch_site**
> SiteBasicModel distributed_engine_service_patch_site(id)

Patch Site

Patch Site object having passed in Id

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import distributed_engine_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.site_basic_model import SiteBasicModel
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.site_update_args import SiteUpdateArgs
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
    api_instance = distributed_engine_api.DistributedEngineApi(api_client)
    id = 1 # int | id
    site_update_args = SiteUpdateArgs(
        data=SiteUpdateModel(
            active=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            enable_cred_ssp_for_win_rm=UpdateFieldValueOfOptionalBoolean(
                dirty=True,
                value=True,
            ),
            enable_rdp_proxy=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            enable_ssh_proxy=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            heartbeat_interval=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            powershell_secret_id=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=1,
            ),
            processing_location=UpdateFieldValueOfProcessingLocationType(
                dirty=True,
                value=ProcessingLocationType("{}"),
            ),
            rdp_proxy_port=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            site_connector_id=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            site_name=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            ssh_proxy_port=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            win_rm_end_point_url=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
        ),
    ) # SiteUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Patch Site
        api_response = api_instance.distributed_engine_service_patch_site(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_patch_site: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Patch Site
        api_response = api_instance.distributed_engine_service_patch_site(id, site_update_args=site_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_patch_site: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id |
 **site_update_args** | [**SiteUpdateArgs**](SiteUpdateArgs.md)| args | [optional]

### Return type

[**SiteBasicModel**](SiteBasicModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Patch Site object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_engine_service_reassign_secrets**
> SiteBasicModel distributed_engine_service_reassign_secrets(id)

Reassign Secrets From the Site

Reassign Secrets From the Site

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import distributed_engine_api
from plugins.model.reassign_secrets_args import ReassignSecretsArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.site_basic_model import SiteBasicModel
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
    api_instance = distributed_engine_api.DistributedEngineApi(api_client)
    id = 1 # int | id
    reassign_secrets_args = ReassignSecretsArgs(
        data=ReassignSecretsModel(
            disable_site=True,
            new_site_id=1,
        ),
    ) # ReassignSecretsArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Reassign Secrets From the Site
        api_response = api_instance.distributed_engine_service_reassign_secrets(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_reassign_secrets: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Reassign Secrets From the Site
        api_response = api_instance.distributed_engine_service_reassign_secrets(id, reassign_secrets_args=reassign_secrets_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_reassign_secrets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id |
 **reassign_secrets_args** | [**ReassignSecretsArgs**](ReassignSecretsArgs.md)| args | [optional]

### Return type

[**SiteBasicModel**](SiteBasicModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The site model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_engine_service_search_engines**
> IPagingOfEngineSummaryModel distributed_engine_service_search_engines()

Search Engines

Search Engines

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import distributed_engine_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.i_paging_of_engine_summary_model import IPagingOfEngineSummaryModel
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
    api_instance = distributed_engine_api.DistributedEngineApi(api_client)
    filter_activation_status = "filter.activationStatus_example" # str | Only return engines with this activation status (optional)
    filter_connection_status = "filter.connectionStatus_example" # str | Only return engines with this connection status (optional)
    filter_friendly_name = "filter.friendlyName_example" # str | Only return engines with a friendly name that contains this text (optional)
    filter_only_include_requiring_action = True # bool | Only include engines that require action.  For example, pending but not deleted or no site assigned. (optional)
    filter_site_id = 1 # int | Only return engines for this site (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Engines
        api_response = api_instance.distributed_engine_service_search_engines(filter_activation_status=filter_activation_status, filter_connection_status=filter_connection_status, filter_friendly_name=filter_friendly_name, filter_only_include_requiring_action=filter_only_include_requiring_action, filter_site_id=filter_site_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_search_engines: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_activation_status** | **str**| Only return engines with this activation status | [optional]
 **filter_connection_status** | **str**| Only return engines with this connection status | [optional]
 **filter_friendly_name** | **str**| Only return engines with a friendly name that contains this text | [optional]
 **filter_only_include_requiring_action** | **bool**| Only include engines that require action.  For example, pending but not deleted or no site assigned. | [optional]
 **filter_site_id** | **int**| Only return engines for this site | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**IPagingOfEngineSummaryModel**](IPagingOfEngineSummaryModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Engines that matched |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_engine_service_search_site_connectors**
> IPagingOfSiteConnectorSummaryModel distributed_engine_service_search_site_connectors()

Search Site Connectors

Search Site Connectors

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import distributed_engine_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.i_paging_of_site_connector_summary_model import IPagingOfSiteConnectorSummaryModel
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
    api_instance = distributed_engine_api.DistributedEngineApi(api_client)
    filter_include_inactive = True # bool | IncludeInactive (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Site Connectors
        api_response = api_instance.distributed_engine_service_search_site_connectors(filter_include_inactive=filter_include_inactive, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_search_site_connectors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_include_inactive** | **bool**| IncludeInactive | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**IPagingOfSiteConnectorSummaryModel**](IPagingOfSiteConnectorSummaryModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Site Connectors that matched |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_engine_service_search_site_logs**
> PagingOfSiteLogSummaryModel distributed_engine_service_search_site_logs(id)

SearchSiteLogs

Search site logs by Site Id

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import distributed_engine_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_site_log_summary_model import PagingOfSiteLogSummaryModel
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
    api_instance = distributed_engine_api.DistributedEngineApi(api_client)
    id = 1 # int | id
    filter_engine_id = 1 # int | Filter by a specific engine ID (optional)
    filter_search_term = "filter.searchTerm_example" # str | Term used to search the Engine Name and/or the Message of the Site Log (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # SearchSiteLogs
        api_response = api_instance.distributed_engine_service_search_site_logs(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_search_site_logs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # SearchSiteLogs
        api_response = api_instance.distributed_engine_service_search_site_logs(id, filter_engine_id=filter_engine_id, filter_search_term=filter_search_term, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_search_site_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id |
 **filter_engine_id** | **int**| Filter by a specific engine ID | [optional]
 **filter_search_term** | **str**| Term used to search the Engine Name and/or the Message of the Site Log | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfSiteLogSummaryModel**](PagingOfSiteLogSummaryModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paged List of Logs |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_engine_service_search_sites**
> PagingOfSiteSummaryModel distributed_engine_service_search_sites()

Search Sites

Search Sites

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import distributed_engine_api
from plugins.model.paging_of_site_summary_model import PagingOfSiteSummaryModel
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
    api_instance = distributed_engine_api.DistributedEngineApi(api_client)
    filter_include_inactive = True # bool | Include inactive sites (optional)
    filter_include_site_metrics = True # bool | When true metrics are included for returned sites such as how many inactive or active sites (optional)
    filter_only_include_sites_that_can_add_new_engines = True # bool | Only returns sites that can have new engines added (optional)
    filter_site_id = 1 # int | Return the site with this ID (optional)
    filter_site_name = "filter.siteName_example" # str | Return sites that partially match this name (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Sites
        api_response = api_instance.distributed_engine_service_search_sites(filter_include_inactive=filter_include_inactive, filter_include_site_metrics=filter_include_site_metrics, filter_only_include_sites_that_can_add_new_engines=filter_only_include_sites_that_can_add_new_engines, filter_site_id=filter_site_id, filter_site_name=filter_site_name, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_search_sites: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_include_inactive** | **bool**| Include inactive sites | [optional]
 **filter_include_site_metrics** | **bool**| When true metrics are included for returned sites such as how many inactive or active sites | [optional]
 **filter_only_include_sites_that_can_add_new_engines** | **bool**| Only returns sites that can have new engines added | [optional]
 **filter_site_id** | **int**| Return the site with this ID | [optional]
 **filter_site_name** | **str**| Return sites that partially match this name | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfSiteSummaryModel**](PagingOfSiteSummaryModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sites that matched |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_engine_service_update_engine_status**
> EngineActivationResultModel distributed_engine_service_update_engine_status()

Activate Engine

Activate the specified engine

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import distributed_engine_api
from plugins.model.engine_activation_request_args import EngineActivationRequestArgs
from plugins.model.engine_activation_result_model import EngineActivationResultModel
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
    api_instance = distributed_engine_api.DistributedEngineApi(api_client)
    engine_activation_request_args = EngineActivationRequestArgs(
        data=EngineActivationRequestModel(
            engines=[
                EngineStatusChangeModel(
                    callback_interval=1,
                    change_type=EngineStatusChangeType("Activate"),
                    engine_id=1,
                    site_connector_id=1,
                    site_id=1,
                    site_name="site_name_example",
                ),
            ],
        ),
    ) # EngineActivationRequestArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Activate Engine
        api_response = api_instance.distributed_engine_service_update_engine_status(engine_activation_request_args=engine_activation_request_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_update_engine_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_activation_request_args** | [**EngineActivationRequestArgs**](EngineActivationRequestArgs.md)| args | [optional]

### Return type

[**EngineActivationResultModel**](EngineActivationResultModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Engine Activation Result Model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_engine_service_update_site_connector**
> SiteConnectorViewModel distributed_engine_service_update_site_connector(id)

Update Site Connector

Update Site Connector object with passed in Id

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import distributed_engine_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.site_connector_view_model import SiteConnectorViewModel
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.site_connector_update_args import SiteConnectorUpdateArgs
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
    api_instance = distributed_engine_api.DistributedEngineApi(api_client)
    id = 1 # int | id
    site_connector_update_args = SiteConnectorUpdateArgs(
        data=SiteConnectorUpdateModel(
            active=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            host_name=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            port=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            queue_type=UpdateFieldValueOfMessageQueueType(
                dirty=True,
                value=MessageQueueType("{}"),
            ),
            shared_access_key_name=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            shared_access_key_value=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            site_connector_name=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            ssl_certificate_thumbprint=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            use_ssl=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
        ),
    ) # SiteConnectorUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Site Connector
        api_response = api_instance.distributed_engine_service_update_site_connector(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_update_site_connector: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Site Connector
        api_response = api_instance.distributed_engine_service_update_site_connector(id, site_connector_update_args=site_connector_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_update_site_connector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id |
 **site_connector_update_args** | [**SiteConnectorUpdateArgs**](SiteConnectorUpdateArgs.md)| args | [optional]

### Return type

[**SiteConnectorViewModel**](SiteConnectorViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Site Connector object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_engine_service_validate_site_connectivity**
> SiteConnectivityValidationResult distributed_engine_service_validate_site_connectivity(site_id)

Validate Site Connectivity

Validate Site Connectivity within a timeout.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import distributed_engine_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.site_connectivity_validation_args import SiteConnectivityValidationArgs
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.site_connectivity_validation_result import SiteConnectivityValidationResult
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
    api_instance = distributed_engine_api.DistributedEngineApi(api_client)
    site_id = 1 # int | Id of Site
    site_connectivity_validation_args = SiteConnectivityValidationArgs(
        data=SiteConnectivityValidationModel(
            timeout=1,
        ),
    ) # SiteConnectivityValidationArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Validate Site Connectivity
        api_response = api_instance.distributed_engine_service_validate_site_connectivity(site_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_validate_site_connectivity: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Validate Site Connectivity
        api_response = api_instance.distributed_engine_service_validate_site_connectivity(site_id, site_connectivity_validation_args=site_connectivity_validation_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_validate_site_connectivity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| Id of Site |
 **site_connectivity_validation_args** | [**SiteConnectivityValidationArgs**](SiteConnectivityValidationArgs.md)| args | [optional]

### Return type

[**SiteConnectivityValidationResult**](SiteConnectivityValidationResult.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SiteConnectivityValidationResult object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributed_engine_service_validate_site_connector**
> SiteConnectorValidationResult distributed_engine_service_validate_site_connector(site_connector_id)

Validate Site Connector

Validate Site Connector and returns model

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import distributed_engine_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.site_connector_validation_result import SiteConnectorValidationResult
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
    api_instance = distributed_engine_api.DistributedEngineApi(api_client)
    site_connector_id = 1 # int | siteConnectorId

    # example passing only required values which don't have defaults set
    try:
        # Validate Site Connector
        api_response = api_instance.distributed_engine_service_validate_site_connector(site_connector_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DistributedEngineApi->distributed_engine_service_validate_site_connector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_connector_id** | **int**| siteConnectorId |

### Return type

[**SiteConnectorValidationResult**](SiteConnectorValidationResult.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Site Connector validation result |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

