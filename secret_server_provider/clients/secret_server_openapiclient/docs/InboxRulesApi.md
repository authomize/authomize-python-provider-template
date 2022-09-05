# secret_server_openapiclient.InboxRulesApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inbox_rules_service_copy_inbox_rule**](InboxRulesApi.md#inbox_rules_service_copy_inbox_rule) | **POST** /v1/inbox-rules/copy | Copy Inbox Rule
[**inbox_rules_service_create_inbox_rule**](InboxRulesApi.md#inbox_rules_service_create_inbox_rule) | **POST** /v1/inbox-rules | Create Inbox Rule
[**inbox_rules_service_create_inbox_rule_condition**](InboxRulesApi.md#inbox_rules_service_create_inbox_rule_condition) | **POST** /v1/inbox-rules/{inboxRuleId}/conditions | Create Inbox Rule Condition
[**inbox_rules_service_get_inbox_rule**](InboxRulesApi.md#inbox_rules_service_get_inbox_rule) | **GET** /v1/inbox-rules/{id} | Get Inbox Rule
[**inbox_rules_service_get_inbox_rule_condition**](InboxRulesApi.md#inbox_rules_service_get_inbox_rule_condition) | **GET** /v1/inbox-rules/conditions/{id} | Get Inbox Rule Condition
[**inbox_rules_service_get_inbox_rule_stub**](InboxRulesApi.md#inbox_rules_service_get_inbox_rule_stub) | **GET** /v1/inbox-rules/stub | Get Inbox Rule Stub
[**inbox_rules_service_patch_inbox_rule**](InboxRulesApi.md#inbox_rules_service_patch_inbox_rule) | **PATCH** /v1/inbox-rules/{id} | Patch Inbox Rule
[**inbox_rules_service_patch_inbox_rule_actions**](InboxRulesApi.md#inbox_rules_service_patch_inbox_rule_actions) | **PATCH** /v1/inbox-rules/{id}/actions | Patch Inbox Rule Actions
[**inbox_rules_service_patch_inbox_rule_subscribers**](InboxRulesApi.md#inbox_rules_service_patch_inbox_rule_subscribers) | **PATCH** /v1/inbox-rules/{ruleId}/subscribers | Patch Inbox Rule Subscribers
[**inbox_rules_service_search_inbox_rule_conditions**](InboxRulesApi.md#inbox_rules_service_search_inbox_rule_conditions) | **GET** /v1/inbox-rules/{id}/conditions | Search Inbox Rule Conditions
[**inbox_rules_service_search_inbox_rules**](InboxRulesApi.md#inbox_rules_service_search_inbox_rules) | **GET** /v1/inbox-rules | Search inbox rules
[**inbox_rules_service_search_log**](InboxRulesApi.md#inbox_rules_service_search_log) | **GET** /v1/inbox-rules/{inboxRuleId}/action-log | Get Inbox Rule Logs By Inbox Rule Id
[**inbox_rules_service_search_subscribers**](InboxRulesApi.md#inbox_rules_service_search_subscribers) | **GET** /v1/inbox-rules/{inboxRuleId}/subscribers | Search inbox rule subscribers
[**inbox_rules_service_subscribe_current_user_to_rule**](InboxRulesApi.md#inbox_rules_service_subscribe_current_user_to_rule) | **POST** /v1/inbox-rules/{ruleId}/subscribe | Subscribe Current User
[**inbox_rules_service_unsubscribe_current_user_from_rule**](InboxRulesApi.md#inbox_rules_service_unsubscribe_current_user_from_rule) | **DELETE** /v1/inbox-rules/{ruleId}/subscribe | Unsubscribe current user
[**inbox_rules_service_update_inbox_rule_condition**](InboxRulesApi.md#inbox_rules_service_update_inbox_rule_condition) | **PUT** /v1/inbox-rules/{inboxRuleId}/conditions | Update Inbox Rule Condition


# **inbox_rules_service_copy_inbox_rule**
> InboxRuleDetailModel inbox_rules_service_copy_inbox_rule()

Copy Inbox Rule

Copy an inbox rule

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import inbox_rules_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.inbox_rule_detail_model import InboxRuleDetailModel
from secret_server_openapiclient.model.inbox_rule_copy_args import InboxRuleCopyArgs
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
    api_instance = inbox_rules_api.InboxRulesApi(api_client)
    inbox_rule_copy_args = InboxRuleCopyArgs(
        data=InboxRuleCopyModel(
            inbox_rule_id_to_copy=1,
            name="name_example",
        ),
    ) # InboxRuleCopyArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Copy Inbox Rule
        api_response = api_instance.inbox_rules_service_copy_inbox_rule(inbox_rule_copy_args=inbox_rule_copy_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling InboxRulesApi->inbox_rules_service_copy_inbox_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_rule_copy_args** | [**InboxRuleCopyArgs**](InboxRuleCopyArgs.md)| args | [optional]

### Return type

[**InboxRuleDetailModel**](InboxRuleDetailModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inbox Rule |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_rules_service_create_inbox_rule**
> InboxRuleDetailModel inbox_rules_service_create_inbox_rule()

Create Inbox Rule

Create a new inbox rule

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import inbox_rules_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.inbox_rule_detail_model import InboxRuleDetailModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.inbox_rule_create_args import InboxRuleCreateArgs
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
    api_instance = inbox_rules_api.InboxRulesApi(api_client)
    inbox_rule_create_args = InboxRuleCreateArgs(
        data=InboxRuleCreateModel(
            active=True,
            can_edit_own_subscription=True,
            conditions=[
                InboxRuleConditionCreateModel(
                    display_value="display_value_example",
                    inbox_data_id=1,
                    inbox_rule_id=1,
                    inbox_rule_operand=InboxRuleConditionOperand("{}"),
                    value_bool=True,
                    value_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    value_int=1,
                    value_string="value_string_example",
                ),
            ],
            high_priority=True,
            inbox_email_template_id=1,
            inbox_message_type_ids=[
                1,
            ],
            inbox_slack_template_id=1,
            is_immediate=True,
            name="name_example",
            send_email=True,
            send_slack=True,
        ),
    ) # InboxRuleCreateArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Inbox Rule
        api_response = api_instance.inbox_rules_service_create_inbox_rule(inbox_rule_create_args=inbox_rule_create_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling InboxRulesApi->inbox_rules_service_create_inbox_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_rule_create_args** | [**InboxRuleCreateArgs**](InboxRuleCreateArgs.md)| args | [optional]

### Return type

[**InboxRuleDetailModel**](InboxRuleDetailModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inbox Rule |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_rules_service_create_inbox_rule_condition**
> InboxRuleConditionDetailModel inbox_rules_service_create_inbox_rule_condition(inbox_rule_id)

Create Inbox Rule Condition

Create a new inbox rule condition

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import inbox_rules_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.inbox_rule_condition_create_args import InboxRuleConditionCreateArgs
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.inbox_rule_condition_detail_model import InboxRuleConditionDetailModel
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
    api_instance = inbox_rules_api.InboxRulesApi(api_client)
    inbox_rule_id = 1 # int | inboxRuleId
    inbox_rule_condition_create_args = InboxRuleConditionCreateArgs(
        data=InboxRuleConditionCreateModel(
            display_value="display_value_example",
            inbox_data_id=1,
            inbox_rule_id=1,
            inbox_rule_operand=InboxRuleConditionOperand("{}"),
            value_bool=True,
            value_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            value_int=1,
            value_string="value_string_example",
        ),
    ) # InboxRuleConditionCreateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Inbox Rule Condition
        api_response = api_instance.inbox_rules_service_create_inbox_rule_condition(inbox_rule_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling InboxRulesApi->inbox_rules_service_create_inbox_rule_condition: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Inbox Rule Condition
        api_response = api_instance.inbox_rules_service_create_inbox_rule_condition(inbox_rule_id, inbox_rule_condition_create_args=inbox_rule_condition_create_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling InboxRulesApi->inbox_rules_service_create_inbox_rule_condition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_rule_id** | **int**| inboxRuleId |
 **inbox_rule_condition_create_args** | [**InboxRuleConditionCreateArgs**](InboxRuleConditionCreateArgs.md)| args | [optional]

### Return type

[**InboxRuleConditionDetailModel**](InboxRuleConditionDetailModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inbox Rule Condition |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_rules_service_get_inbox_rule**
> InboxRuleDetailModel inbox_rules_service_get_inbox_rule(id)

Get Inbox Rule

Retrieve inbox rule by Id

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import inbox_rules_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.inbox_rule_detail_model import InboxRuleDetailModel
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
    api_instance = inbox_rules_api.InboxRulesApi(api_client)
    id = 1 # int | id

    # example passing only required values which don't have defaults set
    try:
        # Get Inbox Rule
        api_response = api_instance.inbox_rules_service_get_inbox_rule(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling InboxRulesApi->inbox_rules_service_get_inbox_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id |

### Return type

[**InboxRuleDetailModel**](InboxRuleDetailModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inbox Rule |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_rules_service_get_inbox_rule_condition**
> InboxRuleConditionDetailModel inbox_rules_service_get_inbox_rule_condition(id)

Get Inbox Rule Condition

Retrieve inbox rule condition by Id

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import inbox_rules_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.inbox_rule_condition_detail_model import InboxRuleConditionDetailModel
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
    api_instance = inbox_rules_api.InboxRulesApi(api_client)
    id = 1 # int | id

    # example passing only required values which don't have defaults set
    try:
        # Get Inbox Rule Condition
        api_response = api_instance.inbox_rules_service_get_inbox_rule_condition(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling InboxRulesApi->inbox_rules_service_get_inbox_rule_condition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id |

### Return type

[**InboxRuleConditionDetailModel**](InboxRuleConditionDetailModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inbox Rule Condition |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_rules_service_get_inbox_rule_stub**
> InboxRuleDetailModel inbox_rules_service_get_inbox_rule_stub()

Get Inbox Rule Stub

Retrieve an empty inbox rule

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import inbox_rules_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.inbox_rule_detail_model import InboxRuleDetailModel
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
    api_instance = inbox_rules_api.InboxRulesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Inbox Rule Stub
        api_response = api_instance.inbox_rules_service_get_inbox_rule_stub()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling InboxRulesApi->inbox_rules_service_get_inbox_rule_stub: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**InboxRuleDetailModel**](InboxRuleDetailModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inbox Rule |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_rules_service_patch_inbox_rule**
> InboxRuleDetailModel inbox_rules_service_patch_inbox_rule(id)

Patch Inbox Rule

Change properties of an inbox rule

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import inbox_rules_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.inbox_rule_detail_model import InboxRuleDetailModel
from secret_server_openapiclient.model.inbox_rule_patch_args import InboxRulePatchArgs
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
    api_instance = inbox_rules_api.InboxRulesApi(api_client)
    id = 1 # int | id
    inbox_rule_patch_args = InboxRulePatchArgs(
        data=InboxRulePatchModel(
            active=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            can_edit_own_subscription=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            high_priority=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            inbox_message_types=UpdateFieldValueOfInt32Array(
                dirty=True,
                value=[
                    1,
                ],
            ),
            is_immediate=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            name=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
        ),
    ) # InboxRulePatchArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Patch Inbox Rule
        api_response = api_instance.inbox_rules_service_patch_inbox_rule(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling InboxRulesApi->inbox_rules_service_patch_inbox_rule: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Patch Inbox Rule
        api_response = api_instance.inbox_rules_service_patch_inbox_rule(id, inbox_rule_patch_args=inbox_rule_patch_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling InboxRulesApi->inbox_rules_service_patch_inbox_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id |
 **inbox_rule_patch_args** | [**InboxRulePatchArgs**](InboxRulePatchArgs.md)| args | [optional]

### Return type

[**InboxRuleDetailModel**](InboxRuleDetailModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inbox Rule |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_rules_service_patch_inbox_rule_actions**
> InboxRuleDetailModel inbox_rules_service_patch_inbox_rule_actions(id)

Patch Inbox Rule Actions

Change Inbox Rule Actions

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import inbox_rules_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.inbox_rule_detail_model import InboxRuleDetailModel
from secret_server_openapiclient.model.inbox_rule_action_patch_args import InboxRuleActionPatchArgs
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
    api_instance = inbox_rules_api.InboxRulesApi(api_client)
    id = 1 # int | id
    inbox_rule_action_patch_args = InboxRuleActionPatchArgs(
        data=InboxRuleActionPatchModel(
            inbox_email_template_id=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=1,
            ),
            inbox_slack_template_id=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=1,
            ),
            send_email=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            send_slack=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
        ),
    ) # InboxRuleActionPatchArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Patch Inbox Rule Actions
        api_response = api_instance.inbox_rules_service_patch_inbox_rule_actions(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling InboxRulesApi->inbox_rules_service_patch_inbox_rule_actions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Patch Inbox Rule Actions
        api_response = api_instance.inbox_rules_service_patch_inbox_rule_actions(id, inbox_rule_action_patch_args=inbox_rule_action_patch_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling InboxRulesApi->inbox_rules_service_patch_inbox_rule_actions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id |
 **inbox_rule_action_patch_args** | [**InboxRuleActionPatchArgs**](InboxRuleActionPatchArgs.md)| args | [optional]

### Return type

[**InboxRuleDetailModel**](InboxRuleDetailModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inbox Rule |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_rules_service_patch_inbox_rule_subscribers**
> InboxRuleSubscriberUpdateResponse inbox_rules_service_patch_inbox_rule_subscribers(rule_id)

Patch Inbox Rule Subscribers

Add, Remove, or unsubscribe groups, users, and external emails to a specific rule

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import inbox_rules_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.inbox_rule_subscribers_patch_args import InboxRuleSubscribersPatchArgs
from secret_server_openapiclient.model.inbox_rule_subscriber_update_response import InboxRuleSubscriberUpdateResponse
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
    api_instance = inbox_rules_api.InboxRulesApi(api_client)
    rule_id = 1 # int | ruleId
    inbox_rule_subscribers_patch_args = InboxRuleSubscribersPatchArgs(
        data=InboxRuleSubscriberPatchModel(
            email_updates=[
                InboxRuleSubscriberEmailUpdate(
                    email_address="email_address_example",
                    subscribe=True,
                ),
            ],
            group_user_updates=[
                InboxRuleSubscriberGroupUserUpdate(
                    group_id=1,
                    subscribe=True,
                    user_id=1,
                ),
            ],
        ),
    ) # InboxRuleSubscribersPatchArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Patch Inbox Rule Subscribers
        api_response = api_instance.inbox_rules_service_patch_inbox_rule_subscribers(rule_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling InboxRulesApi->inbox_rules_service_patch_inbox_rule_subscribers: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Patch Inbox Rule Subscribers
        api_response = api_instance.inbox_rules_service_patch_inbox_rule_subscribers(rule_id, inbox_rule_subscribers_patch_args=inbox_rule_subscribers_patch_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling InboxRulesApi->inbox_rules_service_patch_inbox_rule_subscribers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **int**| ruleId |
 **inbox_rule_subscribers_patch_args** | [**InboxRuleSubscribersPatchArgs**](InboxRuleSubscribersPatchArgs.md)| args | [optional]

### Return type

[**InboxRuleSubscriberUpdateResponse**](InboxRuleSubscriberUpdateResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_rules_service_search_inbox_rule_conditions**
> InboxRuleConditionSummary inbox_rules_service_search_inbox_rule_conditions(id)

Search Inbox Rule Conditions

Search Inbox Rule Conditions

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import inbox_rules_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.inbox_rule_condition_summary import InboxRuleConditionSummary
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
    api_instance = inbox_rules_api.InboxRulesApi(api_client)
    id = 1 # int | id

    # example passing only required values which don't have defaults set
    try:
        # Search Inbox Rule Conditions
        api_response = api_instance.inbox_rules_service_search_inbox_rule_conditions(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling InboxRulesApi->inbox_rules_service_search_inbox_rule_conditions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id |

### Return type

[**InboxRuleConditionSummary**](InboxRuleConditionSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inbox Rule Conditions |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_rules_service_search_inbox_rules**
> PagingOfInboxRuleSummary inbox_rules_service_search_inbox_rules()

Search inbox rules

Search, filter, sort, and page inbox rules

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import inbox_rules_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.paging_of_inbox_rule_summary import PagingOfInboxRuleSummary
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
    api_instance = inbox_rules_api.InboxRulesApi(api_client)
    filter_include_current_user_subscription_status = True # bool | Return the subscription status of the current user whether subscribed directly or via a group. (optional)
    filter_include_inactive = True # bool | Include inactive rules. (optional)
    filter_is_immediate = True # bool | Only return rules that run immediately or on a schedule, depending on value. (optional)
    filter_message_id = 1 # int | Return all rules that will apply to this message id, does not account for time or schedule. (optional)
    filter_message_type_id = 1 # int | Only return rules that apply to this message type.  If a MessageId is passed then this value will be replaced with that message's MessageTypeId. (optional)
    rule_condition_filters_0_display_value = "ruleConditionFilters[0].displayValue_example" # str | Search specifically display values (optional)
    rule_condition_filters_0_inbox_data_id = 1 # int | Which field is being searched.  This value can be null if InboxDataName is passed instead. (optional)
    rule_condition_filters_0_inbox_data_name = "ruleConditionFilters[0].inboxDataName_example" # str | Which field is being searched.  If InboxDataId is passed this value is ignored. (optional)
    rule_condition_filters_0_value_bool = True # bool | Search specifically for boolean values (optional)
    rule_condition_filters_0_value_int = 1 # int | Search specifically for int values (optional)
    rule_condition_filters_0_value_string = "ruleConditionFilters[0].valueString_example" # str | Search specifically for string values with a partial match (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search inbox rules
        api_response = api_instance.inbox_rules_service_search_inbox_rules(filter_include_current_user_subscription_status=filter_include_current_user_subscription_status, filter_include_inactive=filter_include_inactive, filter_is_immediate=filter_is_immediate, filter_message_id=filter_message_id, filter_message_type_id=filter_message_type_id, rule_condition_filters_0_display_value=rule_condition_filters_0_display_value, rule_condition_filters_0_inbox_data_id=rule_condition_filters_0_inbox_data_id, rule_condition_filters_0_inbox_data_name=rule_condition_filters_0_inbox_data_name, rule_condition_filters_0_value_bool=rule_condition_filters_0_value_bool, rule_condition_filters_0_value_int=rule_condition_filters_0_value_int, rule_condition_filters_0_value_string=rule_condition_filters_0_value_string, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling InboxRulesApi->inbox_rules_service_search_inbox_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_include_current_user_subscription_status** | **bool**| Return the subscription status of the current user whether subscribed directly or via a group. | [optional]
 **filter_include_inactive** | **bool**| Include inactive rules. | [optional]
 **filter_is_immediate** | **bool**| Only return rules that run immediately or on a schedule, depending on value. | [optional]
 **filter_message_id** | **int**| Return all rules that will apply to this message id, does not account for time or schedule. | [optional]
 **filter_message_type_id** | **int**| Only return rules that apply to this message type.  If a MessageId is passed then this value will be replaced with that message&#39;s MessageTypeId. | [optional]
 **rule_condition_filters_0_display_value** | **str**| Search specifically display values | [optional]
 **rule_condition_filters_0_inbox_data_id** | **int**| Which field is being searched.  This value can be null if InboxDataName is passed instead. | [optional]
 **rule_condition_filters_0_inbox_data_name** | **str**| Which field is being searched.  If InboxDataId is passed this value is ignored. | [optional]
 **rule_condition_filters_0_value_bool** | **bool**| Search specifically for boolean values | [optional]
 **rule_condition_filters_0_value_int** | **int**| Search specifically for int values | [optional]
 **rule_condition_filters_0_value_string** | **str**| Search specifically for string values with a partial match | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfInboxRuleSummary**](PagingOfInboxRuleSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inbox Rules results |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_rules_service_search_log**
> PagingOfInboxRuleLogSummary inbox_rules_service_search_log(inbox_rule_id)

Get Inbox Rule Logs By Inbox Rule Id

Get Inbox Rule Logs By Inbox Rule Id

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import inbox_rules_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.paging_of_inbox_rule_log_summary import PagingOfInboxRuleLogSummary
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
    api_instance = inbox_rules_api.InboxRulesApi(api_client)
    inbox_rule_id = 1 # int | inboxRuleId
    filter_end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | EndDate (optional)
    filter_rule_action_status = "filter.ruleActionStatus_example" # str | RuleActionStatus (optional)
    filter_start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | StartDate (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Inbox Rule Logs By Inbox Rule Id
        api_response = api_instance.inbox_rules_service_search_log(inbox_rule_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling InboxRulesApi->inbox_rules_service_search_log: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Inbox Rule Logs By Inbox Rule Id
        api_response = api_instance.inbox_rules_service_search_log(inbox_rule_id, filter_end_date=filter_end_date, filter_rule_action_status=filter_rule_action_status, filter_start_date=filter_start_date, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling InboxRulesApi->inbox_rules_service_search_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_rule_id** | **int**| inboxRuleId |
 **filter_end_date** | **datetime**| EndDate | [optional]
 **filter_rule_action_status** | **str**| RuleActionStatus | [optional]
 **filter_start_date** | **datetime**| StartDate | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfInboxRuleLogSummary**](PagingOfInboxRuleLogSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inbox Rule Log results |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_rules_service_search_subscribers**
> PagingOfInboxRuleSubscriberSummary inbox_rules_service_search_subscribers(inbox_rule_id)

Search inbox rule subscribers

Search, filter, sort, and page inbox subscribers

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import inbox_rules_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.paging_of_inbox_rule_subscriber_summary import PagingOfInboxRuleSubscriberSummary
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
    api_instance = inbox_rules_api.InboxRulesApi(api_client)
    inbox_rule_id = 1 # int | inboxRuleId
    filter_account_types = "filter.accountTypes_example" # str | AccountTypes (optional)
    filter_only_include_unsubscribable_users = True # bool | This will ignore most other filters and return only User accounts that belong to groups that are subscribed.  The results will not include users that are directly subscribed as they must be removed from the subscription, not unsubscribed. (optional)
    filter_search_text = "filter.searchText_example" # str | Search text to filter users from the unsubscribable users (optional)
    filter_status = "filter.status_example" # str | Status (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search inbox rule subscribers
        api_response = api_instance.inbox_rules_service_search_subscribers(inbox_rule_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling InboxRulesApi->inbox_rules_service_search_subscribers: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search inbox rule subscribers
        api_response = api_instance.inbox_rules_service_search_subscribers(inbox_rule_id, filter_account_types=filter_account_types, filter_only_include_unsubscribable_users=filter_only_include_unsubscribable_users, filter_search_text=filter_search_text, filter_status=filter_status, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling InboxRulesApi->inbox_rules_service_search_subscribers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_rule_id** | **int**| inboxRuleId |
 **filter_account_types** | **str**| AccountTypes | [optional]
 **filter_only_include_unsubscribable_users** | **bool**| This will ignore most other filters and return only User accounts that belong to groups that are subscribed.  The results will not include users that are directly subscribed as they must be removed from the subscription, not unsubscribed. | [optional]
 **filter_search_text** | **str**| Search text to filter users from the unsubscribable users | [optional]
 **filter_status** | **str**| Status | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfInboxRuleSubscriberSummary**](PagingOfInboxRuleSubscriberSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inbox Rule Subscriber results |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_rules_service_subscribe_current_user_to_rule**
> InboxRuleSubscriptionUpdateResponse inbox_rules_service_subscribe_current_user_to_rule(rule_id)

Subscribe Current User

Subscribe the current user from the rule

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import inbox_rules_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.inbox_rule_subscription_update_response import InboxRuleSubscriptionUpdateResponse
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
    api_instance = inbox_rules_api.InboxRulesApi(api_client)
    rule_id = 1 # int | ruleId

    # example passing only required values which don't have defaults set
    try:
        # Subscribe Current User
        api_response = api_instance.inbox_rules_service_subscribe_current_user_to_rule(rule_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling InboxRulesApi->inbox_rules_service_subscribe_current_user_to_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **int**| ruleId |

### Return type

[**InboxRuleSubscriptionUpdateResponse**](InboxRuleSubscriptionUpdateResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response if successful |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_rules_service_unsubscribe_current_user_from_rule**
> InboxRuleSubscriptionUpdateResponse inbox_rules_service_unsubscribe_current_user_from_rule(rule_id)

Unsubscribe current user

Unsubscribe the current user from the rule

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import inbox_rules_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.inbox_rule_subscription_update_response import InboxRuleSubscriptionUpdateResponse
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
    api_instance = inbox_rules_api.InboxRulesApi(api_client)
    rule_id = 1 # int | ruleId

    # example passing only required values which don't have defaults set
    try:
        # Unsubscribe current user
        api_response = api_instance.inbox_rules_service_unsubscribe_current_user_from_rule(rule_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling InboxRulesApi->inbox_rules_service_unsubscribe_current_user_from_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **int**| ruleId |

### Return type

[**InboxRuleSubscriptionUpdateResponse**](InboxRuleSubscriptionUpdateResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response if successful |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_rules_service_update_inbox_rule_condition**
> InboxRuleDetailModel inbox_rules_service_update_inbox_rule_condition(inbox_rule_id)

Update Inbox Rule Condition

Update inbox rule condition

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import inbox_rules_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.inbox_rule_detail_model import InboxRuleDetailModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.inbox_rule_condition_update_args import InboxRuleConditionUpdateArgs
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
    api_instance = inbox_rules_api.InboxRulesApi(api_client)
    inbox_rule_id = 1 # int | inboxRuleId
    inbox_rule_condition_update_args = InboxRuleConditionUpdateArgs(
        data=[
            InboxRuleConditionUpdateModel(
                display_value="display_value_example",
                inbox_data_id=1,
                inbox_rule_condition_id=1,
                inbox_rule_operand=InboxRuleConditionOperand("{}"),
                value_bool=True,
                value_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                value_int=1,
                value_string="value_string_example",
            ),
        ],
    ) # InboxRuleConditionUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Inbox Rule Condition
        api_response = api_instance.inbox_rules_service_update_inbox_rule_condition(inbox_rule_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling InboxRulesApi->inbox_rules_service_update_inbox_rule_condition: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Inbox Rule Condition
        api_response = api_instance.inbox_rules_service_update_inbox_rule_condition(inbox_rule_id, inbox_rule_condition_update_args=inbox_rule_condition_update_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling InboxRulesApi->inbox_rules_service_update_inbox_rule_condition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_rule_id** | **int**| inboxRuleId |
 **inbox_rule_condition_update_args** | [**InboxRuleConditionUpdateArgs**](InboxRuleConditionUpdateArgs.md)| args | [optional]

### Return type

[**InboxRuleDetailModel**](InboxRuleDetailModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inbox Rule |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

