# plugins.DevOpsSecretsVaultTenantApi

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
import plugins
from plugins.api import dev_ops_secrets_vault_tenant_api
from plugins.model.dev_ops_secrets_vault_create_tenant_args import DevOpsSecretsVaultCreateTenantArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.dev_ops_secrets_vault_tenant_model import DevOpsSecretsVaultTenantModel
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
    api_instance = dev_ops_secrets_vault_tenant_api.DevOpsSecretsVaultTenantApi(api_client)
    dev_ops_secrets_vault_create_tenant_args = DevOpsSecretsVaultCreateTenantArgs(
        data=DevOpsSecretsVaultTenantUpdateModel(
            active=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            secret_id=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            sync_interval=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            tenant_name=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
        ),
    ) # DevOpsSecretsVaultCreateTenantArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Save a DevOps Secrets Vault Tenant.
        api_response = api_instance.dev_ops_secrets_vault_tenant_service_create(dev_ops_secrets_vault_create_tenant_args=dev_ops_secrets_vault_create_tenant_args)
        pprint(api_response)
    except plugins.ApiException as e:
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
import plugins
from plugins.api import dev_ops_secrets_vault_tenant_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_dev_ops_secrets_vault_tenant_summary import PagingOfDevOpsSecretsVaultTenantSummary
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
    api_instance = dev_ops_secrets_vault_tenant_api.DevOpsSecretsVaultTenantApi(api_client)
    filter_include_inactive = True # bool | If inactive tenants should be returned. Defaulted to false. (optional)
    filter_name_search = None # bool, date, datetime, dict, float, int, list, str, none_type | Search by tenant names. (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get DevOps Secrets Vault Tenants.
        api_response = api_instance.dev_ops_secrets_vault_tenant_service_get_list(filter_include_inactive=filter_include_inactive, filter_name_search=filter_name_search, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DevOpsSecretsVaultTenantApi->dev_ops_secrets_vault_tenant_service_get_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_include_inactive** | **bool**| If inactive tenants should be returned. Defaulted to false. | [optional]
 **filter_name_search** | **bool, date, datetime, dict, float, int, list, str, none_type**| Search by tenant names. | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

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
import plugins
from plugins.api import dev_ops_secrets_vault_tenant_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.dev_ops_secrets_vault_tenant_model import DevOpsSecretsVaultTenantModel
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
    api_instance = dev_ops_secrets_vault_tenant_api.DevOpsSecretsVaultTenantApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id

    # example passing only required values which don't have defaults set
    try:
        # Get a DevOps Secrets Vault Tenant.
        api_response = api_instance.dev_ops_secrets_vault_tenant_service_get_tenant(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DevOpsSecretsVaultTenantApi->dev_ops_secrets_vault_tenant_service_get_tenant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |

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
import plugins
from plugins.api import dev_ops_secrets_vault_tenant_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_dev_ops_secrets_vault_tenant_audit_summary import PagingOfDevOpsSecretsVaultTenantAuditSummary
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
    api_instance = dev_ops_secrets_vault_tenant_api.DevOpsSecretsVaultTenantApi(api_client)
    is_exporting = True # bool | isExporting (optional)
    filter_search_text = None # bool, date, datetime, dict, float, int, list, str, none_type | Search for text in the audit log. (optional)
    filter_tenant_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Optional filter by tenant id. (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # DSV Tenant Audits.
        api_response = api_instance.dev_ops_secrets_vault_tenant_service_get_tenant_audits(is_exporting=is_exporting, filter_search_text=filter_search_text, filter_tenant_id=filter_tenant_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DevOpsSecretsVaultTenantApi->dev_ops_secrets_vault_tenant_service_get_tenant_audits: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_exporting** | **bool**| isExporting | [optional]
 **filter_search_text** | **bool, date, datetime, dict, float, int, list, str, none_type**| Search for text in the audit log. | [optional]
 **filter_tenant_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Optional filter by tenant id. | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

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
import plugins
from plugins.api import dev_ops_secrets_vault_tenant_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.dev_ops_secrets_vault_tenant_model import DevOpsSecretsVaultTenantModel
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
    api_instance = dev_ops_secrets_vault_tenant_api.DevOpsSecretsVaultTenantApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # DevOps Secrets Vault Tenant Model.
        api_response = api_instance.dev_ops_secrets_vault_tenant_service_get_tenant_stub()
        pprint(api_response)
    except plugins.ApiException as e:
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
import plugins
from plugins.api import dev_ops_secrets_vault_tenant_api
from plugins.model.dev_ops_secrets_vault_update_tenant_args import DevOpsSecretsVaultUpdateTenantArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.dev_ops_secrets_vault_tenant_model import DevOpsSecretsVaultTenantModel
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
    api_instance = dev_ops_secrets_vault_tenant_api.DevOpsSecretsVaultTenantApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    dev_ops_secrets_vault_update_tenant_args = DevOpsSecretsVaultUpdateTenantArgs(
        data=DevOpsSecretsVaultTenantUpdateModel(
            active=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            secret_id=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            sync_interval=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            tenant_name=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
        ),
    ) # DevOpsSecretsVaultUpdateTenantArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a DevOps Secrets Vault Tenant.
        api_response = api_instance.dev_ops_secrets_vault_tenant_service_update(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DevOpsSecretsVaultTenantApi->dev_ops_secrets_vault_tenant_service_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a DevOps Secrets Vault Tenant.
        api_response = api_instance.dev_ops_secrets_vault_tenant_service_update(id, dev_ops_secrets_vault_update_tenant_args=dev_ops_secrets_vault_update_tenant_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling DevOpsSecretsVaultTenantApi->dev_ops_secrets_vault_tenant_service_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
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

