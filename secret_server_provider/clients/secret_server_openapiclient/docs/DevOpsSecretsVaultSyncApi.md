# secret_server_openapiclient.DevOpsSecretsVaultSyncApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dev_ops_secrets_vault_sync_service_create_sync**](DevOpsSecretsVaultSyncApi.md#dev_ops_secrets_vault_sync_service_create_sync) | **POST** /v1/devops-secrets-vault/add-sync | Create a DevOps sync for a secret.
[**dev_ops_secrets_vault_sync_service_get_sync_status**](DevOpsSecretsVaultSyncApi.md#dev_ops_secrets_vault_sync_service_get_sync_status) | **GET** /v1/devops-secrets-vault/sync/status/{syncMapId} | Information about secret syncing.
[**dev_ops_secrets_vault_sync_service_get_sync_statuses**](DevOpsSecretsVaultSyncApi.md#dev_ops_secrets_vault_sync_service_get_sync_statuses) | **GET** /v1/devops-secrets-vault/sync/status | Information about secrets syncing.
[**dev_ops_secrets_vault_sync_service_sync_secret**](DevOpsSecretsVaultSyncApi.md#dev_ops_secrets_vault_sync_service_sync_secret) | **POST** /v1/devops-secrets-vault/sync | Sync a secret.
[**dev_ops_secrets_vault_sync_service_update_sync**](DevOpsSecretsVaultSyncApi.md#dev_ops_secrets_vault_sync_service_update_sync) | **PUT** /v1/devops-secrets-vault/sync/{syncSecretMapId} | Update a secret sync.


# **dev_ops_secrets_vault_sync_service_create_sync**
> DevOpsSecretsVaultSyncStatusModel dev_ops_secrets_vault_sync_service_create_sync()

Create a DevOps sync for a secret.

Create a sync between a secret and a DevOps Secrets Vault tenant.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import dev_ops_secrets_vault_sync_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.dev_ops_secrets_vault_create_sync_args import DevOpsSecretsVaultCreateSyncArgs
from secret_server_openapiclient.model.dev_ops_secrets_vault_sync_status_model import DevOpsSecretsVaultSyncStatusModel
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
    api_instance = dev_ops_secrets_vault_sync_api.DevOpsSecretsVaultSyncApi(api_client)
    dev_ops_secrets_vault_create_sync_args = DevOpsSecretsVaultCreateSyncArgs(
        data=DevOpsSecretVaultSyncUpdateModel(
            active=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            dsv_tenant_id=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            field_names_path=UpdateFieldValueOfStringArray(
                dirty=True,
                value=[
                    "value_example",
                ],
            ),
            secret_id=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
        ),
    ) # DevOpsSecretsVaultCreateSyncArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a DevOps sync for a secret.
        api_response = api_instance.dev_ops_secrets_vault_sync_service_create_sync(dev_ops_secrets_vault_create_sync_args=dev_ops_secrets_vault_create_sync_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DevOpsSecretsVaultSyncApi->dev_ops_secrets_vault_sync_service_create_sync: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dev_ops_secrets_vault_create_sync_args** | [**DevOpsSecretsVaultCreateSyncArgs**](DevOpsSecretsVaultCreateSyncArgs.md)| args | [optional]

### Return type

[**DevOpsSecretsVaultSyncStatusModel**](DevOpsSecretsVaultSyncStatusModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The status of the secret&#39;s sync. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dev_ops_secrets_vault_sync_service_get_sync_status**
> DevOpsSecretsVaultSyncStatusModel dev_ops_secrets_vault_sync_service_get_sync_status(sync_map_id)

Information about secret syncing.

Get which tenants a secret is syncing to, the current status of the sync, and the last sync time.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import dev_ops_secrets_vault_sync_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.dev_ops_secrets_vault_sync_status_model import DevOpsSecretsVaultSyncStatusModel
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
    api_instance = dev_ops_secrets_vault_sync_api.DevOpsSecretsVaultSyncApi(api_client)
    sync_map_id = 1 # int | syncMapId

    # example passing only required values which don't have defaults set
    try:
        # Information about secret syncing.
        api_response = api_instance.dev_ops_secrets_vault_sync_service_get_sync_status(sync_map_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DevOpsSecretsVaultSyncApi->dev_ops_secrets_vault_sync_service_get_sync_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_map_id** | **int**| syncMapId |

### Return type

[**DevOpsSecretsVaultSyncStatusModel**](DevOpsSecretsVaultSyncStatusModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The status of a secret syncing to a tenant. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dev_ops_secrets_vault_sync_service_get_sync_statuses**
> PagingOfDevOpsSecretsVaultSyncStatusSummary dev_ops_secrets_vault_sync_service_get_sync_statuses()

Information about secrets syncing.

Get which tenants the secrets are syncing to, the current status of the sync, and the last sync time.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import dev_ops_secrets_vault_sync_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.paging_of_dev_ops_secrets_vault_sync_status_summary import PagingOfDevOpsSecretsVaultSyncStatusSummary
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
    api_instance = dev_ops_secrets_vault_sync_api.DevOpsSecretsVaultSyncApi(api_client)
    filter_include_inactive = True # bool | If inactive sync maps should be returned. (optional)
    filter_secret_id = 1 # int | Search by the secret being synced. (optional)
    filter_tenant_id = 1 # int | Search by the tenant being pushed to. (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Information about secrets syncing.
        api_response = api_instance.dev_ops_secrets_vault_sync_service_get_sync_statuses(filter_include_inactive=filter_include_inactive, filter_secret_id=filter_secret_id, filter_tenant_id=filter_tenant_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DevOpsSecretsVaultSyncApi->dev_ops_secrets_vault_sync_service_get_sync_statuses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_include_inactive** | **bool**| If inactive sync maps should be returned. | [optional]
 **filter_secret_id** | **int**| Search by the secret being synced. | [optional]
 **filter_tenant_id** | **int**| Search by the tenant being pushed to. | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfDevOpsSecretsVaultSyncStatusSummary**](PagingOfDevOpsSecretsVaultSyncStatusSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of statuses for secret syncing. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dev_ops_secrets_vault_sync_service_sync_secret**
> [DevOpsSecretsVaultSyncStatusViewModel] dev_ops_secrets_vault_sync_service_sync_secret()

Sync a secret.

Sync a secret to a DevOps Secrets Vault tenant.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import dev_ops_secrets_vault_sync_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.dev_ops_secrets_vault_sync_status_view_model import DevOpsSecretsVaultSyncStatusViewModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.dev_ops_secrets_vault_sync_secrets_args import DevOpsSecretsVaultSyncSecretsArgs
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
    api_instance = dev_ops_secrets_vault_sync_api.DevOpsSecretsVaultSyncApi(api_client)
    dev_ops_secrets_vault_sync_secrets_args = DevOpsSecretsVaultSyncSecretsArgs(
        data=[
            1,
        ],
    ) # DevOpsSecretsVaultSyncSecretsArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Sync a secret.
        api_response = api_instance.dev_ops_secrets_vault_sync_service_sync_secret(dev_ops_secrets_vault_sync_secrets_args=dev_ops_secrets_vault_sync_secrets_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DevOpsSecretsVaultSyncApi->dev_ops_secrets_vault_sync_service_sync_secret: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dev_ops_secrets_vault_sync_secrets_args** | [**DevOpsSecretsVaultSyncSecretsArgs**](DevOpsSecretsVaultSyncSecretsArgs.md)| args | [optional]

### Return type

[**[DevOpsSecretsVaultSyncStatusViewModel]**](DevOpsSecretsVaultSyncStatusViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The status of the secret&#39;s sync. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dev_ops_secrets_vault_sync_service_update_sync**
> DevOpsSecretsVaultSyncStatusModel dev_ops_secrets_vault_sync_service_update_sync(sync_secret_map_id)

Update a secret sync.

Update a sync between a secret and a DevOps Secrets Vault tenant.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import dev_ops_secrets_vault_sync_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.dev_ops_secrets_vault_create_sync_args import DevOpsSecretsVaultCreateSyncArgs
from secret_server_openapiclient.model.dev_ops_secrets_vault_sync_status_model import DevOpsSecretsVaultSyncStatusModel
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
    api_instance = dev_ops_secrets_vault_sync_api.DevOpsSecretsVaultSyncApi(api_client)
    sync_secret_map_id = 1 # int | syncSecretMapId
    dev_ops_secrets_vault_create_sync_args = DevOpsSecretsVaultCreateSyncArgs(
        data=DevOpsSecretVaultSyncUpdateModel(
            active=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            dsv_tenant_id=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            field_names_path=UpdateFieldValueOfStringArray(
                dirty=True,
                value=[
                    "value_example",
                ],
            ),
            secret_id=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
        ),
    ) # DevOpsSecretsVaultCreateSyncArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a secret sync.
        api_response = api_instance.dev_ops_secrets_vault_sync_service_update_sync(sync_secret_map_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DevOpsSecretsVaultSyncApi->dev_ops_secrets_vault_sync_service_update_sync: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a secret sync.
        api_response = api_instance.dev_ops_secrets_vault_sync_service_update_sync(sync_secret_map_id, dev_ops_secrets_vault_create_sync_args=dev_ops_secrets_vault_create_sync_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DevOpsSecretsVaultSyncApi->dev_ops_secrets_vault_sync_service_update_sync: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_secret_map_id** | **int**| syncSecretMapId |
 **dev_ops_secrets_vault_create_sync_args** | [**DevOpsSecretsVaultCreateSyncArgs**](DevOpsSecretsVaultCreateSyncArgs.md)| args | [optional]

### Return type

[**DevOpsSecretsVaultSyncStatusModel**](DevOpsSecretsVaultSyncStatusModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The status of the secret&#39;s sync. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

