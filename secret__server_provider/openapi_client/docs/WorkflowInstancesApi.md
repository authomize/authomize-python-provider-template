# plugins.WorkflowInstancesApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workflow_instances_service_get_by_template_id**](WorkflowInstancesApi.md#workflow_instances_service_get_by_template_id) | **GET** /v1/workflows/instances/template/{id} | Get Workflow Instances By Workflow Template Id.


# **workflow_instances_service_get_by_template_id**
> [WorkflowInstanceDto] workflow_instances_service_get_by_template_id(id)

Get Workflow Instances By Workflow Template Id.

Get active workflow instances that use the given workflow template

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import workflow_instances_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.workflow_instance_dto import WorkflowInstanceDto
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
    api_instance = workflow_instances_api.WorkflowInstancesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Workflow Template ID

    # example passing only required values which don't have defaults set
    try:
        # Get Workflow Instances By Workflow Template Id.
        api_response = api_instance.workflow_instances_service_get_by_template_id(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling WorkflowInstancesApi->workflow_instances_service_get_by_template_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Workflow Template ID |

### Return type

[**[WorkflowInstanceDto]**](WorkflowInstanceDto.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The active workflow instances that use the Workflow Template |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

