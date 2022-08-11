# plugins.VersionApi

All URIs are relative to *https://integrations.secretservercloud.com//api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**version_service_get**](VersionApi.md#version_service_get) | **GET** /v1/version | Secret Server Version


# **version_service_get**
> VersionSummary version_service_get()

Secret Server Version

Retrieve Secret Server Version

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import version_api
from plugins.model.version_summary import VersionSummary
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
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
    api_instance = version_api.VersionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Secret Server Version
        api_response = api_instance.version_service_get()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling VersionApi->version_service_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**VersionSummary**](VersionSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Version Summary |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

