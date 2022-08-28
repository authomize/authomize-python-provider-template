# plugins.SlackApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slack_service_get_configuration_v3**](SlackApi.md#slack_service_get_configuration_v3) | **GET** /v3/slack-configuration | Get Slack Configuration
[**slack_service_handle_event**](SlackApi.md#slack_service_handle_event) | **POST** /v1/slack/event | Slack Event
[**slack_service_handle_interaction**](SlackApi.md#slack_service_handle_interaction) | **POST** /v1/slack/interaction | Slack Interaction
[**slack_service_send_test_slack_message**](SlackApi.md#slack_service_send_test_slack_message) | **GET** /v2/slack-test | Test Slack Configuration
[**slack_service_update_configuration_v3**](SlackApi.md#slack_service_update_configuration_v3) | **PUT** /v3/slack-configuration | Slack Configuration


# **slack_service_get_configuration_v3**
> SlackConfigurationModelV2 slack_service_get_configuration_v3()

Get Slack Configuration

Fetches the Slack configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import slack_api
from plugins.model.slack_configuration_model_v2 import SlackConfigurationModelV2
from plugins.model.internal_server_error_response import InternalServerErrorResponse
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
    api_instance = slack_api.SlackApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Slack Configuration
        api_response = api_instance.slack_service_get_configuration_v3()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SlackApi->slack_service_get_configuration_v3: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SlackConfigurationModelV2**](SlackConfigurationModelV2.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slack_service_handle_event**
> SlackResponse slack_service_handle_event()

Slack Event

Slack event endpoint that only Slack can call, does source validation

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import slack_api
from plugins.model.slack_response import SlackResponse
from plugins.model.internal_server_error_response import InternalServerErrorResponse
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
    api_instance = slack_api.SlackApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Slack Event
        api_response = api_instance.slack_service_handle_event()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SlackApi->slack_service_handle_event: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SlackResponse**](SlackResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slack_service_handle_interaction**
> SlackResponse slack_service_handle_interaction()

Slack Interaction

Slack interation endpoint that only Slack can call, does source validation

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import slack_api
from plugins.model.slack_response import SlackResponse
from plugins.model.internal_server_error_response import InternalServerErrorResponse
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
    api_instance = slack_api.SlackApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Slack Interaction
        api_response = api_instance.slack_service_handle_interaction()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SlackApi->slack_service_handle_interaction: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SlackResponse**](SlackResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slack_service_send_test_slack_message**
> SlackConfigurationTestResultModel slack_service_send_test_slack_message()

Test Slack Configuration

Sends a test Slack message to test the Slack configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import slack_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.slack_configuration_test_result_model import SlackConfigurationTestResultModel
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
    api_instance = slack_api.SlackApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Test Slack Configuration
        api_response = api_instance.slack_service_send_test_slack_message()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SlackApi->slack_service_send_test_slack_message: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SlackConfigurationTestResultModel**](SlackConfigurationTestResultModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slack_service_update_configuration_v3**
> SlackConfigurationModelV2 slack_service_update_configuration_v3()

Slack Configuration

Updates the Slack configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import slack_api
from plugins.model.slack_configuration_model_v2 import SlackConfigurationModelV2
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.slack_configuration_update_args_v2 import SlackConfigurationUpdateArgsV2
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
    api_instance = slack_api.SlackApi(api_client)
    slack_configuration_update_args_v2 = SlackConfigurationUpdateArgsV2(
        data=SlackConfigurationUpdateModelV2(
            app_id=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            bot_token=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            inbox_notifications_enabled=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            secret_interactions_enabled=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            signature_key=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
        ),
    ) # SlackConfigurationUpdateArgsV2 | Slack Configuration Update Options (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Slack Configuration
        api_response = api_instance.slack_service_update_configuration_v3(slack_configuration_update_args_v2=slack_configuration_update_args_v2)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SlackApi->slack_service_update_configuration_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slack_configuration_update_args_v2** | [**SlackConfigurationUpdateArgsV2**](SlackConfigurationUpdateArgsV2.md)| Slack Configuration Update Options | [optional]

### Return type

[**SlackConfigurationModelV2**](SlackConfigurationModelV2.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

