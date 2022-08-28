# plugins.KeyManagementApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**key_management_service_get**](KeyManagementApi.md#key_management_service_get) | **GET** /v1/key-management | Get Key Management Configuration
[**key_management_service_get_key_rotation_audit_users**](KeyManagementApi.md#key_management_service_get_key_rotation_audit_users) | **GET** /v1/key-management/audit/users | Get a List of Unique Users from the Master Encryption Key Rotation Audit List
[**key_management_service_get_master_encryption_key_rotation_info**](KeyManagementApi.md#key_management_service_get_master_encryption_key_rotation_info) | **GET** /v1/key-management/mekrotationinfo | Get Master Encryption Key Rotation Status Info
[**key_management_service_retry_master_encryption_key_status**](KeyManagementApi.md#key_management_service_retry_master_encryption_key_status) | **PUT** /v1/key-management/retrymekstatus | Retry Master Encryption Key Status
[**key_management_service_search_key_rotation_audit**](KeyManagementApi.md#key_management_service_search_key_rotation_audit) | **GET** /v1/key-management/audit | Get a Master Encryption Key Rotation Audit List
[**key_management_service_start_master_encryption_key_rotation**](KeyManagementApi.md#key_management_service_start_master_encryption_key_rotation) | **PUT** /v1/key-management/startmekrotation | Rotate Master Encryption Key
[**key_management_service_stub**](KeyManagementApi.md#key_management_service_stub) | **GET** /v1/key-management/stub | Get Key Management Config Stub
[**key_management_service_update**](KeyManagementApi.md#key_management_service_update) | **PUT** /v1/key-management | Update Key Management Configuration


# **key_management_service_get**
> KeyManagementConfigModel key_management_service_get()

Get Key Management Configuration

Get the current or previous Key Management configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import key_management_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.key_management_config_model import KeyManagementConfigModel
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
    api_instance = key_management_api.KeyManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Key Management Configuration
        api_response = api_instance.key_management_service_get()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling KeyManagementApi->key_management_service_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**KeyManagementConfigModel**](KeyManagementConfigModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | KeyManagementConfigModel object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **key_management_service_get_key_rotation_audit_users**
> [MasterEncryptionKeyRotationInfoAuditUserViewModel] key_management_service_get_key_rotation_audit_users()

Get a List of Unique Users from the Master Encryption Key Rotation Audit List

Get a List of Unique Users from the Master Encryption Key Rotation Audit List

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import key_management_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.master_encryption_key_rotation_info_audit_user_view_model import MasterEncryptionKeyRotationInfoAuditUserViewModel
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
    api_instance = key_management_api.KeyManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get a List of Unique Users from the Master Encryption Key Rotation Audit List
        api_response = api_instance.key_management_service_get_key_rotation_audit_users()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling KeyManagementApi->key_management_service_get_key_rotation_audit_users: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[MasterEncryptionKeyRotationInfoAuditUserViewModel]**](MasterEncryptionKeyRotationInfoAuditUserViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of unique users from the Master Encryption Key Rotation Audits. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **key_management_service_get_master_encryption_key_rotation_info**
> MEKRotationInfoResponseViewModel key_management_service_get_master_encryption_key_rotation_info()

Get Master Encryption Key Rotation Status Info

Gets the status of Master Encryption Key Rotation

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import key_management_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.mek_rotation_info_response_view_model import MEKRotationInfoResponseViewModel
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
    api_instance = key_management_api.KeyManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Master Encryption Key Rotation Status Info
        api_response = api_instance.key_management_service_get_master_encryption_key_rotation_info()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling KeyManagementApi->key_management_service_get_master_encryption_key_rotation_info: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**MEKRotationInfoResponseViewModel**](MEKRotationInfoResponseViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status of Master Encryption Key Rotation |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **key_management_service_retry_master_encryption_key_status**
> MEKRotationInfoResponseViewModel key_management_service_retry_master_encryption_key_status()

Retry Master Encryption Key Status

Retries Current Status of the Master Encryption Key Process

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import key_management_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.mek_rotation_info_response_view_model import MEKRotationInfoResponseViewModel
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
    api_instance = key_management_api.KeyManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retry Master Encryption Key Status
        api_response = api_instance.key_management_service_retry_master_encryption_key_status()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling KeyManagementApi->key_management_service_retry_master_encryption_key_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**MEKRotationInfoResponseViewModel**](MEKRotationInfoResponseViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Whether the Master Encryption Key Rotation retry request was successful |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **key_management_service_search_key_rotation_audit**
> PagingOfMasterEncryptionKeyRotationInfoAuditViewModel key_management_service_search_key_rotation_audit()

Get a Master Encryption Key Rotation Audit List

Search, filter, sort, and page Master Encryption Key Rotation Audits.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import key_management_api
from plugins.model.paging_of_master_encryption_key_rotation_info_audit_view_model import PagingOfMasterEncryptionKeyRotationInfoAuditViewModel
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
    api_instance = key_management_api.KeyManagementApi(api_client)
    is_exporting = True # bool | isExporting (optional)
    filter_action = "filter.action_example" # str | Action (optional)
    filter_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Date (optional)
    filter_search_term = "filter.searchTerm_example" # str | SearchTerm (optional)
    filter_user_id = 1 # int | UserId (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a Master Encryption Key Rotation Audit List
        api_response = api_instance.key_management_service_search_key_rotation_audit(is_exporting=is_exporting, filter_action=filter_action, filter_date=filter_date, filter_search_term=filter_search_term, filter_user_id=filter_user_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling KeyManagementApi->key_management_service_search_key_rotation_audit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_exporting** | **bool**| isExporting | [optional]
 **filter_action** | **str**| Action | [optional]
 **filter_date** | **datetime**| Date | [optional]
 **filter_search_term** | **str**| SearchTerm | [optional]
 **filter_user_id** | **int**| UserId | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfMasterEncryptionKeyRotationInfoAuditViewModel**](PagingOfMasterEncryptionKeyRotationInfoAuditViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of Master Encryption Key Rotation Audits. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **key_management_service_start_master_encryption_key_rotation**
> MEKRotationInfoResponseViewModel key_management_service_start_master_encryption_key_rotation()

Rotate Master Encryption Key

Rotates the Master Encryption Key and marks data for rotation

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import key_management_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.mek_rotation_info_response_view_model import MEKRotationInfoResponseViewModel
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
    api_instance = key_management_api.KeyManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Rotate Master Encryption Key
        api_response = api_instance.key_management_service_start_master_encryption_key_rotation()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling KeyManagementApi->key_management_service_start_master_encryption_key_rotation: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**MEKRotationInfoResponseViewModel**](MEKRotationInfoResponseViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Whether the Master Encryption Key was rotated and a data rotation request initiated |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **key_management_service_stub**
> KeyManagementConfigModel key_management_service_stub()

Get Key Management Config Stub

Return the default values for a new Key Management Config

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import key_management_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.key_management_config_model import KeyManagementConfigModel
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
    api_instance = key_management_api.KeyManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Key Management Config Stub
        api_response = api_instance.key_management_service_stub()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling KeyManagementApi->key_management_service_stub: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**KeyManagementConfigModel**](KeyManagementConfigModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | KeyManagementConfigModel object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **key_management_service_update**
> KeyManagementConfigModel key_management_service_update()

Update Key Management Configuration

Update the Key Management configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import key_management_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.key_management_config_model import KeyManagementConfigModel
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.key_management_config_update_args import KeyManagementConfigUpdateArgs
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
    api_instance = key_management_api.KeyManagementApi(api_client)
    key_management_config_update_args = KeyManagementConfigUpdateArgs(
        aws_kms_access_key_id="aws_kms_access_key_id_example",
        aws_kms_key_arn="aws_kms_key_arn_example",
        aws_kms_key_id="aws_kms_key_id_example",
        aws_kms_secret_access_key="aws_kms_secret_access_key_example",
        azure_key_vault_base_url="azure_key_vault_base_url_example",
        azure_key_vault_key_name="azure_key_vault_key_name_example",
        azure_key_vault_key_version="azure_key_vault_key_version_example",
        azure_key_vault_principal_id="azure_key_vault_principal_id_example",
        azure_key_vault_principal_secret="azure_key_vault_principal_secret_example",
        key_management_type_id=1,
    ) # KeyManagementConfigUpdateArgs | Key Management Config update options (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Key Management Configuration
        api_response = api_instance.key_management_service_update(key_management_config_update_args=key_management_config_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling KeyManagementApi->key_management_service_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_management_config_update_args** | [**KeyManagementConfigUpdateArgs**](KeyManagementConfigUpdateArgs.md)| Key Management Config update options | [optional]

### Return type

[**KeyManagementConfigModel**](KeyManagementConfigModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | KeyManagementConfigModel object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

