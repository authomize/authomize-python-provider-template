# plugins.OneTimePasswordCodeApi

All URIs are relative to *https://integrations.secretservercloud.com//api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**one_time_password_code_service_get**](OneTimePasswordCodeApi.md#one_time_password_code_service_get) | **GET** /v1/one-time-password-code/{id} | Get one time password code and seconds


# **one_time_password_code_service_get**
> [OneTimePasswordCodeModel] one_time_password_code_service_get(id)

Get one time password code and seconds

Get one time password code by secret id

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import one_time_password_code_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.one_time_password_code_model import OneTimePasswordCodeModel
from pprint import pprint
# Defining the host is optional and defaults to https://integrations.secretservercloud.com//api
# See configuration.py for a list of all supported configuration parameters.
configuration = plugins.Configuration(
    host = "https://integrations.secretservercloud.com//api"
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
    api_instance = one_time_password_code_api.OneTimePasswordCodeApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret ID
    number_of_codes_to_generate = None # bool, date, datetime, dict, float, int, list, str, none_type | NumberOfCodesToGenerate (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get one time password code and seconds
        api_response = api_instance.one_time_password_code_service_get(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling OneTimePasswordCodeApi->one_time_password_code_service_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get one time password code and seconds
        api_response = api_instance.one_time_password_code_service_get(id, number_of_codes_to_generate=number_of_codes_to_generate)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling OneTimePasswordCodeApi->one_time_password_code_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret ID |
 **number_of_codes_to_generate** | **bool, date, datetime, dict, float, int, list, str, none_type**| NumberOfCodesToGenerate | [optional]

### Return type

[**[OneTimePasswordCodeModel]**](OneTimePasswordCodeModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | One time password code model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

