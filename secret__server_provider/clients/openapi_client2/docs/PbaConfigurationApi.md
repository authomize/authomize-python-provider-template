# plugins.PbaConfigurationApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pba_configuration_service_confirm_pba_pair**](PbaConfigurationApi.md#pba_configuration_service_confirm_pba_pair) | **POST** /v1/pba-confirm-pair | Confirm Pba Pair
[**pba_configuration_service_get_historical_import_status**](PbaConfigurationApi.md#pba_configuration_service_get_historical_import_status) | **GET** /v1/pba-configuration/get-historical-import-status | Get Historical Import Status
[**pba_configuration_service_get_pba_configuration**](PbaConfigurationApi.md#pba_configuration_service_get_pba_configuration) | **GET** /v1/pba-configuration | Get Pba Configuration
[**pba_configuration_service_process_pba_history_import**](PbaConfigurationApi.md#pba_configuration_service_process_pba_history_import) | **POST** /v1/pba-history-import | Process Pba Historical Import
[**pba_configuration_service_sync_pba_metadata**](PbaConfigurationApi.md#pba_configuration_service_sync_pba_metadata) | **POST** /v1/pba-sync-metadata | Sync Pba Metadata
[**pba_configuration_service_test_pba_connection**](PbaConfigurationApi.md#pba_configuration_service_test_pba_connection) | **POST** /v1/pba-test-connection | Test Pba Connection
[**pba_configuration_service_update_pba_configuration**](PbaConfigurationApi.md#pba_configuration_service_update_pba_configuration) | **PUT** /v1/pba-configuration | Update Pba Configuration


# **pba_configuration_service_confirm_pba_pair**
> PbaConfirmPairModel pba_configuration_service_confirm_pba_pair()

Confirm Pba Pair

Confirm SS Key Pair with Pba

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import pba_configuration_api
from plugins.model.pba_confirm_pair_model import PbaConfirmPairModel
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
    api_instance = pba_configuration_api.PbaConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Confirm Pba Pair
        api_response = api_instance.pba_configuration_service_confirm_pba_pair()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling PbaConfigurationApi->pba_configuration_service_confirm_pba_pair: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**PbaConfirmPairModel**](PbaConfirmPairModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pba Confirm Pair Model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pba_configuration_service_get_historical_import_status**
> PbaHistoricalImportStatusResponseMessage pba_configuration_service_get_historical_import_status()

Get Historical Import Status

Get Historical Import Status.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import pba_configuration_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.pba_historical_import_status_response_message import PbaHistoricalImportStatusResponseMessage
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
    api_instance = pba_configuration_api.PbaConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Historical Import Status
        api_response = api_instance.pba_configuration_service_get_historical_import_status()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling PbaConfigurationApi->pba_configuration_service_get_historical_import_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**PbaHistoricalImportStatusResponseMessage**](PbaHistoricalImportStatusResponseMessage.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PbaHistoricalImportStatusResponseMessage object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pba_configuration_service_get_pba_configuration**
> PbaConfigurationModel pba_configuration_service_get_pba_configuration()

Get Pba Configuration

Get Pba Configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import pba_configuration_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.pba_configuration_model import PbaConfigurationModel
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
    api_instance = pba_configuration_api.PbaConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Pba Configuration
        api_response = api_instance.pba_configuration_service_get_pba_configuration()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling PbaConfigurationApi->pba_configuration_service_get_pba_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**PbaConfigurationModel**](PbaConfigurationModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pba Configuration object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pba_configuration_service_process_pba_history_import**
> PbaHistoricalImportViewModel pba_configuration_service_process_pba_history_import()

Process Pba Historical Import

Process Pba Historical Import

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import pba_configuration_api
from plugins.model.pba_historical_import_view_model import PbaHistoricalImportViewModel
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.pba_historical_import_args import PbaHistoricalImportArgs
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
    api_instance = pba_configuration_api.PbaConfigurationApi(api_client)
    pba_historical_import_args = PbaHistoricalImportArgs(
        end_date=OptionalDateTimeOffset(
            date=dateutil_parser('1970-01-01T00:00:00.00Z'),
            date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            day=1,
            day_of_week=DayOfWeek("{}"),
            day_of_year=1,
            hour=1,
            local_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            millisecond=1,
            minute=1,
            month=1,
            offset="offset_example",
            second=1,
            ticks=1,
            time_of_day="time_of_day_example",
            utc_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            utc_ticks=1,
            year=1,
        ),
        process_import=True,
        start_date=OptionalDateTimeOffset(
            date=dateutil_parser('1970-01-01T00:00:00.00Z'),
            date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            day=1,
            day_of_week=DayOfWeek("{}"),
            day_of_year=1,
            hour=1,
            local_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            millisecond=1,
            minute=1,
            month=1,
            offset="offset_example",
            second=1,
            ticks=1,
            time_of_day="time_of_day_example",
            utc_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            utc_ticks=1,
            year=1,
        ),
    ) # PbaHistoricalImportArgs | Pba Historical Import Options (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Process Pba Historical Import
        api_response = api_instance.pba_configuration_service_process_pba_history_import(pba_historical_import_args=pba_historical_import_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling PbaConfigurationApi->pba_configuration_service_process_pba_history_import: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pba_historical_import_args** | [**PbaHistoricalImportArgs**](PbaHistoricalImportArgs.md)| Pba Historical Import Options | [optional]

### Return type

[**PbaHistoricalImportViewModel**](PbaHistoricalImportViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pba Historical Import |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pba_configuration_service_sync_pba_metadata**
> bool pba_configuration_service_sync_pba_metadata()

Sync Pba Metadata

Sync Pba Metadata

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import pba_configuration_api
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
    api_instance = pba_configuration_api.PbaConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Sync Pba Metadata
        api_response = api_instance.pba_configuration_service_sync_pba_metadata()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling PbaConfigurationApi->pba_configuration_service_sync_pba_metadata: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pba_configuration_service_test_pba_connection**
> bool pba_configuration_service_test_pba_connection()

Test Pba Connection

Test Pba Connection

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import pba_configuration_api
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
    api_instance = pba_configuration_api.PbaConfigurationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Test Pba Connection
        api_response = api_instance.pba_configuration_service_test_pba_connection()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling PbaConfigurationApi->pba_configuration_service_test_pba_connection: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pba_configuration_service_update_pba_configuration**
> PbaConfigurationModel pba_configuration_service_update_pba_configuration()

Update Pba Configuration

Update Pba Configuration

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import pba_configuration_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.pba_configuration_update_args import PbaConfigurationUpdateArgs
from plugins.model.pba_configuration_model import PbaConfigurationModel
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
    api_instance = pba_configuration_api.PbaConfigurationApi(api_client)
    pba_configuration_update_args = PbaConfigurationUpdateArgs(
        data=PbaConfigurationUpdateModel(
            challenge_enabled=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            challenge_lockout_integrated_enabled=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            challenge_lockout_saml_enabled=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            enabled=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            encryption_enabled=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            event_data_upload_interval=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            event_data_upload_size_threshold=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=1,
            ),
            external_pba_url=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            file_upload_enabled=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            metadata_interval=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            pba_integration_key=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            respect_owner_editor_require_approval_enabled=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            retention_days=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            site_id=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            storage_directory_path=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
        ),
    ) # PbaConfigurationUpdateArgs | Pba Configuration Update Options (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Pba Configuration
        api_response = api_instance.pba_configuration_service_update_pba_configuration(pba_configuration_update_args=pba_configuration_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling PbaConfigurationApi->pba_configuration_service_update_pba_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pba_configuration_update_args** | [**PbaConfigurationUpdateArgs**](PbaConfigurationUpdateArgs.md)| Pba Configuration Update Options | [optional]

### Return type

[**PbaConfigurationModel**](PbaConfigurationModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pba Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

