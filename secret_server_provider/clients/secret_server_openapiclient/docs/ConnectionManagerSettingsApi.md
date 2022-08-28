# secret_server_openapiclient.ConnectionManagerSettingsApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connection_manager_settings_service_get**](ConnectionManagerSettingsApi.md#connection_manager_settings_service_get) | **GET** /v1/connection-manager-settings | Get Connection Manager Settings


# **connection_manager_settings_service_get**
> ConnectionManagerSettingsModel connection_manager_settings_service_get()

Get Connection Manager Settings

Get Connection Manager Settings

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import connection_manager_settings_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.connection_manager_settings_model import ConnectionManagerSettingsModel
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
    api_instance = connection_manager_settings_api.ConnectionManagerSettingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Connection Manager Settings
        api_response = api_instance.connection_manager_settings_service_get()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling ConnectionManagerSettingsApi->connection_manager_settings_service_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConnectionManagerSettingsModel**](ConnectionManagerSettingsModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connection Manager Settings |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

