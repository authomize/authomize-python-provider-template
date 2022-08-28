# plugins.SecretPolicyApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**secret_policy_service_create_secret_policy_v2**](SecretPolicyApi.md#secret_policy_service_create_secret_policy_v2) | **POST** /v2/secret-policy | Create a Secret Policy
[**secret_policy_service_get_secret_policy_audit**](SecretPolicyApi.md#secret_policy_service_get_secret_policy_audit) | **GET** /v1/secret-policy/{id}/audit | Get Secret Policy Audits
[**secret_policy_service_get_secret_policy_status**](SecretPolicyApi.md#secret_policy_service_get_secret_policy_status) | **GET** /v1/secret-policy/{id}/status | Get the Secret Policy status
[**secret_policy_service_get_secret_policy_stub_v2**](SecretPolicyApi.md#secret_policy_service_get_secret_policy_stub_v2) | **GET** /v2/secret-policy/stub | Get Secret Policy Stub
[**secret_policy_service_get_secret_policy_v2**](SecretPolicyApi.md#secret_policy_service_get_secret_policy_v2) | **GET** /v2/secret-policy/{id} | Get Secret Policy
[**secret_policy_service_search_secret_policies**](SecretPolicyApi.md#secret_policy_service_search_secret_policies) | **GET** /v1/secret-policy/search | Search Secret Policies
[**secret_policy_service_update_secret_policy_v2**](SecretPolicyApi.md#secret_policy_service_update_secret_policy_v2) | **PATCH** /v2/secret-policy/{id} | Update a Secret Policy


# **secret_policy_service_create_secret_policy_v2**
> SecretPolicyDetailModelV2 secret_policy_service_create_secret_policy_v2()

Create a Secret Policy

Create a Secret Policy and return detail model

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_policy_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_policy_detail_model_v2 import SecretPolicyDetailModelV2
from plugins.model.secret_policy_create_args_v2 import SecretPolicyCreateArgsV2
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
    api_instance = secret_policy_api.SecretPolicyApi(api_client)
    secret_policy_create_args_v2 = SecretPolicyCreateArgsV2(
        data=SecretPolicyCreateModelV2(
            active=True,
            general_items=SecretPolicyGeneralItemsCreateModel(
                jumpbox_route_id=SecretPolicyDataItemOfOptionalGuid(
                    policy_apply_type=PolicyApplyType("{}"),
                    value=None,
                ),
                site_id=SecretPolicyDataItemOfOptionalInt32(
                    policy_apply_type=PolicyApplyType("{}"),
                    value=None,
                ),
            ),
            launcher_items=SecretPolicyLauncherItemsCreateModel(
                launcher_settings=UpdateFieldValueOfSecretPolicyDataItemOfLauncherSettingsData(
                    dirty=True,
                    value=SecretPolicyDataItemOfLauncherSettingsData(
                        policy_apply_type=PolicyApplyType("{}"),
                        value=LauncherSettingsData(
                            allow_clipboard=True,
                            allow_drives=True,
                            allow_printers=True,
                            allow_smart_cards=True,
                            connect_to_console=True,
                            launcher_height=None,
                            launcher_width=None,
                            use_custom_launcher_resolution=True,
                        ),
                    ),
                ),
                web_launcher_requires_incognito_mode=SecretPolicyDataItemOfOptionalBoolean(
                    policy_apply_type=PolicyApplyType("{}"),
                    value=True,
                ),
            ),
            rpc_items=SecretPolicyRpcItemsCreateModel(
                associated_secret_id1=SecretPolicyDataItemOfOptionalInt32(
                    policy_apply_type=PolicyApplyType("{}"),
                    value=None,
                ),
                associated_secret_id2=SecretPolicyDataItemOfOptionalInt32(
                    policy_apply_type=PolicyApplyType("{}"),
                    value=None,
                ),
                auto_change_on_expiration=SecretPolicyDataItemOfOptionalBoolean(
                    policy_apply_type=PolicyApplyType("{}"),
                    value=True,
                ),
                auto_change_schedule=SecretPolicyDataItemOfAutoChangeScheduleDataModel(
                    policy_apply_type=PolicyApplyType("{}"),
                    value=AutoChangeScheduleDataModel(
                        change_only_when_expired=True,
                        change_type=None,
                        days=None,
                        friday=True,
                        monday=True,
                        monthly_day=None,
                        monthly_day_of_month=None,
                        monthly_day_order=None,
                        monthly_day_order_recurrence=None,
                        monthly_day_recurrence=None,
                        monthly_schedule_type=None,
                        saturday=True,
                        starting_on=None,
                        sunday=True,
                        thursday=True,
                        tuesday=True,
                        wednesday=True,
                        weeks=None,
                    ),
                ),
                heart_beat_enabled=SecretPolicyDataItemOfOptionalBoolean(
                    policy_apply_type=PolicyApplyType("{}"),
                    value=True,
                ),
                password_type_web_script_id=SecretPolicyDataItemOfOptionalInt32(
                    policy_apply_type=PolicyApplyType("{}"),
                    value=None,
                ),
                privileged_secret_id=SecretPolicyDataItemOfOptionalInt32(
                    policy_apply_type=PolicyApplyType("{}"),
                    value=None,
                ),
            ),
            secret_policy_description=None,
            secret_policy_name=None,
            security_items=SecretPolicySecurityItemsCreateModel(
                allow_owners_unrestricted_ssh_commands=SecretPolicyDataItemOfOptionalBoolean(
                    policy_apply_type=PolicyApplyType("{}"),
                    value=True,
                ),
                approval_groups=SecretPolicyDataItemOfUserGroupMapDataModelArray(
                    policy_apply_type=PolicyApplyType("{}"),
                    value=[
                        UserGroupMapDataModel(
                            group_id=None,
                            user_group_map_type=UserGroupMapType("{}"),
                        ),
                    ],
                ),
                approval_workflow=SecretPolicyDataItemOfOptionalInt32(
                    policy_apply_type=PolicyApplyType("{}"),
                    value=None,
                ),
                check_out_change_password=SecretPolicyDataItemOfOptionalBoolean(
                    policy_apply_type=PolicyApplyType("{}"),
                    value=True,
                ),
                check_out_enabled=SecretPolicyDataItemOfOptionalBoolean(
                    policy_apply_type=PolicyApplyType("{}"),
                    value=True,
                ),
                check_out_interval_minutes=SecretPolicyDataItemOfOptionalInt32(
                    policy_apply_type=PolicyApplyType("{}"),
                    value=None,
                ),
                enable_ssh_command_restrictions=SecretPolicyDataItemOfOptionalBoolean(
                    policy_apply_type=PolicyApplyType("{}"),
                    value=True,
                ),
                event_pipeline_policy=SecretPolicyDataItemOfOptionalInt32(
                    policy_apply_type=PolicyApplyType("{}"),
                    value=None,
                ),
                hide_launcher_password=SecretPolicyDataItemOfOptionalBoolean(
                    policy_apply_type=PolicyApplyType("{}"),
                    value=True,
                ),
                is_proxy_enabled=SecretPolicyDataItemOfOptionalBoolean(
                    policy_apply_type=PolicyApplyType("{}"),
                    value=True,
                ),
                is_session_recording_enabled=SecretPolicyDataItemOfOptionalBoolean(
                    policy_apply_type=PolicyApplyType("{}"),
                    value=True,
                ),
                require_approval_for_access=SecretPolicyDataItemOfOptionalBoolean(
                    policy_apply_type=PolicyApplyType("{}"),
                    value=True,
                ),
                require_approval_for_access_for_editors=SecretPolicyDataItemOfOptionalBoolean(
                    policy_apply_type=PolicyApplyType("{}"),
                    value=True,
                ),
                require_approval_for_access_for_owners_and_approvers=SecretPolicyDataItemOfOptionalBoolean(
                    policy_apply_type=PolicyApplyType("{}"),
                    value=True,
                ),
                require_view_comment=SecretPolicyDataItemOfOptionalBoolean(
                    policy_apply_type=PolicyApplyType("{}"),
                    value=True,
                ),
                run_launcher_using_ssh_key_secret_id=SecretPolicyDataItemOfOptionalInt32(
                    policy_apply_type=PolicyApplyType("{}"),
                    value=None,
                ),
                ssh_command_blocklist_editors=SecretPolicyDataItemOfOptionalGuid(
                    policy_apply_type=PolicyApplyType("{}"),
                    value=None,
                ),
                ssh_command_blocklist_owners=SecretPolicyDataItemOfOptionalGuid(
                    policy_apply_type=PolicyApplyType("{}"),
                    value=None,
                ),
                ssh_command_blocklist_viewers=SecretPolicyDataItemOfOptionalGuid(
                    policy_apply_type=PolicyApplyType("{}"),
                    value=None,
                ),
                ssh_command_menu_groups=SecretPolicyDataItemOfSshCommandMenuGroupModelArray(
                    policy_apply_type=PolicyApplyType("{}"),
                    value=[
                        SshCommandMenuGroupModel(
                            group_id=None,
                            ssh_command_menu_id=None,
                        ),
                    ],
                ),
                ssh_command_restriction_type=SecretPolicyDataItemOfOptionalCommandRestrictionType(
                    policy_apply_type=PolicyApplyType("{}"),
                    value=None,
                ),
            ),
        ),
    ) # SecretPolicyCreateArgsV2 | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a Secret Policy
        api_response = api_instance.secret_policy_service_create_secret_policy_v2(secret_policy_create_args_v2=secret_policy_create_args_v2)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretPolicyApi->secret_policy_service_create_secret_policy_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_policy_create_args_v2** | [**SecretPolicyCreateArgsV2**](SecretPolicyCreateArgsV2.md)| args | [optional]

### Return type

[**SecretPolicyDetailModelV2**](SecretPolicyDetailModelV2.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Policy that was created |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_policy_service_get_secret_policy_audit**
> IPagingOfSecretPolicyAuditSummary secret_policy_service_get_secret_policy_audit(id)

Get Secret Policy Audits

Get Secret Policy Audits for passed in Id

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_policy_api
from plugins.model.i_paging_of_secret_policy_audit_summary import IPagingOfSecretPolicyAuditSummary
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
    api_instance = secret_policy_api.SecretPolicyApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    is_exporting = True # bool | isExporting (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Secret Policy Audits
        api_response = api_instance.secret_policy_service_get_secret_policy_audit(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretPolicyApi->secret_policy_service_get_secret_policy_audit: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Secret Policy Audits
        api_response = api_instance.secret_policy_service_get_secret_policy_audit(id, is_exporting=is_exporting, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretPolicyApi->secret_policy_service_get_secret_policy_audit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **is_exporting** | **bool**| isExporting | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**IPagingOfSecretPolicyAuditSummary**](IPagingOfSecretPolicyAuditSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Policy Audits |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_policy_service_get_secret_policy_status**
> SecretPolicyStatusModel secret_policy_service_get_secret_policy_status(id)

Get the Secret Policy status

Gets the status of what secrets and folders the policy is applied to.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_policy_api
from plugins.model.secret_policy_status_model import SecretPolicyStatusModel
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
    api_instance = secret_policy_api.SecretPolicyApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id

    # example passing only required values which don't have defaults set
    try:
        # Get the Secret Policy status
        api_response = api_instance.secret_policy_service_get_secret_policy_status(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretPolicyApi->secret_policy_service_get_secret_policy_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |

### Return type

[**SecretPolicyStatusModel**](SecretPolicyStatusModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Policy status for queried policy. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_policy_service_get_secret_policy_stub_v2**
> SecretPolicyDetailModelV2 secret_policy_service_get_secret_policy_stub_v2()

Get Secret Policy Stub

Get Secret Policy

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_policy_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_policy_detail_model_v2 import SecretPolicyDetailModelV2
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
    api_instance = secret_policy_api.SecretPolicyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Secret Policy Stub
        api_response = api_instance.secret_policy_service_get_secret_policy_stub_v2()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretPolicyApi->secret_policy_service_get_secret_policy_stub_v2: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SecretPolicyDetailModelV2**](SecretPolicyDetailModelV2.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stub of a Secret Policy Detail model |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_policy_service_get_secret_policy_v2**
> SecretPolicyDetailModelV2 secret_policy_service_get_secret_policy_v2(id)

Get Secret Policy

Get Secret Policy for passed in Id

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_policy_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_policy_detail_model_v2 import SecretPolicyDetailModelV2
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
    api_instance = secret_policy_api.SecretPolicyApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id

    # example passing only required values which don't have defaults set
    try:
        # Get Secret Policy
        api_response = api_instance.secret_policy_service_get_secret_policy_v2(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretPolicyApi->secret_policy_service_get_secret_policy_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |

### Return type

[**SecretPolicyDetailModelV2**](SecretPolicyDetailModelV2.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Policy if found |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_policy_service_search_secret_policies**
> IPagingOfSecretPolicyModel secret_policy_service_search_secret_policies()

Search Secret Policies

Search Secret Policies

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_policy_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.i_paging_of_secret_policy_model import IPagingOfSecretPolicyModel
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
    api_instance = secret_policy_api.SecretPolicyApi(api_client)
    filter_include_inactive = True # bool | Whether or not to include inactive secret policies (optional)
    filter_secret_policy_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Results will contain this text in the policy name (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Secret Policies
        api_response = api_instance.secret_policy_service_search_secret_policies(filter_include_inactive=filter_include_inactive, filter_secret_policy_name=filter_secret_policy_name, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretPolicyApi->secret_policy_service_search_secret_policies: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_include_inactive** | **bool**| Whether or not to include inactive secret policies | [optional]
 **filter_secret_policy_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Results will contain this text in the policy name | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**IPagingOfSecretPolicyModel**](IPagingOfSecretPolicyModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Policies that matched |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_policy_service_update_secret_policy_v2**
> SecretPolicyDetailModelV2 secret_policy_service_update_secret_policy_v2(id)

Update a Secret Policy

Update a Secret Policy and return detail model

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_policy_api
from plugins.model.secret_policy_update_args_v2 import SecretPolicyUpdateArgsV2
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_policy_detail_model_v2 import SecretPolicyDetailModelV2
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
    api_instance = secret_policy_api.SecretPolicyApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    secret_policy_update_args_v2 = SecretPolicyUpdateArgsV2(
        data=SecretPolicyUpdateModelV2(
            active=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            general_items=SecretPolicyGeneralItemsUpdateModel(
                jumpbox_route_id=UpdateFieldValueOfSecretPolicyDataItemOfOptionalGuid(
                    dirty=True,
                    value=SecretPolicyDataItemOfOptionalGuid(
                        policy_apply_type=PolicyApplyType("{}"),
                        value=None,
                    ),
                ),
                site_id=UpdateFieldValueOfSecretPolicyDataItemOfOptionalInt32(
                    dirty=True,
                    value=SecretPolicyDataItemOfOptionalInt32(
                        policy_apply_type=PolicyApplyType("{}"),
                        value=None,
                    ),
                ),
            ),
            launcher_items=SecretPolicyLauncherItemsUpdateModel(
                launcher_settings=UpdateFieldValueOfSecretPolicyDataItemOfLauncherSettingsData(
                    dirty=True,
                    value=SecretPolicyDataItemOfLauncherSettingsData(
                        policy_apply_type=PolicyApplyType("{}"),
                        value=LauncherSettingsData(
                            allow_clipboard=True,
                            allow_drives=True,
                            allow_printers=True,
                            allow_smart_cards=True,
                            connect_to_console=True,
                            launcher_height=None,
                            launcher_width=None,
                            use_custom_launcher_resolution=True,
                        ),
                    ),
                ),
                web_launcher_requires_incognito_mode=UpdateFieldValueOfSecretPolicyDataItemOfOptionalBoolean(
                    dirty=True,
                    value=SecretPolicyDataItemOfOptionalBoolean(
                        policy_apply_type=PolicyApplyType("{}"),
                        value=True,
                    ),
                ),
            ),
            rpc_items=SecretPolicyRpcItemsUpdateModel(
                associated_secret_id1=UpdateFieldValueOfSecretPolicyDataItemOfOptionalInt32(
                    dirty=True,
                    value=SecretPolicyDataItemOfOptionalInt32(
                        policy_apply_type=PolicyApplyType("{}"),
                        value=None,
                    ),
                ),
                associated_secret_id2=UpdateFieldValueOfSecretPolicyDataItemOfOptionalInt32(
                    dirty=True,
                    value=SecretPolicyDataItemOfOptionalInt32(
                        policy_apply_type=PolicyApplyType("{}"),
                        value=None,
                    ),
                ),
                auto_change_on_expiration=UpdateFieldValueOfSecretPolicyDataItemOfOptionalBoolean(
                    dirty=True,
                    value=SecretPolicyDataItemOfOptionalBoolean(
                        policy_apply_type=PolicyApplyType("{}"),
                        value=True,
                    ),
                ),
                auto_change_schedule=UpdateFieldValueOfSecretPolicyDataItemOfAutoChangeScheduleDataModel(
                    dirty=True,
                    value=SecretPolicyDataItemOfAutoChangeScheduleDataModel(
                        policy_apply_type=PolicyApplyType("{}"),
                        value=AutoChangeScheduleDataModel(
                            change_only_when_expired=True,
                            change_type=None,
                            days=None,
                            friday=True,
                            monday=True,
                            monthly_day=None,
                            monthly_day_of_month=None,
                            monthly_day_order=None,
                            monthly_day_order_recurrence=None,
                            monthly_day_recurrence=None,
                            monthly_schedule_type=None,
                            saturday=True,
                            starting_on=None,
                            sunday=True,
                            thursday=True,
                            tuesday=True,
                            wednesday=True,
                            weeks=None,
                        ),
                    ),
                ),
                heart_beat_enabled=UpdateFieldValueOfSecretPolicyDataItemOfOptionalBoolean(
                    dirty=True,
                    value=SecretPolicyDataItemOfOptionalBoolean(
                        policy_apply_type=PolicyApplyType("{}"),
                        value=True,
                    ),
                ),
                password_type_web_script_id=UpdateFieldValueOfSecretPolicyDataItemOfOptionalInt32(
                    dirty=True,
                    value=SecretPolicyDataItemOfOptionalInt32(
                        policy_apply_type=PolicyApplyType("{}"),
                        value=None,
                    ),
                ),
                privileged_secret_id=UpdateFieldValueOfSecretPolicyDataItemOfOptionalInt32(
                    dirty=True,
                    value=SecretPolicyDataItemOfOptionalInt32(
                        policy_apply_type=PolicyApplyType("{}"),
                        value=None,
                    ),
                ),
            ),
            secret_policy_description=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            secret_policy_name=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            security_items=SecretPolicySecurityItemsUpdateModel(
                allow_owners_unrestricted_ssh_commands=UpdateFieldValueOfSecretPolicyDataItemOfOptionalBoolean(
                    dirty=True,
                    value=SecretPolicyDataItemOfOptionalBoolean(
                        policy_apply_type=PolicyApplyType("{}"),
                        value=True,
                    ),
                ),
                approval_groups=UpdateFieldValueOfSecretPolicyDataItemOfUserGroupMapDataModelArray(
                    dirty=True,
                    value=SecretPolicyDataItemOfUserGroupMapDataModelArray(
                        policy_apply_type=PolicyApplyType("{}"),
                        value=[
                            UserGroupMapDataModel(
                                group_id=None,
                                user_group_map_type=UserGroupMapType("{}"),
                            ),
                        ],
                    ),
                ),
                approval_workflow=UpdateFieldValueOfSecretPolicyDataItemOfOptionalInt32(
                    dirty=True,
                    value=SecretPolicyDataItemOfOptionalInt32(
                        policy_apply_type=PolicyApplyType("{}"),
                        value=None,
                    ),
                ),
                check_out_change_password=UpdateFieldValueOfSecretPolicyDataItemOfOptionalBoolean(
                    dirty=True,
                    value=SecretPolicyDataItemOfOptionalBoolean(
                        policy_apply_type=PolicyApplyType("{}"),
                        value=True,
                    ),
                ),
                check_out_enabled=UpdateFieldValueOfSecretPolicyDataItemOfOptionalBoolean(
                    dirty=True,
                    value=SecretPolicyDataItemOfOptionalBoolean(
                        policy_apply_type=PolicyApplyType("{}"),
                        value=True,
                    ),
                ),
                check_out_interval_minutes=UpdateFieldValueOfSecretPolicyDataItemOfOptionalInt32(
                    dirty=True,
                    value=SecretPolicyDataItemOfOptionalInt32(
                        policy_apply_type=PolicyApplyType("{}"),
                        value=None,
                    ),
                ),
                enable_ssh_command_restrictions=UpdateFieldValueOfSecretPolicyDataItemOfOptionalBoolean(
                    dirty=True,
                    value=SecretPolicyDataItemOfOptionalBoolean(
                        policy_apply_type=PolicyApplyType("{}"),
                        value=True,
                    ),
                ),
                event_pipeline_policy=UpdateFieldValueOfSecretPolicyDataItemOfOptionalInt32(
                    dirty=True,
                    value=SecretPolicyDataItemOfOptionalInt32(
                        policy_apply_type=PolicyApplyType("{}"),
                        value=None,
                    ),
                ),
                hide_launcher_password=UpdateFieldValueOfSecretPolicyDataItemOfOptionalBoolean(
                    dirty=True,
                    value=SecretPolicyDataItemOfOptionalBoolean(
                        policy_apply_type=PolicyApplyType("{}"),
                        value=True,
                    ),
                ),
                is_proxy_enabled=UpdateFieldValueOfSecretPolicyDataItemOfOptionalBoolean(
                    dirty=True,
                    value=SecretPolicyDataItemOfOptionalBoolean(
                        policy_apply_type=PolicyApplyType("{}"),
                        value=True,
                    ),
                ),
                is_session_recording_enabled=UpdateFieldValueOfSecretPolicyDataItemOfOptionalBoolean(
                    dirty=True,
                    value=SecretPolicyDataItemOfOptionalBoolean(
                        policy_apply_type=PolicyApplyType("{}"),
                        value=True,
                    ),
                ),
                require_approval_for_access=UpdateFieldValueOfSecretPolicyDataItemOfOptionalBoolean(
                    dirty=True,
                    value=SecretPolicyDataItemOfOptionalBoolean(
                        policy_apply_type=PolicyApplyType("{}"),
                        value=True,
                    ),
                ),
                require_approval_for_access_for_editors=UpdateFieldValueOfSecretPolicyDataItemOfOptionalBoolean(
                    dirty=True,
                    value=SecretPolicyDataItemOfOptionalBoolean(
                        policy_apply_type=PolicyApplyType("{}"),
                        value=True,
                    ),
                ),
                require_approval_for_access_for_owners_and_approvers=UpdateFieldValueOfSecretPolicyDataItemOfOptionalBoolean(
                    dirty=True,
                    value=SecretPolicyDataItemOfOptionalBoolean(
                        policy_apply_type=PolicyApplyType("{}"),
                        value=True,
                    ),
                ),
                require_view_comment=UpdateFieldValueOfSecretPolicyDataItemOfOptionalBoolean(
                    dirty=True,
                    value=SecretPolicyDataItemOfOptionalBoolean(
                        policy_apply_type=PolicyApplyType("{}"),
                        value=True,
                    ),
                ),
                run_launcher_using_ssh_key_secret_id=UpdateFieldValueOfSecretPolicyDataItemOfOptionalInt32(
                    dirty=True,
                    value=SecretPolicyDataItemOfOptionalInt32(
                        policy_apply_type=PolicyApplyType("{}"),
                        value=None,
                    ),
                ),
                ssh_command_blocklist_editors=UpdateFieldValueOfSecretPolicyDataItemOfOptionalGuid(
                    dirty=True,
                    value=SecretPolicyDataItemOfOptionalGuid(
                        policy_apply_type=PolicyApplyType("{}"),
                        value=None,
                    ),
                ),
                ssh_command_blocklist_owners=UpdateFieldValueOfSecretPolicyDataItemOfOptionalGuid(
                    dirty=True,
                    value=SecretPolicyDataItemOfOptionalGuid(
                        policy_apply_type=PolicyApplyType("{}"),
                        value=None,
                    ),
                ),
                ssh_command_blocklist_viewers=UpdateFieldValueOfSecretPolicyDataItemOfOptionalGuid(
                    dirty=True,
                    value=SecretPolicyDataItemOfOptionalGuid(
                        policy_apply_type=PolicyApplyType("{}"),
                        value=None,
                    ),
                ),
                ssh_command_menu_groups=UpdateFieldValueOfSecretPolicyDataItemOfSshCommandMenuGroupModelArray(
                    dirty=True,
                    value=SecretPolicyDataItemOfSshCommandMenuGroupModelArray(
                        policy_apply_type=PolicyApplyType("{}"),
                        value=[
                            SshCommandMenuGroupModel(
                                group_id=None,
                                ssh_command_menu_id=None,
                            ),
                        ],
                    ),
                ),
                ssh_command_restriction_type=UpdateFieldValueOfSecretPolicyDataItemOfOptionalCommandRestrictionType(
                    dirty=True,
                    value=SecretPolicyDataItemOfOptionalCommandRestrictionType(
                        policy_apply_type=PolicyApplyType("{}"),
                        value=None,
                    ),
                ),
            ),
        ),
    ) # SecretPolicyUpdateArgsV2 | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a Secret Policy
        api_response = api_instance.secret_policy_service_update_secret_policy_v2(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretPolicyApi->secret_policy_service_update_secret_policy_v2: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Secret Policy
        api_response = api_instance.secret_policy_service_update_secret_policy_v2(id, secret_policy_update_args_v2=secret_policy_update_args_v2)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretPolicyApi->secret_policy_service_update_secret_policy_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **secret_policy_update_args_v2** | [**SecretPolicyUpdateArgsV2**](SecretPolicyUpdateArgsV2.md)| args | [optional]

### Return type

[**SecretPolicyDetailModelV2**](SecretPolicyDetailModelV2.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Policy that was updated |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

