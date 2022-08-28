# secret_server_openapiclient.EnterpriseApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enterprise_service_get_request_data**](EnterpriseApi.md#enterprise_service_get_request_data) | **GET** /v1/enterprise/search-request/{requestId} | GetRequestData
[**enterprise_service_search_request_data**](EnterpriseApi.md#enterprise_service_search_request_data) | **POST** /v1/enterprise/search-request | Request Enterprise Data


# **enterprise_service_get_request_data**
> EnterpriseSearchResultModel enterprise_service_get_request_data(request_id)

GetRequestData

Retrieve Enterprise Search Request Data

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import enterprise_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.enterprise_search_result_model import EnterpriseSearchResultModel
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
    api_instance = enterprise_api.EnterpriseApi(api_client)
    request_id = None # bool, date, datetime, dict, float, int, list, str, none_type | requestId

    # example passing only required values which don't have defaults set
    try:
        # GetRequestData
        api_response = api_instance.enterprise_service_get_request_data(request_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling EnterpriseApi->enterprise_service_get_request_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| requestId |

### Return type

[**EnterpriseSearchResultModel**](EnterpriseSearchResultModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | EnterpriseSummaryModel for given TaskId |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprise_service_search_request_data**
> EnterpriseSearchRequestModel enterprise_service_search_request_data()

Request Enterprise Data

Initiate a search request for Enterprise Data

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import enterprise_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.enterprise_search_request_args import EnterpriseSearchRequestArgs
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.enterprise_search_request_model import EnterpriseSearchRequestModel
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
    api_instance = enterprise_api.EnterpriseApi(api_client)
    enterprise_search_request_args = EnterpriseSearchRequestArgs(
        data=EnterpriseSearchRequestFilter(
            end_date=None,
            enterprise_name=None,
            request_fields=[
                EnterpriseSearchRequestFieldModel(
                    field_name=None,
                    field_value=None,
                ),
            ],
            start_date=None,
        ),
    ) # EnterpriseSearchRequestArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Request Enterprise Data
        api_response = api_instance.enterprise_service_search_request_data(enterprise_search_request_args=enterprise_search_request_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling EnterpriseApi->enterprise_service_search_request_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise_search_request_args** | [**EnterpriseSearchRequestArgs**](EnterpriseSearchRequestArgs.md)| args | [optional]

### Return type

[**EnterpriseSearchRequestModel**](EnterpriseSearchRequestModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Model of request |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

