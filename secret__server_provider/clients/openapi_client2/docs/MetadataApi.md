# plugins.MetadataApi

All URIs are relative to *https://integrations.secretservercloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metadata_service_create_metadata**](MetadataApi.md#metadata_service_create_metadata) | **POST** /v1/metadata/{itemType}/{itemId} | Create Metadata
[**metadata_service_delete_metadata**](MetadataApi.md#metadata_service_delete_metadata) | **DELETE** /v1/metadata/{itemType}/{itemId}/{metadataItemDataId} | Delete Metadata
[**metadata_service_get_field_sections**](MetadataApi.md#metadata_service_get_field_sections) | **GET** /v1/metadata/field-sections | Get metadata field sections
[**metadata_service_get_fields**](MetadataApi.md#metadata_service_get_fields) | **GET** /v1/metadata/fields | Get metadata fields
[**metadata_service_search_metadata**](MetadataApi.md#metadata_service_search_metadata) | **GET** /v1/metadata | Search metadata
[**metadata_service_search_metadata_history**](MetadataApi.md#metadata_service_search_metadata_history) | **GET** /v1/metadata/history | Search metadata history
[**metadata_service_update_metadata**](MetadataApi.md#metadata_service_update_metadata) | **PATCH** /v1/metadata/{itemType}/{itemId} | Update or Create Metadata
[**metadata_service_update_metadata_field_section**](MetadataApi.md#metadata_service_update_metadata_field_section) | **PATCH** /v1/metadata/field-sections/{fieldSectionId} | Update a metadata field section


# **metadata_service_create_metadata**
> MetadataModel metadata_service_create_metadata(item_id, item_type)

Create Metadata

Create or update a metadata field for an item

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import metadata_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.metadata_create_args import MetadataCreateArgs
from plugins.model.metadata_model import MetadataModel
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
    api_instance = metadata_api.MetadataApi(api_client)
    item_id = 1 # int | The item ID of the entity to which this metadata is associated
    item_type = "itemType_example" # str | The type of entity to which this metadata is associated
    metadata_create_args = MetadataCreateArgs(
        data=MetadataCreateModel(
            contains_personal_information=True,
            field_data_type="field_data_type_example",
            metadata_field_id=1,
            metadata_field_name="metadata_field_name_example",
            metadata_field_section_description="metadata_field_section_description_example",
            metadata_field_section_id=1,
            metadata_field_section_name="metadata_field_section_name_example",
            metadata_field_section_requires_administer_metadata=True,
            metadata_field_section_requires_entity_edit=True,
            value_bit=True,
            value_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            value_int=1,
            value_number=3.14,
            value_string="value_string_example",
        ),
    ) # MetadataCreateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Metadata
        api_response = api_instance.metadata_service_create_metadata(item_id, item_type)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling MetadataApi->metadata_service_create_metadata: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Metadata
        api_response = api_instance.metadata_service_create_metadata(item_id, item_type, metadata_create_args=metadata_create_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling MetadataApi->metadata_service_create_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**| The item ID of the entity to which this metadata is associated |
 **item_type** | **str**| The type of entity to which this metadata is associated |
 **metadata_create_args** | [**MetadataCreateArgs**](MetadataCreateArgs.md)| args | [optional]

### Return type

[**MetadataModel**](MetadataModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Newly created or updated MetadataModel |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_service_delete_metadata**
> MetadataDeleteResponse metadata_service_delete_metadata(item_id, item_type, metadata_item_data_id)

Delete Metadata

Deletes the metadata value and all history for that item

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import metadata_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.metadata_delete_response import MetadataDeleteResponse
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
    api_instance = metadata_api.MetadataApi(api_client)
    item_id = 1 # int | The item ID of the entity to which this metadata is associated
    item_type = "itemType_example" # str | The type of entity to which this metadata is associated
    metadata_item_data_id = 1 # int | The sequence ID of the metadata record to delete

    # example passing only required values which don't have defaults set
    try:
        # Delete Metadata
        api_response = api_instance.metadata_service_delete_metadata(item_id, item_type, metadata_item_data_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling MetadataApi->metadata_service_delete_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**| The item ID of the entity to which this metadata is associated |
 **item_type** | **str**| The type of entity to which this metadata is associated |
 **metadata_item_data_id** | **int**| The sequence ID of the metadata record to delete |

### Return type

[**MetadataDeleteResponse**](MetadataDeleteResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_service_get_field_sections**
> PagingOfMetadataFieldSectionSummaryModel metadata_service_get_field_sections()

Get metadata field sections

Return all of the metadata sections that have metadata for a specific item.

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import metadata_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_metadata_field_section_summary_model import PagingOfMetadataFieldSectionSummaryModel
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
    api_instance = metadata_api.MetadataApi(api_client)
    filter_item_id = 1 # int | Return sections that have metadata for this specific item id.  MetadataType will be required. (optional)
    filter_metadata_section_filter_id = 1 # int | Return a specific Metadata Section Field ID. (optional)
    filter_metadata_type = "filter.metadataType_example" # str | Only return metadata for a specific type of item.  Will also required an ItemId (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get metadata field sections
        api_response = api_instance.metadata_service_get_field_sections(filter_item_id=filter_item_id, filter_metadata_section_filter_id=filter_metadata_section_filter_id, filter_metadata_type=filter_metadata_type, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling MetadataApi->metadata_service_get_field_sections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_item_id** | **int**| Return sections that have metadata for this specific item id.  MetadataType will be required. | [optional]
 **filter_metadata_section_filter_id** | **int**| Return a specific Metadata Section Field ID. | [optional]
 **filter_metadata_type** | **str**| Only return metadata for a specific type of item.  Will also required an ItemId | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfMetadataFieldSectionSummaryModel**](PagingOfMetadataFieldSectionSummaryModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata Sections that match criteria. |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_service_get_fields**
> PagingOfMetadataFieldSummaryModel metadata_service_get_fields()

Get metadata fields

Returns a list of all of the metadata sections and fields that exist

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import metadata_api
from plugins.model.paging_of_metadata_field_summary_model import PagingOfMetadataFieldSummaryModel
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
    api_instance = metadata_api.MetadataApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get metadata fields
        api_response = api_instance.metadata_service_get_fields()
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling MetadataApi->metadata_service_get_fields: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**PagingOfMetadataFieldSummaryModel**](PagingOfMetadataFieldSummaryModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata Fields that exist |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_service_search_metadata**
> PagingOfMetadataSummaryModel metadata_service_search_metadata()

Search metadata

Search, filter, sort, and page metadata

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import metadata_api
from plugins.model.paging_of_metadata_summary_model import PagingOfMetadataSummaryModel
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
    api_instance = metadata_api.MetadataApi(api_client)
    filter_item_id = 1 # int | Will only return metadata for this entity ID.  MetadataType will also be required. (optional)
    filter_meta_data_field_id = 1 # int | Return a specific metadata field (optional)
    filter_metadata_type = "filter.metadataType_example" # str | Will only return metadata for this type.  ItemId will also be required. (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search metadata
        api_response = api_instance.metadata_service_search_metadata(filter_item_id=filter_item_id, filter_meta_data_field_id=filter_meta_data_field_id, filter_metadata_type=filter_metadata_type, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling MetadataApi->metadata_service_search_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_item_id** | **int**| Will only return metadata for this entity ID.  MetadataType will also be required. | [optional]
 **filter_meta_data_field_id** | **int**| Return a specific metadata field | [optional]
 **filter_metadata_type** | **str**| Will only return metadata for this type.  ItemId will also be required. | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfMetadataSummaryModel**](PagingOfMetadataSummaryModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata search results |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_service_search_metadata_history**
> PagingOfMetadataHistorySummaryModel metadata_service_search_metadata_history()

Search metadata history

Search, filter, sort, and page metadata history

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import metadata_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
from plugins.model.paging_of_metadata_history_summary_model import PagingOfMetadataHistorySummaryModel
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
    api_instance = metadata_api.MetadataApi(api_client)
    is_exporting = True # bool | isExporting (optional)
    filter_end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only return history metadata values that were entered before this time (optional)
    filter_item_id = 1 # int | Will only return metadata for this entity ID.  MetadataType will also be required. (optional)
    filter_meta_data_field_id = 1 # int | Return a specific metadata field (optional)
    filter_metadata_type = "filter.metadataType_example" # str | Will only return metadata for this type.  ItemId will also be required. (optional)
    filter_start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only return history metadata values that were entered after this time (optional)
    skip = 1 # int | Number of records to skip before taking results (optional)
    sort_by_0_direction = "sortBy[0].direction_example" # str | Sort direction (optional)
    sort_by_0_name = "sortBy[0].name_example" # str | Sort field name (optional)
    sort_by_0_priority = 1 # int | Priority index. Sorts with lower values are executed earlier (optional)
    take = 1 # int | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search metadata history
        api_response = api_instance.metadata_service_search_metadata_history(is_exporting=is_exporting, filter_end_date=filter_end_date, filter_item_id=filter_item_id, filter_meta_data_field_id=filter_meta_data_field_id, filter_metadata_type=filter_metadata_type, filter_start_date=filter_start_date, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling MetadataApi->metadata_service_search_metadata_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_exporting** | **bool**| isExporting | [optional]
 **filter_end_date** | **datetime**| Only return history metadata values that were entered before this time | [optional]
 **filter_item_id** | **int**| Will only return metadata for this entity ID.  MetadataType will also be required. | [optional]
 **filter_meta_data_field_id** | **int**| Return a specific metadata field | [optional]
 **filter_metadata_type** | **str**| Will only return metadata for this type.  ItemId will also be required. | [optional]
 **filter_start_date** | **datetime**| Only return history metadata values that were entered after this time | [optional]
 **skip** | **int**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **str**| Sort direction | [optional]
 **sort_by_0_name** | **str**| Sort field name | [optional]
 **sort_by_0_priority** | **int**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **int**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfMetadataHistorySummaryModel**](PagingOfMetadataHistorySummaryModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata search history results |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_service_update_metadata**
> MetadataModel metadata_service_update_metadata(item_id, item_type)

Update or Create Metadata

Update or create a metadata field for an item

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import metadata_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.metadata_model import MetadataModel
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.metadata_update_args import MetadataUpdateArgs
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
    api_instance = metadata_api.MetadataApi(api_client)
    item_id = 1 # int | The item ID of the entity to which this metadata is associated
    item_type = "itemType_example" # str | The type of entity to which this metadata is associated
    metadata_update_args = MetadataUpdateArgs(
        data=MetadataUpdateModel(
            contains_personal_information=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            metadata_item_data_id=1,
            value_bit=UpdateFieldValueOfOptionalBoolean(
                dirty=True,
                value=True,
            ),
            value_date_time=UpdateFieldValueOfOptionalDateTime(
                dirty=True,
                value=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
            value_int=UpdateFieldValueOfOptionalInt32(
                dirty=True,
                value=1,
            ),
            value_number=UpdateFieldValueOfOptionalDouble(
                dirty=True,
                value=3.14,
            ),
            value_string=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
        ),
    ) # MetadataUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update or Create Metadata
        api_response = api_instance.metadata_service_update_metadata(item_id, item_type)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling MetadataApi->metadata_service_update_metadata: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update or Create Metadata
        api_response = api_instance.metadata_service_update_metadata(item_id, item_type, metadata_update_args=metadata_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling MetadataApi->metadata_service_update_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**| The item ID of the entity to which this metadata is associated |
 **item_type** | **str**| The type of entity to which this metadata is associated |
 **metadata_update_args** | [**MetadataUpdateArgs**](MetadataUpdateArgs.md)| args | [optional]

### Return type

[**MetadataModel**](MetadataModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Newly created or updated MetadataModel |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_service_update_metadata_field_section**
> MetadataFieldSectionSummaryModel metadata_service_update_metadata_field_section(field_section_id)

Update a metadata field section

Update a metadata field section

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import metadata_api
from plugins.model.metadata_field_section_update_args import MetadataFieldSectionUpdateArgs
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.metadata_field_section_summary_model import MetadataFieldSectionSummaryModel
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
    api_instance = metadata_api.MetadataApi(api_client)
    field_section_id = 1 # int | The section ID of the field to which this metadata is associated
    item_id = 1 # int | The item ID of the entity to which this metadata is associated (optional)
    item_type = "itemType_example" # str | The type of entity to which this metadata is associated (optional)
    metadata_field_section_update_args = MetadataFieldSectionUpdateArgs(
        data=MetadataFieldSectionUpdateModel(
            metadata_field_section_description=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            metadata_field_section_name=UpdateFieldValueOfString(
                dirty=True,
                value="value_example",
            ),
            metadata_field_section_requires_administer_metadata=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
            metadata_field_section_requires_entity_edit=UpdateFieldValueOfBoolean(
                dirty=True,
                value=True,
            ),
        ),
    ) # MetadataFieldSectionUpdateArgs | args (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a metadata field section
        api_response = api_instance.metadata_service_update_metadata_field_section(field_section_id)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling MetadataApi->metadata_service_update_metadata_field_section: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a metadata field section
        api_response = api_instance.metadata_service_update_metadata_field_section(field_section_id, item_id=item_id, item_type=item_type, metadata_field_section_update_args=metadata_field_section_update_args)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling MetadataApi->metadata_service_update_metadata_field_section: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_section_id** | **int**| The section ID of the field to which this metadata is associated |
 **item_id** | **int**| The item ID of the entity to which this metadata is associated | [optional]
 **item_type** | **str**| The type of entity to which this metadata is associated | [optional]
 **metadata_field_section_update_args** | [**MetadataFieldSectionUpdateArgs**](MetadataFieldSectionUpdateArgs.md)| args | [optional]

### Return type

[**MetadataFieldSectionSummaryModel**](MetadataFieldSectionSummaryModel.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated metadata field section |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

