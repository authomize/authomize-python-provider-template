# plugins.CategorizedListsApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**categorized_lists_service_add_item_to_list**](CategorizedListsApi.md#categorized_lists_service_add_item_to_list) | **POST** /v1/lists/{categorizedListId}/options/single | Adds an option to a list
[**categorized_lists_service_add_items_to_list**](CategorizedListsApi.md#categorized_lists_service_add_items_to_list) | **POST** /v1/lists/{categorizedListId}/options | Adds options to a list
[**categorized_lists_service_add_items_to_list_from_file**](CategorizedListsApi.md#categorized_lists_service_add_items_to_list_from_file) | **POST** /v1/lists/{categorizedListId}/options/file | Upload a file of list options
[**categorized_lists_service_add_items_to_list_with_category**](CategorizedListsApi.md#categorized_lists_service_add_items_to_list_with_category) | **POST** /v1/lists/{categorizedListId}/options/{category} | Adds options to the list with the specified category
[**categorized_lists_service_create_list**](CategorizedListsApi.md#categorized_lists_service_create_list) | **POST** /v1/lists | Create a list
[**categorized_lists_service_delete_list**](CategorizedListsApi.md#categorized_lists_service_delete_list) | **DELETE** /v1/lists/{categorizedListId} | Delete List
[**categorized_lists_service_get_all_lists_user_may_see**](CategorizedListsApi.md#categorized_lists_service_get_all_lists_user_may_see) | **GET** /v1/lists/summary | Get a list of lists available to current user
[**categorized_lists_service_get_categories_for_list**](CategorizedListsApi.md#categorized_lists_service_get_categories_for_list) | **GET** /v1/lists/{categorizedListId}/categories | Get a list&#39;s current categories
[**categorized_lists_service_get_list**](CategorizedListsApi.md#categorized_lists_service_get_list) | **GET** /v1/lists/{categorizedListId} | Get a list
[**categorized_lists_service_get_list_items**](CategorizedListsApi.md#categorized_lists_service_get_list_items) | **GET** /v1/lists/{categorizedListId}/options | Get a list&#39;s items
[**categorized_lists_service_remove_item_from_list**](CategorizedListsApi.md#categorized_lists_service_remove_item_from_list) | **DELETE** /v1/lists/{listId}/options/{optionId} | Delete a list option from a list
[**categorized_lists_service_remove_items_from_list**](CategorizedListsApi.md#categorized_lists_service_remove_items_from_list) | **DELETE** /v1/lists/{categorizedListId}/options | Delete all list options from a list
[**categorized_lists_service_replace_items_in_list**](CategorizedListsApi.md#categorized_lists_service_replace_items_in_list) | **PUT** /v1/lists/{categorizedListId}/options/replace | Replaces options in a list
[**categorized_lists_service_search**](CategorizedListsApi.md#categorized_lists_service_search) | **GET** /v1/lists | Search Lists
[**categorized_lists_service_search_list_audit**](CategorizedListsApi.md#categorized_lists_service_search_list_audit) | **GET** /v1/lists/{categorizedListId}/audits | Get Audits for List
[**categorized_lists_service_update_item_in_list**](CategorizedListsApi.md#categorized_lists_service_update_item_in_list) | **PUT** /v1/lists/{categorizedListId}/options/single | Updates an option in a list
[**categorized_lists_service_update_items_in_list**](CategorizedListsApi.md#categorized_lists_service_update_items_in_list) | **PUT** /v1/lists/{categorizedListId}/options | Updates options in a list
[**categorized_lists_service_update_list**](CategorizedListsApi.md#categorized_lists_service_update_list) | **PUT** /v1/lists/{categorizedListId} | Update a list


# **categorized_lists_service_add_item_to_list**
> PagingOfCategorizedListItemViewModel categorized_lists_service_add_item_to_list(categorized_list_id)

Adds an option to a list

Adds an option to the list with the provided ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import categorized_lists_api
from plugins.model.categorized_list_item_single_create_args import CategorizedListItemSingleCreateArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_categorized_list_item_view_model import PagingOfCategorizedListItemViewModel
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
    api_instance = categorized_lists_api.CategorizedListsApi(api_client)
    categorized_list_id = "categorizedListId_example" # str | List ID
    categorized_list_item_single_create_args = CategorizedListItemSingleCreateArgs(
        option=CategorizedListItemCreateModel(
            category=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            value=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
        ),
    ) # CategorizedListItemSingleCreateArgs | List option to be added (optional)

    # example passing only required values which don't have defaults set
    try:
        # Adds an option to a list
        api_response = api_instance.categorized_lists_service_add_item_to_list(categorized_list_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling CategorizedListsApi->categorized_lists_service_add_item_to_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Adds an option to a list
        api_response = api_instance.categorized_lists_service_add_item_to_list(categorized_list_id, categorized_list_item_single_create_args=categorized_list_item_single_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling CategorizedListsApi->categorized_lists_service_add_item_to_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **categorized_list_id** | **str**| List ID |
 **categorized_list_item_single_create_args** | [**CategorizedListItemSingleCreateArgs**](CategorizedListItemSingleCreateArgs.md)| List option to be added | [optional]

### Return type

[**PagingOfCategorizedListItemViewModel**](PagingOfCategorizedListItemViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new option in the list |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **categorized_lists_service_add_items_to_list**
> PagingOfCategorizedListItemViewModel categorized_lists_service_add_items_to_list(categorized_list_id)

Adds options to a list

Adds the options to the list with the provided ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import categorized_lists_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.categorized_list_item_create_args import CategorizedListItemCreateArgs
from plugins.model.paging_of_categorized_list_item_view_model import PagingOfCategorizedListItemViewModel
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
    api_instance = categorized_lists_api.CategorizedListsApi(api_client)
    categorized_list_id = "categorizedListId_example" # str | List ID
    categorized_list_item_create_args = CategorizedListItemCreateArgs(
        data=[
            CategorizedListItemCreateModel(
                category=UpdateFieldValueOfString(
                    dirty=True,
                    value="value_example",
                ),
                value=UpdateFieldValueOfString(
                    dirty=True,
                    value="value_example",
                ),
            ),
        ],
    ) # CategorizedListItemCreateArgs | List options to be added (optional)

    # example passing only required values which don't have defaults set
    try:
        # Adds options to a list
        api_response = api_instance.categorized_lists_service_add_items_to_list(categorized_list_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling CategorizedListsApi->categorized_lists_service_add_items_to_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Adds options to a list
        api_response = api_instance.categorized_lists_service_add_items_to_list(categorized_list_id, categorized_list_item_create_args=categorized_list_item_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling CategorizedListsApi->categorized_lists_service_add_items_to_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **categorized_list_id** | **str**| List ID |
 **categorized_list_item_create_args** | [**CategorizedListItemCreateArgs**](CategorizedListItemCreateArgs.md)| List options to be added | [optional]

### Return type

[**PagingOfCategorizedListItemViewModel**](PagingOfCategorizedListItemViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new options in the list |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **categorized_lists_service_add_items_to_list_from_file**
> PagingOfCategorizedListItemModel categorized_lists_service_add_items_to_list_from_file(categorized_list_id)

Upload a file of list options

Adds the options from the given file to the list with the provided ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import categorized_lists_api
from plugins.model.paging_of_categorized_list_item_model import PagingOfCategorizedListItemModel
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.categorized_list_item_create_with_file_args import CategorizedListItemCreateWithFileArgs
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
    api_instance = categorized_lists_api.CategorizedListsApi(api_client)
    categorized_list_id = "categorizedListId_example" # str | List ID
    categorized_list_item_create_with_file_args = CategorizedListItemCreateWithFileArgs(
        delimiter={},
null,
    ) # CategorizedListItemCreateWithFileArgs | File containing list options to add (optional)

    # example passing only required values which don't have defaults set
    try:
        # Upload a file of list options
        api_response = api_instance.categorized_lists_service_add_items_to_list_from_file(categorized_list_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling CategorizedListsApi->categorized_lists_service_add_items_to_list_from_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload a file of list options
        api_response = api_instance.categorized_lists_service_add_items_to_list_from_file(categorized_list_id, categorized_list_item_create_with_file_args=categorized_list_item_create_with_file_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling CategorizedListsApi->categorized_lists_service_add_items_to_list_from_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **categorized_list_id** | **str**| List ID |
 **categorized_list_item_create_with_file_args** | [**CategorizedListItemCreateWithFileArgs**](CategorizedListItemCreateWithFileArgs.md)| File containing list options to add | [optional]

### Return type

[**PagingOfCategorizedListItemModel**](PagingOfCategorizedListItemModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new options in the list |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **categorized_lists_service_add_items_to_list_with_category**
> PagingOfCategorizedListItemViewModel categorized_lists_service_add_items_to_list_with_category(categorized_list_id, category)

Adds options to the list with the specified category

Adds the options to the list with the provided ID with the specified category

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import categorized_lists_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.categorized_list_item_create_args import CategorizedListItemCreateArgs
from plugins.model.paging_of_categorized_list_item_view_model import PagingOfCategorizedListItemViewModel
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
    api_instance = categorized_lists_api.CategorizedListsApi(api_client)
    categorized_list_id = "categorizedListId_example" # str | List ID
    category = "category_example" # str | Category to assign
    categorized_list_item_create_args = CategorizedListItemCreateArgs(
        data=[
            CategorizedListItemCreateModel(
                category=UpdateFieldValueOfString(
                    dirty=True,
                    value="value_example",
                ),
                value=UpdateFieldValueOfString(
                    dirty=True,
                    value="value_example",
                ),
            ),
        ],
    ) # CategorizedListItemCreateArgs | List options to be added (optional)

    # example passing only required values which don't have defaults set
    try:
        # Adds options to the list with the specified category
        api_response = api_instance.categorized_lists_service_add_items_to_list_with_category(categorized_list_id, category)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling CategorizedListsApi->categorized_lists_service_add_items_to_list_with_category: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Adds options to the list with the specified category
        api_response = api_instance.categorized_lists_service_add_items_to_list_with_category(categorized_list_id, category, categorized_list_item_create_args=categorized_list_item_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling CategorizedListsApi->categorized_lists_service_add_items_to_list_with_category: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **categorized_list_id** | **str**| List ID |
 **category** | **str**| Category to assign |
 **categorized_list_item_create_args** | [**CategorizedListItemCreateArgs**](CategorizedListItemCreateArgs.md)| List options to be added | [optional]

### Return type

[**PagingOfCategorizedListItemViewModel**](PagingOfCategorizedListItemViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new options in the list |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **categorized_lists_service_create_list**
> CategorizedListModel categorized_lists_service_create_list()

Create a list

Creates the given list

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import categorized_lists_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.categorized_list_create_args import CategorizedListCreateArgs
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.categorized_list_model import CategorizedListModel
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
    api_instance = categorized_lists_api.CategorizedListsApi(api_client)
    categorized_list_create_args = CategorizedListCreateArgs(
        data=CategorizedListUpdateModel(
            active=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            description=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            name=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
        ),
    ) # CategorizedListCreateArgs | List be added (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a list
        api_response = api_instance.categorized_lists_service_create_list(categorized_list_create_args=categorized_list_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling CategorizedListsApi->categorized_lists_service_create_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **categorized_list_create_args** | [**CategorizedListCreateArgs**](CategorizedListCreateArgs.md)| List be added | [optional]

### Return type

[**CategorizedListModel**](CategorizedListModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new list |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **categorized_lists_service_delete_list**
> CategorizedListDeleteModel categorized_lists_service_delete_list(categorized_list_id)

Delete List

Delete a List by ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import categorized_lists_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.categorized_list_delete_model import CategorizedListDeleteModel
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
    api_instance = categorized_lists_api.CategorizedListsApi(api_client)
    categorized_list_id = "categorizedListId_example" # str | ID of list to be deleted

    # example passing only required values which don't have defaults set
    try:
        # Delete List
        api_response = api_instance.categorized_lists_service_delete_list(categorized_list_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling CategorizedListsApi->categorized_lists_service_delete_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **categorized_list_id** | **str**| ID of list to be deleted |

### Return type

[**CategorizedListDeleteModel**](CategorizedListDeleteModel.md)

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

# **categorized_lists_service_get_all_lists_user_may_see**
> PagingOfSimpleCategorizedList categorized_lists_service_get_all_lists_user_may_see()

Get a list of lists available to current user

Returns a list of lists for the current user

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import categorized_lists_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_simple_categorized_list import PagingOfSimpleCategorizedList
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
    api_instance = categorized_lists_api.CategorizedListsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get a list of lists available to current user
        api_response = api_instance.categorized_lists_service_get_all_lists_user_may_see()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling CategorizedListsApi->categorized_lists_service_get_all_lists_user_may_see: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**PagingOfSimpleCategorizedList**](PagingOfSimpleCategorizedList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of lists for the current user |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **categorized_lists_service_get_categories_for_list**
> PagingOfString categorized_lists_service_get_categories_for_list(categorized_list_id)

Get a list's current categories

Returns the list's categories for the provided ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import categorized_lists_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_string import PagingOfString
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
    api_instance = categorized_lists_api.CategorizedListsApi(api_client)
    categorized_list_id = "categorizedListId_example" # str | List ID

    # example passing only required values which don't have defaults set
    try:
        # Get a list's current categories
        api_response = api_instance.categorized_lists_service_get_categories_for_list(categorized_list_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling CategorizedListsApi->categorized_lists_service_get_categories_for_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **categorized_list_id** | **str**| List ID |

### Return type

[**PagingOfString**](PagingOfString.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list&#39;s categories |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **categorized_lists_service_get_list**
> CategorizedListModel categorized_lists_service_get_list(categorized_list_id)

Get a list

Returns the list for the provided ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import categorized_lists_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.categorized_list_model import CategorizedListModel
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
    api_instance = categorized_lists_api.CategorizedListsApi(api_client)
    categorized_list_id = "categorizedListId_example" # str | List ID

    # example passing only required values which don't have defaults set
    try:
        # Get a list
        api_response = api_instance.categorized_lists_service_get_list(categorized_list_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling CategorizedListsApi->categorized_lists_service_get_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **categorized_list_id** | **str**| List ID |

### Return type

[**CategorizedListModel**](CategorizedListModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list with provided ID |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **categorized_lists_service_get_list_items**
> PagingOfCategorizedListItemModel categorized_lists_service_get_list_items(categorized_list_id)

Get a list's items

Returns the list's options for the provided ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import categorized_lists_api
from plugins.model.paging_of_categorized_list_item_model import PagingOfCategorizedListItemModel
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
    api_instance = categorized_lists_api.CategorizedListsApi(api_client)
    categorized_list_id = "categorizedListId_example" # str | List ID
    filter_category = "filter.category_example" # str | Category text to filter by. If empty or not included, will return items for all categories. (optional)
    filter_null_category_is_uncategorized = True # bool | If true and Category value is an empty string or not included, will return only uncategorized items; otherwise, an empty category filter is treated as no category filter. (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a list's items
        api_response = api_instance.categorized_lists_service_get_list_items(categorized_list_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling CategorizedListsApi->categorized_lists_service_get_list_items: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list's items
        api_response = api_instance.categorized_lists_service_get_list_items(categorized_list_id, filter_category=filter_category, filter_null_category_is_uncategorized=filter_null_category_is_uncategorized, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling CategorizedListsApi->categorized_lists_service_get_list_items: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **categorized_list_id** | **str**| List ID |
 **filter_category** | **str**| Category text to filter by. If empty or not included, will return items for all categories. | [optional]
 **filter_null_category_is_uncategorized** | **bool**| If true and Category value is an empty string or not included, will return only uncategorized items; otherwise, an empty category filter is treated as no category filter. | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfCategorizedListItemModel**](PagingOfCategorizedListItemModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list&#39;s options |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **categorized_lists_service_remove_item_from_list**
> CategorizedListItemDeleteModel categorized_lists_service_remove_item_from_list(list_id, option_id)

Delete a list option from a list

Delete a list option from a list

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import categorized_lists_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.categorized_list_item_delete_model import CategorizedListItemDeleteModel
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
    api_instance = categorized_lists_api.CategorizedListsApi(api_client)
    list_id = "listId_example" # str | List id
    option_id = "optionId_example" # str | List option id

    # example passing only required values which don't have defaults set
    try:
        # Delete a list option from a list
        api_response = api_instance.categorized_lists_service_remove_item_from_list(list_id, option_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling CategorizedListsApi->categorized_lists_service_remove_item_from_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**| List id |
 **option_id** | **str**| List option id |

### Return type

[**CategorizedListItemDeleteModel**](CategorizedListItemDeleteModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List option deletion result |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **categorized_lists_service_remove_items_from_list**
> CategorizedListDeleteModel categorized_lists_service_remove_items_from_list(categorized_list_id)

Delete all list options from a list

Delete all list options from a list

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import categorized_lists_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.categorized_list_delete_model import CategorizedListDeleteModel
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
    api_instance = categorized_lists_api.CategorizedListsApi(api_client)
    categorized_list_id = "categorizedListId_example" # str | List ID

    # example passing only required values which don't have defaults set
    try:
        # Delete all list options from a list
        api_response = api_instance.categorized_lists_service_remove_items_from_list(categorized_list_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling CategorizedListsApi->categorized_lists_service_remove_items_from_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **categorized_list_id** | **str**| List ID |

### Return type

[**CategorizedListDeleteModel**](CategorizedListDeleteModel.md)

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

# **categorized_lists_service_replace_items_in_list**
> PagingOfCategorizedListItemViewModel categorized_lists_service_replace_items_in_list(categorized_list_id)

Replaces options in a list

Replaces all options currently in the list with the given options

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import categorized_lists_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.categorized_list_item_create_args import CategorizedListItemCreateArgs
from plugins.model.paging_of_categorized_list_item_view_model import PagingOfCategorizedListItemViewModel
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
    api_instance = categorized_lists_api.CategorizedListsApi(api_client)
    categorized_list_id = "categorizedListId_example" # str | List ID
    categorized_list_item_create_args = CategorizedListItemCreateArgs(
        data=[
            CategorizedListItemCreateModel(
                category=UpdateFieldValueOfString(
                    dirty=True,
                    value="value_example",
                ),
                value=UpdateFieldValueOfString(
                    dirty=True,
                    value="value_example",
                ),
            ),
        ],
    ) # CategorizedListItemCreateArgs | List options to be added (optional)

    # example passing only required values which don't have defaults set
    try:
        # Replaces options in a list
        api_response = api_instance.categorized_lists_service_replace_items_in_list(categorized_list_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling CategorizedListsApi->categorized_lists_service_replace_items_in_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Replaces options in a list
        api_response = api_instance.categorized_lists_service_replace_items_in_list(categorized_list_id, categorized_list_item_create_args=categorized_list_item_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling CategorizedListsApi->categorized_lists_service_replace_items_in_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **categorized_list_id** | **str**| List ID |
 **categorized_list_item_create_args** | [**CategorizedListItemCreateArgs**](CategorizedListItemCreateArgs.md)| List options to be added | [optional]

### Return type

[**PagingOfCategorizedListItemViewModel**](PagingOfCategorizedListItemViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new item in the list |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **categorized_lists_service_search**
> PagingOfCategorizedListSummary categorized_lists_service_search()

Search Lists

Search, filter, sort, and page lists

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import categorized_lists_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_categorized_list_summary import PagingOfCategorizedListSummary
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
    api_instance = categorized_lists_api.CategorizedListsApi(api_client)
    filter_include_active = True # bool | Whether to include active lists in results (when excluded equals true) (optional)
    filter_include_inactive = True # bool | Whether to include inactive lists in results (optional)
    filter_search_text = "filter.searchText_example" # str | Search text (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Lists
        api_response = api_instance.categorized_lists_service_search(filter_include_active=filter_include_active, filter_include_inactive=filter_include_inactive, filter_search_text=filter_search_text, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling CategorizedListsApi->categorized_lists_service_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_include_active** | **bool**| Whether to include active lists in results (when excluded equals true) | [optional]
 **filter_include_inactive** | **bool**| Whether to include inactive lists in results | [optional]
 **filter_search_text** | **str**| Search text | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfCategorizedListSummary**](PagingOfCategorizedListSummary.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **categorized_lists_service_search_list_audit**
> PagingOfCategorizedListAuditModel categorized_lists_service_search_list_audit(categorized_list_id)

Get Audits for List

Search, filter, sort, and page List Audits.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import categorized_lists_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.paging_of_categorized_list_audit_model import PagingOfCategorizedListAuditModel
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
    api_instance = categorized_lists_api.CategorizedListsApi(api_client)
    categorized_list_id = "categorizedListId_example" # str | List Id
    is_exporting = True # bool | isExporting (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Audits for List
        api_response = api_instance.categorized_lists_service_search_list_audit(categorized_list_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling CategorizedListsApi->categorized_lists_service_search_list_audit: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Audits for List
        api_response = api_instance.categorized_lists_service_search_list_audit(categorized_list_id, is_exporting=is_exporting, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling CategorizedListsApi->categorized_lists_service_search_list_audit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **categorized_list_id** | **str**| List Id |
 **is_exporting** | **bool**| isExporting | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfCategorizedListAuditModel**](PagingOfCategorizedListAuditModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of Audits for List. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **categorized_lists_service_update_item_in_list**
> PagingOfCategorizedListItemViewModel categorized_lists_service_update_item_in_list(categorized_list_id)

Updates an option in a list

Updates an option in the list with the provided ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import categorized_lists_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.categorized_list_item_single_update_args import CategorizedListItemSingleUpdateArgs
from plugins.model.paging_of_categorized_list_item_view_model import PagingOfCategorizedListItemViewModel
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
    api_instance = categorized_lists_api.CategorizedListsApi(api_client)
    categorized_list_id = "categorizedListId_example" # str | List ID
    categorized_list_item_single_update_args = CategorizedListItemSingleUpdateArgs(
        option=CategorizedListItemUpdateModel(
            categorized_list_item_id="categorized_list_item_id_example",
            category=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            value=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
        ),
    ) # CategorizedListItemSingleUpdateArgs | List option to be updated (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates an option in a list
        api_response = api_instance.categorized_lists_service_update_item_in_list(categorized_list_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling CategorizedListsApi->categorized_lists_service_update_item_in_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates an option in a list
        api_response = api_instance.categorized_lists_service_update_item_in_list(categorized_list_id, categorized_list_item_single_update_args=categorized_list_item_single_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling CategorizedListsApi->categorized_lists_service_update_item_in_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **categorized_list_id** | **str**| List ID |
 **categorized_list_item_single_update_args** | [**CategorizedListItemSingleUpdateArgs**](CategorizedListItemSingleUpdateArgs.md)| List option to be updated | [optional]

### Return type

[**PagingOfCategorizedListItemViewModel**](PagingOfCategorizedListItemViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated options in the list |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **categorized_lists_service_update_items_in_list**
> PagingOfCategorizedListItemViewModel categorized_lists_service_update_items_in_list(categorized_list_id)

Updates options in a list

Updates the options in the list with the provided ID

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import categorized_lists_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.categorized_list_item_update_args import CategorizedListItemUpdateArgs
from plugins.model.paging_of_categorized_list_item_view_model import PagingOfCategorizedListItemViewModel
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
    api_instance = categorized_lists_api.CategorizedListsApi(api_client)
    categorized_list_id = "categorizedListId_example" # str | List ID
    categorized_list_item_update_args = CategorizedListItemUpdateArgs(
        data=[
            CategorizedListItemUpdateModel(
                categorized_list_item_id="categorized_list_item_id_example",
                category=UpdateFieldValueOfString(
                    dirty=True,
                    value="value_example",
                ),
                value=UpdateFieldValueOfString(
                    dirty=True,
                    value="value_example",
                ),
            ),
        ],
    ) # CategorizedListItemUpdateArgs | List options to be updated (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates options in a list
        api_response = api_instance.categorized_lists_service_update_items_in_list(categorized_list_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling CategorizedListsApi->categorized_lists_service_update_items_in_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates options in a list
        api_response = api_instance.categorized_lists_service_update_items_in_list(categorized_list_id, categorized_list_item_update_args=categorized_list_item_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling CategorizedListsApi->categorized_lists_service_update_items_in_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **categorized_list_id** | **str**| List ID |
 **categorized_list_item_update_args** | [**CategorizedListItemUpdateArgs**](CategorizedListItemUpdateArgs.md)| List options to be updated | [optional]

### Return type

[**PagingOfCategorizedListItemViewModel**](PagingOfCategorizedListItemViewModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated options in the list |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **categorized_lists_service_update_list**
> CategorizedListModel categorized_lists_service_update_list(categorized_list_id)

Update a list

Updates a given list

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import categorized_lists_api
from plugins.model.categorized_list_update_args import CategorizedListUpdateArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.categorized_list_model import CategorizedListModel
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
    api_instance = categorized_lists_api.CategorizedListsApi(api_client)
    categorized_list_id = "categorizedListId_example" # str | List ID
    categorized_list_update_args = CategorizedListUpdateArgs(
        data=CategorizedListUpdateModel(
            active=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            description=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            name=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
        ),
    ) # CategorizedListUpdateArgs | List to be updated (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a list
        api_response = api_instance.categorized_lists_service_update_list(categorized_list_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling CategorizedListsApi->categorized_lists_service_update_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a list
        api_response = api_instance.categorized_lists_service_update_list(categorized_list_id, categorized_list_update_args=categorized_list_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling CategorizedListsApi->categorized_lists_service_update_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **categorized_list_id** | **str**| List ID |
 **categorized_list_update_args** | [**CategorizedListUpdateArgs**](CategorizedListUpdateArgs.md)| List to be updated | [optional]

### Return type

[**CategorizedListModel**](CategorizedListModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated list |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

