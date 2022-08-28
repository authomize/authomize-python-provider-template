# secret_server_openapiclient.DisasterRecoveryApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disaster_recovery_service_delete_disaster_recovery_data_replica**](DisasterRecoveryApi.md#disaster_recovery_service_delete_disaster_recovery_data_replica) | **DELETE** /v1/disaster-recovery/data-replication/{replicaId} | Delete Disaster Recovery Data Replica
[**disaster_recovery_service_get_disaster_recovery_configuration_audits**](DisasterRecoveryApi.md#disaster_recovery_service_get_disaster_recovery_configuration_audits) | **GET** /v1/disaster-recovery/audits | Get Disaster Recovery Configuration Audits
[**disaster_recovery_service_get_disaster_recovery_data_replica**](DisasterRecoveryApi.md#disaster_recovery_service_get_disaster_recovery_data_replica) | **GET** /v1/disaster-recovery/data-replication/{replicaId} | Get Disaster Recovery Data Replica
[**disaster_recovery_service_get_disaster_recovery_data_replication_logs**](DisasterRecoveryApi.md#disaster_recovery_service_get_disaster_recovery_data_replication_logs) | **GET** /v1/disaster-recovery/logs | Get Disaster Recovery Replication Logs
[**disaster_recovery_service_get_disaster_recovery_incoming_configuration**](DisasterRecoveryApi.md#disaster_recovery_service_get_disaster_recovery_incoming_configuration) | **GET** /v1/disaster-recovery/incoming-configuration | Get Disaster Recovery Incoming Configuration
[**disaster_recovery_service_get_disaster_recovery_outgoing_configuration**](DisasterRecoveryApi.md#disaster_recovery_service_get_disaster_recovery_outgoing_configuration) | **GET** /v1/disaster-recovery/outgoing-configuration | Get Disaster Recovery Outgoing Configuration
[**disaster_recovery_service_patch_disaster_recovery_data_replica**](DisasterRecoveryApi.md#disaster_recovery_service_patch_disaster_recovery_data_replica) | **PATCH** /v1/disaster-recovery/data-replication/{replicaId} | Patch Disaster Recovery Data Replica
[**disaster_recovery_service_patch_disaster_recovery_incoming_configuration**](DisasterRecoveryApi.md#disaster_recovery_service_patch_disaster_recovery_incoming_configuration) | **PATCH** /v1/disaster-recovery/incoming-configuration | Patch Disaster Recovery Incoming Configuration
[**disaster_recovery_service_post_disaster_recovery_handshake**](DisasterRecoveryApi.md#disaster_recovery_service_post_disaster_recovery_handshake) | **POST** /v1/disaster-recovery/handshake | Disaster Recovery Handshake
[**disaster_recovery_service_request_data_replica_replication_package**](DisasterRecoveryApi.md#disaster_recovery_service_request_data_replica_replication_package) | **POST** /v1/disaster-recovery/data-replication/package | Request Disaster Recovery Data Replica Replication Package
[**disaster_recovery_service_request_data_replica_replication_start**](DisasterRecoveryApi.md#disaster_recovery_service_request_data_replica_replication_start) | **POST** /v1/disaster-recovery/data-replication/start | Request Disaster Recovery Data Replica Replication Start
[**disaster_recovery_service_request_data_replica_replication_status**](DisasterRecoveryApi.md#disaster_recovery_service_request_data_replica_replication_status) | **POST** /v1/disaster-recovery/data-replication/status | Request Disaster Recovery Data Replica Replication Status
[**disaster_recovery_service_run_disaster_recovery_data_replica_test_now**](DisasterRecoveryApi.md#disaster_recovery_service_run_disaster_recovery_data_replica_test_now) | **POST** /v1/disaster-recovery/data-replication/test | Test Disaster Recovery Data Replication
[**disaster_recovery_service_run_disaster_recovery_data_replication_now**](DisasterRecoveryApi.md#disaster_recovery_service_run_disaster_recovery_data_replication_now) | **POST** /v1/disaster-recovery/data-replication/run-now | Start Disaster Recovery Data Replication


# **disaster_recovery_service_delete_disaster_recovery_data_replica**
> bool disaster_recovery_service_delete_disaster_recovery_data_replica(replica_id)

Delete Disaster Recovery Data Replica

Delete the data replica.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import disaster_recovery_api
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
    api_instance = disaster_recovery_api.DisasterRecoveryApi(api_client)
    replica_id = None # bool, date, datetime, dict, float, int, list, str, none_type | replicaId

    # example passing only required values which don't have defaults set
    try:
        # Delete Disaster Recovery Data Replica
        api_response = api_instance.disaster_recovery_service_delete_disaster_recovery_data_replica(replica_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DisasterRecoveryApi->disaster_recovery_service_delete_disaster_recovery_data_replica: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replica_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| replicaId |

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
**200** | True if the data replica was deleted. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disaster_recovery_service_get_disaster_recovery_configuration_audits**
> PagingOfDisasterRecoveryAuditViewModel disaster_recovery_service_get_disaster_recovery_configuration_audits()

Get Disaster Recovery Configuration Audits

Retrieve the audits for the Disaster Recovery configuration.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import disaster_recovery_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.paging_of_disaster_recovery_audit_view_model import PagingOfDisasterRecoveryAuditViewModel
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
    api_instance = disaster_recovery_api.DisasterRecoveryApi(api_client)
    audit_type = None # bool, date, datetime, dict, float, int, list, str, none_type | auditType (optional)
    is_exporting = True # bool | isExporting (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Disaster Recovery Configuration Audits
        api_response = api_instance.disaster_recovery_service_get_disaster_recovery_configuration_audits(audit_type=audit_type, is_exporting=is_exporting, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DisasterRecoveryApi->disaster_recovery_service_get_disaster_recovery_configuration_audits: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audit_type** | **bool, date, datetime, dict, float, int, list, str, none_type**| auditType | [optional]
 **is_exporting** | **bool**| isExporting | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfDisasterRecoveryAuditViewModel**](PagingOfDisasterRecoveryAuditViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Disaster Recovery Configuration Audits |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disaster_recovery_service_get_disaster_recovery_data_replica**
> DisasterRecoveryDataReplicaModel disaster_recovery_service_get_disaster_recovery_data_replica(replica_id)

Get Disaster Recovery Data Replica

Retrieve the settings and descriptions for the Disaster Recovery data replica view model.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import disaster_recovery_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.disaster_recovery_data_replica_model import DisasterRecoveryDataReplicaModel
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
    api_instance = disaster_recovery_api.DisasterRecoveryApi(api_client)
    replica_id = None # bool, date, datetime, dict, float, int, list, str, none_type | replicaId

    # example passing only required values which don't have defaults set
    try:
        # Get Disaster Recovery Data Replica
        api_response = api_instance.disaster_recovery_service_get_disaster_recovery_data_replica(replica_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DisasterRecoveryApi->disaster_recovery_service_get_disaster_recovery_data_replica: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replica_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| replicaId |

### Return type

[**DisasterRecoveryDataReplicaModel**](DisasterRecoveryDataReplicaModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Disaster Recovery Data Replica |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disaster_recovery_service_get_disaster_recovery_data_replication_logs**
> PagingOfDisasterRecoveryDataReplicationLogViewModel disaster_recovery_service_get_disaster_recovery_data_replication_logs()

Get Disaster Recovery Replication Logs

Retrieve the logs for each run of Disaster Recovery Replication

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import disaster_recovery_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.paging_of_disaster_recovery_data_replication_log_view_model import PagingOfDisasterRecoveryDataReplicationLogViewModel
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
    api_instance = disaster_recovery_api.DisasterRecoveryApi(api_client)
    log_type = None # bool, date, datetime, dict, float, int, list, str, none_type | logType (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Disaster Recovery Replication Logs
        api_response = api_instance.disaster_recovery_service_get_disaster_recovery_data_replication_logs(log_type=log_type, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DisasterRecoveryApi->disaster_recovery_service_get_disaster_recovery_data_replication_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_type** | **bool, date, datetime, dict, float, int, list, str, none_type**| logType | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfDisasterRecoveryDataReplicationLogViewModel**](PagingOfDisasterRecoveryDataReplicationLogViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Disaster Recovery Replication Logs |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disaster_recovery_service_get_disaster_recovery_incoming_configuration**
> DisasterRecoveryIncomingConfigurationModel disaster_recovery_service_get_disaster_recovery_incoming_configuration()

Get Disaster Recovery Incoming Configuration

Retrieve the settings and descriptions for the Disaster Recovery incoming configuration view model.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import disaster_recovery_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.disaster_recovery_incoming_configuration_model import DisasterRecoveryIncomingConfigurationModel
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
    api_instance = disaster_recovery_api.DisasterRecoveryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Disaster Recovery Incoming Configuration
        api_response = api_instance.disaster_recovery_service_get_disaster_recovery_incoming_configuration()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DisasterRecoveryApi->disaster_recovery_service_get_disaster_recovery_incoming_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**DisasterRecoveryIncomingConfigurationModel**](DisasterRecoveryIncomingConfigurationModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Disaster Recovery Incoming Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disaster_recovery_service_get_disaster_recovery_outgoing_configuration**
> DisasterRecoveryOutgoingConfigurationModel disaster_recovery_service_get_disaster_recovery_outgoing_configuration()

Get Disaster Recovery Outgoing Configuration

Retrieve the settings and descriptions for the Disaster Recovery Outgoing Configuration view model.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import disaster_recovery_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.disaster_recovery_outgoing_configuration_model import DisasterRecoveryOutgoingConfigurationModel
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
    api_instance = disaster_recovery_api.DisasterRecoveryApi(api_client)
    filter_location = None # bool, date, datetime, dict, float, int, list, str, none_type | Only return data replicas with locations containing this text. (optional)
    filter_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Only return data replicas with names containing this text. (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Disaster Recovery Outgoing Configuration
        api_response = api_instance.disaster_recovery_service_get_disaster_recovery_outgoing_configuration(filter_location=filter_location, filter_name=filter_name, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DisasterRecoveryApi->disaster_recovery_service_get_disaster_recovery_outgoing_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_location** | **bool, date, datetime, dict, float, int, list, str, none_type**| Only return data replicas with locations containing this text. | [optional]
 **filter_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Only return data replicas with names containing this text. | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**DisasterRecoveryOutgoingConfigurationModel**](DisasterRecoveryOutgoingConfigurationModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Disaster Recovery Outgoing Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disaster_recovery_service_patch_disaster_recovery_data_replica**
> DisasterRecoveryDataReplicaModel disaster_recovery_service_patch_disaster_recovery_data_replica(replica_id)

Patch Disaster Recovery Data Replica

Patch Disaster Recovery Data Replica by sending one or more fields with dirty set to true.  This will return the actual updated view model.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import disaster_recovery_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.disaster_recovery_data_replica_model import DisasterRecoveryDataReplicaModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.disaster_recovery_data_replica_args import DisasterRecoveryDataReplicaArgs
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
    api_instance = disaster_recovery_api.DisasterRecoveryApi(api_client)
    replica_id = None # bool, date, datetime, dict, float, int, list, str, none_type | replicaId
    disaster_recovery_data_replica_args = DisasterRecoveryDataReplicaArgs(
        data=DisasterRecoveryDataReplicaUpdateModel(
            data_replica_id=None,
            folder_ids=UpdateFieldValueOfInt32Array(
                dirty=True,
                value=[
                    None,
                ],
            ),
            name=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            status=UpdateFieldValueOfDisasterRecoveryDataReplicaStatus(
                dirty=True,
                value=DisasterRecoveryDataReplicaStatus("{}"),
            ),
        ),
    ) # DisasterRecoveryDataReplicaArgs | Disaster Recovery Data Replica Update Settings (optional)

    # example passing only required values which don't have defaults set
    try:
        # Patch Disaster Recovery Data Replica
        api_response = api_instance.disaster_recovery_service_patch_disaster_recovery_data_replica(replica_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DisasterRecoveryApi->disaster_recovery_service_patch_disaster_recovery_data_replica: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Patch Disaster Recovery Data Replica
        api_response = api_instance.disaster_recovery_service_patch_disaster_recovery_data_replica(replica_id, disaster_recovery_data_replica_args=disaster_recovery_data_replica_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DisasterRecoveryApi->disaster_recovery_service_patch_disaster_recovery_data_replica: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replica_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| replicaId |
 **disaster_recovery_data_replica_args** | [**DisasterRecoveryDataReplicaArgs**](DisasterRecoveryDataReplicaArgs.md)| Disaster Recovery Data Replica Update Settings | [optional]

### Return type

[**DisasterRecoveryDataReplicaModel**](DisasterRecoveryDataReplicaModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Disaster Recovery Data Replica |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disaster_recovery_service_patch_disaster_recovery_incoming_configuration**
> DisasterRecoveryIncomingConfigurationModel disaster_recovery_service_patch_disaster_recovery_incoming_configuration()

Patch Disaster Recovery Incoming Configuration

Patch Disaster Recovery Incoming Configuration by sending one or more fields with dirty set to true.  This will return the actual updated view model.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import disaster_recovery_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.disaster_recovery_configuration_args import DisasterRecoveryConfigurationArgs
from secret_server_openapiclient.model.disaster_recovery_incoming_configuration_model import DisasterRecoveryIncomingConfigurationModel
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
    api_instance = disaster_recovery_api.DisasterRecoveryApi(api_client)
    disaster_recovery_configuration_args = DisasterRecoveryConfigurationArgs(
        data=DisasterRecoveryConfigurationUpdateModel(
            data_package_storage_path=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            data_replication_enabled=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            data_replication_group_id=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=None,
            ),
            data_source_key=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            data_source_url=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            replication_interval_minutes=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
        ),
    ) # DisasterRecoveryConfigurationArgs | Disaster Recovery Incoming Configuration Update Settings (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Patch Disaster Recovery Incoming Configuration
        api_response = api_instance.disaster_recovery_service_patch_disaster_recovery_incoming_configuration(disaster_recovery_configuration_args=disaster_recovery_configuration_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DisasterRecoveryApi->disaster_recovery_service_patch_disaster_recovery_incoming_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disaster_recovery_configuration_args** | [**DisasterRecoveryConfigurationArgs**](DisasterRecoveryConfigurationArgs.md)| Disaster Recovery Incoming Configuration Update Settings | [optional]

### Return type

[**DisasterRecoveryIncomingConfigurationModel**](DisasterRecoveryIncomingConfigurationModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Disaster Recovery Incoming Configuration |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disaster_recovery_service_post_disaster_recovery_handshake**
> DisasterRecoveryHandshakeModel disaster_recovery_service_post_disaster_recovery_handshake()

Disaster Recovery Handshake

Try to add the requesting data replica to the receiving data source.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import disaster_recovery_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.disaster_recovery_handshake_model import DisasterRecoveryHandshakeModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.disaster_recovery_handshake_args import DisasterRecoveryHandshakeArgs
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
    api_instance = disaster_recovery_api.DisasterRecoveryApi(api_client)
    disaster_recovery_handshake_args = DisasterRecoveryHandshakeArgs(
        encrypted_parts=[
            None,
        ],
    ) # DisasterRecoveryHandshakeArgs | Disaster Recovery Handshake arguments encrypted using the data source's public key. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Disaster Recovery Handshake
        api_response = api_instance.disaster_recovery_service_post_disaster_recovery_handshake(disaster_recovery_handshake_args=disaster_recovery_handshake_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DisasterRecoveryApi->disaster_recovery_service_post_disaster_recovery_handshake: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disaster_recovery_handshake_args** | [**DisasterRecoveryHandshakeArgs**](DisasterRecoveryHandshakeArgs.md)| Disaster Recovery Handshake arguments encrypted using the data source&#39;s public key. | [optional]

### Return type

[**DisasterRecoveryHandshakeModel**](DisasterRecoveryHandshakeModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Disaster Recovery Handshake response encrypted using the data replica&#39;s public key. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disaster_recovery_service_request_data_replica_replication_package**
> DisasterRecoveryDataSourceToDataReplicaModel disaster_recovery_service_request_data_replica_replication_package()

Request Disaster Recovery Data Replica Replication Package

Request a data replication package for this replica from the Data Source.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import disaster_recovery_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.disaster_recovery_data_replica_to_data_source_args import DisasterRecoveryDataReplicaToDataSourceArgs
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.disaster_recovery_data_source_to_data_replica_model import DisasterRecoveryDataSourceToDataReplicaModel
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
    api_instance = disaster_recovery_api.DisasterRecoveryApi(api_client)
    disaster_recovery_data_replica_to_data_source_args = DisasterRecoveryDataReplicaToDataSourceArgs(
        data_replica_id=None,
        encrypted_request=None,
    ) # DisasterRecoveryDataReplicaToDataSourceArgs | Disaster Recovery Data Replica to Data Source request encrypted using the symmetric key from the data replica. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Request Disaster Recovery Data Replica Replication Package
        api_response = api_instance.disaster_recovery_service_request_data_replica_replication_package(disaster_recovery_data_replica_to_data_source_args=disaster_recovery_data_replica_to_data_source_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DisasterRecoveryApi->disaster_recovery_service_request_data_replica_replication_package: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disaster_recovery_data_replica_to_data_source_args** | [**DisasterRecoveryDataReplicaToDataSourceArgs**](DisasterRecoveryDataReplicaToDataSourceArgs.md)| Disaster Recovery Data Replica to Data Source request encrypted using the symmetric key from the data replica. | [optional]

### Return type

[**DisasterRecoveryDataSourceToDataReplicaModel**](DisasterRecoveryDataSourceToDataReplicaModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Disaster Recovery Data Replica Replication Package response encrypted using the symmetric key for this data replica. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disaster_recovery_service_request_data_replica_replication_start**
> DisasterRecoveryDataSourceToDataReplicaModel disaster_recovery_service_request_data_replica_replication_start()

Request Disaster Recovery Data Replica Replication Start

Request that data replication be started for the given replica.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import disaster_recovery_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.disaster_recovery_data_replica_to_data_source_args import DisasterRecoveryDataReplicaToDataSourceArgs
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.disaster_recovery_data_source_to_data_replica_model import DisasterRecoveryDataSourceToDataReplicaModel
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
    api_instance = disaster_recovery_api.DisasterRecoveryApi(api_client)
    disaster_recovery_data_replica_to_data_source_args = DisasterRecoveryDataReplicaToDataSourceArgs(
        data_replica_id=None,
        encrypted_request=None,
    ) # DisasterRecoveryDataReplicaToDataSourceArgs | Disaster Recovery Data Replica to Data Source request encrypted using the symmetric key from the data replica. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Request Disaster Recovery Data Replica Replication Start
        api_response = api_instance.disaster_recovery_service_request_data_replica_replication_start(disaster_recovery_data_replica_to_data_source_args=disaster_recovery_data_replica_to_data_source_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DisasterRecoveryApi->disaster_recovery_service_request_data_replica_replication_start: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disaster_recovery_data_replica_to_data_source_args** | [**DisasterRecoveryDataReplicaToDataSourceArgs**](DisasterRecoveryDataReplicaToDataSourceArgs.md)| Disaster Recovery Data Replica to Data Source request encrypted using the symmetric key from the data replica. | [optional]

### Return type

[**DisasterRecoveryDataSourceToDataReplicaModel**](DisasterRecoveryDataSourceToDataReplicaModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Disaster Recovery Data Replica Replication Start response encrypted using the symmetric key for this data replica. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disaster_recovery_service_request_data_replica_replication_status**
> DisasterRecoveryDataSourceToDataReplicaModel disaster_recovery_service_request_data_replica_replication_status()

Request Disaster Recovery Data Replica Replication Status

Request the data replication status for this replica from the Data Source.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import disaster_recovery_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.disaster_recovery_data_replica_to_data_source_args import DisasterRecoveryDataReplicaToDataSourceArgs
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.disaster_recovery_data_source_to_data_replica_model import DisasterRecoveryDataSourceToDataReplicaModel
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
    api_instance = disaster_recovery_api.DisasterRecoveryApi(api_client)
    disaster_recovery_data_replica_to_data_source_args = DisasterRecoveryDataReplicaToDataSourceArgs(
        data_replica_id=None,
        encrypted_request=None,
    ) # DisasterRecoveryDataReplicaToDataSourceArgs | Disaster Recovery Data Replica to Data Source request encrypted using the symmetric key from the data replica. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Request Disaster Recovery Data Replica Replication Status
        api_response = api_instance.disaster_recovery_service_request_data_replica_replication_status(disaster_recovery_data_replica_to_data_source_args=disaster_recovery_data_replica_to_data_source_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DisasterRecoveryApi->disaster_recovery_service_request_data_replica_replication_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disaster_recovery_data_replica_to_data_source_args** | [**DisasterRecoveryDataReplicaToDataSourceArgs**](DisasterRecoveryDataReplicaToDataSourceArgs.md)| Disaster Recovery Data Replica to Data Source request encrypted using the symmetric key from the data replica. | [optional]

### Return type

[**DisasterRecoveryDataSourceToDataReplicaModel**](DisasterRecoveryDataSourceToDataReplicaModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Disaster Recovery Data Replica Replication Status response encrypted using the symmetric key for this data replica. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disaster_recovery_service_run_disaster_recovery_data_replica_test_now**
> DisasterRecoveryDataReplicaMessageResponse disaster_recovery_service_run_disaster_recovery_data_replica_test_now()

Test Disaster Recovery Data Replication

Test Disaster Recovery data replication as configured.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import disaster_recovery_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.disaster_recovery_data_replica_message_response import DisasterRecoveryDataReplicaMessageResponse
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
    api_instance = disaster_recovery_api.DisasterRecoveryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Test Disaster Recovery Data Replication
        api_response = api_instance.disaster_recovery_service_run_disaster_recovery_data_replica_test_now()
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DisasterRecoveryApi->disaster_recovery_service_run_disaster_recovery_data_replica_test_now: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**DisasterRecoveryDataReplicaMessageResponse**](DisasterRecoveryDataReplicaMessageResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Whether the connection between the data replica and data source is configured correctly. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disaster_recovery_service_run_disaster_recovery_data_replication_now**
> DisasterRecoveryDataReplicaMessageResponse disaster_recovery_service_run_disaster_recovery_data_replication_now()

Start Disaster Recovery Data Replication

Start Disaster Recovery data replication as configured.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import disaster_recovery_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.disaster_recovery_data_replica_message_response import DisasterRecoveryDataReplicaMessageResponse
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
    api_instance = disaster_recovery_api.DisasterRecoveryApi(api_client)
    minutes = None # bool, date, datetime, dict, float, int, list, str, none_type | minutes (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Start Disaster Recovery Data Replication
        api_response = api_instance.disaster_recovery_service_run_disaster_recovery_data_replication_now(minutes=minutes)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling DisasterRecoveryApi->disaster_recovery_service_run_disaster_recovery_data_replication_now: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **minutes** | **bool, date, datetime, dict, float, int, list, str, none_type**| minutes | [optional]

### Return type

[**DisasterRecoveryDataReplicaMessageResponse**](DisasterRecoveryDataReplicaMessageResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | True if the job was queued |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

