# plugins.ApplicationAccountsApi

All URIs are relative to *https://integrations.secretservercloud.com//api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**application_accounts_service_lookup_account**](ApplicationAccountsApi.md#application_accounts_service_lookup_account) | **GET** /v1/application-accounts/lookup | Lookup Application Accounts


# **application_accounts_service_lookup_account**
> PagingOfUserLookup application_accounts_service_lookup_account()

Lookup Application Accounts

Search, filter, sort, and page application accounts, returning only user id and display

### Example

* Api Key Authentication (BearerToken):

```python
import time
import plugins
from plugins.api import application_accounts_api
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.paging_of_user_lookup import PagingOfUserLookup
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse
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
    api_instance = application_accounts_api.ApplicationAccountsApi(api_client)
    filter_include_all = True # bool | IncludeAll (optional)
    filter_include_inactive = True # bool | Include inactive application accounts in the results. Inactive application accounts are included by default. (optional)
    filter_search_text = None # bool, date, datetime, dict, float, int, list, str, none_type | Search text (optional)
    skip = None # bool, date, datetime, dict, float, int, list, str, none_type | Number of records to skip before taking results (optional)
    sort_by_0_direction = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort direction (optional)
    sort_by_0_name = None # bool, date, datetime, dict, float, int, list, str, none_type | Sort field name (optional)
    sort_by_0_priority = None # bool, date, datetime, dict, float, int, list, str, none_type | Priority index. Sorts with lower values are executed earlier (optional)
    take = None # bool, date, datetime, dict, float, int, list, str, none_type | Maximum number of records to include in results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Lookup Application Accounts
        api_response = api_instance.application_accounts_service_lookup_account(filter_include_all=filter_include_all, filter_include_inactive=filter_include_inactive, filter_search_text=filter_search_text, skip=skip, sort_by_0_direction=sort_by_0_direction, sort_by_0_name=sort_by_0_name, sort_by_0_priority=sort_by_0_priority, take=take)
        pprint(api_response)
    except plugins.ApiException as e:
        print("Exception when calling ApplicationAccountsApi->application_accounts_service_lookup_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_include_all** | **bool**| IncludeAll | [optional]
 **filter_include_inactive** | **bool**| Include inactive application accounts in the results. Inactive application accounts are included by default. | [optional]
 **filter_search_text** | **bool, date, datetime, dict, float, int, list, str, none_type**| Search text | [optional]
 **skip** | **bool, date, datetime, dict, float, int, list, str, none_type**| Number of records to skip before taking results | [optional]
 **sort_by_0_direction** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort direction | [optional]
 **sort_by_0_name** | **bool, date, datetime, dict, float, int, list, str, none_type**| Sort field name | [optional]
 **sort_by_0_priority** | **bool, date, datetime, dict, float, int, list, str, none_type**| Priority index. Sorts with lower values are executed earlier | [optional]
 **take** | **bool, date, datetime, dict, float, int, list, str, none_type**| Maximum number of records to include in results | [optional]

### Return type

[**PagingOfUserLookup**](PagingOfUserLookup.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User search result object |  -  |
**400** | Bad request |  -  |
**403** | Authentication failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

