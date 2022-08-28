# secret_server_openapiclient.DomainNameIndexApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**domain_name_index_service_create_domain_name_index**](DomainNameIndexApi.md#domain_name_index_service_create_domain_name_index) | **POST** /v1/domain-index/create | Create a new domain name index
[**domain_name_index_service_delete_single_domain_name_index**](DomainNameIndexApi.md#domain_name_index_service_delete_single_domain_name_index) | **PUT** /v1/domain-index/delete/{id} | Delete a domain name index
[**domain_name_index_service_expire_all_domain_name_index**](DomainNameIndexApi.md#domain_name_index_service_expire_all_domain_name_index) | **POST** /v1/domain-index/expire-all | Expire all domain name index records
[**domain_name_index_service_expire_single_domain_name_index**](DomainNameIndexApi.md#domain_name_index_service_expire_single_domain_name_index) | **POST** /v1/domain-index/expire/{id} | Expire a domain name index
[**domain_name_index_service_get_domain_name_index**](DomainNameIndexApi.md#domain_name_index_service_get_domain_name_index) | **GET** /v1/domain-index | Get a domain name index
[**domain_name_index_service_truncate_domain_name_index**](DomainNameIndexApi.md#domain_name_index_service_truncate_domain_name_index) | **DELETE** /v1/domain-index/delete-all | Delete all domain name index records
[**domain_name_index_service_update_domain_name_index**](DomainNameIndexApi.md#domain_name_index_service_update_domain_name_index) | **PATCH** /v1/domain-index/{id} | Update a domain name index


# **domain_name_index_service_create_domain_name_index**
> DomainNameIndexModel domain_name_index_service_create_domain_name_index()

Create a new domain name index

Creates a new domain name index with suggested discovery source id

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import domain_name_index_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.domain_name_index_model import DomainNameIndexModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.domain_name_index_create_args import DomainNameIndexCreateArgs
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
    api_instance = domain_name_index_api.DomainNameIndexApi(api_client)
    domain_name_index_create_args = DomainNameIndexCreateArgs(
        data=DomainNameIndexCreateModel(
            discovery_source_id_suggested=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=None,
            ),
            domain_marked_as_ignored=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            domain_name_discovered=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
        ),
    ) # DomainNameIndexCreateArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new domain name index
        api_response = api_instance.domain_name_index_service_create_domain_name_index(domain_name_index_create_args=domain_name_index_create_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DomainNameIndexApi->domain_name_index_service_create_domain_name_index: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name_index_create_args** | [**DomainNameIndexCreateArgs**](DomainNameIndexCreateArgs.md)| args | [optional]

### Return type

[**DomainNameIndexModel**](DomainNameIndexModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new domain name index |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_name_index_service_delete_single_domain_name_index**
> bool domain_name_index_service_delete_single_domain_name_index(id)

Delete a domain name index

Delete an existing domain name index using the existing domain name index ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import domain_name_index_api
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
    api_instance = domain_name_index_api.DomainNameIndexApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Delete success

    # example passing only required values which don't have defaults set
    try:
        # Delete a domain name index
        api_response = api_instance.domain_name_index_service_delete_single_domain_name_index(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DomainNameIndexApi->domain_name_index_service_delete_single_domain_name_index: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Delete success |

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
**200** | Delete success |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_name_index_service_expire_all_domain_name_index**
> bool domain_name_index_service_expire_all_domain_name_index()

Expire all domain name index records

Expire existing domain name index records

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import domain_name_index_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.domain_name_index_expire_update_args import DomainNameIndexExpireUpdateArgs
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
    api_instance = domain_name_index_api.DomainNameIndexApi(api_client)
    domain_name_index_expire_update_args = DomainNameIndexExpireUpdateArgs(
        data=DomainNameIndexExpireUpdateModel(
            domain_name_index_id=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=None,
            ),
            re_index_now=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
        ),
    ) # DomainNameIndexExpireUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Expire all domain name index records
        api_response = api_instance.domain_name_index_service_expire_all_domain_name_index(domain_name_index_expire_update_args=domain_name_index_expire_update_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DomainNameIndexApi->domain_name_index_service_expire_all_domain_name_index: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name_index_expire_update_args** | [**DomainNameIndexExpireUpdateArgs**](DomainNameIndexExpireUpdateArgs.md)| args | [optional]

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
**200** | Expire success |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_name_index_service_expire_single_domain_name_index**
> DomainNameIndexModel domain_name_index_service_expire_single_domain_name_index(id)

Expire a domain name index

Expire an existing domain name index using the existing domain name index ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import domain_name_index_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.domain_name_index_model import DomainNameIndexModel
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
    api_instance = domain_name_index_api.DomainNameIndexApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Domain Name Index ID

    # example passing only required values which don't have defaults set
    try:
        # Expire a domain name index
        api_response = api_instance.domain_name_index_service_expire_single_domain_name_index(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DomainNameIndexApi->domain_name_index_service_expire_single_domain_name_index: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Domain Name Index ID |

### Return type

[**DomainNameIndexModel**](DomainNameIndexModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated domain name index |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_name_index_service_get_domain_name_index**
> PagingOfDomainNameIndexSummary domain_name_index_service_get_domain_name_index()

Get a domain name index

Returns the domain name index

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import domain_name_index_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.paging_of_domain_name_index_summary import PagingOfDomainNameIndexSummary
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
    api_instance = domain_name_index_api.DomainNameIndexApi(api_client)
    filter_discovery_source_id_scanned = None # bool, date, datetime, dict, float, int, list, str, none_type | DiscoverySourceIdScanned (optional)
    filter_domain_name = None # bool, date, datetime, dict, float, int, list, str, none_type | DomainName (optional)
    filter_domain_resolve_type = None # bool, date, datetime, dict, float, int, list, str, none_type | DomainResolveType (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a domain name index
        api_response = api_instance.domain_name_index_service_get_domain_name_index(filter_discovery_source_id_scanned=filter_discovery_source_id_scanned, filter_domain_name=filter_domain_name, filter_domain_resolve_type=filter_domain_resolve_type, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DomainNameIndexApi->domain_name_index_service_get_domain_name_index: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_discovery_source_id_scanned** | **bool, date, datetime, dict, float, int, list, str, none_type**| DiscoverySourceIdScanned | [optional]
 **filter_domain_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| DomainName | [optional]
 **filter_domain_resolve_type** | **bool, date, datetime, dict, float, int, list, str, none_type**| DomainResolveType | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfDomainNameIndexSummary**](PagingOfDomainNameIndexSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Domain Name Index View |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_name_index_service_truncate_domain_name_index**
> bool domain_name_index_service_truncate_domain_name_index()

Delete all domain name index records

Delete existing domain name index records

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import domain_name_index_api
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
    api_instance = domain_name_index_api.DomainNameIndexApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Delete all domain name index records
        api_response = api_instance.domain_name_index_service_truncate_domain_name_index()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DomainNameIndexApi->domain_name_index_service_truncate_domain_name_index: %s\n" % e)
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
**200** | Delete success |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_name_index_service_update_domain_name_index**
> DomainNameIndexModel domain_name_index_service_update_domain_name_index(id)

Update a domain name index

Update an existing domain name index using the existing domain name index ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import domain_name_index_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.domain_name_index_model import DomainNameIndexModel
from secret_server_openapiclient.model.domain_name_index_update_args import DomainNameIndexUpdateArgs
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
    api_instance = domain_name_index_api.DomainNameIndexApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Domain Name Index ID
    domain_name_index_update_args = DomainNameIndexUpdateArgs(
        data=DomainNameIndexUpdateModel(
            discovery_source_id_suggested=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=None,
            ),
            domain_marked_as_ignored=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
        ),
    ) # DomainNameIndexUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a domain name index
        api_response = api_instance.domain_name_index_service_update_domain_name_index(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DomainNameIndexApi->domain_name_index_service_update_domain_name_index: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a domain name index
        api_response = api_instance.domain_name_index_service_update_domain_name_index(id, domain_name_index_update_args=domain_name_index_update_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DomainNameIndexApi->domain_name_index_service_update_domain_name_index: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Domain Name Index ID |
 **domain_name_index_update_args** | [**DomainNameIndexUpdateArgs**](DomainNameIndexUpdateArgs.md)| args | [optional]

### Return type

[**DomainNameIndexModel**](DomainNameIndexModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated domain name index |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

