# secret_server_openapiclient.SdkClientRulesApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sdk_client_rules_service_create_client_rule**](SdkClientRulesApi.md#sdk_client_rules_service_create_client_rule) | **POST** /v1/sdk-client-rules | Create New SDK Client Rule
[**sdk_client_rules_service_delete**](SdkClientRulesApi.md#sdk_client_rules_service_delete) | **DELETE** /v1/sdk-client-rules/{id} | Delete SDK Client Rule
[**sdk_client_rules_service_get**](SdkClientRulesApi.md#sdk_client_rules_service_get) | **GET** /v1/sdk-client-rules/{id} | Get SDK Client Rule
[**sdk_client_rules_service_get_onboarding_key**](SdkClientRulesApi.md#sdk_client_rules_service_get_onboarding_key) | **GET** /v1/sdk-client-rules/{id}/onboarding-key | Get Onboarding Key for SDK Client Rule
[**sdk_client_rules_service_search_client_rules**](SdkClientRulesApi.md#sdk_client_rules_service_search_client_rules) | **GET** /v1/sdk-client-rules | Search SDK Client Rules
[**sdk_client_rules_service_stub**](SdkClientRulesApi.md#sdk_client_rules_service_stub) | **GET** /v1/sdk-client-rules/stub | Get SDK Client Rule Stub
[**sdk_client_rules_service_update_client_rule**](SdkClientRulesApi.md#sdk_client_rules_service_update_client_rule) | **PUT** /v1/sdk-client-rules/{id} | Update SDK Client Rule


# **sdk_client_rules_service_create_client_rule**
> SdkClientRuleModel sdk_client_rules_service_create_client_rule()

Create New SDK Client Rule

Create a new SDK Client rule

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import sdk_client_rules_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.sdk_client_rule_create_args import SdkClientRuleCreateArgs
from secret_server_openapiclient.model.sdk_client_rule_model import SdkClientRuleModel
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
    api_instance = sdk_client_rules_api.SdkClientRulesApi(api_client)
    sdk_client_rule_create_args = SdkClientRuleCreateArgs(
        details="details_example",
        name="name_example",
        require_onboarding_key=True,
        user_id=1,
    ) # SdkClientRuleCreateArgs | SDK Client Rule creation options (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create New SDK Client Rule
        api_response = api_instance.sdk_client_rules_service_create_client_rule(sdk_client_rule_create_args=sdk_client_rule_create_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SdkClientRulesApi->sdk_client_rules_service_create_client_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_client_rule_create_args** | [**SdkClientRuleCreateArgs**](SdkClientRuleCreateArgs.md)| SDK Client Rule creation options | [optional]

### Return type

[**SdkClientRuleModel**](SdkClientRuleModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SdkClientRuleModel |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sdk_client_rules_service_delete**
> DeletedModel sdk_client_rules_service_delete(id)

Delete SDK Client Rule

Delete a SDK Client rule by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import sdk_client_rules_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.deleted_model import DeletedModel
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
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
    api_instance = sdk_client_rules_api.SdkClientRulesApi(api_client)
    id = 1 # int | SDK Client Rule Id

    # example passing only required values which don't have defaults set
    try:
        # Delete SDK Client Rule
        api_response = api_instance.sdk_client_rules_service_delete(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SdkClientRulesApi->sdk_client_rules_service_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| SDK Client Rule Id |

### Return type

[**DeletedModel**](DeletedModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DeletedModel |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sdk_client_rules_service_get**
> SdkClientRuleModel sdk_client_rules_service_get(id)

Get SDK Client Rule

Get a single SDK Client rule by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import sdk_client_rules_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.sdk_client_rule_model import SdkClientRuleModel
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
    api_instance = sdk_client_rules_api.SdkClientRulesApi(api_client)
    id = 1 # int | SDK Client Rule Id

    # example passing only required values which don't have defaults set
    try:
        # Get SDK Client Rule
        api_response = api_instance.sdk_client_rules_service_get(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SdkClientRulesApi->sdk_client_rules_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| SDK Client Rule Id |

### Return type

[**SdkClientRuleModel**](SdkClientRuleModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SdkClientRuleModel |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sdk_client_rules_service_get_onboarding_key**
> str sdk_client_rules_service_get_onboarding_key(id)

Get Onboarding Key for SDK Client Rule

Get the onboarding key for a single SDK Client rule by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import sdk_client_rules_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
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
    api_instance = sdk_client_rules_api.SdkClientRulesApi(api_client)
    id = 1 # int | SDK Client Rule Id

    # example passing only required values which don't have defaults set
    try:
        # Get Onboarding Key for SDK Client Rule
        api_response = api_instance.sdk_client_rules_service_get_onboarding_key(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SdkClientRulesApi->sdk_client_rules_service_get_onboarding_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| SDK Client Rule Id |

### Return type

**str**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SdkClientRuleModel |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sdk_client_rules_service_search_client_rules**
> PagingOfSdkClientRuleSummaryAndSdkClientRuleFilter sdk_client_rules_service_search_client_rules()

Search SDK Client Rules

Search, filter, sort, and page app SDK Client rules

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import sdk_client_rules_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.paging_of_sdk_client_rule_summary_and_sdk_client_rule_filter import PagingOfSdkClientRuleSummaryAndSdkClientRuleFilter
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
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
    api_instance = sdk_client_rules_api.SdkClientRulesApi(api_client)
    filter_operator = "filter.operator_example" # str | Operator (optional)
    filter_search_text = "filter.searchText_example" # str | SearchText (optional)
    filter_user_id = 1 # int | UserId (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search SDK Client Rules
        api_response = api_instance.sdk_client_rules_service_search_client_rules(filter_operator=filter_operator, filter_search_text=filter_search_text, filter_user_id=filter_user_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SdkClientRulesApi->sdk_client_rules_service_search_client_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_operator** | **str**| Operator | [optional]
 **filter_search_text** | **str**| SearchText | [optional]
 **filter_user_id** | **int**| UserId | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfSdkClientRuleSummaryAndSdkClientRuleFilter**](PagingOfSdkClientRuleSummaryAndSdkClientRuleFilter.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SDK Client Rule search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sdk_client_rules_service_stub**
> SdkClientRuleModel sdk_client_rules_service_stub()

Get SDK Client Rule Stub

Return the default values for a new SDK Client rule

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import sdk_client_rules_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.sdk_client_rule_model import SdkClientRuleModel
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
    api_instance = sdk_client_rules_api.SdkClientRulesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get SDK Client Rule Stub
        api_response = api_instance.sdk_client_rules_service_stub()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SdkClientRulesApi->sdk_client_rules_service_stub: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SdkClientRuleModel**](SdkClientRuleModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SdkClientRuleModel |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sdk_client_rules_service_update_client_rule**
> SdkClientRuleModel sdk_client_rules_service_update_client_rule(id)

Update SDK Client Rule

Update a single SDK Client rule by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import sdk_client_rules_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.sdk_client_rule_model import SdkClientRuleModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.sdk_client_rule_update_args import SdkClientRuleUpdateArgs
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
    api_instance = sdk_client_rules_api.SdkClientRulesApi(api_client)
    id = 1 # int | SDK Client Rule Id
    sdk_client_rule_update_args = SdkClientRuleUpdateArgs(
        details="details_example",
        name="name_example",
        require_onboarding_key=True,
        user_id=1,
    ) # SdkClientRuleUpdateArgs | SDK Client Rule update options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update SDK Client Rule
        api_response = api_instance.sdk_client_rules_service_update_client_rule(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SdkClientRulesApi->sdk_client_rules_service_update_client_rule: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update SDK Client Rule
        api_response = api_instance.sdk_client_rules_service_update_client_rule(id, sdk_client_rule_update_args=sdk_client_rule_update_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling SdkClientRulesApi->sdk_client_rules_service_update_client_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| SDK Client Rule Id |
 **sdk_client_rule_update_args** | [**SdkClientRuleUpdateArgs**](SdkClientRuleUpdateArgs.md)| SDK Client Rule update options | [optional]

### Return type

[**SdkClientRuleModel**](SdkClientRuleModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SdkClientRuleModel |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

