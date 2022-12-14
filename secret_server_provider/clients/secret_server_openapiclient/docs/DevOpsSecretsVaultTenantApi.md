# secret_server_openapiclient.DevOpsSecretsVaultTenantApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dev_ops_secrets_vault_tenant_service_create**](DevOpsSecretsVaultTenantApi.md#dev_ops_secrets_vault_tenant_service_create) | **POST** /v1/devops-secrets-vault/tenant | Save a DevOps Secrets Vault Tenant.
[**dev_ops_secrets_vault_tenant_service_get_list**](DevOpsSecretsVaultTenantApi.md#dev_ops_secrets_vault_tenant_service_get_list) | **GET** /v1/devops-secrets-vault/tenant | Get DevOps Secrets Vault Tenants.
[**dev_ops_secrets_vault_tenant_service_get_tenant**](DevOpsSecretsVaultTenantApi.md#dev_ops_secrets_vault_tenant_service_get_tenant) | **GET** /v1/devops-secrets-vault/tenant/{id} | Get a DevOps Secrets Vault Tenant.
[**dev_ops_secrets_vault_tenant_service_get_tenant_audits**](DevOpsSecretsVaultTenantApi.md#dev_ops_secrets_vault_tenant_service_get_tenant_audits) | **GET** /v1/devops-secrets-vault/tenant/audits | DSV Tenant Audits.
[**dev_ops_secrets_vault_tenant_service_get_tenant_stub**](DevOpsSecretsVaultTenantApi.md#dev_ops_secrets_vault_tenant_service_get_tenant_stub) | **GET** /v1/devops-secrets-vault/tenant/stub | DevOps Secrets Vault Tenant Model.
[**dev_ops_secrets_vault_tenant_service_update**](DevOpsSecretsVaultTenantApi.md#dev_ops_secrets_vault_tenant_service_update) | **PUT** /v1/devops-secrets-vault/tenant/{id} | Update a DevOps Secrets Vault Tenant.


# **dev_ops_secrets_vault_tenant_service_create**
> DevOpsSecretsVaultTenantModel dev_ops_secrets_vault_tenant_service_create()

Save a DevOps Secrets Vault Tenant.

Creates an existing DevOps Secrets Vault Tenant, or creates a new one.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import dev_ops_secrets_vault_tenant_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.dev_ops_secrets_vault_create_tenant_args import DevOpsSecretsVaultCreateTenantArgs
from secret_server_openapiclient.model.dev_ops_secrets_vault_tenant_model import DevOpsSecretsVaultTenantModel
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
    api_instance = dev_ops_secrets_vault_tenant_api.DevOpsSecretsVaultTenantApi(api_client)
    dev_ops_secrets_vault_create_tenant_args = DevOpsSecretsVaultCreateTenantArgs(
        data=DevOpsSecretsVaultTenantUpdateModel(
            active=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            secret_id=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            sync_interval=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            tenant_name=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
        ),
    ) # DevOpsSecretsVaultCreateTenantArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Save a DevOps Secrets Vault Tenant.
        api_response = api_instance.dev_ops_secrets_vault_tenant_service_create(dev_ops_secrets_vault_create_tenant_args=dev_ops_secrets_vault_create_tenant_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DevOpsSecretsVaultTenantApi->dev_ops_secrets_vault_tenant_service_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dev_ops_secrets_vault_create_tenant_args** | [**DevOpsSecretsVaultCreateTenantArgs**](DevOpsSecretsVaultCreateTenantArgs.md)| args | [optional]

### Return type

[**DevOpsSecretsVaultTenantModel**](DevOpsSecretsVaultTenantModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The DevOps Secrets Vault Tenant Id. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dev_ops_secrets_vault_tenant_service_get_list**
> PagingOfDevOpsSecretsVaultTenantSummary dev_ops_secrets_vault_tenant_service_get_list()

Get DevOps Secrets Vault Tenants.

Search, filter, sort, and page DevOps Secrets Vault Tenants.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import dev_ops_secrets_vault_tenant_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.paging_of_dev_ops_secrets_vault_tenant_summary import PagingOfDevOpsSecretsVaultTenantSummary
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
    api_instance = dev_ops_secrets_vault_tenant_api.DevOpsSecretsVaultTenantApi(api_client)
    filter_include_inactive = True # bool | If inactive tenants should be returned. Defaulted to false. (optional)
    filter_name_search = "filter.nameSearch_example" # str | Search by tenant names. (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get DevOps Secrets Vault Tenants.
        api_response = api_instance.dev_ops_secrets_vault_tenant_service_get_list(filter_include_inactive=filter_include_inactive, filter_name_search=filter_name_search, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DevOpsSecretsVaultTenantApi->dev_ops_secrets_vault_tenant_service_get_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_include_inactive** | **bool**| If inactive tenants should be returned. Defaulted to false. | [optional]
 **filter_name_search** | **str**| Search by tenant names. | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfDevOpsSecretsVaultTenantSummary**](PagingOfDevOpsSecretsVaultTenantSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The DevOps Secrets Vault Tenants that were found. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dev_ops_secrets_vault_tenant_service_get_tenant**
> DevOpsSecretsVaultTenantModel dev_ops_secrets_vault_tenant_service_get_tenant(id)

Get a DevOps Secrets Vault Tenant.

Get the DevOps Secrets Vault Tenant with the Tenant ID provided.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import dev_ops_secrets_vault_tenant_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.dev_ops_secrets_vault_tenant_model import DevOpsSecretsVaultTenantModel
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
    api_instance = dev_ops_secrets_vault_tenant_api.DevOpsSecretsVaultTenantApi(api_client)
    id = 1 # int | id

    # example passing only required values which don't have defaults set
    try:
        # Get a DevOps Secrets Vault Tenant.
        api_response = api_instance.dev_ops_secrets_vault_tenant_service_get_tenant(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DevOpsSecretsVaultTenantApi->dev_ops_secrets_vault_tenant_service_get_tenant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id |

### Return type

[**DevOpsSecretsVaultTenantModel**](DevOpsSecretsVaultTenantModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The DevOps Secrets Vault Tenant model. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dev_ops_secrets_vault_tenant_service_get_tenant_audits**
> PagingOfDevOpsSecretsVaultTenantAuditSummary dev_ops_secrets_vault_tenant_service_get_tenant_audits()

DSV Tenant Audits.

Retrieves the changes made to your DSV Tenants.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import dev_ops_secrets_vault_tenant_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.paging_of_dev_ops_secrets_vault_tenant_audit_summary import PagingOfDevOpsSecretsVaultTenantAuditSummary
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
    api_instance = dev_ops_secrets_vault_tenant_api.DevOpsSecretsVaultTenantApi(api_client)
    is_exporting = True # bool | isExporting (optional)
    filter_search_text = "filter.searchText_example" # str | Search for text in the audit log. (optional)
    filter_tenant_id = 1 # int | Optional filter by tenant id. (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # DSV Tenant Audits.
        api_response = api_instance.dev_ops_secrets_vault_tenant_service_get_tenant_audits(is_exporting=is_exporting, filter_search_text=filter_search_text, filter_tenant_id=filter_tenant_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DevOpsSecretsVaultTenantApi->dev_ops_secrets_vault_tenant_service_get_tenant_audits: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_exporting** | **bool**| isExporting | [optional]
 **filter_search_text** | **str**| Search for text in the audit log. | [optional]
 **filter_tenant_id** | **int**| Optional filter by tenant id. | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfDevOpsSecretsVaultTenantAuditSummary**](PagingOfDevOpsSecretsVaultTenantAuditSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The paginated list of DSV Tenant audits. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dev_ops_secrets_vault_tenant_service_get_tenant_stub**
> DevOpsSecretsVaultTenantModel dev_ops_secrets_vault_tenant_service_get_tenant_stub()

DevOps Secrets Vault Tenant Model.

Retrieve an empty instance of a DevOps Secrets Vault Tenant.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import dev_ops_secrets_vault_tenant_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.dev_ops_secrets_vault_tenant_model import DevOpsSecretsVaultTenantModel
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
    api_instance = dev_ops_secrets_vault_tenant_api.DevOpsSecretsVaultTenantApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # DevOps Secrets Vault Tenant Model.
        api_response = api_instance.dev_ops_secrets_vault_tenant_service_get_tenant_stub()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DevOpsSecretsVaultTenantApi->dev_ops_secrets_vault_tenant_service_get_tenant_stub: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**DevOpsSecretsVaultTenantModel**](DevOpsSecretsVaultTenantModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A DevOps Secrets Vault Tenant with no values. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dev_ops_secrets_vault_tenant_service_update**
> DevOpsSecretsVaultTenantModel dev_ops_secrets_vault_tenant_service_update(id)

Update a DevOps Secrets Vault Tenant.

Updates an existing DevOps Secrets Vault Tenant, or creates a new one.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import dev_ops_secrets_vault_tenant_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.dev_ops_secrets_vault_update_tenant_args import DevOpsSecretsVaultUpdateTenantArgs
from secret_server_openapiclient.model.dev_ops_secrets_vault_tenant_model import DevOpsSecretsVaultTenantModel
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
    api_instance = dev_ops_secrets_vault_tenant_api.DevOpsSecretsVaultTenantApi(api_client)
    id = 1 # int | id
    dev_ops_secrets_vault_update_tenant_args = DevOpsSecretsVaultUpdateTenantArgs(
        data=DevOpsSecretsVaultTenantUpdateModel(
            active=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            secret_id=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            sync_interval=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            tenant_name=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
        ),
    ) # DevOpsSecretsVaultUpdateTenantArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a DevOps Secrets Vault Tenant.
        api_response = api_instance.dev_ops_secrets_vault_tenant_service_update(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DevOpsSecretsVaultTenantApi->dev_ops_secrets_vault_tenant_service_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a DevOps Secrets Vault Tenant.
        api_response = api_instance.dev_ops_secrets_vault_tenant_service_update(id, dev_ops_secrets_vault_update_tenant_args=dev_ops_secrets_vault_update_tenant_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DevOpsSecretsVaultTenantApi->dev_ops_secrets_vault_tenant_service_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id |
 **dev_ops_secrets_vault_update_tenant_args** | [**DevOpsSecretsVaultUpdateTenantArgs**](DevOpsSecretsVaultUpdateTenantArgs.md)| args | [optional]

### Return type

[**DevOpsSecretsVaultTenantModel**](DevOpsSecretsVaultTenantModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The DevOps Secrets Vault Tenant Id. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

