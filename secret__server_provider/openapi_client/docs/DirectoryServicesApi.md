# plugins.DirectoryServicesApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**directory_services_service_create_domain**](DirectoryServicesApi.md#directory_services_service_create_domain) | **POST** /v1/directory-services/domains | Create Domain
[**directory_services_service_get_directory_group_members**](DirectoryServicesApi.md#directory_services_service_get_directory_group_members) | **GET** /v1/directory-services/domains/{domainId}/members | Search in the directory for members of a group
[**directory_services_service_get_directory_services_configuration**](DirectoryServicesApi.md#directory_services_service_get_directory_services_configuration) | **GET** /v1/directory-services/configuration | Directory Services Configuration
[**directory_services_service_get_domain**](DirectoryServicesApi.md#directory_services_service_get_domain) | **GET** /v1/directory-services/domains/{id} | Get a Domain
[**directory_services_service_get_domain_stub**](DirectoryServicesApi.md#directory_services_service_get_domain_stub) | **GET** /v1/directory-services/domains/stub | Get a Domain Stub
[**directory_services_service_get_ldap_sync_settings**](DirectoryServicesApi.md#directory_services_service_get_ldap_sync_settings) | **GET** /v1/directory-services/domains/ldap-settings/{id} | Get Ldap synchronization settings for a domain
[**directory_services_service_get_synchronization_log**](DirectoryServicesApi.md#directory_services_service_get_synchronization_log) | **GET** /v1/directory-services/synchronization/logs | Get Synchronization Log
[**directory_services_service_get_synchronization_status**](DirectoryServicesApi.md#directory_services_service_get_synchronization_status) | **GET** /v1/directory-services/synchronization | Directory Services Sync Status
[**directory_services_service_link_domain_group**](DirectoryServicesApi.md#directory_services_service_link_domain_group) | **POST** /v1/directory-services/domains/{domainId}/group | Link a group from the directory
[**directory_services_service_patch_directory_services_configuration**](DirectoryServicesApi.md#directory_services_service_patch_directory_services_configuration) | **PATCH** /v1/directory-services/configuration | Update Directory Services Configuration
[**directory_services_service_patch_domain**](DirectoryServicesApi.md#directory_services_service_patch_domain) | **PATCH** /v1/directory-services/domains/{domainId} | Patch a domain
[**directory_services_service_patch_ldap_sync_settings**](DirectoryServicesApi.md#directory_services_service_patch_ldap_sync_settings) | **PATCH** /v1/directory-services/domains/ldap-settings/{domainId} | Patch Ldap Sync Settings for a domain
[**directory_services_service_search_directory_for_groups**](DirectoryServicesApi.md#directory_services_service_search_directory_for_groups) | **GET** /v1/directory-services/domains/{domainId}/groups/search-directory | Search in the directory for groups
[**directory_services_service_search_domains**](DirectoryServicesApi.md#directory_services_service_search_domains) | **GET** /v1/directory-services/domains | Search Domains
[**directory_services_service_synchronize_now**](DirectoryServicesApi.md#directory_services_service_synchronize_now) | **POST** /v1/directory-services/synchronization-now | Synchronize all directory services
[**directory_services_service_unlink_domain_group**](DirectoryServicesApi.md#directory_services_service_unlink_domain_group) | **DELETE** /v1/directory-services/domains/{domainId}/group/{groupId} | Unlink a group from domain


# **directory_services_service_create_domain**
> DomainModel directory_services_service_create_domain()

Create Domain

Create a new domain to be used for directory services synchronization / integration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import directory_services_api
from plugins.model.domain_create_args import DomainCreateArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.domain_model import DomainModel
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
    api_instance = directory_services_api.DirectoryServicesApi(api_client)
    domain_create_args = DomainCreateArgs(
        data=DomainCreateModel(
            active=True,
            auth_type=None,
            client_id=None,
            client_secret=None,
            distinguished_name=None,
            domain_name=None,
            domain_type=DomainType("{}"),
            friendly_name=None,
            multifactor_authentication_provider=MultifactorAuthenticationProviderTypes("{}"),
            site_id=None,
            synchronization_secret_id=None,
            tenant_id=None,
            user_auth_type=None,
            use_secure_ldap=True,
        ),
    ) # DomainCreateArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Domain
        api_response = api_instance.directory_services_service_create_domain(domain_create_args=domain_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DirectoryServicesApi->directory_services_service_create_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_create_args** | [**DomainCreateArgs**](DomainCreateArgs.md)| args | [optional]

### Return type

[**DomainModel**](DomainModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Domain that was just created |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **directory_services_service_get_directory_group_members**
> DirectoryServicesGroupMemberResponse directory_services_service_get_directory_group_members(domain_id)

Search in the directory for members of a group

Using the credentials defined on the domain find members of a group within the directory

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import directory_services_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.directory_services_group_member_response import DirectoryServicesGroupMemberResponse
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
    api_instance = directory_services_api.DirectoryServicesApi(api_client)
    domain_id = None # bool, date, datetime, dict, float, int, list, str, none_type | domainId
    domain_identifier = None # bool, date, datetime, dict, float, int, list, str, none_type | The unique directory identifier for the group to be linked.  For example, this is ADGuid in Active Directory (optional)
    group_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Name of the Group (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search in the directory for members of a group
        api_response = api_instance.directory_services_service_get_directory_group_members(domain_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DirectoryServicesApi->directory_services_service_get_directory_group_members: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search in the directory for members of a group
        api_response = api_instance.directory_services_service_get_directory_group_members(domain_id, domain_identifier=domain_identifier, group_name=group_name)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DirectoryServicesApi->directory_services_service_get_directory_group_members: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| domainId |
 **domain_identifier** | **bool, date, datetime, dict, float, int, list, str, none_type**| The unique directory identifier for the group to be linked.  For example, this is ADGuid in Active Directory | [optional]
 **group_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Name of the Group | [optional]

### Return type

[**DirectoryServicesGroupMemberResponse**](DirectoryServicesGroupMemberResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of users in the passed in group |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **directory_services_service_get_directory_services_configuration**
> DirectoryServicesConfigurationModel directory_services_service_get_directory_services_configuration()

Directory Services Configuration

Retrieve the current settings for Directory Services configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import directory_services_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.directory_services_configuration_model import DirectoryServicesConfigurationModel
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
    api_instance = directory_services_api.DirectoryServicesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Directory Services Configuration
        api_response = api_instance.directory_services_service_get_directory_services_configuration()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DirectoryServicesApi->directory_services_service_get_directory_services_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**DirectoryServicesConfigurationModel**](DirectoryServicesConfigurationModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Directory Services Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **directory_services_service_get_domain**
> DomainModel directory_services_service_get_domain(id)

Get a Domain

Get a Domain

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import directory_services_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.domain_model import DomainModel
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
    api_instance = directory_services_api.DirectoryServicesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id

    # example passing only required values which don't have defaults set
    try:
        # Get a Domain
        api_response = api_instance.directory_services_service_get_domain(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DirectoryServicesApi->directory_services_service_get_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |

### Return type

[**DomainModel**](DomainModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Domain that was found |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **directory_services_service_get_domain_stub**
> DomainModel directory_services_service_get_domain_stub()

Get a Domain Stub

Get a Domain Stub

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import directory_services_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.domain_model import DomainModel
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
    api_instance = directory_services_api.DirectoryServicesApi(api_client)
    domain_type = None # bool, date, datetime, dict, float, int, list, str, none_type | domainType (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a Domain Stub
        api_response = api_instance.directory_services_service_get_domain_stub(domain_type=domain_type)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DirectoryServicesApi->directory_services_service_get_domain_stub: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_type** | **bool, date, datetime, dict, float, int, list, str, none_type**| domainType | [optional]

### Return type

[**DomainModel**](DomainModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Domain Stub |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **directory_services_service_get_ldap_sync_settings**
> LdapSyncSettingsViewModel directory_services_service_get_ldap_sync_settings(id)

Get Ldap synchronization settings for a domain

Get Ldap synchronization settings for a domain

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import directory_services_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.ldap_sync_settings_view_model import LdapSyncSettingsViewModel
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
    api_instance = directory_services_api.DirectoryServicesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id

    # example passing only required values which don't have defaults set
    try:
        # Get Ldap synchronization settings for a domain
        api_response = api_instance.directory_services_service_get_ldap_sync_settings(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DirectoryServicesApi->directory_services_service_get_ldap_sync_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |

### Return type

[**LdapSyncSettingsViewModel**](LdapSyncSettingsViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ldap synchronization settings for the domain |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **directory_services_service_get_synchronization_log**
> PagingOfDirectoryServicesSynchronizationLogEntry directory_services_service_get_synchronization_log()

Get Synchronization Log

Get Synchronization Log

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import directory_services_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.paging_of_directory_services_synchronization_log_entry import PagingOfDirectoryServicesSynchronizationLogEntry
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
    api_instance = directory_services_api.DirectoryServicesApi(api_client)
    filter_end_date = None # bool, date, datetime, dict, float, int, list, str, none_type | EndDate (optional)
    filter_search_text = None # bool, date, datetime, dict, float, int, list, str, none_type | SearchText (optional)
    filter_start_date = None # bool, date, datetime, dict, float, int, list, str, none_type | StartDate (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Synchronization Log
        api_response = api_instance.directory_services_service_get_synchronization_log(filter_end_date=filter_end_date, filter_search_text=filter_search_text, filter_start_date=filter_start_date, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DirectoryServicesApi->directory_services_service_get_synchronization_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_end_date** | **bool, date, datetime, dict, float, int, list, str, none_type**| EndDate | [optional]
 **filter_search_text** | **bool, date, datetime, dict, float, int, list, str, none_type**| SearchText | [optional]
 **filter_start_date** | **bool, date, datetime, dict, float, int, list, str, none_type**| StartDate | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfDirectoryServicesSynchronizationLogEntry**](PagingOfDirectoryServicesSynchronizationLogEntry.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Synchronization log entries |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **directory_services_service_get_synchronization_status**
> DirectoryServicesSynchronizationStatus directory_services_service_get_synchronization_status()

Directory Services Sync Status

Return status of directory services synchronization

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import directory_services_api
from plugins.model.directory_services_synchronization_status import DirectoryServicesSynchronizationStatus
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
    api_instance = directory_services_api.DirectoryServicesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Directory Services Sync Status
        api_response = api_instance.directory_services_service_get_synchronization_status()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DirectoryServicesApi->directory_services_service_get_synchronization_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**DirectoryServicesSynchronizationStatus**](DirectoryServicesSynchronizationStatus.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Whether or not the sync has started |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **directory_services_service_link_domain_group**
> bool directory_services_service_link_domain_group(domain_id)

Link a group from the directory

Linking or adding a group to a domain will synchronize all users from the directory to SS that are members of this group.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import directory_services_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.link_external_group_args import LinkExternalGroupArgs
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
    api_instance = directory_services_api.DirectoryServicesApi(api_client)
    domain_id = None # bool, date, datetime, dict, float, int, list, str, none_type | domainId
    link_external_group_args = LinkExternalGroupArgs(
        data=LinkExternalGroupSettings(
            domain_identifier=None,
            name=None,
        ),
    ) # LinkExternalGroupArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Link a group from the directory
        api_response = api_instance.directory_services_service_link_domain_group(domain_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DirectoryServicesApi->directory_services_service_link_domain_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Link a group from the directory
        api_response = api_instance.directory_services_service_link_domain_group(domain_id, link_external_group_args=link_external_group_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DirectoryServicesApi->directory_services_service_link_domain_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| domainId |
 **link_external_group_args** | [**LinkExternalGroupArgs**](LinkExternalGroupArgs.md)| args | [optional]

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
**200** | Success status |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **directory_services_service_patch_directory_services_configuration**
> DirectoryServicesConfigurationModel directory_services_service_patch_directory_services_configuration()

Update Directory Services Configuration

Update the current settings for Directory Services configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import directory_services_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.directory_services_configuration_update_args import DirectoryServicesConfigurationUpdateArgs
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.directory_services_configuration_model import DirectoryServicesConfigurationModel
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
    api_instance = directory_services_api.DirectoryServicesApi(api_client)
    directory_services_configuration_update_args = DirectoryServicesConfigurationUpdateArgs(
        data=DirectoryServicesConfigurationUpdateModel(
            days_to_keep_operational_logs=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            disable_inactive_users_months=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            enable_directory_integration=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            enable_directory_synchronization=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            enable_integrated_windows_authentication=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            enable_user_disabling=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            synchronization_interval_days=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            synchronization_interval_hours=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            synchronization_interval_minutes=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            user_account_options=UpdateFieldValueOfDirectoryServicesSynchronizationUserOption(
                dirty=True,
                value=DirectoryServicesSynchronizationUserOption("{}"),
            ),
        ),
    ) # DirectoryServicesConfigurationUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Directory Services Configuration
        api_response = api_instance.directory_services_service_patch_directory_services_configuration(directory_services_configuration_update_args=directory_services_configuration_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DirectoryServicesApi->directory_services_service_patch_directory_services_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **directory_services_configuration_update_args** | [**DirectoryServicesConfigurationUpdateArgs**](DirectoryServicesConfigurationUpdateArgs.md)| args | [optional]

### Return type

[**DirectoryServicesConfigurationModel**](DirectoryServicesConfigurationModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Directory Services Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **directory_services_service_patch_domain**
> DomainModel directory_services_service_patch_domain(domain_id)

Patch a domain

Patch a domain

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import directory_services_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.domain_model import DomainModel
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.domain_patch_args import DomainPatchArgs
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
    api_instance = directory_services_api.DirectoryServicesApi(api_client)
    domain_id = None # bool, date, datetime, dict, float, int, list, str, none_type | domainId
    domain_patch_args = DomainPatchArgs(
        data=DomainPatchModel(
            active=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            auth_type=UpdateFieldValueOfOptionalAuthType(
                dirty=True,
                value=None,
            ),
            client_id=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            client_secret=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            distinguished_name=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            domain_name=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            friendly_name=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            multifactor_authentication_provider=UpdateFieldValueOfMultifactorAuthenticationProviderTypes(
                dirty=True,
                value=MultifactorAuthenticationProviderTypes("{}"),
            ),
            site_id=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            synchronization_secret_id=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=None,
            ),
            tenant_id=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            user_auth_type=UpdateFieldValueOfOptionalAuthType(
                dirty=True,
                value=None,
            ),
            use_secure_ldap=UpdateFieldValueOfOptionalBoolean(
                dirty=True,
                value=True,
            ),
        ),
    ) # DomainPatchArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Patch a domain
        api_response = api_instance.directory_services_service_patch_domain(domain_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DirectoryServicesApi->directory_services_service_patch_domain: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Patch a domain
        api_response = api_instance.directory_services_service_patch_domain(domain_id, domain_patch_args=domain_patch_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DirectoryServicesApi->directory_services_service_patch_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| domainId |
 **domain_patch_args** | [**DomainPatchArgs**](DomainPatchArgs.md)| args | [optional]

### Return type

[**DomainModel**](DomainModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Domain that was just updated |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **directory_services_service_patch_ldap_sync_settings**
> LdapSyncSettingsViewModel directory_services_service_patch_ldap_sync_settings(domain_id)

Patch Ldap Sync Settings for a domain

Patch Ldap Sync Settings for a domain

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import directory_services_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.ldap_sync_settings_view_model import LdapSyncSettingsViewModel
from plugins.model.ldap_sync_settings_patch_args import LdapSyncSettingsPatchArgs
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
    api_instance = directory_services_api.DirectoryServicesApi(api_client)
    domain_id = None # bool, date, datetime, dict, float, int, list, str, none_type | domainId
    ldap_sync_settings_patch_args = LdapSyncSettingsPatchArgs(
        data=LdapSyncSettingsPatchModel(
            base_dn_code=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            display_name_attribute=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            email_attribute=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            group_member_attribute=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            group_name_attribute=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            group_object_classes=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            group_search_filter=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            guid_attribute=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            username_attribute=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            user_object_classes=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            user_principal_name_attribute=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
        ),
    ) # LdapSyncSettingsPatchArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Patch Ldap Sync Settings for a domain
        api_response = api_instance.directory_services_service_patch_ldap_sync_settings(domain_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DirectoryServicesApi->directory_services_service_patch_ldap_sync_settings: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Patch Ldap Sync Settings for a domain
        api_response = api_instance.directory_services_service_patch_ldap_sync_settings(domain_id, ldap_sync_settings_patch_args=ldap_sync_settings_patch_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DirectoryServicesApi->directory_services_service_patch_ldap_sync_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| domainId |
 **ldap_sync_settings_patch_args** | [**LdapSyncSettingsPatchArgs**](LdapSyncSettingsPatchArgs.md)| args | [optional]

### Return type

[**LdapSyncSettingsViewModel**](LdapSyncSettingsViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Domain that was just updated |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **directory_services_service_search_directory_for_groups**
> ExternalGroupViewModel directory_services_service_search_directory_for_groups(domain_id)

Search in the directory for groups

Using the credentials defined on the domain search within the directory for groups

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import directory_services_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.external_group_view_model import ExternalGroupViewModel
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
    api_instance = directory_services_api.DirectoryServicesApi(api_client)
    domain_id = None # bool, date, datetime, dict, float, int, list, str, none_type | domainId
    search_text = None # bool, date, datetime, dict, float, int, list, str, none_type | Search text. Use * for wildcards, ex: Admin*. Leave empty to return all. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search in the directory for groups
        api_response = api_instance.directory_services_service_search_directory_for_groups(domain_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DirectoryServicesApi->directory_services_service_search_directory_for_groups: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search in the directory for groups
        api_response = api_instance.directory_services_service_search_directory_for_groups(domain_id, search_text=search_text)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DirectoryServicesApi->directory_services_service_search_directory_for_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| domainId |
 **search_text** | **bool, date, datetime, dict, float, int, list, str, none_type**| Search text. Use * for wildcards, ex: Admin*. Leave empty to return all. | [optional]

### Return type

[**ExternalGroupViewModel**](ExternalGroupViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of groups matching search criteria |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **directory_services_service_search_domains**
> IPagingOfDomainSummaryModel directory_services_service_search_domains()

Search Domains

Search Domains

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import directory_services_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.i_paging_of_domain_summary_model import IPagingOfDomainSummaryModel
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
    api_instance = directory_services_api.DirectoryServicesApi(api_client)
    filter_domain_name = None # bool, date, datetime, dict, float, int, list, str, none_type | DomainName (optional)
    filter_include_inactive = True # bool | IncludeInactive (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Domains
        api_response = api_instance.directory_services_service_search_domains(filter_domain_name=filter_domain_name, filter_include_inactive=filter_include_inactive, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DirectoryServicesApi->directory_services_service_search_domains: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_domain_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| DomainName | [optional]
 **filter_include_inactive** | **bool**| IncludeInactive | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**IPagingOfDomainSummaryModel**](IPagingOfDomainSummaryModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Domains that matched |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **directory_services_service_synchronize_now**
> bool directory_services_service_synchronize_now()

Synchronize all directory services

Run synchronize to update users and groups for all configurated and enabled domains in all directories and domains

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import directory_services_api
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
    api_instance = directory_services_api.DirectoryServicesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Synchronize all directory services
        api_response = api_instance.directory_services_service_synchronize_now()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DirectoryServicesApi->directory_services_service_synchronize_now: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | True if the command was initiated successfully |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **directory_services_service_unlink_domain_group**
> bool directory_services_service_unlink_domain_group(domain_id, group_id)

Unlink a group from domain

Unlinking a group from a domain will disable future synchronization updates. The group will also be disabled.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import directory_services_api
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
    api_instance = directory_services_api.DirectoryServicesApi(api_client)
    domain_id = None # bool, date, datetime, dict, float, int, list, str, none_type | domainId
    group_id = None # bool, date, datetime, dict, float, int, list, str, none_type | groupId

    # example passing only required values which don't have defaults set
    try:
        # Unlink a group from domain
        api_response = api_instance.directory_services_service_unlink_domain_group(domain_id, group_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DirectoryServicesApi->directory_services_service_unlink_domain_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| domainId |
 **group_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| groupId |

### Return type

**bool**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success status |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

