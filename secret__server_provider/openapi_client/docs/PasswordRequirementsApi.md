# plugins.PasswordRequirementsApi

All URIs are relative to *https://integrations.secretservercloud.com//api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**password_requirements_service_create**](PasswordRequirementsApi.md#password_requirements_service_create) | **POST** /v1/password-requirements | Create Password Requirement
[**password_requirements_service_get**](PasswordRequirementsApi.md#password_requirements_service_get) | **GET** /v1/password-requirements/{id} | Get Password Requirement
[**password_requirements_service_patch**](PasswordRequirementsApi.md#password_requirements_service_patch) | **PATCH** /v1/password-requirements/{id} | PatchPasswordRequirement
[**password_requirements_service_search_password_requirements**](PasswordRequirementsApi.md#password_requirements_service_search_password_requirements) | **GET** /v1/password-requirements | Search Password Requirements
[**password_requirements_service_update_rules**](PasswordRequirementsApi.md#password_requirements_service_update_rules) | **PUT** /v1/password-requirements/{id}/rules | Update Password Requirement Rules


# **password_requirements_service_create**
> PasswordRequirementModel password_requirements_service_create()

Create Password Requirement

Create Password Requirement

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import password_requirements_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.password_requirement_create_args import PasswordRequirementCreateArgs
from plugins.model.password_requirement_model import PasswordRequirementModel
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
    api_instance = password_requirements_api.PasswordRequirementsApi(api_client)
    password_requirement_create_args = PasswordRequirementCreateArgs(
        data=PasswordRequirementCreateModel(
            allowed_character_set_id=None,
            allow_minimum_character_sets=True,
            description=None,
            is_default=True,
            max_password_length=None,
            minimum_required_character_sets=None,
            min_password_length=None,
            name=None,
            password_requirement_rules=[
                PasswordRequirementRuleCreateModel(
                    character_set_id=None,
                    min_characters_required=None,
                    password_requirement_type=PasswordRequirementType("{}"),
                ),
            ],
            prevent_dictionary_words=True,
            prevent_sequential_pattern=True,
            prevent_spatial_pattern=True,
            prevent_username=True,
        ),
    ) # PasswordRequirementCreateArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Password Requirement
        api_response = api_instance.password_requirements_service_create(password_requirement_create_args=password_requirement_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling PasswordRequirementsApi->password_requirements_service_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_requirement_create_args** | [**PasswordRequirementCreateArgs**](PasswordRequirementCreateArgs.md)| args | [optional]

### Return type

[**PasswordRequirementModel**](PasswordRequirementModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Password requirement |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **password_requirements_service_get**
> PasswordRequirementModel password_requirements_service_get(id)

Get Password Requirement

Get password requirements

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import password_requirements_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.password_requirement_model import PasswordRequirementModel
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
    api_instance = password_requirements_api.PasswordRequirementsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id

    # example passing only required values which don't have defaults set
    try:
        # Get Password Requirement
        api_response = api_instance.password_requirements_service_get(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling PasswordRequirementsApi->password_requirements_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |

### Return type

[**PasswordRequirementModel**](PasswordRequirementModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Password requirement |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **password_requirements_service_patch**
> PasswordRequirementModel password_requirements_service_patch(id)

PatchPasswordRequirement

Patch Password Requirement

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import password_requirements_api
from plugins.model.password_requirement_patch_args import PasswordRequirementPatchArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.password_requirement_model import PasswordRequirementModel
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
    api_instance = password_requirements_api.PasswordRequirementsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    password_requirement_patch_args = PasswordRequirementPatchArgs(
        data=PasswordRequirementPatchModel(
            allowed_character_set=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            description=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            is_default=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            max_password_length=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            minimum_required_character_sets=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=None,
            ),
            min_password_length=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            name=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            password_dictionaries=UpdateFieldValueOfInt32Array(
                dirty=True,
                value=[
                    None,
                ],
            ),
            prevent_dictionary_words=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            prevent_sequential_pattern=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            prevent_spatial_pattern=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            prevent_username=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
        ),
    ) # PasswordRequirementPatchArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # PatchPasswordRequirement
        api_response = api_instance.password_requirements_service_patch(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling PasswordRequirementsApi->password_requirements_service_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # PatchPasswordRequirement
        api_response = api_instance.password_requirements_service_patch(id, password_requirement_patch_args=password_requirement_patch_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling PasswordRequirementsApi->password_requirements_service_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **password_requirement_patch_args** | [**PasswordRequirementPatchArgs**](PasswordRequirementPatchArgs.md)| args | [optional]

### Return type

[**PasswordRequirementModel**](PasswordRequirementModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Password requirement |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **password_requirements_service_search_password_requirements**
> PagingOfPasswordRequirementsSummary password_requirements_service_search_password_requirements()

Search Password Requirements

Search, filter, sort, and page password requirements

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import password_requirements_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_password_requirements_summary import PagingOfPasswordRequirementsSummary
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
    api_instance = password_requirements_api.PasswordRequirementsApi(api_client)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Password Requirements
        api_response = api_instance.password_requirements_service_search_password_requirements(skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling PasswordRequirementsApi->password_requirements_service_search_password_requirements: %s\n" % e)
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

[**PagingOfPasswordRequirementsSummary**](PagingOfPasswordRequirementsSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Password requirements collection |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **password_requirements_service_update_rules**
> PasswordRequirementModel password_requirements_service_update_rules(id)

Update Password Requirement Rules

Update Password Requirement Rules

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import password_requirements_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.password_requirement_model import PasswordRequirementModel
from plugins.model.password_requirement_rule_update_args import PasswordRequirementRuleUpdateArgs
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
    api_instance = password_requirements_api.PasswordRequirementsApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    password_requirement_rule_update_args = PasswordRequirementRuleUpdateArgs(
        data=[
            PasswordRequirementRuleUpdateModel(
                character_set_id=None,
                min_characters_required=None,
                password_requirement_rule_id=None,
                password_requirement_type=PasswordRequirementType("{}"),
            ),
        ],
    ) # PasswordRequirementRuleUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Password Requirement Rules
        api_response = api_instance.password_requirements_service_update_rules(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling PasswordRequirementsApi->password_requirements_service_update_rules: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Password Requirement Rules
        api_response = api_instance.password_requirements_service_update_rules(id, password_requirement_rule_update_args=password_requirement_rule_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling PasswordRequirementsApi->password_requirements_service_update_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **password_requirement_rule_update_args** | [**PasswordRequirementRuleUpdateArgs**](PasswordRequirementRuleUpdateArgs.md)| args | [optional]

### Return type

[**PasswordRequirementModel**](PasswordRequirementModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Password requirement |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

