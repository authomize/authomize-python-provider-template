# secret_server_openapiclient.ActivationsApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activations_service_activate**](ActivationsApi.md#activations_service_activate) | **POST** /v1/activations | Perform an online activation of Secret Server


# **activations_service_activate**
> bool activations_service_activate()

Perform an online activation of Secret Server

Perform an online activation of Secret Server

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import activations_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.online_activation_args import OnlineActivationArgs
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
    api_instance = activations_api.ActivationsApi(api_client)
    online_activation_args = OnlineActivationArgs(
        email=None,
        name=None,
        phone_number=None,
    ) # OnlineActivationArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Perform an online activation of Secret Server
        api_response = api_instance.activations_service_activate(online_activation_args=online_activation_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ActivationsApi->activations_service_activate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **online_activation_args** | [**OnlineActivationArgs**](OnlineActivationArgs.md)| args | [optional]

### Return type

**bool**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Activation result |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

