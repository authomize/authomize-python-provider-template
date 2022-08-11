# plugins.ApplicationRequestApi

All URIs are relative to *https://integrations.secretservercloud.com//api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**application_request_service_get_audits**](ApplicationRequestApi.md#application_request_service_get_audits) | **GET** /v1/application-access-request-audits | Get Application Access Request Audits by Device Id.
[**application_request_service_get_request_by_device_id**](ApplicationRequestApi.md#application_request_service_get_request_by_device_id) | **GET** /v1/application-access-request/{deviceId} | Get Application Access Requests by Device Id.
[**application_request_service_search_requests_by_status**](ApplicationRequestApi.md#application_request_service_search_requests_by_status) | **GET** /v1/application-access-requests | Get Application Access Requests by Status for Current User.
[**application_request_service_update_request**](ApplicationRequestApi.md#application_request_service_update_request) | **PATCH** /v1/application-access-request/{deviceId} | Update Application Access Requests by Device Id.


# **application_request_service_get_audits**
> PagingOfApplicationAccessRequestAuditViewModel application_request_service_get_audits()

Get Application Access Request Audits by Device Id.

Get Application Access Request Audits by Device Id.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import application_request_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.paging_of_application_access_request_audit_view_model import PagingOfApplicationAccessRequestAuditViewModel
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
    api_instance = application_request_api.ApplicationRequestApi(api_client)
    is_exporting = True # bool | isExporting (optional)
    filter_device_id = None # bool, date, datetime, dict, float, int, list, str, none_type | DeviceId (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Application Access Request Audits by Device Id.
        api_response = api_instance.application_request_service_get_audits(is_exporting=is_exporting, filter_device_id=filter_device_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ApplicationRequestApi->application_request_service_get_audits: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_exporting** | **bool**| isExporting | [optional]
 **filter_device_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| DeviceId | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfApplicationAccessRequestAuditViewModel**](PagingOfApplicationAccessRequestAuditViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Application Access Request Audit View Model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_request_service_get_request_by_device_id**
> ApplicationAccessRequestViewModel application_request_service_get_request_by_device_id(device_id)

Get Application Access Requests by Device Id.

Get Application Access Requests by Device Id.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import application_request_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.application_access_request_view_model import ApplicationAccessRequestViewModel
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
    api_instance = application_request_api.ApplicationRequestApi(api_client)
    device_id = None # bool, date, datetime, dict, float, int, list, str, none_type | deviceId

    # example passing only required values which don't have defaults set
    try:
        # Get Application Access Requests by Device Id.
        api_response = api_instance.application_request_service_get_request_by_device_id(device_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ApplicationRequestApi->application_request_service_get_request_by_device_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| deviceId |

### Return type

[**ApplicationAccessRequestViewModel**](ApplicationAccessRequestViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Access Model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_request_service_search_requests_by_status**
> PagingOfApplicationAccessRequestViewModel application_request_service_search_requests_by_status()

Get Application Access Requests by Status for Current User.

Get Application Access Requests by Status for Current User.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import application_request_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.paging_of_application_access_request_view_model import PagingOfApplicationAccessRequestViewModel
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
    api_instance = application_request_api.ApplicationRequestApi(api_client)
    filter_status = None # bool, date, datetime, dict, float, int, list, str, none_type | Status (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Application Access Requests by Status for Current User.
        api_response = api_instance.application_request_service_search_requests_by_status(filter_status=filter_status, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ApplicationRequestApi->application_request_service_search_requests_by_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_status** | **bool, date, datetime, dict, float, int, list, str, none_type**| Status | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfApplicationAccessRequestViewModel**](PagingOfApplicationAccessRequestViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Access Model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_request_service_update_request**
> ApplicationAccessRequestViewModel application_request_service_update_request(device_id)

Update Application Access Requests by Device Id.

Update Application Access Requests by Device Id.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import application_request_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.application_access_request_view_model import ApplicationAccessRequestViewModel
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.application_access_request_update_args import ApplicationAccessRequestUpdateArgs
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
    api_instance = application_request_api.ApplicationRequestApi(api_client)
    device_id = None # bool, date, datetime, dict, float, int, list, str, none_type | deviceId
    application_access_request_update_args = ApplicationAccessRequestUpdateArgs(
        data=ApplicationAccessRequestUpdateModel(
            status=UpdateFieldValueOfApplicationAccessStatusRequestType(
                dirty=True,
                value=ApplicationAccessStatusRequestType("{}"),
            ),
        ),
    ) # ApplicationAccessRequestUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Application Access Requests by Device Id.
        api_response = api_instance.application_request_service_update_request(device_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ApplicationRequestApi->application_request_service_update_request: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Application Access Requests by Device Id.
        api_response = api_instance.application_request_service_update_request(device_id, application_access_request_update_args=application_access_request_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ApplicationRequestApi->application_request_service_update_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| deviceId |
 **application_access_request_update_args** | [**ApplicationAccessRequestUpdateArgs**](ApplicationAccessRequestUpdateArgs.md)| args | [optional]

### Return type

[**ApplicationAccessRequestViewModel**](ApplicationAccessRequestViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Access Model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

