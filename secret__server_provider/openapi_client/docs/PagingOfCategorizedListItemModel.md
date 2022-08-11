# PagingOfCategorizedListItemModel

Specify paging and sorting options for querying records and returning results

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_count** | **bool, date, datetime, dict, float, int, list, str, none_type** | Number of result batches available with current query options | [optional] 
**current_page** | **bool, date, datetime, dict, float, int, list, str, none_type** | Index of current result page | [optional] 
**has_next** | **bool** | Whether there are any results in additional pages | [optional] 
**has_prev** | **bool** | Whether there are any results in previous pages | [optional] 
**next_skip** | **bool, date, datetime, dict, float, int, list, str, none_type** | Correct value of &#39;skip&#39; for the next page of results | [optional] 
**page_count** | **bool, date, datetime, dict, float, int, list, str, none_type** | Number of result pages available with current query options | [optional] 
**prev_skip** | **bool, date, datetime, dict, float, int, list, str, none_type** | Correct value of &#39;skip&#39; for the previous page of results | [optional] 
**records** | [**[CategorizedListItemModel]**](CategorizedListItemModel.md) | Query results | [optional] 
**severity** | [**Severity**](Severity.md) |  | [optional] 
**skip** | **bool, date, datetime, dict, float, int, list, str, none_type** | Number of records to skip before taking results | [optional] 
**sort_by** | [**[Sort]**](Sort.md) | List of sort properties | [optional] 
**success** | **bool** | Whether the query executed successfully | [optional] 
**take** | **bool, date, datetime, dict, float, int, list, str, none_type** | Maximum number of records to include in results | [optional] 
**total** | **bool, date, datetime, dict, float, int, list, str, none_type** | Total number of results available | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


