# plugins.InboxApi

All URIs are relative to *https://integrations.secretservercloud.com//api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inbox_service_copy_inbox_template**](InboxApi.md#inbox_service_copy_inbox_template) | **POST** /v1/inbox/templates/copy | Copy an  inbox template
[**inbox_service_create_inbox_template**](InboxApi.md#inbox_service_create_inbox_template) | **POST** /v1/inbox/templates | Create inbox template
[**inbox_service_create_inbox_template_locale**](InboxApi.md#inbox_service_create_inbox_template_locale) | **POST** /v1/inbox/templates/template-locale | Create inbox template locale
[**inbox_service_delete_resource**](InboxApi.md#inbox_service_delete_resource) | **DELETE** /v1/inbox/templates/resources/{id} | Delete inbox resource
[**inbox_service_get_inbox_message**](InboxApi.md#inbox_service_get_inbox_message) | **GET** /v1/inbox/message/{messageId} | Get Inbox Message by Id
[**inbox_service_get_inbox_message_data_names**](InboxApi.md#inbox_service_get_inbox_message_data_names) | **GET** /v1/inbox/data-names | Inbox Message Type Data Names
[**inbox_service_get_inbox_message_types**](InboxApi.md#inbox_service_get_inbox_message_types) | **GET** /v1/inbox/message-types | Get inbox message types
[**inbox_service_get_inbox_template**](InboxApi.md#inbox_service_get_inbox_template) | **GET** /v1/inbox/templates/{templateId} | Get inbox template
[**inbox_service_get_inbox_template_locale**](InboxApi.md#inbox_service_get_inbox_template_locale) | **GET** /v1/inbox/templates/{templateId}/locales/{localeId} | Get inbox template locale
[**inbox_service_get_inbox_templates**](InboxApi.md#inbox_service_get_inbox_templates) | **GET** /v1/inbox/templates | Get inbox templates
[**inbox_service_get_notifications**](InboxApi.md#inbox_service_get_notifications) | **GET** /v1/notifications | Get inbox notifications
[**inbox_service_get_notifications_status**](InboxApi.md#inbox_service_get_notifications_status) | **GET** /v1/notifications/status | Notification Status
[**inbox_service_get_resource**](InboxApi.md#inbox_service_get_resource) | **GET** /v1/inbox/templates/resources/{id} | Get inbox resource
[**inbox_service_mark_alert_notification_read**](InboxApi.md#inbox_service_mark_alert_notification_read) | **POST** /v1/notifications/notification-read | Mark alert notification as read
[**inbox_service_mark_alert_notification_unread**](InboxApi.md#inbox_service_mark_alert_notification_unread) | **POST** /v1/notifications/notification-unread | Mark alert notification as unread
[**inbox_service_patch_inbox_template**](InboxApi.md#inbox_service_patch_inbox_template) | **PATCH** /v1/inbox/templates/{templateId} | Patch inbox template
[**inbox_service_patch_inbox_template_locale**](InboxApi.md#inbox_service_patch_inbox_template_locale) | **PATCH** /v1/inbox/templates/{templateId}/locales/{localeId} | Patch inbox template locale
[**inbox_service_search_inbox_messages**](InboxApi.md#inbox_service_search_inbox_messages) | **GET** /v1/inbox/messages/{messageTypeId?} | Search inbox messages
[**inbox_service_search_resources**](InboxApi.md#inbox_service_search_resources) | **GET** /v1/inbox/templates/resources | Get inbox resources
[**inbox_service_send_test_message**](InboxApi.md#inbox_service_send_test_message) | **POST** /v1/inbox/send-test-message | Send Test Inbox Message
[**inbox_service_update_message_read_status**](InboxApi.md#inbox_service_update_message_read_status) | **POST** /v1/inbox/update-read | Mark messages read or unread
[**inbox_service_upload_resource**](InboxApi.md#inbox_service_upload_resource) | **PUT** /v1/inbox/templates/resources | Upload an embedded resource


# **inbox_service_copy_inbox_template**
> InboxTemplateDetailModel inbox_service_copy_inbox_template()

Copy an  inbox template

Create a copy of an inbox template

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import inbox_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.inbox_template_copy_args import InboxTemplateCopyArgs
from plugins.model.inbox_template_detail_model import InboxTemplateDetailModel
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
    api_instance = inbox_api.InboxApi(api_client)
    inbox_template_copy_args = InboxTemplateCopyArgs(
        data=InboxTemplateCopyModel(
            inbox_template_id_to_copy=None,
            name=None,
        ),
    ) # InboxTemplateCopyArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Copy an  inbox template
        api_response = api_instance.inbox_service_copy_inbox_template(inbox_template_copy_args=inbox_template_copy_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling InboxApi->inbox_service_copy_inbox_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_template_copy_args** | [**InboxTemplateCopyArgs**](InboxTemplateCopyArgs.md)| args | [optional]

### Return type

[**InboxTemplateDetailModel**](InboxTemplateDetailModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inbox Template Details |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_service_create_inbox_template**
> InboxTemplateDetailModel inbox_service_create_inbox_template()

Create inbox template

Create inbox template

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import inbox_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.inbox_template_create_args import InboxTemplateCreateArgs
from plugins.model.inbox_template_detail_model import InboxTemplateDetailModel
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
    api_instance = inbox_api.InboxApi(api_client)
    inbox_template_create_args = InboxTemplateCreateArgs(
        data=InboxTemplateCreateModel(
            template_name=None,
            template_type=InboxTemplateType("{}"),
        ),
    ) # InboxTemplateCreateArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create inbox template
        api_response = api_instance.inbox_service_create_inbox_template(inbox_template_create_args=inbox_template_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling InboxApi->inbox_service_create_inbox_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_template_create_args** | [**InboxTemplateCreateArgs**](InboxTemplateCreateArgs.md)| args | [optional]

### Return type

[**InboxTemplateDetailModel**](InboxTemplateDetailModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inbox Template Details |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_service_create_inbox_template_locale**
> InboxTemplateLocaleModel inbox_service_create_inbox_template_locale()

Create inbox template locale

Create inbox template locale

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import inbox_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.inbox_template_locale_create_args import InboxTemplateLocaleCreateArgs
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.inbox_template_locale_model import InboxTemplateLocaleModel
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
    api_instance = inbox_api.InboxApi(api_client)
    inbox_template_locale_create_args = InboxTemplateLocaleCreateArgs(
        data=InboxTemplateLocaleCreateModel(
            inbox_template_id=None,
            locale_culture_id=None,
            subject=None,
            template_body=None,
        ),
    ) # InboxTemplateLocaleCreateArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create inbox template locale
        api_response = api_instance.inbox_service_create_inbox_template_locale(inbox_template_locale_create_args=inbox_template_locale_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling InboxApi->inbox_service_create_inbox_template_locale: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_template_locale_create_args** | [**InboxTemplateLocaleCreateArgs**](InboxTemplateLocaleCreateArgs.md)| args | [optional]

### Return type

[**InboxTemplateLocaleModel**](InboxTemplateLocaleModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inbox Template Locale |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_service_delete_resource**
> InboxResourceDeleteResponse inbox_service_delete_resource(id)

Delete inbox resource

Delete inbox resource

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import inbox_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.inbox_resource_delete_response import InboxResourceDeleteResponse
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
    api_instance = inbox_api.InboxApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id

    # example passing only required values which don't have defaults set
    try:
        # Delete inbox resource
        api_response = api_instance.inbox_service_delete_resource(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling InboxApi->inbox_service_delete_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |

### Return type

[**InboxResourceDeleteResponse**](InboxResourceDeleteResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success message |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_service_get_inbox_message**
> InboxMessageSummary inbox_service_get_inbox_message(message_id)

Get Inbox Message by Id

Gets the message summary by id

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import inbox_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.inbox_message_summary import InboxMessageSummary
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
    api_instance = inbox_api.InboxApi(api_client)
    message_id = None # bool, date, datetime, dict, float, int, list, str, none_type | messageId

    # example passing only required values which don't have defaults set
    try:
        # Get Inbox Message by Id
        api_response = api_instance.inbox_service_get_inbox_message(message_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling InboxApi->inbox_service_get_inbox_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| messageId |

### Return type

[**InboxMessageSummary**](InboxMessageSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inbox Message |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_service_get_inbox_message_data_names**
> [InboxData] inbox_service_get_inbox_message_data_names()

Inbox Message Type Data Names

Get the data names by type for inbox messages

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import inbox_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.inbox_data import InboxData
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
    api_instance = inbox_api.InboxApi(api_client)
    message_type_ids = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | messageTypeIds (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Inbox Message Type Data Names
        api_response = api_instance.inbox_service_get_inbox_message_data_names(message_type_ids=message_type_ids)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling InboxApi->inbox_service_get_inbox_message_data_names: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_type_ids** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| messageTypeIds | [optional]

### Return type

[**[InboxData]**](InboxData.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inbox Message results |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_service_get_inbox_message_types**
> [InboxMessageTypeSummary] inbox_service_get_inbox_message_types()

Get inbox message types

Get inbox message types

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import inbox_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.inbox_message_type_summary import InboxMessageTypeSummary
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
    api_instance = inbox_api.InboxApi(api_client)
    include_current_user_message_counts = True # bool | When true the number of each message type the current user has will be added to the response and only message types with a count > 0 will be returned. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get inbox message types
        api_response = api_instance.inbox_service_get_inbox_message_types(include_current_user_message_counts=include_current_user_message_counts)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling InboxApi->inbox_service_get_inbox_message_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_current_user_message_counts** | **bool**| When true the number of each message type the current user has will be added to the response and only message types with a count &gt; 0 will be returned. | [optional]

### Return type

[**[InboxMessageTypeSummary]**](InboxMessageTypeSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Message Types |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_service_get_inbox_template**
> InboxTemplateDetailModel inbox_service_get_inbox_template(template_id)

Get inbox template

Get inbox template

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import inbox_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.inbox_template_detail_model import InboxTemplateDetailModel
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
    api_instance = inbox_api.InboxApi(api_client)
    template_id = None # bool, date, datetime, dict, float, int, list, str, none_type | templateId

    # example passing only required values which don't have defaults set
    try:
        # Get inbox template
        api_response = api_instance.inbox_service_get_inbox_template(template_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling InboxApi->inbox_service_get_inbox_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| templateId |

### Return type

[**InboxTemplateDetailModel**](InboxTemplateDetailModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inbox Template Details |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_service_get_inbox_template_locale**
> InboxTemplateLocaleModel inbox_service_get_inbox_template_locale(locale_id, template_id)

Get inbox template locale

Get inbox template locale

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import inbox_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.inbox_template_locale_model import InboxTemplateLocaleModel
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
    api_instance = inbox_api.InboxApi(api_client)
    locale_id = None # bool, date, datetime, dict, float, int, list, str, none_type | localeId
    template_id = None # bool, date, datetime, dict, float, int, list, str, none_type | templateId

    # example passing only required values which don't have defaults set
    try:
        # Get inbox template locale
        api_response = api_instance.inbox_service_get_inbox_template_locale(locale_id, template_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling InboxApi->inbox_service_get_inbox_template_locale: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locale_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| localeId |
 **template_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| templateId |

### Return type

[**InboxTemplateLocaleModel**](InboxTemplateLocaleModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inbox Template Locale |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_service_get_inbox_templates**
> PagingOfInboxTemplateModel inbox_service_get_inbox_templates()

Get inbox templates

Get, sort, and page inbox templates

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import inbox_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_inbox_template_model import PagingOfInboxTemplateModel
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
    api_instance = inbox_api.InboxApi(api_client)
    filter_template_type = None # bool, date, datetime, dict, float, int, list, str, none_type | Only return templates of this type.  When null returns all types (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get inbox templates
        api_response = api_instance.inbox_service_get_inbox_templates(filter_template_type=filter_template_type, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling InboxApi->inbox_service_get_inbox_templates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_template_type** | **bool, date, datetime, dict, float, int, list, str, none_type**| Only return templates of this type.  When null returns all types | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfInboxTemplateModel**](PagingOfInboxTemplateModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inbox Template results |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_service_get_notifications**
> AlertNotificationsWrapper inbox_service_get_notifications()

Get inbox notifications

Get inbox notifications

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import inbox_api
from plugins.model.alert_notifications_wrapper import AlertNotificationsWrapper
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
    api_instance = inbox_api.InboxApi(api_client)
    include_archived = True # bool | includeArchived (optional)
    mark_alerts_as_viewed = True # bool | markAlertsAsViewed (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get inbox notifications
        api_response = api_instance.inbox_service_get_notifications(include_archived=include_archived, mark_alerts_as_viewed=mark_alerts_as_viewed)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling InboxApi->inbox_service_get_notifications: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_archived** | **bool**| includeArchived | [optional]
 **mark_alerts_as_viewed** | **bool**| markAlertsAsViewed | [optional]

### Return type

[**AlertNotificationsWrapper**](AlertNotificationsWrapper.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Notifications with returned count and indication of new notifications |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_service_get_notifications_status**
> NotificationStatusModel inbox_service_get_notifications_status()

Notification Status

Get the notification status

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import inbox_api
from plugins.model.notification_status_model import NotificationStatusModel
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
    api_instance = inbox_api.InboxApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Notification Status
        api_response = api_instance.inbox_service_get_notifications_status()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling InboxApi->inbox_service_get_notifications_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**NotificationStatusModel**](NotificationStatusModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Indication of whether the system has alerts and the last checked time |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_service_get_resource**
> InboxResourceData inbox_service_get_resource(id)

Get inbox resource

Get inbox resource

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import inbox_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.inbox_resource_data import InboxResourceData
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
    api_instance = inbox_api.InboxApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id

    # example passing only required values which don't have defaults set
    try:
        # Get inbox resource
        api_response = api_instance.inbox_service_get_resource(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling InboxApi->inbox_service_get_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |

### Return type

[**InboxResourceData**](InboxResourceData.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inbox Resource Data |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_service_mark_alert_notification_read**
> bool inbox_service_mark_alert_notification_read()

Mark alert notification as read

Mark alert notification as read

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import inbox_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.alert_notification_read_event_args import AlertNotificationReadEventArgs
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
    api_instance = inbox_api.InboxApi(api_client)
    alert_notification_read_event_args = AlertNotificationReadEventArgs(
        notification_id=None,
    ) # AlertNotificationReadEventArgs | model (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Mark alert notification as read
        api_response = api_instance.inbox_service_mark_alert_notification_read(alert_notification_read_event_args=alert_notification_read_event_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling InboxApi->inbox_service_mark_alert_notification_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_notification_read_event_args** | [**AlertNotificationReadEventArgs**](AlertNotificationReadEventArgs.md)| model | [optional]

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
**200** | Success |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_service_mark_alert_notification_unread**
> bool inbox_service_mark_alert_notification_unread()

Mark alert notification as unread

Mark alert notification as unread

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import inbox_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.alert_notification_unread_event_args import AlertNotificationUnreadEventArgs
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
    api_instance = inbox_api.InboxApi(api_client)
    alert_notification_unread_event_args = AlertNotificationUnreadEventArgs(
        notification_id=None,
    ) # AlertNotificationUnreadEventArgs | model (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Mark alert notification as unread
        api_response = api_instance.inbox_service_mark_alert_notification_unread(alert_notification_unread_event_args=alert_notification_unread_event_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling InboxApi->inbox_service_mark_alert_notification_unread: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_notification_unread_event_args** | [**AlertNotificationUnreadEventArgs**](AlertNotificationUnreadEventArgs.md)| model | [optional]

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
**200** | Success |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_service_patch_inbox_template**
> InboxTemplateDetailModel inbox_service_patch_inbox_template(template_id)

Patch inbox template

Patch inbox template

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import inbox_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.inbox_template_detail_model import InboxTemplateDetailModel
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.inbox_template_update_args import InboxTemplateUpdateArgs
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
    api_instance = inbox_api.InboxApi(api_client)
    template_id = None # bool, date, datetime, dict, float, int, list, str, none_type | templateId
    inbox_template_update_args = InboxTemplateUpdateArgs(
        data=InboxTemplateUpdateModel(
            template_name=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            template_type=UpdateFieldValueOfInboxTemplateType(
                dirty=True,
                value=InboxTemplateType("{}"),
            ),
        ),
    ) # InboxTemplateUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Patch inbox template
        api_response = api_instance.inbox_service_patch_inbox_template(template_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling InboxApi->inbox_service_patch_inbox_template: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Patch inbox template
        api_response = api_instance.inbox_service_patch_inbox_template(template_id, inbox_template_update_args=inbox_template_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling InboxApi->inbox_service_patch_inbox_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| templateId |
 **inbox_template_update_args** | [**InboxTemplateUpdateArgs**](InboxTemplateUpdateArgs.md)| args | [optional]

### Return type

[**InboxTemplateDetailModel**](InboxTemplateDetailModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inbox Template Details |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_service_patch_inbox_template_locale**
> InboxTemplateLocaleModel inbox_service_patch_inbox_template_locale(locale_id, template_id)

Patch inbox template locale

Patch inbox template locale

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import inbox_api
from plugins.model.inbox_template_locale_update_args import InboxTemplateLocaleUpdateArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.inbox_template_locale_model import InboxTemplateLocaleModel
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
    api_instance = inbox_api.InboxApi(api_client)
    locale_id = None # bool, date, datetime, dict, float, int, list, str, none_type | localeId
    template_id = None # bool, date, datetime, dict, float, int, list, str, none_type | templateId
    inbox_template_locale_update_args = InboxTemplateLocaleUpdateArgs(
        data=InboxTemplateLocaleUpdateModel(
            subject=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            template_body=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
        ),
    ) # InboxTemplateLocaleUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Patch inbox template locale
        api_response = api_instance.inbox_service_patch_inbox_template_locale(locale_id, template_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling InboxApi->inbox_service_patch_inbox_template_locale: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Patch inbox template locale
        api_response = api_instance.inbox_service_patch_inbox_template_locale(locale_id, template_id, inbox_template_locale_update_args=inbox_template_locale_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling InboxApi->inbox_service_patch_inbox_template_locale: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locale_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| localeId |
 **template_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| templateId |
 **inbox_template_locale_update_args** | [**InboxTemplateLocaleUpdateArgs**](InboxTemplateLocaleUpdateArgs.md)| args | [optional]

### Return type

[**InboxTemplateLocaleModel**](InboxTemplateLocaleModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inbox Template Locale |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_service_search_inbox_messages**
> PagingOfInboxMessageSummary inbox_service_search_inbox_messages()

Search inbox messages

Search, filter, sort, and page inbox messages

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import inbox_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_inbox_message_summary import PagingOfInboxMessageSummary
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
    api_instance = inbox_api.InboxApi(api_client)
    message_type_id = None # bool, date, datetime, dict, float, int, list, str, none_type | messageTypeId (optional)
    filter_end_date = None # bool, date, datetime, dict, float, int, list, str, none_type | EndDate (optional)
    message_data_filters_0_display_value = None # bool, date, datetime, dict, float, int, list, str, none_type | Search specifically display values (optional)
    message_data_filters_0_inbox_data_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Which field is being searched (optional)
    message_data_filters_0_value_bool = True # bool | Search specifically for boolean values (optional)
    message_data_filters_0_value_date_time_end = None # bool, date, datetime, dict, float, int, list, str, none_type | Search specifically for date values less than this date (optional)
    message_data_filters_0_value_date_time_start = None # bool, date, datetime, dict, float, int, list, str, none_type | Search specifically for date values greater than this date (optional)
    message_data_filters_0_value_int = None # bool, date, datetime, dict, float, int, list, str, none_type | Search specifically for int values (optional)
    message_data_filters_0_value_string = None # bool, date, datetime, dict, float, int, list, str, none_type | Search specifically for string values (optional)
    filter_message_type_ids = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | MessageTypeIds (optional)
    filter_read_status_filter = None # bool, date, datetime, dict, float, int, list, str, none_type | ReadStatusFilter (optional)
    filter_start_date = None # bool, date, datetime, dict, float, int, list, str, none_type | StartDate (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search inbox messages
        api_response = api_instance.inbox_service_search_inbox_messages(message_type_id=message_type_id, filter_end_date=filter_end_date, message_data_filters_0_display_value=message_data_filters_0_display_value, message_data_filters_0_inbox_data_name=message_data_filters_0_inbox_data_name, message_data_filters_0_value_bool=message_data_filters_0_value_bool, message_data_filters_0_value_date_time_end=message_data_filters_0_value_date_time_end, message_data_filters_0_value_date_time_start=message_data_filters_0_value_date_time_start, message_data_filters_0_value_int=message_data_filters_0_value_int, message_data_filters_0_value_string=message_data_filters_0_value_string, filter_message_type_ids=filter_message_type_ids, filter_read_status_filter=filter_read_status_filter, filter_start_date=filter_start_date, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling InboxApi->inbox_service_search_inbox_messages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_type_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| messageTypeId | [optional]
 **filter_end_date** | **bool, date, datetime, dict, float, int, list, str, none_type**| EndDate | [optional]
 **message_data_filters_0_display_value** | **bool, date, datetime, dict, float, int, list, str, none_type**| Search specifically display values | [optional]
 **message_data_filters_0_inbox_data_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Which field is being searched | [optional]
 **message_data_filters_0_value_bool** | **bool**| Search specifically for boolean values | [optional]
 **message_data_filters_0_value_date_time_end** | **bool, date, datetime, dict, float, int, list, str, none_type**| Search specifically for date values less than this date | [optional]
 **message_data_filters_0_value_date_time_start** | **bool, date, datetime, dict, float, int, list, str, none_type**| Search specifically for date values greater than this date | [optional]
 **message_data_filters_0_value_int** | **bool, date, datetime, dict, float, int, list, str, none_type**| Search specifically for int values | [optional]
 **message_data_filters_0_value_string** | **bool, date, datetime, dict, float, int, list, str, none_type**| Search specifically for string values | [optional]
 **filter_message_type_ids** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| MessageTypeIds | [optional]
 **filter_read_status_filter** | **bool, date, datetime, dict, float, int, list, str, none_type**| ReadStatusFilter | [optional]
 **filter_start_date** | **bool, date, datetime, dict, float, int, list, str, none_type**| StartDate | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfInboxMessageSummary**](PagingOfInboxMessageSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inbox Message results |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_service_search_resources**
> PagingOfInboxResourceSummary inbox_service_search_resources()

Get inbox resources

Get, sort, and page inbox resources

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import inbox_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_inbox_resource_summary import PagingOfInboxResourceSummary
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
    api_instance = inbox_api.InboxApi(api_client)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get inbox resources
        api_response = api_instance.inbox_service_search_resources(skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling InboxApi->inbox_service_search_resources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfInboxResourceSummary**](PagingOfInboxResourceSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inbox Resource Results |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_service_send_test_message**
> InboxTestMessageResult inbox_service_send_test_message()

Send Test Inbox Message

Send a test message to another user that will appear in their inbox.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import inbox_api
from plugins.model.inbox_test_message_args import InboxTestMessageArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.inbox_test_message_result import InboxTestMessageResult
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
    api_instance = inbox_api.InboxApi(api_client)
    inbox_test_message_args = InboxTestMessageArgs(
        data=InboxTestMessageModel(
            group_id=None,
            message=None,
            subject=None,
        ),
    ) # InboxTestMessageArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send Test Inbox Message
        api_response = api_instance.inbox_service_send_test_message(inbox_test_message_args=inbox_test_message_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling InboxApi->inbox_service_send_test_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_test_message_args** | [**InboxTestMessageArgs**](InboxTestMessageArgs.md)| args | [optional]

### Return type

[**InboxTestMessageResult**](InboxTestMessageResult.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success if the message was published for processing |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_service_update_message_read_status**
> bool inbox_service_update_message_read_status()

Mark messages read or unread

Mark messages read or unread

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import inbox_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.inbox_message_set_message_read_status_args import InboxMessageSetMessageReadStatusArgs
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
    api_instance = inbox_api.InboxApi(api_client)
    inbox_message_set_message_read_status_args = InboxMessageSetMessageReadStatusArgs(
        data=InboxMessageSetMessageReadStatusModel(
            message_ids=[
                None,
            ],
            read=True,
        ),
    ) # InboxMessageSetMessageReadStatusArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Mark messages read or unread
        api_response = api_instance.inbox_service_update_message_read_status(inbox_message_set_message_read_status_args=inbox_message_set_message_read_status_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling InboxApi->inbox_service_update_message_read_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_message_set_message_read_status_args** | [**InboxMessageSetMessageReadStatusArgs**](InboxMessageSetMessageReadStatusArgs.md)| args | [optional]

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
**200** | True or an error |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_service_upload_resource**
> bool inbox_service_upload_resource()

Upload an embedded resource

Upload an embedded resource

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import inbox_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.inbox_resource_upload_args import InboxResourceUploadArgs
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
    api_instance = inbox_api.InboxApi(api_client)
    inbox_resource_upload_args = InboxResourceUploadArgs(
null,
        file_attachment=None,
        file_name=None,
        slug=None,
    ) # InboxResourceUploadArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload an embedded resource
        api_response = api_instance.inbox_service_upload_resource(inbox_resource_upload_args=inbox_resource_upload_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling InboxApi->inbox_service_upload_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_resource_upload_args** | [**InboxResourceUploadArgs**](InboxResourceUploadArgs.md)| args | [optional]

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
**200** | True or an error |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

