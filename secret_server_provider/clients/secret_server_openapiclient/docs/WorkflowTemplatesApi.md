# secret_server_openapiclient.WorkflowTemplatesApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workflow_templates_service_cancel_request**](WorkflowTemplatesApi.md#workflow_templates_service_cancel_request) | **POST** /v1/workflows/templates/{id}/cancel-requests | Cancel Workflow Requests
[**workflow_templates_service_create_workflow_template**](WorkflowTemplatesApi.md#workflow_templates_service_create_workflow_template) | **POST** /v1/workflows/templates | Create a Workflow Template
[**workflow_templates_service_get_template**](WorkflowTemplatesApi.md#workflow_templates_service_get_template) | **GET** /v1/workflows/templates/{id} | Get a Workflow Template
[**workflow_templates_service_get_workflow_entities**](WorkflowTemplatesApi.md#workflow_templates_service_get_workflow_entities) | **GET** /v1/workflows/templates/{id}/entities/{includeAll} | Count of Entities using a Workflow Template
[**workflow_templates_service_search_template_audit**](WorkflowTemplatesApi.md#workflow_templates_service_search_template_audit) | **GET** /v1/workflows/templates/{id}/audits | Get a Workflow Template Audit List
[**workflow_templates_service_search_workflow_templates**](WorkflowTemplatesApi.md#workflow_templates_service_search_workflow_templates) | **GET** /v1/workflows/templates | Search Workflow Templates
[**workflow_templates_service_stub_workflow_template**](WorkflowTemplatesApi.md#workflow_templates_service_stub_workflow_template) | **GET** /v1/workflows/templates/stub | Get a Workflow Template Stub
[**workflow_templates_service_update_workflow_template**](WorkflowTemplatesApi.md#workflow_templates_service_update_workflow_template) | **PUT** /v1/workflows/templates/{id} | Update a Workflow Template


# **workflow_templates_service_cancel_request**
> bool, date, datetime, dict, float, int, list, str, none_type workflow_templates_service_cancel_request(id)

Cancel Workflow Requests

Cancel all Workflow Requests that are using the provided Workflow Template.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import workflow_templates_api
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
    api_instance = workflow_templates_api.WorkflowTemplatesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Workflow Template Id

    # example passing only required values which don't have defaults set
    try:
        # Cancel Workflow Requests
        api_response = api_instance.workflow_templates_service_cancel_request(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling WorkflowTemplatesApi->workflow_templates_service_cancel_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Workflow Template Id |

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
**200** | Confirmation of cancellation. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_templates_service_create_workflow_template**
> bool, date, datetime, dict, float, int, list, str, none_type workflow_templates_service_create_workflow_template()

Create a Workflow Template

Create a new Workflow Template.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import workflow_templates_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.workflow_template_create_args import WorkflowTemplateCreateArgs
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
    api_instance = workflow_templates_api.WorkflowTemplatesApi(api_client)
    workflow_template_create_args = WorkflowTemplateCreateArgs(
        configuration_json=None,
        description=None,
        expiration_minutes=None,
        name=None,
        workflow_type=WorkflowType("{}"),
    ) # WorkflowTemplateCreateArgs | Workflow Template creation options (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a Workflow Template
        api_response = api_instance.workflow_templates_service_create_workflow_template(workflow_template_create_args=workflow_template_create_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling WorkflowTemplatesApi->workflow_templates_service_create_workflow_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_template_create_args** | [**WorkflowTemplateCreateArgs**](WorkflowTemplateCreateArgs.md)| Workflow Template creation options | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new Workflow Template&#39;s ID. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_templates_service_get_template**
> WorkflowTemplateDetailModel workflow_templates_service_get_template(id)

Get a Workflow Template

Request a specific Workflow Template by ID.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import workflow_templates_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.workflow_template_detail_model import WorkflowTemplateDetailModel
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
    api_instance = workflow_templates_api.WorkflowTemplatesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Workflow Template Id

    # example passing only required values which don't have defaults set
    try:
        # Get a Workflow Template
        api_response = api_instance.workflow_templates_service_get_template(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling WorkflowTemplatesApi->workflow_templates_service_get_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Workflow Template Id |

### Return type

[**WorkflowTemplateDetailModel**](WorkflowTemplateDetailModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Workflow Template. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_templates_service_get_workflow_entities**
> bool, date, datetime, dict, float, int, list, str, none_type workflow_templates_service_get_workflow_entities(id, include_all)

Count of Entities using a Workflow Template

Request the number of entities that use the Workflow Template.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import workflow_templates_api
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
    api_instance = workflow_templates_api.WorkflowTemplatesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Workflow Template Id
    include_all = True # bool | includeAll

    # example passing only required values which don't have defaults set
    try:
        # Count of Entities using a Workflow Template
        api_response = api_instance.workflow_templates_service_get_workflow_entities(id, include_all)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling WorkflowTemplatesApi->workflow_templates_service_get_workflow_entities: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Workflow Template Id |
 **include_all** | **bool**| includeAll |

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
**200** | The number of entities that use the workflow template. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_templates_service_search_template_audit**
> PagingOfWorkflowTemplateAuditModel workflow_templates_service_search_template_audit(id)

Get a Workflow Template Audit List

Search, filter, sort, and page Workflow Template Audits.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import workflow_templates_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.paging_of_workflow_template_audit_model import PagingOfWorkflowTemplateAuditModel
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
    api_instance = workflow_templates_api.WorkflowTemplatesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Workflow Template Id
    is_exporting = True # bool | isExporting (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a Workflow Template Audit List
        api_response = api_instance.workflow_templates_service_search_template_audit(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling WorkflowTemplatesApi->workflow_templates_service_search_template_audit: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a Workflow Template Audit List
        api_response = api_instance.workflow_templates_service_search_template_audit(id, is_exporting=is_exporting, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling WorkflowTemplatesApi->workflow_templates_service_search_template_audit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Workflow Template Id |
 **is_exporting** | **bool**| isExporting | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfWorkflowTemplateAuditModel**](PagingOfWorkflowTemplateAuditModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of Workflow Template Audits. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_templates_service_search_workflow_templates**
> PagingOfWorkflowTemplateDetailModel workflow_templates_service_search_workflow_templates()

Search Workflow Templates

Search, filter, sort, and page Workflow Templates.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import workflow_templates_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.paging_of_workflow_template_detail_model import PagingOfWorkflowTemplateDetailModel
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
    api_instance = workflow_templates_api.WorkflowTemplatesApi(api_client)
    filter_include_inactive = True # bool | IncludeInactive (optional)
    filter_workflow_type = None # bool, date, datetime, dict, float, int, list, str, none_type | WorkflowType (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Workflow Templates
        api_response = api_instance.workflow_templates_service_search_workflow_templates(filter_include_inactive=filter_include_inactive, filter_workflow_type=filter_workflow_type, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling WorkflowTemplatesApi->workflow_templates_service_search_workflow_templates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_include_inactive** | **bool**| IncludeInactive | [optional]
 **filter_workflow_type** | **bool, date, datetime, dict, float, int, list, str, none_type**| WorkflowType | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfWorkflowTemplateDetailModel**](PagingOfWorkflowTemplateDetailModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of Workflow Templates. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_templates_service_stub_workflow_template**
> WorkflowTemplateDetailModel workflow_templates_service_stub_workflow_template()

Get a Workflow Template Stub

Get an empty Workflow Template.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import workflow_templates_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.workflow_template_detail_model import WorkflowTemplateDetailModel
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
    api_instance = workflow_templates_api.WorkflowTemplatesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get a Workflow Template Stub
        api_response = api_instance.workflow_templates_service_stub_workflow_template()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling WorkflowTemplatesApi->workflow_templates_service_stub_workflow_template: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**WorkflowTemplateDetailModel**](WorkflowTemplateDetailModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An Workflow Template. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_templates_service_update_workflow_template**
> WorkflowTemplateDetailModel workflow_templates_service_update_workflow_template(id)

Update a Workflow Template

Update a single Workflow Template by ID.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import workflow_templates_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.workflow_template_detail_model import WorkflowTemplateDetailModel
from secret_server_openapiclient.model.workflow_template_update_model import WorkflowTemplateUpdateModel
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
    api_instance = workflow_templates_api.WorkflowTemplatesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Workflow Template ID
    workflow_template_update_model = WorkflowTemplateUpdateModel(
        active=UpdateFieldValueOfBoolean(
            dirty=True,
            value=True,
        ),
        configuration_json=UpdateFieldValueOfString(
            dirty=True,
            value=None,
        ),
        description=UpdateFieldValueOfString(
            dirty=True,
            value=None,
        ),
        expiration_minutes=UpdateFieldValueOfOptionalInt32(
            dirty=True,
            value=None,
        ),
        is_copy=UpdateFieldValueOfOptionalBoolean(
            dirty=True,
            value=True,
        ),
        name=UpdateFieldValueOfString(
            dirty=True,
            value=None,
        ),
    ) # WorkflowTemplateUpdateModel | Workflow Template update options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a Workflow Template
        api_response = api_instance.workflow_templates_service_update_workflow_template(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling WorkflowTemplatesApi->workflow_templates_service_update_workflow_template: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Workflow Template
        api_response = api_instance.workflow_templates_service_update_workflow_template(id, workflow_template_update_model=workflow_template_update_model)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling WorkflowTemplatesApi->workflow_templates_service_update_workflow_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Workflow Template ID |
 **workflow_template_update_model** | [**WorkflowTemplateUpdateModel**](WorkflowTemplateUpdateModel.md)| Workflow Template update options | [optional]

### Return type

[**WorkflowTemplateDetailModel**](WorkflowTemplateDetailModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Workflow Template. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

