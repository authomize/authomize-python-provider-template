# plugins.BulkOperationsApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_operations_service_get_progress**](BulkOperationsApi.md#bulk_operations_service_get_progress) | **GET** /v1/bulk-operations/{id}/progress | Progress


# **bulk_operations_service_get_progress**
> BulkOperationProgressModel bulk_operations_service_get_progress(id)

Progress

Get the progress of a bulk operation by id.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import bulk_operations_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.bulk_operation_progress_model import BulkOperationProgressModel
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
    api_instance = bulk_operations_api.BulkOperationsApi(api_client)
    id = "id_example" # str | Id of Bulk operation to retrieve.

    # example passing only required values which don't have defaults set
    try:
        # Progress
        api_response = api_instance.bulk_operations_service_get_progress(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling BulkOperationsApi->bulk_operations_service_get_progress: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of Bulk operation to retrieve. |

### Return type

[**BulkOperationProgressModel**](BulkOperationProgressModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BulkOperationProgressModel object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

