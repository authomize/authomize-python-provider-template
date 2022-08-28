# plugins.SecretTemplatesApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**secret_templates_service_add_password_dictionary**](SecretTemplatesApi.md#secret_templates_service_add_password_dictionary) | **POST** /v1/secret-templates/password-requirements/password-dictionaries | Creates new password dictionary
[**secret_templates_service_copy**](SecretTemplatesApi.md#secret_templates_service_copy) | **POST** /v1/secret-templates/{id}/copy | Copy Secret Template
[**secret_templates_service_create_field**](SecretTemplatesApi.md#secret_templates_service_create_field) | **POST** /v1/secret-templates/{templateId} | Create Secret Template Field For Template
[**secret_templates_service_create_secret_template_extended_mapping**](SecretTemplatesApi.md#secret_templates_service_create_secret_template_extended_mapping) | **POST** /v1/secret-templates/{secretTemplateId}/extended-mappings/{extendedTypeId} | Create a Secret Template Extended Mapping
[**secret_templates_service_create_secret_template_launcher**](SecretTemplatesApi.md#secret_templates_service_create_secret_template_launcher) | **POST** /v1/secret-templates/{secretTemplateId}/launchers/{launcherTypeId} | Create a Secret Template Launcher
[**secret_templates_service_create_template**](SecretTemplatesApi.md#secret_templates_service_create_template) | **POST** /v1/secret-templates | Create Secret Template
[**secret_templates_service_create_template_field**](SecretTemplatesApi.md#secret_templates_service_create_template_field) | **POST** /v1/secret-templates/{secretTemplateId}/fields | Create Secret Template Field
[**secret_templates_service_delete_extended_mapping**](SecretTemplatesApi.md#secret_templates_service_delete_extended_mapping) | **DELETE** /v1/secret-templates/{secretTemplateId}/extended-mappings/{extendedTypeId} | Delete Extended Mapping
[**secret_templates_service_delete_password_dictionary**](SecretTemplatesApi.md#secret_templates_service_delete_password_dictionary) | **DELETE** /v1/secret-templates/password-requirements/password-dictionaries/{id} | Deletes a specific password dictionary by ID
[**secret_templates_service_delete_secret_template_launcher**](SecretTemplatesApi.md#secret_templates_service_delete_secret_template_launcher) | **DELETE** /v1/secret-templates/{secretTemplateId}/launchers/{launcherTypeId} | Delete Secret Template Launcher
[**secret_templates_service_disable_field**](SecretTemplatesApi.md#secret_templates_service_disable_field) | **DELETE** /v1/secret-templates/fields/{templateFieldId} | Disable a Secret Template Field For Template
[**secret_templates_service_export**](SecretTemplatesApi.md#secret_templates_service_export) | **GET** /v1/secret-templates/{id}/export | Export Secret Template
[**secret_templates_service_generate_password**](SecretTemplatesApi.md#secret_templates_service_generate_password) | **POST** /v1/secret-templates/generate-password/{secretfieldId} | Generate Password
[**secret_templates_service_get_password_dictionaries**](SecretTemplatesApi.md#secret_templates_service_get_password_dictionaries) | **GET** /v1/secret-templates/password-requirements/password-dictionaries | Get password dictionaries
[**secret_templates_service_get_password_dictionary**](SecretTemplatesApi.md#secret_templates_service_get_password_dictionary) | **GET** /v1/secret-templates/password-requirements/password-dictionaries/{id} | Gets password dictionary items by ID
[**secret_templates_service_get_secret_template_extended_mapping**](SecretTemplatesApi.md#secret_templates_service_get_secret_template_extended_mapping) | **GET** /v1/secret-templates/{secretTemplateId}/extended-mappings/{extendedTypeId} | Get a single Secret Template Extended Mappings
[**secret_templates_service_get_secret_template_launcher**](SecretTemplatesApi.md#secret_templates_service_get_secret_template_launcher) | **GET** /v1/secret-templates/{secretTemplateId}/launchers/{launcherTypeId} | Get a Secret Template Launcher
[**secret_templates_service_get_secret_template_password_type**](SecretTemplatesApi.md#secret_templates_service_get_secret_template_password_type) | **GET** /v1/secret-templates/{secretTemplateId}/password-type | Get Secret Template Password Changer
[**secret_templates_service_get_template_field**](SecretTemplatesApi.md#secret_templates_service_get_template_field) | **GET** /v1/secret-templates/fields/{secretFieldId} | Get Secret Template Field
[**secret_templates_service_get_templates**](SecretTemplatesApi.md#secret_templates_service_get_templates) | **GET** /v1/templates/{folderId?} | Get Secret Templates 
[**secret_templates_service_get_v2**](SecretTemplatesApi.md#secret_templates_service_get_v2) | **GET** /v2/secret-templates/{secretTemplateId} | Get Secret Template Details
[**secret_templates_service_import_secret_template**](SecretTemplatesApi.md#secret_templates_service_import_secret_template) | **POST** /v1/secret-templates/import | Import Secret Template
[**secret_templates_service_patch_secret_template_password_changer**](SecretTemplatesApi.md#secret_templates_service_patch_secret_template_password_changer) | **PATCH** /v1/secret-templates/{secretTemplateId}/password-type | Patch Secret Template password type
[**secret_templates_service_patch_template_field**](SecretTemplatesApi.md#secret_templates_service_patch_template_field) | **PATCH** /v1/secret-templates/fields/{secretTemplateFieldId} | Patch Secret Template Field
[**secret_templates_service_patch_template_v2**](SecretTemplatesApi.md#secret_templates_service_patch_template_v2) | **PATCH** /v2/secret-templates/{secretTemplateId} | Patch Secret Template V2
[**secret_templates_service_put**](SecretTemplatesApi.md#secret_templates_service_put) | **PUT** /v1/secret-templates/{templateId} | Update Secret Template Field
[**secret_templates_service_search**](SecretTemplatesApi.md#secret_templates_service_search) | **GET** /v1/secret-templates | Search Secret Templates
[**secret_templates_service_search_launcher_types**](SecretTemplatesApi.md#secret_templates_service_search_launcher_types) | **GET** /v1/secret-templates/launcher-types | Get Launcher Types
[**secret_templates_service_search_secret_template_extended_mappings**](SecretTemplatesApi.md#secret_templates_service_search_secret_template_extended_mappings) | **GET** /v1/secret-templates/extended-mappings | Get Secret Template Extended Mappings
[**secret_templates_service_search_secret_template_extended_types**](SecretTemplatesApi.md#secret_templates_service_search_secret_template_extended_types) | **GET** /v1/secret-templates/extended-types | Get Secret Template Extended Types
[**secret_templates_service_search_secret_template_launchers**](SecretTemplatesApi.md#secret_templates_service_search_secret_template_launchers) | **GET** /v1/secret-templates/launchers | Get Secret Template Launchers
[**secret_templates_service_search_template_fields**](SecretTemplatesApi.md#secret_templates_service_search_template_fields) | **GET** /v1/secret-templates/fields/search | Search Secret Template Fields
[**secret_templates_service_sort_template_fields**](SecretTemplatesApi.md#secret_templates_service_sort_template_fields) | **POST** /v1/secret-templates/{secretTemplateId}/fields/sort | Sort Secret Template Fields
[**secret_templates_service_stub_secret_template_extended_mapping**](SecretTemplatesApi.md#secret_templates_service_stub_secret_template_extended_mapping) | **GET** /v1/secret-templates/{secretTemplateId}/extended-mappings/{extendedTypeId}/stub | Stub a Secret Template Extended Mappings
[**secret_templates_service_stub_secret_template_launcher**](SecretTemplatesApi.md#secret_templates_service_stub_secret_template_launcher) | **GET** /v1/secret-templates/{secretTemplateId}/launchers/{launcherTypeId}/stub | Stub a Secret Template Launchers
[**secret_templates_service_stub_template_field**](SecretTemplatesApi.md#secret_templates_service_stub_template_field) | **GET** /v1/secret-templates/fields/stub | Stub Secret Template Field
[**secret_templates_service_update_password_dictionary**](SecretTemplatesApi.md#secret_templates_service_update_password_dictionary) | **PUT** /v1/secret-templates/password-requirements/password-dictionaries | Updates a new password dictionary
[**secret_templates_service_update_secret_template_extended_mapping**](SecretTemplatesApi.md#secret_templates_service_update_secret_template_extended_mapping) | **PATCH** /v1/secret-templates/{secretTemplateId}/extended-mappings/{extendedTypeId} | Update a Secret Template Extended Mapping
[**secret_templates_service_update_secret_template_launcher**](SecretTemplatesApi.md#secret_templates_service_update_secret_template_launcher) | **PATCH** /v1/secret-templates/{secretTemplateId}/launchers/{launcherTypeId} | Update a Secret Template Launcher
[**secret_templates_service_update_secret_template_password_type**](SecretTemplatesApi.md#secret_templates_service_update_secret_template_password_type) | **PUT** /v1/secret-templates/password-type/{templateId} | Update Secret Templates Password Type


# **secret_templates_service_add_password_dictionary**
> bool secret_templates_service_add_password_dictionary()

Creates new password dictionary

Add new password dictionary

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    dictionary_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Dictionary Name (optional)
    file =  # file | Uploaded file (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates new password dictionary
        api_response = api_instance.secret_templates_service_add_password_dictionary(dictionary_name=dictionary_name, file=file)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_add_password_dictionary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dictionary_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Dictionary Name | [optional]
 **file** | **file**| Uploaded file | [optional]

### Return type

**bool**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | True |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_copy**
> SecretTemplateDetailModel secret_templates_service_copy(id)

Copy Secret Template

Copy a single secret template by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.secret_template_detail_model import SecretTemplateDetailModel
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_template_copy_args import SecretTemplateCopyArgs
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret template ID
    secret_template_copy_args = SecretTemplateCopyArgs(
        data=SecretTemplateCopyModel(
            name=None,
        ),
    ) # SecretTemplateCopyArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Copy Secret Template
        api_response = api_instance.secret_templates_service_copy(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_copy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Copy Secret Template
        api_response = api_instance.secret_templates_service_copy(id, secret_template_copy_args=secret_template_copy_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_copy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret template ID |
 **secret_template_copy_args** | [**SecretTemplateCopyArgs**](SecretTemplateCopyArgs.md)| args | [optional]

### Return type

[**SecretTemplateDetailModel**](SecretTemplateDetailModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret template data |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_create_field**
> SecretTemplateField secret_templates_service_create_field(template_id)

Create Secret Template Field For Template

Create a new Secret Template Field For Template

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
from plugins.model.secret_template_field_create_args import SecretTemplateFieldCreateArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_template_field import SecretTemplateField
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    template_id = None # bool, date, datetime, dict, float, int, list, str, none_type | templateId
    secret_template_field_create_args = SecretTemplateFieldCreateArgs(
        description=None,
        display_name=None,
        editable_permission=None,
        edit_requires=EditRequiresOptions("{}"),
        field_slug_name=None,
        generate_password_character_set=None,
        generate_password_length=None,
        hide_on_view=True,
        history_length=None,
        is_expiration_field=True,
        is_file=True,
        is_indexable=True,
        is_notes=True,
        is_password=True,
        is_required=True,
        is_url=True,
        list_type=ListType("{}"),
        must_encrypt=True,
        name=None,
        password_requirement_id=None,
        password_type_field_id=None,
        sort_order=None,
    ) # SecretTemplateFieldCreateArgs | Secret Template Field creation options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Secret Template Field For Template
        api_response = api_instance.secret_templates_service_create_field(template_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_create_field: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Secret Template Field For Template
        api_response = api_instance.secret_templates_service_create_field(template_id, secret_template_field_create_args=secret_template_field_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_create_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| templateId |
 **secret_template_field_create_args** | [**SecretTemplateFieldCreateArgs**](SecretTemplateFieldCreateArgs.md)| Secret Template Field creation options | [optional]

### Return type

[**SecretTemplateField**](SecretTemplateField.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Template Field object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_create_secret_template_extended_mapping**
> SecretTemplateExtendedMappingModel secret_templates_service_create_secret_template_extended_mapping(extended_type_id, secret_template_id)

Create a Secret Template Extended Mapping

Create an extended mappings for a Secret Template

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.secret_template_extended_mapping_create_args import SecretTemplateExtendedMappingCreateArgs
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_template_extended_mapping_model import SecretTemplateExtendedMappingModel
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    extended_type_id = None # bool, date, datetime, dict, float, int, list, str, none_type | extendedTypeId
    secret_template_id = None # bool, date, datetime, dict, float, int, list, str, none_type | secretTemplateId
    secret_template_extended_mapping_create_args = SecretTemplateExtendedMappingCreateArgs(
        data=SecretTemplateExtendedMappingCreateModel(
            fields=[
                SecretTemplateExtendedMappingCreateFieldModel(
                    extended_field_id=None,
                    secret_field_id=None,
                ),
            ],
        ),
    ) # SecretTemplateExtendedMappingCreateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a Secret Template Extended Mapping
        api_response = api_instance.secret_templates_service_create_secret_template_extended_mapping(extended_type_id, secret_template_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_create_secret_template_extended_mapping: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a Secret Template Extended Mapping
        api_response = api_instance.secret_templates_service_create_secret_template_extended_mapping(extended_type_id, secret_template_id, secret_template_extended_mapping_create_args=secret_template_extended_mapping_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_create_secret_template_extended_mapping: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extended_type_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| extendedTypeId |
 **secret_template_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| secretTemplateId |
 **secret_template_extended_mapping_create_args** | [**SecretTemplateExtendedMappingCreateArgs**](SecretTemplateExtendedMappingCreateArgs.md)| args | [optional]

### Return type

[**SecretTemplateExtendedMappingModel**](SecretTemplateExtendedMappingModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created extended mappings |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_create_secret_template_launcher**
> SecretTemplateLauncherModel secret_templates_service_create_secret_template_launcher(launcher_type_id, secret_template_id)

Create a Secret Template Launcher

Create a Launcher for a Secret Template

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
from plugins.model.secret_template_launcher_model import SecretTemplateLauncherModel
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.secret_template_launcher_create_args import SecretTemplateLauncherCreateArgs
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    launcher_type_id = None # bool, date, datetime, dict, float, int, list, str, none_type | launcherTypeId
    secret_template_id = None # bool, date, datetime, dict, float, int, list, str, none_type | secretTemplateId
    secret_template_launcher_create_args = SecretTemplateLauncherCreateArgs(
        data=SecretTemplateLauncherCreateModel(
            fields=[
                SecretTemplateLauncherCreateFieldModel(
                    default_value=None,
                    launcher_type_field_id=None,
                    secret_field_id=None,
                ),
            ],
        ),
    ) # SecretTemplateLauncherCreateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a Secret Template Launcher
        api_response = api_instance.secret_templates_service_create_secret_template_launcher(launcher_type_id, secret_template_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_create_secret_template_launcher: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a Secret Template Launcher
        api_response = api_instance.secret_templates_service_create_secret_template_launcher(launcher_type_id, secret_template_id, secret_template_launcher_create_args=secret_template_launcher_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_create_secret_template_launcher: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **launcher_type_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| launcherTypeId |
 **secret_template_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| secretTemplateId |
 **secret_template_launcher_create_args** | [**SecretTemplateLauncherCreateArgs**](SecretTemplateLauncherCreateArgs.md)| args | [optional]

### Return type

[**SecretTemplateLauncherModel**](SecretTemplateLauncherModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Launchers |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_create_template**
> SecretTemplateModel secret_templates_service_create_template()

Create Secret Template

Create a new Secret Template

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.secret_template_create_args import SecretTemplateCreateArgs
from plugins.model.secret_template_model import SecretTemplateModel
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    secret_template_create_args = SecretTemplateCreateArgs(
        fields=[
            SecretTemplateFieldCreateArgs(
                description=None,
                display_name=None,
                editable_permission=None,
                edit_requires=EditRequiresOptions("{}"),
                field_slug_name=None,
                generate_password_character_set=None,
                generate_password_length=None,
                hide_on_view=True,
                history_length=None,
                is_expiration_field=True,
                is_file=True,
                is_indexable=True,
                is_notes=True,
                is_password=True,
                is_required=True,
                is_url=True,
                list_type=ListType("{}"),
                must_encrypt=True,
                name=None,
                password_requirement_id=None,
                password_type_field_id=None,
                sort_order=None,
            ),
        ],
        name=None,
    ) # SecretTemplateCreateArgs | Secret Template creation options (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Secret Template
        api_response = api_instance.secret_templates_service_create_template(secret_template_create_args=secret_template_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_create_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_template_create_args** | [**SecretTemplateCreateArgs**](SecretTemplateCreateArgs.md)| Secret Template creation options | [optional]

### Return type

[**SecretTemplateModel**](SecretTemplateModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Template object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_create_template_field**
> SecretTemplateFieldModel secret_templates_service_create_template_field(secret_template_id)

Create Secret Template Field

Create a secret template field

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
from plugins.model.secret_template_field_model import SecretTemplateFieldModel
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_field_create_args import SecretFieldCreateArgs
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    secret_template_id = None # bool, date, datetime, dict, float, int, list, str, none_type | secretTemplateId
    secret_field_create_args = SecretFieldCreateArgs(
        data=SecretTemplateFieldCreateModel(
            data_type=FieldDataType("{}"),
            description=None,
            field_slug_name=None,
            name=None,
        ),
    ) # SecretFieldCreateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Secret Template Field
        api_response = api_instance.secret_templates_service_create_template_field(secret_template_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_create_template_field: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Secret Template Field
        api_response = api_instance.secret_templates_service_create_template_field(secret_template_id, secret_field_create_args=secret_field_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_create_template_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_template_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| secretTemplateId |
 **secret_field_create_args** | [**SecretFieldCreateArgs**](SecretFieldCreateArgs.md)| args | [optional]

### Return type

[**SecretTemplateFieldModel**](SecretTemplateFieldModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Template Field |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_delete_extended_mapping**
> SecretTemplateExtendedMappingDeleteResponseModel secret_templates_service_delete_extended_mapping(extended_type_id, secret_template_id)

Delete Extended Mapping

Delete an extended mapping

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.secret_template_extended_mapping_delete_response_model import SecretTemplateExtendedMappingDeleteResponseModel
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    extended_type_id = None # bool, date, datetime, dict, float, int, list, str, none_type | extendedTypeId
    secret_template_id = None # bool, date, datetime, dict, float, int, list, str, none_type | secretTemplateId

    # example passing only required values which don't have defaults set
    try:
        # Delete Extended Mapping
        api_response = api_instance.secret_templates_service_delete_extended_mapping(extended_type_id, secret_template_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_delete_extended_mapping: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extended_type_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| extendedTypeId |
 **secret_template_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| secretTemplateId |

### Return type

[**SecretTemplateExtendedMappingDeleteResponseModel**](SecretTemplateExtendedMappingDeleteResponseModel.md)

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

# **secret_templates_service_delete_password_dictionary**
> bool secret_templates_service_delete_password_dictionary(id)

Deletes a specific password dictionary by ID

Deletes a specific custom password dictionary with the contents.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id

    # example passing only required values which don't have defaults set
    try:
        # Deletes a specific password dictionary by ID
        api_response = api_instance.secret_templates_service_delete_password_dictionary(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_delete_password_dictionary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |

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
**200** | true |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_delete_secret_template_launcher**
> SecretTemplateLauncherDeleteResultModel secret_templates_service_delete_secret_template_launcher(launcher_type_id, secret_template_id)

Delete Secret Template Launcher

Delete or remove the mapping of a specific launcher type from a specific Secret template

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_template_launcher_delete_result_model import SecretTemplateLauncherDeleteResultModel
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    launcher_type_id = None # bool, date, datetime, dict, float, int, list, str, none_type | launcherTypeId
    secret_template_id = None # bool, date, datetime, dict, float, int, list, str, none_type | secretTemplateId

    # example passing only required values which don't have defaults set
    try:
        # Delete Secret Template Launcher
        api_response = api_instance.secret_templates_service_delete_secret_template_launcher(launcher_type_id, secret_template_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_delete_secret_template_launcher: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **launcher_type_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| launcherTypeId |
 **secret_template_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| secretTemplateId |

### Return type

[**SecretTemplateLauncherDeleteResultModel**](SecretTemplateLauncherDeleteResultModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete success |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_disable_field**
> SecretTemplateField secret_templates_service_disable_field(template_field_id)

Disable a Secret Template Field For Template

Disable a Secret Template Field For Template

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_template_field import SecretTemplateField
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    template_field_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret Template Field to disable

    # example passing only required values which don't have defaults set
    try:
        # Disable a Secret Template Field For Template
        api_response = api_instance.secret_templates_service_disable_field(template_field_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_disable_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_field_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret Template Field to disable |

### Return type

[**SecretTemplateField**](SecretTemplateField.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Template Field object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_export**
> SecretTemplateExportModel secret_templates_service_export(id)

Export Secret Template

Export a single secret template by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
from plugins.model.secret_template_export_model import SecretTemplateExportModel
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret template ID

    # example passing only required values which don't have defaults set
    try:
        # Export Secret Template
        api_response = api_instance.secret_templates_service_export(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_export: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret template ID |

### Return type

[**SecretTemplateExportModel**](SecretTemplateExportModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret template export data |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_generate_password**
> bool, date, datetime, dict, float, int, list, str, none_type secret_templates_service_generate_password(secretfield_id)

Generate Password

Generates a new password matching the Secret Field requirements

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    secretfield_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret field Id

    # example passing only required values which don't have defaults set
    try:
        # Generate Password
        api_response = api_instance.secret_templates_service_generate_password(secretfield_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_generate_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secretfield_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret field Id |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Generate Password result |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_get_password_dictionaries**
> [PasswordDictionaryModel] secret_templates_service_get_password_dictionaries()

Get password dictionaries

Returns the list of custom password dictionaries.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
from plugins.model.password_dictionary_model import PasswordDictionaryModel
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get password dictionaries
        api_response = api_instance.secret_templates_service_get_password_dictionaries()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_get_password_dictionaries: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[PasswordDictionaryModel]**](PasswordDictionaryModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of password dictionary ID and names. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_get_password_dictionary**
> secret_templates_service_get_password_dictionary(id)

Gets password dictionary items by ID

Returns a file containing the items of a specific custom password dictionary.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id

    # example passing only required values which don't have defaults set
    try:
        # Gets password dictionary items by ID
        api_instance.secret_templates_service_get_password_dictionary(id)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_get_password_dictionary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |

### Return type

void (empty response body)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Unknown or empty response |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_get_secret_template_extended_mapping**
> SecretTemplateExtendedMappingModel secret_templates_service_get_secret_template_extended_mapping(extended_type_id, secret_template_id)

Get a single Secret Template Extended Mappings

Get an extended mapping for a Secret Template

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_template_extended_mapping_model import SecretTemplateExtendedMappingModel
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    extended_type_id = None # bool, date, datetime, dict, float, int, list, str, none_type | extendedTypeId
    secret_template_id = None # bool, date, datetime, dict, float, int, list, str, none_type | secretTemplateId

    # example passing only required values which don't have defaults set
    try:
        # Get a single Secret Template Extended Mappings
        api_response = api_instance.secret_templates_service_get_secret_template_extended_mapping(extended_type_id, secret_template_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_get_secret_template_extended_mapping: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extended_type_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| extendedTypeId |
 **secret_template_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| secretTemplateId |

### Return type

[**SecretTemplateExtendedMappingModel**](SecretTemplateExtendedMappingModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Extended Mapping Detail |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_get_secret_template_launcher**
> SecretTemplateLauncherModel secret_templates_service_get_secret_template_launcher(launcher_type_id, secret_template_id)

Get a Secret Template Launcher

Get launcher detail for a Secret Template

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
from plugins.model.secret_template_launcher_model import SecretTemplateLauncherModel
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    launcher_type_id = None # bool, date, datetime, dict, float, int, list, str, none_type | launcherTypeId
    secret_template_id = None # bool, date, datetime, dict, float, int, list, str, none_type | secretTemplateId

    # example passing only required values which don't have defaults set
    try:
        # Get a Secret Template Launcher
        api_response = api_instance.secret_templates_service_get_secret_template_launcher(launcher_type_id, secret_template_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_get_secret_template_launcher: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **launcher_type_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| launcherTypeId |
 **secret_template_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| secretTemplateId |

### Return type

[**SecretTemplateLauncherModel**](SecretTemplateLauncherModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Launcher Detail |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_get_secret_template_password_type**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} secret_templates_service_get_secret_template_password_type(secret_template_id)

Get Secret Template Password Changer

Get the password changer for a secret template if defined

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    secret_template_id = None # bool, date, datetime, dict, float, int, list, str, none_type | secretTemplateId

    # example passing only required values which don't have defaults set
    try:
        # Get Secret Template Password Changer
        api_response = api_instance.secret_templates_service_get_secret_template_password_type(secret_template_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_get_secret_template_password_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_template_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| secretTemplateId |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Template Password Changer |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_get_template_field**
> SecretTemplateFieldModel secret_templates_service_get_template_field(secret_field_id)

Get Secret Template Field

Retrieve a secret template field

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
from plugins.model.secret_template_field_model import SecretTemplateFieldModel
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    secret_field_id = None # bool, date, datetime, dict, float, int, list, str, none_type | secretFieldId

    # example passing only required values which don't have defaults set
    try:
        # Get Secret Template Field
        api_response = api_instance.secret_templates_service_get_template_field(secret_field_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_get_template_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_field_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| secretFieldId |

### Return type

[**SecretTemplateFieldModel**](SecretTemplateFieldModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Template Field |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_get_templates**
> TemplateViewModel secret_templates_service_get_templates()

Get Secret Templates 

Get Secret Templates with optional folderId

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.template_view_model import TemplateViewModel
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    folder_id = None # bool, date, datetime, dict, float, int, list, str, none_type | folderId (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Secret Templates 
        api_response = api_instance.secret_templates_service_get_templates(folder_id=folder_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_get_templates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| folderId | [optional]

### Return type

[**TemplateViewModel**](TemplateViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Templates |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_get_v2**
> SecretTemplateDetailModel secret_templates_service_get_v2(secret_template_id)

Get Secret Template Details

Get a single secret template details by Id

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.secret_template_detail_model import SecretTemplateDetailModel
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    secret_template_id = None # bool, date, datetime, dict, float, int, list, str, none_type | secretTemplateId

    # example passing only required values which don't have defaults set
    try:
        # Get Secret Template Details
        api_response = api_instance.secret_templates_service_get_v2(secret_template_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_get_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_template_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| secretTemplateId |

### Return type

[**SecretTemplateDetailModel**](SecretTemplateDetailModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Template Details |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_import_secret_template**
> SecretTemplateModel secret_templates_service_import_secret_template()

Import Secret Template

Imports a secret template from xml

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.secret_template_model import SecretTemplateModel
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_template_import_args import SecretTemplateImportArgs
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    secret_template_import_args = SecretTemplateImportArgs(
        data=SecretTemplateImportModel(
            template_xml=None,
        ),
    ) # SecretTemplateImportArgs | args (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Import Secret Template
        api_response = api_instance.secret_templates_service_import_secret_template(secret_template_import_args=secret_template_import_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_import_secret_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_template_import_args** | [**SecretTemplateImportArgs**](SecretTemplateImportArgs.md)| args | [optional]

### Return type

[**SecretTemplateModel**](SecretTemplateModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The imported template |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_patch_secret_template_password_changer**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} secret_templates_service_patch_secret_template_password_changer(secret_template_id)

Patch Secret Template password type

Create or assign password type settings on a secret template

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_template_password_type_patch_args import SecretTemplatePasswordTypePatchArgs
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    secret_template_id = None # bool, date, datetime, dict, float, int, list, str, none_type | secretTemplateId
    secret_template_password_type_patch_args = SecretTemplatePasswordTypePatchArgs(
        data=SecretTemplatePasswordTypePatchModel(
            default_privileged_secret_id=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=None,
            ),
            enable_heartbeat=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            enable_rpc=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            fields=UpdateFieldValueOfSecretTemplatePasswordTypeFieldMappingUpdateModelArray(
                dirty=True,
                value=[
                    SecretTemplatePasswordTypeFieldMappingUpdateModel(
                        password_type_field_id=None,
                        secret_field_id=None,
                    ),
                ],
            ),
            heartbeat_interval_days=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            heartbeat_interval_hours=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            heartbeat_interval_minutes=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            password_type_id=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=None,
            ),
            rpc_interval_days=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            rpc_interval_hours=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            rpc_interval_minutes=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            rpc_max_attempts=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=None,
            ),
        ),
    ) # SecretTemplatePasswordTypePatchArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Patch Secret Template password type
        api_response = api_instance.secret_templates_service_patch_secret_template_password_changer(secret_template_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_patch_secret_template_password_changer: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Patch Secret Template password type
        api_response = api_instance.secret_templates_service_patch_secret_template_password_changer(secret_template_id, secret_template_password_type_patch_args=secret_template_password_type_patch_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_patch_secret_template_password_changer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_template_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| secretTemplateId |
 **secret_template_password_type_patch_args** | [**SecretTemplatePasswordTypePatchArgs**](SecretTemplatePasswordTypePatchArgs.md)| args | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated secret template password type |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_patch_template_field**
> SecretTemplateFieldModel secret_templates_service_patch_template_field(secret_template_field_id)

Patch Secret Template Field

Patch a secret template field

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
from plugins.model.secret_template_field_model import SecretTemplateFieldModel
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_field_patch_args import SecretFieldPatchArgs
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    secret_template_field_id = None # bool, date, datetime, dict, float, int, list, str, none_type | secretTemplateFieldId
    secret_field_patch_args = SecretFieldPatchArgs(
        data=SecretTemplateFieldPatchModel(
            active=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            data_type=UpdateFieldValueOfFieldDataType(
                dirty=True,
                value=FieldDataType("{}"),
            ),
            description=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            dropdown_options_to_add=UpdateFieldValueOfStringArray(
                dirty=True,
                value=[
                    None,
                ],
            ),
            dropdown_options_to_remove=UpdateFieldValueOfSecretTemplateFieldOptionRemoveModelArray(
                dirty=True,
                value=[
                    SecretTemplateFieldOptionRemoveModel(
                        id=None,
                        value=None,
                    ),
                ],
            ),
            dropdown_options_to_update=UpdateFieldValueOfSecretTemplateFieldOptionUpdateModelArray(
                dirty=True,
                value=[
                    SecretTemplateFieldOptionUpdateModel(
                        id=None,
                        value=None,
                    ),
                ],
            ),
            edit_requires_permission=UpdateFieldValueOfFieldPermissionType(
                dirty=True,
                value=FieldPermissionType("{}"),
            ),
            expose_for_display=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            history_length=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            name=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            password_requirement=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=None,
            ),
            required=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            save_all_history=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            searchable=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            slug_name=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            sort_order=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            viewing_requires_edit=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
        ),
    ) # SecretFieldPatchArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Patch Secret Template Field
        api_response = api_instance.secret_templates_service_patch_template_field(secret_template_field_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_patch_template_field: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Patch Secret Template Field
        api_response = api_instance.secret_templates_service_patch_template_field(secret_template_field_id, secret_field_patch_args=secret_field_patch_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_patch_template_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_template_field_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| secretTemplateFieldId |
 **secret_field_patch_args** | [**SecretFieldPatchArgs**](SecretFieldPatchArgs.md)| args | [optional]

### Return type

[**SecretTemplateFieldModel**](SecretTemplateFieldModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Template Field |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_patch_template_v2**
> SecretTemplateDetailModel secret_templates_service_patch_template_v2(secret_template_id)

Patch Secret Template V2

Patch secret template details

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.secret_template_detail_model import SecretTemplateDetailModel
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_template_detail_patch_args import SecretTemplateDetailPatchArgs
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    secret_template_id = None # bool, date, datetime, dict, float, int, list, str, none_type | secretTemplateId
    secret_template_detail_patch_args = SecretTemplateDetailPatchArgs(
        data=SecretTemplateDetailPatchModel(
            active=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            description=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            expiration_change_required_on_field_id=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            expiration_days=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            expiration_enabled=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            name=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            name_pattern=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            name_pattern_error_message=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            one_time_password_duration=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            one_time_password_enabled=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            one_time_password_hash=UpdateFieldValueOfPasswordHashType(
                dirty=True,
                value=PasswordHashType("SHA1"),
            ),
            one_time_password_length=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            save_all_name_history=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            secret_name_history_length=UpdateFieldValueOfInt32(
                dirty=True,
                value=None,
            ),
            ssh_key_format=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            ssh_key_size=UpdateFieldValueOfSshKeySizeType(
                dirty=True,
                value=SshKeySizeType("Key1024"),
            ),
            validate_password_requirements_on_create=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            validate_password_requirements_on_edit=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
        ),
    ) # SecretTemplateDetailPatchArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Patch Secret Template V2
        api_response = api_instance.secret_templates_service_patch_template_v2(secret_template_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_patch_template_v2: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Patch Secret Template V2
        api_response = api_instance.secret_templates_service_patch_template_v2(secret_template_id, secret_template_detail_patch_args=secret_template_detail_patch_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_patch_template_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_template_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| secretTemplateId |
 **secret_template_detail_patch_args** | [**SecretTemplateDetailPatchArgs**](SecretTemplateDetailPatchArgs.md)| args | [optional]

### Return type

[**SecretTemplateDetailModel**](SecretTemplateDetailModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Template Details |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_put**
> SecretTemplateField secret_templates_service_put(template_id)

Update Secret Template Field

Update a Secret Template Field

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_template_field_update_args import SecretTemplateFieldUpdateArgs
from plugins.model.secret_template_field import SecretTemplateField
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    template_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret Template ID
    secret_template_field_update_args = SecretTemplateFieldUpdateArgs(
        description=None,
        display_name=None,
        editable_permission=None,
        edit_requires=EditRequiresOptions("{}"),
        field_slug_name=None,
        generate_password_character_set=None,
        generate_password_length=None,
        hide_on_view=True,
        history_length=None,
        is_expiration_field=True,
        is_file=True,
        is_indexable=True,
        is_notes=True,
        is_password=True,
        is_required=True,
        is_url=True,
        list_type=ListType("{}"),
        must_encrypt=True,
        name=None,
        password_requirement_id=None,
        password_type_field_id=None,
        secret_template_field_id=None,
        sort_order=None,
    ) # SecretTemplateFieldUpdateArgs | Secret Template Options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Secret Template Field
        api_response = api_instance.secret_templates_service_put(template_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Secret Template Field
        api_response = api_instance.secret_templates_service_put(template_id, secret_template_field_update_args=secret_template_field_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret Template ID |
 **secret_template_field_update_args** | [**SecretTemplateFieldUpdateArgs**](SecretTemplateFieldUpdateArgs.md)| Secret Template Options | [optional]

### Return type

[**SecretTemplateField**](SecretTemplateField.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Template Field |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_search**
> PagingOfSecretTemplateSummary secret_templates_service_search()

Search Secret Templates

Search, filter, sort, and page secret templates

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_secret_template_summary import PagingOfSecretTemplateSummary
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    filter_include_inactive = True # bool | Whether to include inactive secret templates in the results (optional)
    filter_include_secret_count = True # bool | Whether to populate Secret count in the results (optional)
    filter_password_type_ids = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | List of Password Type Ids (optional)
    filter_search_text = None # bool, date, datetime, dict, float, int, list, str, none_type | Search text (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Secret Templates
        api_response = api_instance.secret_templates_service_search(filter_include_inactive=filter_include_inactive, filter_include_secret_count=filter_include_secret_count, filter_password_type_ids=filter_password_type_ids, filter_search_text=filter_search_text, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_include_inactive** | **bool**| Whether to include inactive secret templates in the results | [optional]
 **filter_include_secret_count** | **bool**| Whether to populate Secret count in the results | [optional]
 **filter_password_type_ids** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| List of Password Type Ids | [optional]
 **filter_search_text** | **bool, date, datetime, dict, float, int, list, str, none_type**| Search text | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfSecretTemplateSummary**](PagingOfSecretTemplateSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret template search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_search_launcher_types**
> PagingOfLauncherTypeSummary secret_templates_service_search_launcher_types()

Get Launcher Types

Get a paged list of all of the Launcher Types that exist

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_launcher_type_summary import PagingOfLauncherTypeSummary
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    filter_application_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Application name (optional)
    filter_include_inactive = True # bool | Include inactive launcher types (optional)
    filter_include_system_launchers = True # bool | Include system launcher types (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Launcher Types
        api_response = api_instance.secret_templates_service_search_launcher_types(filter_application_name=filter_application_name, filter_include_inactive=filter_include_inactive, filter_include_system_launchers=filter_include_system_launchers, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_search_launcher_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_application_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Application name | [optional]
 **filter_include_inactive** | **bool**| Include inactive launcher types | [optional]
 **filter_include_system_launchers** | **bool**| Include system launcher types | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfLauncherTypeSummary**](PagingOfLauncherTypeSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of launcher types |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_search_secret_template_extended_mappings**
> PagingOfSecretTemplateExtendedMappingSummary secret_templates_service_search_secret_template_extended_mappings()

Get Secret Template Extended Mappings

Get all of the extended mappings for a Secret Template

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.paging_of_secret_template_extended_mapping_summary import PagingOfSecretTemplateExtendedMappingSummary
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    filter_secret_template_id = None # bool, date, datetime, dict, float, int, list, str, none_type | SecretTemplateId (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Secret Template Extended Mappings
        api_response = api_instance.secret_templates_service_search_secret_template_extended_mappings(filter_secret_template_id=filter_secret_template_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_search_secret_template_extended_mappings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_secret_template_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| SecretTemplateId | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfSecretTemplateExtendedMappingSummary**](PagingOfSecretTemplateExtendedMappingSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of extended mappings |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_search_secret_template_extended_types**
> PagingOfSecretTemplateExtendedTypeSummary secret_templates_service_search_secret_template_extended_types()

Get Secret Template Extended Types

Get all of the extended types

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_secret_template_extended_type_summary import PagingOfSecretTemplateExtendedTypeSummary
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Secret Template Extended Types
        api_response = api_instance.secret_templates_service_search_secret_template_extended_types(skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_search_secret_template_extended_types: %s\n" % e)
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

[**PagingOfSecretTemplateExtendedTypeSummary**](PagingOfSecretTemplateExtendedTypeSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of extended types |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_search_secret_template_launchers**
> PagingOfSecretTemplateLauncherSummary secret_templates_service_search_secret_template_launchers()

Get Secret Template Launchers

Get all of the Launchers for a Secret Template

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.paging_of_secret_template_launcher_summary import PagingOfSecretTemplateLauncherSummary
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    filter_secret_template_id = None # bool, date, datetime, dict, float, int, list, str, none_type | SecretTemplateId (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Secret Template Launchers
        api_response = api_instance.secret_templates_service_search_secret_template_launchers(filter_secret_template_id=filter_secret_template_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_search_secret_template_launchers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_secret_template_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| SecretTemplateId | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfSecretTemplateLauncherSummary**](PagingOfSecretTemplateLauncherSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Launchers |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_search_template_fields**
> PagingOfSecretTemplateFieldSummaryModel secret_templates_service_search_template_fields()

Search Secret Template Fields

Search, filter, sort, and page secret template fields

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_secret_template_field_summary_model import PagingOfSecretTemplateFieldSummaryModel
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    filter_include_inactive = True # bool | Whether to include inactive secret template fields in the results (optional)
    filter_secret_template_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret Template Id to filter by (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Secret Template Fields
        api_response = api_instance.secret_templates_service_search_template_fields(filter_include_inactive=filter_include_inactive, filter_secret_template_id=filter_secret_template_id, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_search_template_fields: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_include_inactive** | **bool**| Whether to include inactive secret template fields in the results | [optional]
 **filter_secret_template_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret Template Id to filter by | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfSecretTemplateFieldSummaryModel**](PagingOfSecretTemplateFieldSummaryModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret template field summary result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_sort_template_fields**
> SecretTemplateFieldSortResultModel secret_templates_service_sort_template_fields(secret_template_id)

Sort Secret Template Fields

Sort secret template fields for a secret template

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.secret_template_field_sort_args import SecretTemplateFieldSortArgs
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_template_field_sort_result_model import SecretTemplateFieldSortResultModel
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    secret_template_id = None # bool, date, datetime, dict, float, int, list, str, none_type | secretTemplateId
    secret_template_field_sort_args = SecretTemplateFieldSortArgs(
        data=SecretTemplateFieldSortModel(
            field_ids=[
                None,
            ],
        ),
    ) # SecretTemplateFieldSortArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Sort Secret Template Fields
        api_response = api_instance.secret_templates_service_sort_template_fields(secret_template_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_sort_template_fields: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Sort Secret Template Fields
        api_response = api_instance.secret_templates_service_sort_template_fields(secret_template_id, secret_template_field_sort_args=secret_template_field_sort_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_sort_template_fields: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_template_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| secretTemplateId |
 **secret_template_field_sort_args** | [**SecretTemplateFieldSortArgs**](SecretTemplateFieldSortArgs.md)| args | [optional]

### Return type

[**SecretTemplateFieldSortResultModel**](SecretTemplateFieldSortResultModel.md)

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

# **secret_templates_service_stub_secret_template_extended_mapping**
> SecretTemplateExtendedMappingModel secret_templates_service_stub_secret_template_extended_mapping(extended_type_id, secret_template_id)

Stub a Secret Template Extended Mappings

Gets a stub that can be used to create an extended mapping

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_template_extended_mapping_model import SecretTemplateExtendedMappingModel
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    extended_type_id = None # bool, date, datetime, dict, float, int, list, str, none_type | extendedTypeId
    secret_template_id = None # bool, date, datetime, dict, float, int, list, str, none_type | secretTemplateId

    # example passing only required values which don't have defaults set
    try:
        # Stub a Secret Template Extended Mappings
        api_response = api_instance.secret_templates_service_stub_secret_template_extended_mapping(extended_type_id, secret_template_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_stub_secret_template_extended_mapping: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extended_type_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| extendedTypeId |
 **secret_template_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| secretTemplateId |

### Return type

[**SecretTemplateExtendedMappingModel**](SecretTemplateExtendedMappingModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stub of extended mapping |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_stub_secret_template_launcher**
> SecretTemplateLauncherModel secret_templates_service_stub_secret_template_launcher(launcher_type_id, secret_template_id)

Stub a Secret Template Launchers

Gets a stub that can be used to create an launcher

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
from plugins.model.secret_template_launcher_model import SecretTemplateLauncherModel
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    launcher_type_id = None # bool, date, datetime, dict, float, int, list, str, none_type | launcherTypeId
    secret_template_id = None # bool, date, datetime, dict, float, int, list, str, none_type | secretTemplateId

    # example passing only required values which don't have defaults set
    try:
        # Stub a Secret Template Launchers
        api_response = api_instance.secret_templates_service_stub_secret_template_launcher(launcher_type_id, secret_template_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_stub_secret_template_launcher: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **launcher_type_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| launcherTypeId |
 **secret_template_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| secretTemplateId |

### Return type

[**SecretTemplateLauncherModel**](SecretTemplateLauncherModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stub of template launcher |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_stub_template_field**
> SecretTemplateFieldModel secret_templates_service_stub_template_field()

Stub Secret Template Field

Retrieve an empty secret template field

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
from plugins.model.secret_template_field_model import SecretTemplateFieldModel
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Stub Secret Template Field
        api_response = api_instance.secret_templates_service_stub_template_field()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_stub_template_field: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SecretTemplateFieldModel**](SecretTemplateFieldModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret Template Field |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_update_password_dictionary**
> bool secret_templates_service_update_password_dictionary()

Updates a new password dictionary

Updates password dictionary

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    dictionary_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Dictionary ID to Update (optional)
    dictionary_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Dictionary Name (optional)
    file =  # file | Uploaded file (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates a new password dictionary
        api_response = api_instance.secret_templates_service_update_password_dictionary(dictionary_id=dictionary_id, dictionary_name=dictionary_name, file=file)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_update_password_dictionary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dictionary_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Dictionary ID to Update | [optional]
 **dictionary_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Dictionary Name | [optional]
 **file** | **file**| Uploaded file | [optional]

### Return type

**bool**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | True |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_update_secret_template_extended_mapping**
> SecretTemplateExtendedMappingModel secret_templates_service_update_secret_template_extended_mapping(extended_type_id, secret_template_id)

Update a Secret Template Extended Mapping

Update extended mappings for a Secret Template

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.secret_template_extended_mapping_update_args import SecretTemplateExtendedMappingUpdateArgs
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_template_extended_mapping_model import SecretTemplateExtendedMappingModel
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    extended_type_id = None # bool, date, datetime, dict, float, int, list, str, none_type | extendedTypeId
    secret_template_id = None # bool, date, datetime, dict, float, int, list, str, none_type | secretTemplateId
    secret_template_extended_mapping_update_args = SecretTemplateExtendedMappingUpdateArgs(
        data=SecretTemplateExtendedMappingUpdateModel(
            fields=UpdateFieldValueOfSecretTemplateExtendedMappingUpdateFieldModelArray(
                dirty=True,
                value=[
                    SecretTemplateExtendedMappingUpdateFieldModel(
                        extended_field_id=None,
                        secret_field_id=None,
                    ),
                ],
            ),
        ),
    ) # SecretTemplateExtendedMappingUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a Secret Template Extended Mapping
        api_response = api_instance.secret_templates_service_update_secret_template_extended_mapping(extended_type_id, secret_template_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_update_secret_template_extended_mapping: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Secret Template Extended Mapping
        api_response = api_instance.secret_templates_service_update_secret_template_extended_mapping(extended_type_id, secret_template_id, secret_template_extended_mapping_update_args=secret_template_extended_mapping_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_update_secret_template_extended_mapping: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extended_type_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| extendedTypeId |
 **secret_template_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| secretTemplateId |
 **secret_template_extended_mapping_update_args** | [**SecretTemplateExtendedMappingUpdateArgs**](SecretTemplateExtendedMappingUpdateArgs.md)| args | [optional]

### Return type

[**SecretTemplateExtendedMappingModel**](SecretTemplateExtendedMappingModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of extended mappings |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_update_secret_template_launcher**
> SecretTemplateLauncherModel secret_templates_service_update_secret_template_launcher(launcher_type_id, secret_template_id)

Update a Secret Template Launcher

Update a Launchers for a Secret Template

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
from plugins.model.secret_template_launcher_model import SecretTemplateLauncherModel
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.secret_template_launcher_update_args import SecretTemplateLauncherUpdateArgs
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    launcher_type_id = None # bool, date, datetime, dict, float, int, list, str, none_type | launcherTypeId
    secret_template_id = None # bool, date, datetime, dict, float, int, list, str, none_type | secretTemplateId
    secret_template_launcher_update_args = SecretTemplateLauncherUpdateArgs(
        data=SecretTemplateLauncherUpdateModel(
            allow_list=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=None,
            ),
            connect_as_command=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            connect_as_command_response=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            connect_as_timeout_in_seconds=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=None,
            ),
            deny_list=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=None,
            ),
            expected_prompt_ending=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            fields=UpdateFieldValueOfSecretTemplateLauncherFieldValueModelArray(
                dirty=True,
                value=[
                    SecretTemplateLauncherFieldValueModel(
                        default_type=None,
                        default_type_int_max=None,
                        default_type_int_min=None,
                        default_value=None,
                        launcher_type_field_id=None,
                        launcher_type_field_name=None,
                        promptable_field=True,
                        secret_field_id=None,
                        secret_field_name=None,
                    ),
                ],
            ),
            include_machines_from_dependencies=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            line_ending=UpdateFieldValueOfOptionalLauncherConnectAsLineEnding(
                dirty=True,
                value=None,
            ),
            restrict_as=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=None,
            ),
            restrict_by_secret_field=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=None,
            ),
            restrict_user_input=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
        ),
    ) # SecretTemplateLauncherUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a Secret Template Launcher
        api_response = api_instance.secret_templates_service_update_secret_template_launcher(launcher_type_id, secret_template_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_update_secret_template_launcher: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Secret Template Launcher
        api_response = api_instance.secret_templates_service_update_secret_template_launcher(launcher_type_id, secret_template_id, secret_template_launcher_update_args=secret_template_launcher_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_update_secret_template_launcher: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **launcher_type_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| launcherTypeId |
 **secret_template_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| secretTemplateId |
 **secret_template_launcher_update_args** | [**SecretTemplateLauncherUpdateArgs**](SecretTemplateLauncherUpdateArgs.md)| args | [optional]

### Return type

[**SecretTemplateLauncherModel**](SecretTemplateLauncherModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Launchers |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_templates_service_update_secret_template_password_type**
> SecretTemplateModel secret_templates_service_update_secret_template_password_type(template_id)

Update Secret Templates Password Type

Update A Secret template Password Type Options and Fields

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import secret_templates_api
from plugins.model.secret_template_password_type_update_args import SecretTemplatePasswordTypeUpdateArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.secret_template_model import SecretTemplateModel
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
    api_instance = secret_templates_api.SecretTemplatesApi(api_client)
    template_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Secret template ID
    secret_template_password_type_update_args = SecretTemplatePasswordTypeUpdateArgs(
        password_type_id=None,
        secret_field_password_type_field_dictionary={},
    ) # SecretTemplatePasswordTypeUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Secret Templates Password Type
        api_response = api_instance.secret_templates_service_update_secret_template_password_type(template_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_update_secret_template_password_type: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Secret Templates Password Type
        api_response = api_instance.secret_templates_service_update_secret_template_password_type(template_id, secret_template_password_type_update_args=secret_template_password_type_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling SecretTemplatesApi->secret_templates_service_update_secret_template_password_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Secret template ID |
 **secret_template_password_type_update_args** | [**SecretTemplatePasswordTypeUpdateArgs**](SecretTemplatePasswordTypeUpdateArgs.md)| args | [optional]

### Return type

[**SecretTemplateModel**](SecretTemplateModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret template object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

