# secret_server_openapiclient.DualControlsApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dual_controls_service_authorize_dual_control**](DualControlsApi.md#dual_controls_service_authorize_dual_control) | **POST** /v1/dual-controls/auth/{dualControlType}/{id} | Authorize a dual control
[**dual_controls_service_create**](DualControlsApi.md#dual_controls_service_create) | **POST** /v1/dual-controls | Create Dual Control
[**dual_controls_service_delete**](DualControlsApi.md#dual_controls_service_delete) | **DELETE** /v1/dual-controls/{id} | Delete Dual Control
[**dual_controls_service_get**](DualControlsApi.md#dual_controls_service_get) | **GET** /v1/dual-controls/{id} | Get Dual Control
[**dual_controls_service_get_all_reports**](DualControlsApi.md#dual_controls_service_get_all_reports) | **GET** /v1/dual-controls/state/{dualControlType}/{id} | Get dual control state for the current item
[**dual_controls_service_get_types**](DualControlsApi.md#dual_controls_service_get_types) | **GET** /v1/dual-controls/types | Get Dual Control Types
[**dual_controls_service_search_dual_controls**](DualControlsApi.md#dual_controls_service_search_dual_controls) | **GET** /v1/dual-controls | Search Dual Controls
[**dual_controls_service_stub**](DualControlsApi.md#dual_controls_service_stub) | **GET** /v1/dual-controls/stub | Get Dual Control Stub
[**dual_controls_service_update**](DualControlsApi.md#dual_controls_service_update) | **PUT** /v1/dual-controls/{id} | Update Dual Control


# **dual_controls_service_authorize_dual_control**
> DualControlAuthResult dual_controls_service_authorize_dual_control(dual_control_type, id)

Authorize a dual control

Authorize a dual control

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import dual_controls_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.dual_control_auth_args import DualControlAuthArgs
from secret_server_openapiclient.model.dual_control_auth_result import DualControlAuthResult
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
    api_instance = dual_controls_api.DualControlsApi(api_client)
    dual_control_type = "dualControlType_example" # str | dualControlType
    id = 1 # int | id
    dual_control_auth_args = DualControlAuthArgs(
        data=DualControlAuthDataModel(
            domain=1,
            password="password_example",
            two_factor_token="two_factor_token_example",
            username="username_example",
        ),
    ) # DualControlAuthArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Authorize a dual control
        api_response = api_instance.dual_controls_service_authorize_dual_control(dual_control_type, id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DualControlsApi->dual_controls_service_authorize_dual_control: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Authorize a dual control
        api_response = api_instance.dual_controls_service_authorize_dual_control(dual_control_type, id, dual_control_auth_args=dual_control_auth_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DualControlsApi->dual_controls_service_authorize_dual_control: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dual_control_type** | **str**| dualControlType |
 **id** | **int**| id |
 **dual_control_auth_args** | [**DualControlAuthArgs**](DualControlAuthArgs.md)| args | [optional]

### Return type

[**DualControlAuthResult**](DualControlAuthResult.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dual control authorization result |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dual_controls_service_create**
> DualControlModel dual_controls_service_create()

Create Dual Control

Create a new dual control

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import dual_controls_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.dual_control_model import DualControlModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.dual_control_create_args import DualControlCreateArgs
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
    api_instance = dual_controls_api.DualControlsApi(api_client)
    dual_control_create_args = DualControlCreateArgs(
        active=True,
        dual_control_approval_groups=[
            IDualControlApprovalGroup(
                dual_control_id=1,
                enabled=True,
                group_id=1,
                group_name="group_name_example",
                id=1,
            ),
        ],
        dual_control_type_id=1,
        item_id=1,
    ) # DualControlCreateArgs | Dual control creation options (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Dual Control
        api_response = api_instance.dual_controls_service_create(dual_control_create_args=dual_control_create_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DualControlsApi->dual_controls_service_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dual_control_create_args** | [**DualControlCreateArgs**](DualControlCreateArgs.md)| Dual control creation options | [optional]

### Return type

[**DualControlModel**](DualControlModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dual control object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dual_controls_service_delete**
> DeletedModel dual_controls_service_delete(id)

Delete Dual Control

Delete a dual control by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import dual_controls_api
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
    api_instance = dual_controls_api.DualControlsApi(api_client)
    id = 1 # int | Dual control ID

    # example passing only required values which don't have defaults set
    try:
        # Delete Dual Control
        api_response = api_instance.dual_controls_service_delete(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DualControlsApi->dual_controls_service_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Dual control ID |

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
**200** | Object deletion result |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dual_controls_service_get**
> DualControlModel dual_controls_service_get(id)

Get Dual Control

Get a single dual control by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import dual_controls_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.dual_control_model import DualControlModel
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
    api_instance = dual_controls_api.DualControlsApi(api_client)
    id = 1 # int | Dual control ID

    # example passing only required values which don't have defaults set
    try:
        # Get Dual Control
        api_response = api_instance.dual_controls_service_get(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DualControlsApi->dual_controls_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Dual control ID |

### Return type

[**DualControlModel**](DualControlModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dual control object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dual_controls_service_get_all_reports**
> DualControlStateModel dual_controls_service_get_all_reports(dual_control_type, id)

Get dual control state for the current item

Get dual control state for the current item

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import dual_controls_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.dual_control_state_model import DualControlStateModel
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
    api_instance = dual_controls_api.DualControlsApi(api_client)
    dual_control_type = "dualControlType_example" # str | dualControlType
    id = 1 # int | id

    # example passing only required values which don't have defaults set
    try:
        # Get dual control state for the current item
        api_response = api_instance.dual_controls_service_get_all_reports(dual_control_type, id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DualControlsApi->dual_controls_service_get_all_reports: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dual_control_type** | **str**| dualControlType |
 **id** | **int**| id |

### Return type

[**DualControlStateModel**](DualControlStateModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dual Control State |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dual_controls_service_get_types**
> [DualControlTypeModel] dual_controls_service_get_types()

Get Dual Control Types

Return a list of Dual Control Types

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import dual_controls_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.dual_control_type_model import DualControlTypeModel
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
    api_instance = dual_controls_api.DualControlsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Dual Control Types
        api_response = api_instance.dual_controls_service_get_types()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DualControlsApi->dual_controls_service_get_types: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[DualControlTypeModel]**](DualControlTypeModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dual control type objects |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dual_controls_service_search_dual_controls**
> PagingOfDualControlSummary dual_controls_service_search_dual_controls()

Search Dual Controls

Search, filter, sort, and page dual controls

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import dual_controls_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.paging_of_dual_control_summary import PagingOfDualControlSummary
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
    api_instance = dual_controls_api.DualControlsApi(api_client)
    filter_include_inactive = True # bool | Whether to include inactive items (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Dual Controls
        api_response = api_instance.dual_controls_service_search_dual_controls(filter_include_inactive=filter_include_inactive, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DualControlsApi->dual_controls_service_search_dual_controls: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_include_inactive** | **bool**| Whether to include inactive items | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfDualControlSummary**](PagingOfDualControlSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dual control search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dual_controls_service_stub**
> DualControlModel dual_controls_service_stub()

Get Dual Control Stub

Return the default values for a new dual control

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import dual_controls_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.dual_control_model import DualControlModel
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
    api_instance = dual_controls_api.DualControlsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Dual Control Stub
        api_response = api_instance.dual_controls_service_stub()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DualControlsApi->dual_controls_service_stub: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**DualControlModel**](DualControlModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dual control object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dual_controls_service_update**
> DualControlModel dual_controls_service_update(id)

Update Dual Control

Update a single dual control by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import dual_controls_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.dual_control_model import DualControlModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.dual_control_update_args import DualControlUpdateArgs
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
    api_instance = dual_controls_api.DualControlsApi(api_client)
    id = 1 # int | Dual control ID
    dual_control_update_args = DualControlUpdateArgs(
        active=True,
        dual_control_approval_groups=[
            IDualControlApprovalGroup(
                dual_control_id=1,
                enabled=True,
                group_id=1,
                group_name="group_name_example",
                id=1,
            ),
        ],
        dual_control_type_id=1,
        id=1,
        item_id=1,
    ) # DualControlUpdateArgs | Dual control update options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Dual Control
        api_response = api_instance.dual_controls_service_update(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DualControlsApi->dual_controls_service_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Dual Control
        api_response = api_instance.dual_controls_service_update(id, dual_control_update_args=dual_control_update_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DualControlsApi->dual_controls_service_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Dual control ID |
 **dual_control_update_args** | [**DualControlUpdateArgs**](DualControlUpdateArgs.md)| Dual control update options | [optional]

### Return type

[**DualControlModel**](DualControlModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dual control object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

