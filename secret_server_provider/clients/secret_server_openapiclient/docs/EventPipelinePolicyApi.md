# secret_server_openapiclient.EventPipelinePolicyApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**event_pipeline_policy_service_activate_event_pipeline_policy**](EventPipelinePolicyApi.md#event_pipeline_policy_service_activate_event_pipeline_policy) | **PUT** /v1/event-pipeline-policy/{id}/activate | Activate Event Pipeline Policy
[**event_pipeline_policy_service_add_pipeline_to_event_pipeline_policy**](EventPipelinePolicyApi.md#event_pipeline_policy_service_add_pipeline_to_event_pipeline_policy) | **POST** /v1/event-pipeline-policy/{id} | Add Pipeline To Event Pipeline Policy
[**event_pipeline_policy_service_create_event_pipeline_policy**](EventPipelinePolicyApi.md#event_pipeline_policy_service_create_event_pipeline_policy) | **POST** /v1/event-pipeline-policy | Create Pipeline Policy
[**event_pipeline_policy_service_duplicate_event_pipeline_policy**](EventPipelinePolicyApi.md#event_pipeline_policy_service_duplicate_event_pipeline_policy) | **POST** /v1/event-pipeline-policy/duplicate | Duplicate Event Pipeline Policy
[**event_pipeline_policy_service_export_event_pipeline_policy**](EventPipelinePolicyApi.md#event_pipeline_policy_service_export_event_pipeline_policy) | **GET** /v1/event-pipeline-policy/export/{id} | Export Event Pipeline Policy
[**event_pipeline_policy_service_get_child_folder_data_for_pipeline_policy_folder**](EventPipelinePolicyApi.md#event_pipeline_policy_service_get_child_folder_data_for_pipeline_policy_folder) | **GET** /v1/event-pipeline-policy/{id}/folders/{folderId}/childdata | Get Child Folder Data For Pipeline Policy Folder
[**event_pipeline_policy_service_get_event_pipeline_policies**](EventPipelinePolicyApi.md#event_pipeline_policy_service_get_event_pipeline_policies) | **GET** /v1/event-pipeline-policy/list | Get Event Pipeline Policies
[**event_pipeline_policy_service_get_event_pipeline_policy**](EventPipelinePolicyApi.md#event_pipeline_policy_service_get_event_pipeline_policy) | **GET** /v1/event-pipeline-policy/{id} | Get Event Pipeline Policy
[**event_pipeline_policy_service_get_event_pipeline_policy_run_activity**](EventPipelinePolicyApi.md#event_pipeline_policy_service_get_event_pipeline_policy_run_activity) | **GET** /v1/event-pipeline-policy/activity | Get Event Pipeline Policy Run Activity
[**event_pipeline_policy_service_get_event_pipeline_policy_runs**](EventPipelinePolicyApi.md#event_pipeline_policy_service_get_event_pipeline_policy_runs) | **GET** /v1/event-pipeline-policy/runs | Get Event Pipeline Policy Runs
[**event_pipeline_policy_service_get_folders_for_pipeline_policies**](EventPipelinePolicyApi.md#event_pipeline_policy_service_get_folders_for_pipeline_policies) | **GET** /v1/event-pipeline-policy/{id}/folders | Get Folders For Pipeline Policies
[**event_pipeline_policy_service_get_group_count_for_pipeline_policy**](EventPipelinePolicyApi.md#event_pipeline_policy_service_get_group_count_for_pipeline_policy) | **GET** /v1/event-pipeline-policy/{id}/groups/count | Get Group Count For Pipeline Policy
[**event_pipeline_policy_service_get_groups_for_pipeline_policies**](EventPipelinePolicyApi.md#event_pipeline_policy_service_get_groups_for_pipeline_policies) | **GET** /v1/event-pipeline-policy/{id}/groups | Get Groups For Pipeline Policies
[**event_pipeline_policy_service_get_secret_policies_for_pipeline_policies**](EventPipelinePolicyApi.md#event_pipeline_policy_service_get_secret_policies_for_pipeline_policies) | **GET** /v1/event-pipeline-policy/{id}/secretpolicies | Get Secret Policies For Pipeline Policies
[**event_pipeline_policy_service_import_event_pipeline_policy**](EventPipelinePolicyApi.md#event_pipeline_policy_service_import_event_pipeline_policy) | **POST** /v1/event-pipeline-policy/import | Import Event Pipeline Policy
[**event_pipeline_policy_service_remove_event_pipeline_from_policy**](EventPipelinePolicyApi.md#event_pipeline_policy_service_remove_event_pipeline_from_policy) | **DELETE** /v1/event-pipeline-policy/{policyId}/pipeline/{pipelineId} | Remove Event Pipeline From Policy
[**event_pipeline_policy_service_update_event_pipeline_policy**](EventPipelinePolicyApi.md#event_pipeline_policy_service_update_event_pipeline_policy) | **PUT** /v1/event-pipeline-policy/{id} | Update Event Pipeline Policy
[**event_pipeline_policy_service_update_event_pipeline_policy_folder_maps**](EventPipelinePolicyApi.md#event_pipeline_policy_service_update_event_pipeline_policy_folder_maps) | **PUT** /v1/event-pipeline-policy/{id}/folders | Update Event Pipeline Policy Folder Maps
[**event_pipeline_policy_service_update_event_pipeline_policy_group_maps**](EventPipelinePolicyApi.md#event_pipeline_policy_service_update_event_pipeline_policy_group_maps) | **PUT** /v1/event-pipeline-policy/{id}/groups | Update Event Pipeline Policy Group Maps
[**event_pipeline_policy_service_update_event_pipeline_policy_sort_order**](EventPipelinePolicyApi.md#event_pipeline_policy_service_update_event_pipeline_policy_sort_order) | **PUT** /v1/event-pipeline-policy/{id}/order | Update Event Pipeline Policy Sort Order


# **event_pipeline_policy_service_activate_event_pipeline_policy**
> bool event_pipeline_policy_service_activate_event_pipeline_policy(id)

Activate Event Pipeline Policy

Activate a specific policy

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import event_pipeline_policy_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.event_pipeline_policy_activate_args import EventPipelinePolicyActivateArgs
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
    api_instance = event_pipeline_policy_api.EventPipelinePolicyApi(api_client)
    id = 1 # int | Event Pipeline Policy ID
    event_pipeline_policy_activate_args = EventPipelinePolicyActivateArgs(
        activate=True,
    ) # EventPipelinePolicyActivateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Activate Event Pipeline Policy
        api_response = api_instance.event_pipeline_policy_service_activate_event_pipeline_policy(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling EventPipelinePolicyApi->event_pipeline_policy_service_activate_event_pipeline_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Activate Event Pipeline Policy
        api_response = api_instance.event_pipeline_policy_service_activate_event_pipeline_policy(id, event_pipeline_policy_activate_args=event_pipeline_policy_activate_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling EventPipelinePolicyApi->event_pipeline_policy_service_activate_event_pipeline_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Event Pipeline Policy ID |
 **event_pipeline_policy_activate_args** | [**EventPipelinePolicyActivateArgs**](EventPipelinePolicyActivateArgs.md)| args | [optional]

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
**200** | boolean indicating success |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_pipeline_policy_service_add_pipeline_to_event_pipeline_policy**
> EventPipelinePolicyMapModel event_pipeline_policy_service_add_pipeline_to_event_pipeline_policy(id)

Add Pipeline To Event Pipeline Policy

Returns data pertaining to children of a folder that has a particular pipeline policy assigned

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import event_pipeline_policy_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.event_pipeline_policy_add_pipeline_args import EventPipelinePolicyAddPipelineArgs
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.event_pipeline_policy_map_model import EventPipelinePolicyMapModel
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
    api_instance = event_pipeline_policy_api.EventPipelinePolicyApi(api_client)
    id = 1 # int | Event Pipeline Policy ID
    event_pipeline_policy_add_pipeline_args = EventPipelinePolicyAddPipelineArgs(
        data=EventPipelinePolicyAddPipelineModel(
            event_pipeline_id=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
        ),
    ) # EventPipelinePolicyAddPipelineArgs | eventPipelinePolicyAddPipelineArgs (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add Pipeline To Event Pipeline Policy
        api_response = api_instance.event_pipeline_policy_service_add_pipeline_to_event_pipeline_policy(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling EventPipelinePolicyApi->event_pipeline_policy_service_add_pipeline_to_event_pipeline_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add Pipeline To Event Pipeline Policy
        api_response = api_instance.event_pipeline_policy_service_add_pipeline_to_event_pipeline_policy(id, event_pipeline_policy_add_pipeline_args=event_pipeline_policy_add_pipeline_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling EventPipelinePolicyApi->event_pipeline_policy_service_add_pipeline_to_event_pipeline_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Event Pipeline Policy ID |
 **event_pipeline_policy_add_pipeline_args** | [**EventPipelinePolicyAddPipelineArgs**](EventPipelinePolicyAddPipelineArgs.md)| eventPipelinePolicyAddPipelineArgs | [optional]

### Return type

[**EventPipelinePolicyMapModel**](EventPipelinePolicyMapModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pipeline policy children |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_pipeline_policy_service_create_event_pipeline_policy**
> EventPipelinePolicyModel event_pipeline_policy_service_create_event_pipeline_policy()

Create Pipeline Policy

Create Pipeline Policy

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import event_pipeline_policy_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.event_pipeline_policy_model import EventPipelinePolicyModel
from secret_server_openapiclient.model.event_pipeline_policy_create_args import EventPipelinePolicyCreateArgs
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
    api_instance = event_pipeline_policy_api.EventPipelinePolicyApi(api_client)
    event_pipeline_policy_create_args = EventPipelinePolicyCreateArgs(
        data=EventPipelinePolicyCreateModel(
            active=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            event_entity_type_id=UpdateFieldValueOfInt32(
                dirty=True,
                value=1,
            ),
            event_pipeline_policy_description=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            event_pipeline_policy_name=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            external_instance_id="external_instance_id_example",
            is_system=True,
            pipelines=UpdateFieldValueOfEventPipelineUpdateModelArray(
                dirty=True,
                value=[
                    EventPipelineUpdateModel(
                        active=UpdateFieldValueOfBoolean(
                            dirty=True,
                            value=True,
                        ),
                        event_pipeline_description=UpdateFieldValueOfString(
                            dirty=True,
                            value="value_example",
                        ),
                        event_pipeline_name=UpdateFieldValueOfString(
                            dirty=True,
                            value="value_example",
                        ),
                        filters=UpdateFieldValueOfEventPipelineFilterMapUpdateModelArray(
                            dirty=True,
                            value=[
                                EventPipelineFilterMapUpdateModel(
                                    event_pipeline_filter_id=UpdateFieldValueOfInt32(
                                        dirty=True,
                                        value=1,
                                    ),
                                    event_pipeline_filter_map_id=UpdateFieldValueOfOptionalInt32(
                                        dirty=True,
                                        value=1,
                                    ),
                                    event_pipeline_filter_name=UpdateFieldValueOfString(
                                        dirty=True,
                                        value="value_example",
                                    ),
                                    settings=UpdateFieldValueOfSettingUpdateModelArray(
                                        dirty=True,
                                        value=[
                                            SettingUpdateModel(
                                                setting_name=UpdateFieldValueOfString(
                                                    dirty=True,
                                                    value="value_example",
                                                ),
                                                setting_value=UpdateFieldValueOfString(
                                                    dirty=True,
                                                    value="value_example",
                                                ),
                                            ),
                                        ],
                                    ),
                                    sort_order=UpdateFieldValueOfInt32(
                                        dirty=True,
                                        value=1,
                                    ),
                                ),
                            ],
                        ),
                        tasks=UpdateFieldValueOfEventPipelineTaskMapUpdateModelArray(
                            dirty=True,
                            value=[
                                EventPipelineTaskMapUpdateModel(
                                    event_pipeline_task_id=UpdateFieldValueOfInt32(
                                        dirty=True,
                                        value=1,
                                    ),
                                    event_pipeline_task_map_id=UpdateFieldValueOfOptionalInt32(
                                        dirty=True,
                                        value=1,
                                    ),
                                    event_pipeline_task_name=UpdateFieldValueOfString(
                                        dirty=True,
                                        value="value_example",
                                    ),
                                    settings=UpdateFieldValueOfSettingUpdateModelArray(
                                        dirty=True,
                                        value=[
                                            SettingUpdateModel(
                                                setting_name=UpdateFieldValueOfString(
                                                    dirty=True,
                                                    value="value_example",
                                                ),
                                                setting_value=UpdateFieldValueOfString(
                                                    dirty=True,
                                                    value="value_example",
                                                ),
                                            ),
                                        ],
                                    ),
                                    sort_order=UpdateFieldValueOfInt32(
                                        dirty=True,
                                        value=1,
                                    ),
                                ),
                            ],
                        ),
                        triggers=UpdateFieldValueOfEventPipelineTriggerUpdateModelArray(
                            dirty=True,
                            value=[
                                EventPipelineTriggerUpdateModel(
                                    event_action_id=UpdateFieldValueOfInt32(
                                        dirty=True,
                                        value=1,
                                    ),
                                ),
                            ],
                        ),
                    ),
                ],
            ),
            reuse_existing_pipelines=True,
        ),
    ) # EventPipelinePolicyCreateArgs | eventPipelinePolicy (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Pipeline Policy
        api_response = api_instance.event_pipeline_policy_service_create_event_pipeline_policy(event_pipeline_policy_create_args=event_pipeline_policy_create_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling EventPipelinePolicyApi->event_pipeline_policy_service_create_event_pipeline_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_pipeline_policy_create_args** | [**EventPipelinePolicyCreateArgs**](EventPipelinePolicyCreateArgs.md)| eventPipelinePolicy | [optional]

### Return type

[**EventPipelinePolicyModel**](EventPipelinePolicyModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Newly created model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_pipeline_policy_service_duplicate_event_pipeline_policy**
> EventPipelinePolicyModel event_pipeline_policy_service_duplicate_event_pipeline_policy()

Duplicate Event Pipeline Policy

Create a duplicate of a policy

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import event_pipeline_policy_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.event_pipeline_policy_import_args import EventPipelinePolicyImportArgs
from secret_server_openapiclient.model.event_pipeline_policy_model import EventPipelinePolicyModel
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
    api_instance = event_pipeline_policy_api.EventPipelinePolicyApi(api_client)
    event_pipeline_policy_import_args = EventPipelinePolicyImportArgs(
        data="data_example",
    ) # EventPipelinePolicyImportArgs | importPolicy (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Duplicate Event Pipeline Policy
        api_response = api_instance.event_pipeline_policy_service_duplicate_event_pipeline_policy(event_pipeline_policy_import_args=event_pipeline_policy_import_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling EventPipelinePolicyApi->event_pipeline_policy_service_duplicate_event_pipeline_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_pipeline_policy_import_args** | [**EventPipelinePolicyImportArgs**](EventPipelinePolicyImportArgs.md)| importPolicy | [optional]

### Return type

[**EventPipelinePolicyModel**](EventPipelinePolicyModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The duplicated model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_pipeline_policy_service_export_event_pipeline_policy**
> str event_pipeline_policy_service_export_event_pipeline_policy(id)

Export Event Pipeline Policy

Export a policy

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import event_pipeline_policy_api
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
    api_instance = event_pipeline_policy_api.EventPipelinePolicyApi(api_client)
    id = 1 # int | Event Pipeline Policy ID

    # example passing only required values which don't have defaults set
    try:
        # Export Event Pipeline Policy
        api_response = api_instance.event_pipeline_policy_service_export_event_pipeline_policy(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling EventPipelinePolicyApi->event_pipeline_policy_service_export_event_pipeline_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Event Pipeline Policy ID |

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
**200** | the exported json of the policy |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_pipeline_policy_service_get_child_folder_data_for_pipeline_policy_folder**
> [EventPipelinePolicyFolderChildData] event_pipeline_policy_service_get_child_folder_data_for_pipeline_policy_folder(folder_id, id)

Get Child Folder Data For Pipeline Policy Folder

Get all of the child data for a specific folder

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import event_pipeline_policy_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.event_pipeline_policy_folder_child_data import EventPipelinePolicyFolderChildData
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
    api_instance = event_pipeline_policy_api.EventPipelinePolicyApi(api_client)
    folder_id = 1 # int | Folder ID
    id = 1 # int | Event Pipeline Policy ID

    # example passing only required values which don't have defaults set
    try:
        # Get Child Folder Data For Pipeline Policy Folder
        api_response = api_instance.event_pipeline_policy_service_get_child_folder_data_for_pipeline_policy_folder(folder_id, id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling EventPipelinePolicyApi->event_pipeline_policy_service_get_child_folder_data_for_pipeline_policy_folder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**| Folder ID |
 **id** | **int**| Event Pipeline Policy ID |

### Return type

[**[EventPipelinePolicyFolderChildData]**](EventPipelinePolicyFolderChildData.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of child data |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_pipeline_policy_service_get_event_pipeline_policies**
> PagingOfEventPipelinePolicySummary event_pipeline_policy_service_get_event_pipeline_policies()

Get Event Pipeline Policies

Get all pipeline policies

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import event_pipeline_policy_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.paging_of_event_pipeline_policy_summary import PagingOfEventPipelinePolicySummary
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
    api_instance = event_pipeline_policy_api.EventPipelinePolicyApi(api_client)
    filter_event_pipeline_id = 1 # int | EventPipelineId (optional)
    filter_event_pipeline_policy_name = "filter.eventPipelinePolicyName_example" # str | EventPipelinePolicyName (optional)
    filter_folder_id = 1 # int | FolderId (optional)
    filter_include_active = True # bool | IncludeActive (optional)
    filter_include_inactive = True # bool | IncludeInactive (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Event Pipeline Policies
        api_response = api_instance.event_pipeline_policy_service_get_event_pipeline_policies(filter_event_pipeline_id=filter_event_pipeline_id, filter_event_pipeline_policy_name=filter_event_pipeline_policy_name, filter_folder_id=filter_folder_id, filter_include_active=filter_include_active, filter_include_inactive=filter_include_inactive, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling EventPipelinePolicyApi->event_pipeline_policy_service_get_event_pipeline_policies: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_event_pipeline_id** | **int**| EventPipelineId | [optional]
 **filter_event_pipeline_policy_name** | **str**| EventPipelinePolicyName | [optional]
 **filter_folder_id** | **int**| FolderId | [optional]
 **filter_include_active** | **bool**| IncludeActive | [optional]
 **filter_include_inactive** | **bool**| IncludeInactive | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfEventPipelinePolicySummary**](PagingOfEventPipelinePolicySummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paged list of all policies |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_pipeline_policy_service_get_event_pipeline_policy**
> EventPipelinePolicyModel event_pipeline_policy_service_get_event_pipeline_policy(id)

Get Event Pipeline Policy

Get a specific policy by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import event_pipeline_policy_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.event_pipeline_policy_model import EventPipelinePolicyModel
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
    api_instance = event_pipeline_policy_api.EventPipelinePolicyApi(api_client)
    id = 1 # int | Event Pipeline Policy ID

    # example passing only required values which don't have defaults set
    try:
        # Get Event Pipeline Policy
        api_response = api_instance.event_pipeline_policy_service_get_event_pipeline_policy(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling EventPipelinePolicyApi->event_pipeline_policy_service_get_event_pipeline_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Event Pipeline Policy ID |

### Return type

[**EventPipelinePolicyModel**](EventPipelinePolicyModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Policy details |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_pipeline_policy_service_get_event_pipeline_policy_run_activity**
> [EventPipelinePolicyRunActivityViewModel] event_pipeline_policy_service_get_event_pipeline_policy_run_activity()

Get Event Pipeline Policy Run Activity

Get all activity for a specific policy run ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import event_pipeline_policy_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.event_pipeline_policy_run_activity_view_model import EventPipelinePolicyRunActivityViewModel
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
    api_instance = event_pipeline_policy_api.EventPipelinePolicyApi(api_client)
    event_pipeline_id = 1 # int | eventPipelineId (optional)
    event_pipeline_policy_run_id = "eventPipelinePolicyRunId_example" # str | Event Pipeline Policy Run ID (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Event Pipeline Policy Run Activity
        api_response = api_instance.event_pipeline_policy_service_get_event_pipeline_policy_run_activity(event_pipeline_id=event_pipeline_id, event_pipeline_policy_run_id=event_pipeline_policy_run_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling EventPipelinePolicyApi->event_pipeline_policy_service_get_event_pipeline_policy_run_activity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_pipeline_id** | **int**| eventPipelineId | [optional]
 **event_pipeline_policy_run_id** | **str**| Event Pipeline Policy Run ID | [optional]

### Return type

[**[EventPipelinePolicyRunActivityViewModel]**](EventPipelinePolicyRunActivityViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details for a specific run |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_pipeline_policy_service_get_event_pipeline_policy_runs**
> PagingOfEventPipelineRunViewModel event_pipeline_policy_service_get_event_pipeline_policy_runs()

Get Event Pipeline Policy Runs

Get all runs by specific search criteria

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import event_pipeline_policy_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.paging_of_event_pipeline_run_view_model import PagingOfEventPipelineRunViewModel
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
    api_instance = event_pipeline_policy_api.EventPipelinePolicyApi(api_client)
    filter_event_pipeline_policy_id = 1 # int | EventPipelinePolicyId (optional)
    filter_event_pipeline_policy_run_id = "filter.eventPipelinePolicyRunId_example" # str | EventPipelinePolicyRunId (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Event Pipeline Policy Runs
        api_response = api_instance.event_pipeline_policy_service_get_event_pipeline_policy_runs(filter_event_pipeline_policy_id=filter_event_pipeline_policy_id, filter_event_pipeline_policy_run_id=filter_event_pipeline_policy_run_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling EventPipelinePolicyApi->event_pipeline_policy_service_get_event_pipeline_policy_runs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_event_pipeline_policy_id** | **int**| EventPipelinePolicyId | [optional]
 **filter_event_pipeline_policy_run_id** | **str**| EventPipelinePolicyRunId | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfEventPipelineRunViewModel**](PagingOfEventPipelineRunViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paged list of policy runs |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_pipeline_policy_service_get_folders_for_pipeline_policies**
> [FolderSimpleViewModel] event_pipeline_policy_service_get_folders_for_pipeline_policies(id)

Get Folders For Pipeline Policies

Get all of the folders for a policy pipeline

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import event_pipeline_policy_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.folder_simple_view_model import FolderSimpleViewModel
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
    api_instance = event_pipeline_policy_api.EventPipelinePolicyApi(api_client)
    id = 1 # int | Event Pipeline Policy ID

    # example passing only required values which don't have defaults set
    try:
        # Get Folders For Pipeline Policies
        api_response = api_instance.event_pipeline_policy_service_get_folders_for_pipeline_policies(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling EventPipelinePolicyApi->event_pipeline_policy_service_get_folders_for_pipeline_policies: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Event Pipeline Policy ID |

### Return type

[**[FolderSimpleViewModel]**](FolderSimpleViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all folders to which this policy is applied |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_pipeline_policy_service_get_group_count_for_pipeline_policy**
> int event_pipeline_policy_service_get_group_count_for_pipeline_policy(id)

Get Group Count For Pipeline Policy

Returns the count of groups that have a particular pipeline policy assigned

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import event_pipeline_policy_api
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
    api_instance = event_pipeline_policy_api.EventPipelinePolicyApi(api_client)
    id = 1 # int | Event Pipeline Policy ID

    # example passing only required values which don't have defaults set
    try:
        # Get Group Count For Pipeline Policy
        api_response = api_instance.event_pipeline_policy_service_get_group_count_for_pipeline_policy(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling EventPipelinePolicyApi->event_pipeline_policy_service_get_group_count_for_pipeline_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Event Pipeline Policy ID |

### Return type

**int**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Number of groups affected |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_pipeline_policy_service_get_groups_for_pipeline_policies**
> [UserGroupSearchResultModel] event_pipeline_policy_service_get_groups_for_pipeline_policies(id)

Get Groups For Pipeline Policies

Get all of the groups that apply this pipeline

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import event_pipeline_policy_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.user_group_search_result_model import UserGroupSearchResultModel
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
    api_instance = event_pipeline_policy_api.EventPipelinePolicyApi(api_client)
    id = 1 # int | Event Pipeline Policy ID

    # example passing only required values which don't have defaults set
    try:
        # Get Groups For Pipeline Policies
        api_response = api_instance.event_pipeline_policy_service_get_groups_for_pipeline_policies(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling EventPipelinePolicyApi->event_pipeline_policy_service_get_groups_for_pipeline_policies: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Event Pipeline Policy ID |

### Return type

[**[UserGroupSearchResultModel]**](UserGroupSearchResultModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all groups |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_pipeline_policy_service_get_secret_policies_for_pipeline_policies**
> PagingOfSecretPolicyViewModel event_pipeline_policy_service_get_secret_policies_for_pipeline_policies(id)

Get Secret Policies For Pipeline Policies

Get all of the secret polocies that are related to this pipeline

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import event_pipeline_policy_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.paging_of_secret_policy_view_model import PagingOfSecretPolicyViewModel
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
    api_instance = event_pipeline_policy_api.EventPipelinePolicyApi(api_client)
    id = 1 # int | Event Pipeline Policy ID
    filter_event_pipeline_policy_id = 1 # int | EventPipelinePolicyId (optional)
    filter_event_pipeline_policy_name = "filter.eventPipelinePolicyName_example" # str | EventPipelinePolicyName (optional)
    filter_include_active = True # bool | IncludeActive (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Secret Policies For Pipeline Policies
        api_response = api_instance.event_pipeline_policy_service_get_secret_policies_for_pipeline_policies(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling EventPipelinePolicyApi->event_pipeline_policy_service_get_secret_policies_for_pipeline_policies: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Secret Policies For Pipeline Policies
        api_response = api_instance.event_pipeline_policy_service_get_secret_policies_for_pipeline_policies(id, filter_event_pipeline_policy_id=filter_event_pipeline_policy_id, filter_event_pipeline_policy_name=filter_event_pipeline_policy_name, filter_include_active=filter_include_active, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling EventPipelinePolicyApi->event_pipeline_policy_service_get_secret_policies_for_pipeline_policies: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Event Pipeline Policy ID |
 **filter_event_pipeline_policy_id** | **int**| EventPipelinePolicyId | [optional]
 **filter_event_pipeline_policy_name** | **str**| EventPipelinePolicyName | [optional]
 **filter_include_active** | **bool**| IncludeActive | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfSecretPolicyViewModel**](PagingOfSecretPolicyViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paged list of secret policies |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_pipeline_policy_service_import_event_pipeline_policy**
> EventPipelinePolicyModel event_pipeline_policy_service_import_event_pipeline_policy()

Import Event Pipeline Policy

Import a policy

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import event_pipeline_policy_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.event_pipeline_policy_import_args import EventPipelinePolicyImportArgs
from secret_server_openapiclient.model.event_pipeline_policy_model import EventPipelinePolicyModel
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
    api_instance = event_pipeline_policy_api.EventPipelinePolicyApi(api_client)
    event_pipeline_policy_import_args = EventPipelinePolicyImportArgs(
        data="data_example",
    ) # EventPipelinePolicyImportArgs | importPolicy (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Import Event Pipeline Policy
        api_response = api_instance.event_pipeline_policy_service_import_event_pipeline_policy(event_pipeline_policy_import_args=event_pipeline_policy_import_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling EventPipelinePolicyApi->event_pipeline_policy_service_import_event_pipeline_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_pipeline_policy_import_args** | [**EventPipelinePolicyImportArgs**](EventPipelinePolicyImportArgs.md)| importPolicy | [optional]

### Return type

[**EventPipelinePolicyModel**](EventPipelinePolicyModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The imported policy model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_pipeline_policy_service_remove_event_pipeline_from_policy**
> bool event_pipeline_policy_service_remove_event_pipeline_from_policy(pipeline_id, policy_id)

Remove Event Pipeline From Policy

Remove a pipeline from a specific policy

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import event_pipeline_policy_api
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
    api_instance = event_pipeline_policy_api.EventPipelinePolicyApi(api_client)
    pipeline_id = 1 # int | Event Pipeline ID
    policy_id = 1 # int | Event Pipeline Policy ID

    # example passing only required values which don't have defaults set
    try:
        # Remove Event Pipeline From Policy
        api_response = api_instance.event_pipeline_policy_service_remove_event_pipeline_from_policy(pipeline_id, policy_id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling EventPipelinePolicyApi->event_pipeline_policy_service_remove_event_pipeline_from_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_id** | **int**| Event Pipeline ID |
 **policy_id** | **int**| Event Pipeline Policy ID |

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
**200** | boolean indicating success |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_pipeline_policy_service_update_event_pipeline_policy**
> EventPipelinePolicyModel event_pipeline_policy_service_update_event_pipeline_policy(id)

Update Event Pipeline Policy

Update a policy

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import event_pipeline_policy_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.event_pipeline_policy_model import EventPipelinePolicyModel
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.event_pipeline_policy_update_args import EventPipelinePolicyUpdateArgs
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
    api_instance = event_pipeline_policy_api.EventPipelinePolicyApi(api_client)
    id = 1 # int | Event Pipeline Policy ID
    event_pipeline_policy_update_args = EventPipelinePolicyUpdateArgs(
        data=EventPipelinePolicyUpdateModel(
            active=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            event_pipeline_policy_description=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            event_pipeline_policy_name=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
        ),
    ) # EventPipelinePolicyUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Event Pipeline Policy
        api_response = api_instance.event_pipeline_policy_service_update_event_pipeline_policy(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling EventPipelinePolicyApi->event_pipeline_policy_service_update_event_pipeline_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Event Pipeline Policy
        api_response = api_instance.event_pipeline_policy_service_update_event_pipeline_policy(id, event_pipeline_policy_update_args=event_pipeline_policy_update_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling EventPipelinePolicyApi->event_pipeline_policy_service_update_event_pipeline_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Event Pipeline Policy ID |
 **event_pipeline_policy_update_args** | [**EventPipelinePolicyUpdateArgs**](EventPipelinePolicyUpdateArgs.md)| args | [optional]

### Return type

[**EventPipelinePolicyModel**](EventPipelinePolicyModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The update policy |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_pipeline_policy_service_update_event_pipeline_policy_folder_maps**
> bool event_pipeline_policy_service_update_event_pipeline_policy_folder_maps(id)

Update Event Pipeline Policy Folder Maps

Adds or updates the Pipeline Policy Folder Maps to reflect the collection of folder maps for the pipeline policy that was passed in.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import event_pipeline_policy_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.event_pipeline_policy_folder_map_update_args import EventPipelinePolicyFolderMapUpdateArgs
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
    api_instance = event_pipeline_policy_api.EventPipelinePolicyApi(api_client)
    id = 1 # int | Event Pipeline Policy ID
    event_pipeline_policy_folder_map_update_args = EventPipelinePolicyFolderMapUpdateArgs(
        data=[
            1,
        ],
    ) # EventPipelinePolicyFolderMapUpdateArgs | eventPipelinePolicyFolderMaps (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Event Pipeline Policy Folder Maps
        api_response = api_instance.event_pipeline_policy_service_update_event_pipeline_policy_folder_maps(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling EventPipelinePolicyApi->event_pipeline_policy_service_update_event_pipeline_policy_folder_maps: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Event Pipeline Policy Folder Maps
        api_response = api_instance.event_pipeline_policy_service_update_event_pipeline_policy_folder_maps(id, event_pipeline_policy_folder_map_update_args=event_pipeline_policy_folder_map_update_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling EventPipelinePolicyApi->event_pipeline_policy_service_update_event_pipeline_policy_folder_maps: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Event Pipeline Policy ID |
 **event_pipeline_policy_folder_map_update_args** | [**EventPipelinePolicyFolderMapUpdateArgs**](EventPipelinePolicyFolderMapUpdateArgs.md)| eventPipelinePolicyFolderMaps | [optional]

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
**200** | boolean indicating success |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_pipeline_policy_service_update_event_pipeline_policy_group_maps**
> bool event_pipeline_policy_service_update_event_pipeline_policy_group_maps(id)

Update Event Pipeline Policy Group Maps

Adds or updates the Pipeline Policy Group Maps to reflect the collection of group maps for the pipeline policy that was passed in.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import event_pipeline_policy_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.event_pipeline_policy_group_map_update_args import EventPipelinePolicyGroupMapUpdateArgs
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
    api_instance = event_pipeline_policy_api.EventPipelinePolicyApi(api_client)
    id = 1 # int | Event Pipeline Policy ID
    event_pipeline_policy_group_map_update_args = EventPipelinePolicyGroupMapUpdateArgs(
        data=[
            1,
        ],
    ) # EventPipelinePolicyGroupMapUpdateArgs | eventPipelinePolicyGroupMaps (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Event Pipeline Policy Group Maps
        api_response = api_instance.event_pipeline_policy_service_update_event_pipeline_policy_group_maps(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling EventPipelinePolicyApi->event_pipeline_policy_service_update_event_pipeline_policy_group_maps: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Event Pipeline Policy Group Maps
        api_response = api_instance.event_pipeline_policy_service_update_event_pipeline_policy_group_maps(id, event_pipeline_policy_group_map_update_args=event_pipeline_policy_group_map_update_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling EventPipelinePolicyApi->event_pipeline_policy_service_update_event_pipeline_policy_group_maps: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Event Pipeline Policy ID |
 **event_pipeline_policy_group_map_update_args** | [**EventPipelinePolicyGroupMapUpdateArgs**](EventPipelinePolicyGroupMapUpdateArgs.md)| eventPipelinePolicyGroupMaps | [optional]

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
**200** | boolean indicating success |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_pipeline_policy_service_update_event_pipeline_policy_sort_order**
> EventPipelinePolicyModel event_pipeline_policy_service_update_event_pipeline_policy_sort_order(id)

Update Event Pipeline Policy Sort Order

Update the sort order of a policy

### Example

* Api Key Authentication (BearerToken):

```python
import time
import secret_server_openapiclient
from secret_server_openapiclient.api import event_pipeline_policy_api
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.event_pipeline_policy_model import EventPipelinePolicyModel
from secret_server_openapiclient.model.event_pipeline_policy_sort_order_update_args import EventPipelinePolicySortOrderUpdateArgs
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
    api_instance = event_pipeline_policy_api.EventPipelinePolicyApi(api_client)
    id = 1 # int | Event Pipeline Policy ID
    event_pipeline_policy_sort_order_update_args = EventPipelinePolicySortOrderUpdateArgs(
        new_sort_order=1,
    ) # EventPipelinePolicySortOrderUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Event Pipeline Policy Sort Order
        api_response = api_instance.event_pipeline_policy_service_update_event_pipeline_policy_sort_order(id)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling EventPipelinePolicyApi->event_pipeline_policy_service_update_event_pipeline_policy_sort_order: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Event Pipeline Policy Sort Order
        api_response = api_instance.event_pipeline_policy_service_update_event_pipeline_policy_sort_order(id, event_pipeline_policy_sort_order_update_args=event_pipeline_policy_sort_order_update_args)
        pprint(api_response)
    except secret_server_openapiclient.ApiException as e:
        print("Exception when calling EventPipelinePolicyApi->event_pipeline_policy_service_update_event_pipeline_policy_sort_order: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Event Pipeline Policy ID |
 **event_pipeline_policy_sort_order_update_args** | [**EventPipelinePolicySortOrderUpdateArgs**](EventPipelinePolicySortOrderUpdateArgs.md)| args | [optional]

### Return type

[**EventPipelinePolicyModel**](EventPipelinePolicyModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updated policy |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

