# SearchIndexerModel

Configuration for Secret search indexer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days_to_keep_logs** | **int** | How many days to keep the logs for the search indexer | [optional] 
**enabled** | **bool** | Whether or not the search indexer is enabled | [optional] 
**indexing_separators** | **[str]** | Characters that split keys to be indexed | [optional] 
**index_mode** | [**SearchIndexMode**](SearchIndexMode.md) |  | [optional] 
**index_percent_complete** | **float** | The percent of the index that is built | [optional] 
**last_index_date** | **datetime** | The time of the last indexing | [optional] 
**log_available** | **bool** | Whether or not a log is available for the Secret Search Indexer | [optional] 
**status** | [**SearchIndexStatus**](SearchIndexStatus.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


