# secret_server_openapiclient.ExtendedFieldsApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extended_fields_service_get_regex_by_secret**](ExtendedFieldsApi.md#extended_fields_service_get_regex_by_secret) | **GET** /v1/extended-fields/regex/{secretId} | Get Extended Regex values by Secret


# **extended_fields_service_get_regex_by_secret**
> RegexValuesSummary extended_fields_service_get_regex_by_secret(secret_id)

Get Extended Regex values by Secret

Retrieve Extended Regex values for a Secret

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import extended_fields_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.regex_values_summary import RegexValuesSummary
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
    api_instance = extended_fields_api.ExtendedFieldsApi(api_client)
    secret_id = 1 # int | secretId

    # example passing only required values which don't have defaults set
    try:
        # Get Extended Regex values by Secret
        api_response = api_instance.extended_fields_service_get_regex_by_secret(secret_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ExtendedFieldsApi->extended_fields_service_get_regex_by_secret: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_id** | **int**| secretId |

### Return type

[**RegexValuesSummary**](RegexValuesSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Regex Values Summary |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

