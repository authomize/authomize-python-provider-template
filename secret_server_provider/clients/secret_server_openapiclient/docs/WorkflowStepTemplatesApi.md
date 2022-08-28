# secret_server_openapiclient.WorkflowStepTemplatesApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workflow_step_templates_service_create_step**](WorkflowStepTemplatesApi.md#workflow_step_templates_service_create_step) | **POST** /v1/workflows/templates/{id}/steps | Create Workflow Step
[**workflow_step_templates_service_get_template_step**](WorkflowStepTemplatesApi.md#workflow_step_templates_service_get_template_step) | **GET** /v1/workflows/templates/{id}/steps/{stepNum} | Get a Workflow Template Step
[**workflow_step_templates_service_get_template_steps**](WorkflowStepTemplatesApi.md#workflow_step_templates_service_get_template_steps) | **GET** /v1/workflows/templates/{id}/steps | Get Workflow Template Steps
[**workflow_step_templates_service_stub**](WorkflowStepTemplatesApi.md#workflow_step_templates_service_stub) | **GET** /v1/workflows/templates/steps/stub | Get a Workflow Template Step Stub
[**workflow_step_templates_service_update_step**](WorkflowStepTemplatesApi.md#workflow_step_templates_service_update_step) | **PUT** /v1/workflows/templates/{id}/steps | Update Workflow Template Steps
[**workflow_step_templates_service_update_step_model**](WorkflowStepTemplatesApi.md#workflow_step_templates_service_update_step_model) | **PUT** /v1/workflows/templates/{id}/steps/{stepNum} | Update a Workflow Template Step


# **workflow_step_templates_service_create_step**
> bool, date, datetime, dict, float, int, list, str, none_type workflow_step_templates_service_create_step(id)

Create Workflow Step

Create a step for a Workflow Template

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import workflow_step_templates_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.workflow_step_template_create_args import WorkflowStepTemplateCreateArgs
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
    api_instance = workflow_step_templates_api.WorkflowStepTemplatesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Workflow Template Id
    workflow_step_template_create_args = WorkflowStepTemplateCreateArgs(
        configuration=AccessRequestStepConfigurationModel(
            approver_groups=[
                AccessReviewerModel(
                    access_reviewer_id=None,
                    display_name=None,
                    group_id=None,
                    is_owner=True,
                    is_user=True,
                    workflow_step_template_id=None,
                    workflow_template_id=None,
                ),
            ],
            approve_step=None,
            expire_step=None,
            num_approvals_required=None,
        ),
        name=None,
        order=None,
        workflow_template_id=None,
    ) # WorkflowStepTemplateCreateArgs | Workflow Template Step creation options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Workflow Step
        api_response = api_instance.workflow_step_templates_service_create_step(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling WorkflowStepTemplatesApi->workflow_step_templates_service_create_step: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Workflow Step
        api_response = api_instance.workflow_step_templates_service_create_step(id, workflow_step_template_create_args=workflow_step_template_create_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling WorkflowStepTemplatesApi->workflow_step_templates_service_create_step: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Workflow Template Id |
 **workflow_step_template_create_args** | [**WorkflowStepTemplateCreateArgs**](WorkflowStepTemplateCreateArgs.md)| Workflow Template Step creation options | [optional]

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
**200** | New Workflow Template Steps ID |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_step_templates_service_get_template_step**
> WorkflowStepTemplateDetailModel workflow_step_templates_service_get_template_step(id, step_num)

Get a Workflow Template Step

Get a step for a workflow template

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import workflow_step_templates_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.workflow_step_template_detail_model import WorkflowStepTemplateDetailModel
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
    api_instance = workflow_step_templates_api.WorkflowStepTemplatesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Workflow Template Id
    step_num = None # bool, date, datetime, dict, float, int, list, str, none_type | Workflow Step Number

    # example passing only required values which don't have defaults set
    try:
        # Get a Workflow Template Step
        api_response = api_instance.workflow_step_templates_service_get_template_step(id, step_num)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling WorkflowStepTemplatesApi->workflow_step_templates_service_get_template_step: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Workflow Template Id |
 **step_num** | **bool, date, datetime, dict, float, int, list, str, none_type**| Workflow Step Number |

### Return type

[**WorkflowStepTemplateDetailModel**](WorkflowStepTemplateDetailModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A workflow step model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_step_templates_service_get_template_steps**
> PagingOfWorkflowStepTemplateDetailModel workflow_step_templates_service_get_template_steps(id)

Get Workflow Template Steps

Get all the steps for a workflow template

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import workflow_step_templates_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.paging_of_workflow_step_template_detail_model import PagingOfWorkflowStepTemplateDetailModel
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
    api_instance = workflow_step_templates_api.WorkflowStepTemplatesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Workflow Template ID
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Workflow Template Steps
        api_response = api_instance.workflow_step_templates_service_get_template_steps(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling WorkflowStepTemplatesApi->workflow_step_templates_service_get_template_steps: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Workflow Template Steps
        api_response = api_instance.workflow_step_templates_service_get_template_steps(id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling WorkflowStepTemplatesApi->workflow_step_templates_service_get_template_steps: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Workflow Template ID |
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfWorkflowStepTemplateDetailModel**](PagingOfWorkflowStepTemplateDetailModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of workflow step models |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_step_templates_service_stub**
> WorkflowTemplateDetailModel workflow_step_templates_service_stub()

Get a Workflow Template Step Stub

Get an empty Workflow Template Step

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import workflow_step_templates_api
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
    api_instance = workflow_step_templates_api.WorkflowStepTemplatesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get a Workflow Template Step Stub
        api_response = api_instance.workflow_step_templates_service_stub()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling WorkflowStepTemplatesApi->workflow_step_templates_service_stub: %s\n" % e)
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
**200** | An empty workflow step |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_step_templates_service_update_step**
> [WorkflowStepTemplateDetailModel] workflow_step_templates_service_update_step(id)

Update Workflow Template Steps

Update the steps for a workflow template

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import workflow_step_templates_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.workflow_step_template_update_args import WorkflowStepTemplateUpdateArgs
from secret_server_openapiclient.model.workflow_step_template_detail_model import WorkflowStepTemplateDetailModel
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
    api_instance = workflow_step_templates_api.WorkflowStepTemplatesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Workflow Template ID
    workflow_step_template_update_args = WorkflowStepTemplateUpdateArgs(
        workflow_step_templates=[
            WorkflowStepTemplateDetailModel(
                configuration=AccessRequestStepConfigurationModel(
                    approver_groups=[
                        AccessReviewerModel(
                            access_reviewer_id=None,
                            display_name=None,
                            group_id=None,
                            is_owner=True,
                            is_user=True,
                            workflow_step_template_id=None,
                            workflow_template_id=None,
                        ),
                    ],
                    approve_step=None,
                    expire_step=None,
                    num_approvals_required=None,
                ),
                expiration_minutes=None,
                name=None,
                order=None,
                workflow_step_template_id=None,
                workflow_template_id=None,
            ),
        ],
    ) # WorkflowStepTemplateUpdateArgs | Workflow Template Steps creation options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Workflow Template Steps
        api_response = api_instance.workflow_step_templates_service_update_step(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling WorkflowStepTemplatesApi->workflow_step_templates_service_update_step: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Workflow Template Steps
        api_response = api_instance.workflow_step_templates_service_update_step(id, workflow_step_template_update_args=workflow_step_template_update_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling WorkflowStepTemplatesApi->workflow_step_templates_service_update_step: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Workflow Template ID |
 **workflow_step_template_update_args** | [**WorkflowStepTemplateUpdateArgs**](WorkflowStepTemplateUpdateArgs.md)| Workflow Template Steps creation options | [optional]

### Return type

[**[WorkflowStepTemplateDetailModel]**](WorkflowStepTemplateDetailModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The workflow template steps |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflow_step_templates_service_update_step_model**
> WorkflowStepTemplateDetailModel workflow_step_templates_service_update_step_model(id, step_num)

Update a Workflow Template Step

Updates a single Workflow Template Step by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import workflow_step_templates_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.workflow_step_template_update_model import WorkflowStepTemplateUpdateModel
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.workflow_step_template_detail_model import WorkflowStepTemplateDetailModel
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
    api_instance = workflow_step_templates_api.WorkflowStepTemplatesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Workflow Template ID
    step_num = None # bool, date, datetime, dict, float, int, list, str, none_type | Workflow Step Number
    workflow_step_template_update_model = WorkflowStepTemplateUpdateModel(
        configuration=AccessRequestStepConfigurationModel(
            approver_groups=[
                AccessReviewerModel(
                    access_reviewer_id=None,
                    display_name=None,
                    group_id=None,
                    is_owner=True,
                    is_user=True,
                    workflow_step_template_id=None,
                    workflow_template_id=None,
                ),
            ],
            approve_step=None,
            expire_step=None,
            num_approvals_required=None,
        ),
        expiration_minutes=None,
        name=None,
        order=None,
        workflow_step_template_id=None,
    ) # WorkflowStepTemplateUpdateModel | Workflow Template update options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a Workflow Template Step
        api_response = api_instance.workflow_step_templates_service_update_step_model(id, step_num)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling WorkflowStepTemplatesApi->workflow_step_templates_service_update_step_model: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Workflow Template Step
        api_response = api_instance.workflow_step_templates_service_update_step_model(id, step_num, workflow_step_template_update_model=workflow_step_template_update_model)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling WorkflowStepTemplatesApi->workflow_step_templates_service_update_step_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Workflow Template ID |
 **step_num** | **bool, date, datetime, dict, float, int, list, str, none_type**| Workflow Step Number |
 **workflow_step_template_update_model** | [**WorkflowStepTemplateUpdateModel**](WorkflowStepTemplateUpdateModel.md)| Workflow Template update options | [optional]

### Return type

[**WorkflowStepTemplateDetailModel**](WorkflowStepTemplateDetailModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workflow Template Step |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

