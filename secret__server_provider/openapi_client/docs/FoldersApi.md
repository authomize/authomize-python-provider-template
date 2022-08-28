# plugins.FoldersApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**folders_service_associate_template_to_folder**](FoldersApi.md#folders_service_associate_template_to_folder) | **POST** /v1/folders/{id}/templates | Associate Template to Folder
[**folders_service_create**](FoldersApi.md#folders_service_create) | **POST** /v1/folders | Create Folder
[**folders_service_delete**](FoldersApi.md#folders_service_delete) | **DELETE** /v1/folders/{id} | Delete Folder
[**folders_service_dissassociate_template_to_folder**](FoldersApi.md#folders_service_dissassociate_template_to_folder) | **DELETE** /v1/folders/{id}/templates/{templateId} | Disassociate Template from Folder
[**folders_service_get**](FoldersApi.md#folders_service_get) | **GET** /v1/folders/{id} | Get Folder
[**folders_service_get_audits**](FoldersApi.md#folders_service_get_audits) | **GET** /v1/folders/{id}/audit | Folder Audits
[**folders_service_get_folder_detail**](FoldersApi.md#folders_service_get_folder_detail) | **GET** /v1/folder-details/{id} | Get Folder Details
[**folders_service_get_pinned_folders**](FoldersApi.md#folders_service_get_pinned_folders) | **GET** /v1/folders/pinned | Get Pinned Folders
[**folders_service_lookup**](FoldersApi.md#folders_service_lookup) | **GET** /v1/folders/lookup | Lookup Folders
[**folders_service_patch_folder**](FoldersApi.md#folders_service_patch_folder) | **PATCH** /v1/folder/{id} | Patch a Folder
[**folders_service_patch_folder_permissions**](FoldersApi.md#folders_service_patch_folder_permissions) | **PATCH** /v1/folder/{folderId}/permissions | Patch Folder Permissions
[**folders_service_pin_folder**](FoldersApi.md#folders_service_pin_folder) | **PATCH** /v1/folder/{id}/pinned | Pin Folder
[**folders_service_search**](FoldersApi.md#folders_service_search) | **GET** /v1/folders | Search Folders
[**folders_service_stub**](FoldersApi.md#folders_service_stub) | **GET** /v1/folders/stub | Get Folder Stub
[**folders_service_unpin_folder**](FoldersApi.md#folders_service_unpin_folder) | **DELETE** /v1/folder/{id}/pinned | Unpin Folder
[**folders_service_update**](FoldersApi.md#folders_service_update) | **PUT** /v1/folders/{id} | Update Folder


# **folders_service_associate_template_to_folder**
> FolderTemplateModel folders_service_associate_template_to_folder(id)

Associate Template to Folder

Allow secrets based on the template to be created in the folder. If the folder has no associated templates, then any template can be used.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import folders_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.folder_template_args import FolderTemplateArgs
from plugins.model.folder_template_model import FolderTemplateModel
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
    api_instance = folders_api.FoldersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Folder ID
    folder_template_args = FolderTemplateArgs(
        folder_id=None,
        template_id=None,
    ) # FolderTemplateArgs | Folder template association options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Associate Template to Folder
        api_response = api_instance.folders_service_associate_template_to_folder(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling FoldersApi->folders_service_associate_template_to_folder: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Associate Template to Folder
        api_response = api_instance.folders_service_associate_template_to_folder(id, folder_template_args=folder_template_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling FoldersApi->folders_service_associate_template_to_folder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Folder ID |
 **folder_template_args** | [**FolderTemplateArgs**](FolderTemplateArgs.md)| Folder template association options | [optional]

### Return type

[**FolderTemplateModel**](FolderTemplateModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folder object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folders_service_create**
> FolderModel folders_service_create()

Create Folder

Create a new secret folder

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import folders_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.folder_model import FolderModel
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.folder_create_args import FolderCreateArgs
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
    api_instance = folders_api.FoldersApi(api_client)
    folder_create_args = FolderCreateArgs(
        folder_name=None,
        folder_type_id=None,
        inherit_permissions=True,
        inherit_secret_policy=True,
        parent_folder_id=None,
        secret_policy_id=None,
    ) # FolderCreateArgs | Folder creation options (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Folder
        api_response = api_instance.folders_service_create(folder_create_args=folder_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling FoldersApi->folders_service_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_create_args** | [**FolderCreateArgs**](FolderCreateArgs.md)| Folder creation options | [optional]

### Return type

[**FolderModel**](FolderModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folder object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folders_service_delete**
> DeletedModel folders_service_delete(id)

Delete Folder

Delete a folder by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import folders_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.deleted_model import DeletedModel
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
    api_instance = folders_api.FoldersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Folder ID

    # example passing only required values which don't have defaults set
    try:
        # Delete Folder
        api_response = api_instance.folders_service_delete(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling FoldersApi->folders_service_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Folder ID |

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

# **folders_service_dissassociate_template_to_folder**
> DeletedModel folders_service_dissassociate_template_to_folder(id, template_id)

Disassociate Template from Folder

Remove the ability to create secrets based on the template in this folder. If the folder has no associated templates, then any template can be used.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import folders_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.deleted_model import DeletedModel
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
    api_instance = folders_api.FoldersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Folder ID
    template_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Template ID

    # example passing only required values which don't have defaults set
    try:
        # Disassociate Template from Folder
        api_response = api_instance.folders_service_dissassociate_template_to_folder(id, template_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling FoldersApi->folders_service_dissassociate_template_to_folder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Folder ID |
 **template_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Template ID |

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
**200** | Folder object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folders_service_get**
> FolderModel folders_service_get(id)

Get Folder

Get a single folder by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import folders_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.folder_model import FolderModel
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
    api_instance = folders_api.FoldersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Folder ID
    get_all_children = True # bool | Whether to retrieve all child folders of the requested folder (optional)
    include_associated_templates = True # bool | Whether to list associated secret templates (optional)
    folder_path = None # bool, date, datetime, dict, float, int, list, str, none_type | A full path to a folder including the folder name can be passed as a query string parameter when the folder ID is set to 0.  This will lookup the folder ID by path. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Folder
        api_response = api_instance.folders_service_get(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling FoldersApi->folders_service_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Folder
        api_response = api_instance.folders_service_get(id, get_all_children=get_all_children, include_associated_templates=include_associated_templates, folder_path=folder_path)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling FoldersApi->folders_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Folder ID |
 **get_all_children** | **bool**| Whether to retrieve all child folders of the requested folder | [optional]
 **include_associated_templates** | **bool**| Whether to list associated secret templates | [optional]
 **folder_path** | **bool, date, datetime, dict, float, int, list, str, none_type**| A full path to a folder including the folder name can be passed as a query string parameter when the folder ID is set to 0.  This will lookup the folder ID by path. | [optional]

### Return type

[**FolderModel**](FolderModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folder object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folders_service_get_audits**
> PagingOfFolderAuditSummary folders_service_get_audits(id)

Folder Audits

Retrieve a list of audits for folder by ID.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import folders_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.paging_of_folder_audit_summary import PagingOfFolderAuditSummary
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
    api_instance = folders_api.FoldersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Folder ID
    is_exporting = True # bool | isExporting (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Folder Audits
        api_response = api_instance.folders_service_get_audits(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling FoldersApi->folders_service_get_audits: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Folder Audits
        api_response = api_instance.folders_service_get_audits(id, is_exporting=is_exporting, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling FoldersApi->folders_service_get_audits: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Folder ID |
 **is_exporting** | **bool**| isExporting | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfFolderAuditSummary**](PagingOfFolderAuditSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Specify paging and sorting options for querying records and returning results |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folders_service_get_folder_detail**
> FolderDetailViewModel folders_service_get_folder_detail(id)

Get Folder Details

Get Folder Details

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import folders_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.folder_detail_view_model import FolderDetailViewModel
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
    api_instance = folders_api.FoldersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | id
    return_empty_instead_of_no_access_exception = True # bool | returnEmptyInsteadOfNoAccessException (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Folder Details
        api_response = api_instance.folders_service_get_folder_detail(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling FoldersApi->folders_service_get_folder_detail: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Folder Details
        api_response = api_instance.folders_service_get_folder_detail(id, return_empty_instead_of_no_access_exception=return_empty_instead_of_no_access_exception)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling FoldersApi->folders_service_get_folder_detail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| id |
 **return_empty_instead_of_no_access_exception** | **bool**| returnEmptyInsteadOfNoAccessException | [optional]

### Return type

[**FolderDetailViewModel**](FolderDetailViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folder Details |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folders_service_get_pinned_folders**
> PagingOfPinnedFolderModel folders_service_get_pinned_folders()

Get Pinned Folders

Return a list of folders that the current user has pinned

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import folders_api
from plugins.model.paging_of_pinned_folder_model import PagingOfPinnedFolderModel
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
    api_instance = folders_api.FoldersApi(api_client)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Pinned Folders
        api_response = api_instance.folders_service_get_pinned_folders(skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling FoldersApi->folders_service_get_pinned_folders: %s\n" % e)
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

[**PagingOfPinnedFolderModel**](PagingOfPinnedFolderModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of pinned folders |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folders_service_lookup**
> PagingOfFolderLookup folders_service_lookup()

Lookup Folders

Search, filter, sort, and page secret folders, returning only folder ID and name

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import folders_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.paging_of_folder_lookup import PagingOfFolderLookup
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
    api_instance = folders_api.FoldersApi(api_client)
    filter_folder_type_id = None # bool, date, datetime, dict, float, int, list, str, none_type | The icon to display for the folder. Depricated in latest UI. Use 1 when setting this value. (optional)
    filter_only_include_root_folders = True # bool | When true only root folders will be returned and ParentFolderId will be ignored (optional)
    filter_parent_folder_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Only returns folders that are children of the specified folder. (optional)
    filter_permission_required = None # bool, date, datetime, dict, float, int, list, str, none_type | Specify whether to filter by Owner, Edit, AddSecret, View folder permission. Default is View. (optional)
    filter_search_text = None # bool, date, datetime, dict, float, int, list, str, none_type | Search term to match against folder names. Search returns any folder where the search term is contained in the folder name. (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Lookup Folders
        api_response = api_instance.folders_service_lookup(filter_folder_type_id=filter_folder_type_id, filter_only_include_root_folders=filter_only_include_root_folders, filter_parent_folder_id=filter_parent_folder_id, filter_permission_required=filter_permission_required, filter_search_text=filter_search_text, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling FoldersApi->folders_service_lookup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_folder_type_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| The icon to display for the folder. Depricated in latest UI. Use 1 when setting this value. | [optional]
 **filter_only_include_root_folders** | **bool**| When true only root folders will be returned and ParentFolderId will be ignored | [optional]
 **filter_parent_folder_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Only returns folders that are children of the specified folder. | [optional]
 **filter_permission_required** | **bool, date, datetime, dict, float, int, list, str, none_type**| Specify whether to filter by Owner, Edit, AddSecret, View folder permission. Default is View. | [optional]
 **filter_search_text** | **bool, date, datetime, dict, float, int, list, str, none_type**| Search term to match against folder names. Search returns any folder where the search term is contained in the folder name. | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfFolderLookup**](PagingOfFolderLookup.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folder search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folders_service_patch_folder**
> FolderBasicModel folders_service_patch_folder(id)

Patch a Folder

Patch a single secret folder by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import folders_api
from plugins.model.folder_basic_model import FolderBasicModel
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.folder_patch_args import FolderPatchArgs
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
    api_instance = folders_api.FoldersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Folder ID
    folder_patch_args = FolderPatchArgs(
        data=FolderPatchModel(
            allowed_templates=[
                None,
            ],
            allow_remove_owner=True,
            enable_inherit_permissions=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            enable_inherit_secret_policy=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            folder_name=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            permissons=[
                FolderPermissionModel(
                    folder_access_role_id=None,
                    folder_access_role_name=None,
                    folder_id=None,
                    group_id=None,
                    group_name=None,
                    id=None,
                    known_as=None,
                    secret_access_role_id=None,
                    secret_access_role_name=None,
                    user_id=None,
                    user_name=None,
                ),
            ],
            secret_policy=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=None,
            ),
        ),
    ) # FolderPatchArgs | Folder update options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Patch a Folder
        api_response = api_instance.folders_service_patch_folder(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling FoldersApi->folders_service_patch_folder: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Patch a Folder
        api_response = api_instance.folders_service_patch_folder(id, folder_patch_args=folder_patch_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling FoldersApi->folders_service_patch_folder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Folder ID |
 **folder_patch_args** | [**FolderPatchArgs**](FolderPatchArgs.md)| Folder update options | [optional]

### Return type

[**FolderBasicModel**](FolderBasicModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folder object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folders_service_patch_folder_permissions**
> FolderPermissionsPatchResultModel folders_service_patch_folder_permissions(folder_id)

Patch Folder Permissions

Add, delete, and update some permissions as opposed to a full replace of all permissions for a folder

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import folders_api
from plugins.model.folder_permissions_patch_args import FolderPermissionsPatchArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.folder_permissions_patch_result_model import FolderPermissionsPatchResultModel
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
    api_instance = folders_api.FoldersApi(api_client)
    folder_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Folder ID
    folder_permissions_patch_args = FolderPermissionsPatchArgs(
        data=FolderPermissionsPatchData(
            add_or_update_items=[
                FolderPermissionsGroupUpdateModel(
                    folder_access_role_id=None,
                    group_id=None,
                    secret_access_role_id=None,
                    user_id=None,
                ),
            ],
            allow_remove_owner=True,
            inherit_permissions=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            remove_items=[
                FolderPermissionsGroupModel(
                    group_id=None,
                    user_id=None,
                ),
            ],
        ),
    ) # FolderPermissionsPatchArgs | Folder permission update options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Patch Folder Permissions
        api_response = api_instance.folders_service_patch_folder_permissions(folder_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling FoldersApi->folders_service_patch_folder_permissions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Patch Folder Permissions
        api_response = api_instance.folders_service_patch_folder_permissions(folder_id, folder_permissions_patch_args=folder_permissions_patch_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling FoldersApi->folders_service_patch_folder_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Folder ID |
 **folder_permissions_patch_args** | [**FolderPermissionsPatchArgs**](FolderPermissionsPatchArgs.md)| Folder permission update options | [optional]

### Return type

[**FolderPermissionsPatchResultModel**](FolderPermissionsPatchResultModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success result |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folders_service_pin_folder**
> PinFolderResultModel folders_service_pin_folder(id)

Pin Folder

Pin a single folder or update settings for the pinned folder for the current user

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import folders_api
from plugins.model.pin_folder_args import PinFolderArgs
from plugins.model.pin_folder_result_model import PinFolderResultModel
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
    api_instance = folders_api.FoldersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Folder ID
    pin_folder_args = PinFolderArgs(
        data=PinFolderData(
            active_filter=UpdateFieldValueOfOptionalBoolean(
                dirty=True,
                value=True,
            ),
            display_name=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            include_subfolders=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            last_viewed=UpdateFieldValueOfOptionalDateTime(
                dirty=True,
                value=None,
            ),
            search_text=UpdateFieldValueOfString(
                dirty=True,
                value=None,
            ),
            selected_folder_id=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=None,
            ),
            show_cards=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            template_filter=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=None,
            ),
        ),
    ) # PinFolderArgs | Pin Folder Args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Pin Folder
        api_response = api_instance.folders_service_pin_folder(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling FoldersApi->folders_service_pin_folder: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Pin Folder
        api_response = api_instance.folders_service_pin_folder(id, pin_folder_args=pin_folder_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling FoldersApi->folders_service_pin_folder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Folder ID |
 **pin_folder_args** | [**PinFolderArgs**](PinFolderArgs.md)| Pin Folder Args | [optional]

### Return type

[**PinFolderResultModel**](PinFolderResultModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success Status |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folders_service_search**
> PagingOfFolderSummary folders_service_search()

Search Folders

Search, filter, sort, and page secret folders

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import folders_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_folder_summary import PagingOfFolderSummary
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
    api_instance = folders_api.FoldersApi(api_client)
    filter_folder_type_id = None # bool, date, datetime, dict, float, int, list, str, none_type | The icon to display for the folder. Depricated in latest UI. Use 1 when setting this value. (optional)
    filter_only_include_root_folders = True # bool | When true only root folders will be returned and ParentFolderId will be ignored (optional)
    filter_parent_folder_id = None # bool, date, datetime, dict, float, int, list, str, none_type | Only returns folders that are children of the specified folder. (optional)
    filter_permission_required = None # bool, date, datetime, dict, float, int, list, str, none_type | Specify whether to filter by Owner, Edit, AddSecret, View folder permission. Default is View. (optional)
    filter_search_text = None # bool, date, datetime, dict, float, int, list, str, none_type | Search term to match against folder names. Search returns any folder where the search term is contained in the folder name. (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Folders
        api_response = api_instance.folders_service_search(filter_folder_type_id=filter_folder_type_id, filter_only_include_root_folders=filter_only_include_root_folders, filter_parent_folder_id=filter_parent_folder_id, filter_permission_required=filter_permission_required, filter_search_text=filter_search_text, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling FoldersApi->folders_service_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_folder_type_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| The icon to display for the folder. Depricated in latest UI. Use 1 when setting this value. | [optional]
 **filter_only_include_root_folders** | **bool**| When true only root folders will be returned and ParentFolderId will be ignored | [optional]
 **filter_parent_folder_id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Only returns folders that are children of the specified folder. | [optional]
 **filter_permission_required** | **bool, date, datetime, dict, float, int, list, str, none_type**| Specify whether to filter by Owner, Edit, AddSecret, View folder permission. Default is View. | [optional]
 **filter_search_text** | **bool, date, datetime, dict, float, int, list, str, none_type**| Search term to match against folder names. Search returns any folder where the search term is contained in the folder name. | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfFolderSummary**](PagingOfFolderSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folder search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folders_service_stub**
> FolderModel folders_service_stub()

Get Folder Stub

Return the default values for a new secret folder

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import folders_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.folder_model import FolderModel
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
    api_instance = folders_api.FoldersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Folder Stub
        api_response = api_instance.folders_service_stub()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling FoldersApi->folders_service_stub: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**FolderModel**](FolderModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folder object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folders_service_unpin_folder**
> UnpinFolderResultModel folders_service_unpin_folder(id)

Unpin Folder

Unpin a folder for the current user.  This will remove any settings for this user for this pinned folder.  If not pinned already it will still return success.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import folders_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.unpin_folder_result_model import UnpinFolderResultModel
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
    api_instance = folders_api.FoldersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Folder ID

    # example passing only required values which don't have defaults set
    try:
        # Unpin Folder
        api_response = api_instance.folders_service_unpin_folder(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling FoldersApi->folders_service_unpin_folder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Folder ID |

### Return type

[**UnpinFolderResultModel**](UnpinFolderResultModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success Status |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **folders_service_update**
> FolderModel folders_service_update(id)

Update Folder

Update a single secret folder by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import folders_api
from plugins.model.folder_update_args import FolderUpdateArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.folder_model import FolderModel
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
    api_instance = folders_api.FoldersApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Folder ID
    folder_update_args = FolderUpdateArgs(
        folder_name=None,
        folder_type_id=None,
        id=None,
        inherit_permissions=True,
        inherit_secret_policy=True,
        parent_folder_id=None,
        secret_policy_id=None,
    ) # FolderUpdateArgs | Folder update options (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Folder
        api_response = api_instance.folders_service_update(id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling FoldersApi->folders_service_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Folder
        api_response = api_instance.folders_service_update(id, folder_update_args=folder_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling FoldersApi->folders_service_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Folder ID |
 **folder_update_args** | [**FolderUpdateArgs**](FolderUpdateArgs.md)| Folder update options | [optional]

### Return type

[**FolderModel**](FolderModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folder object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

