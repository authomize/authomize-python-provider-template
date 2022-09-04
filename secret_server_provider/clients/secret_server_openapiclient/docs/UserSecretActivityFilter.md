# UserSecretActivityFilter

Filter which secrets that had activity to include

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **datetime** | Include secrets accessed before this date.  Can be null which will not filter by any end date and results in today basically. | [optional] 
**exclude_inactive_secrets** | **bool** | Exclude any inactive secrets | [optional] 
**exclude_rotated_secrets** | **bool** | Exclude any secrets that rotate | [optional] 
**folder_id** | **int** | Only include secrets in a specific folder.  Exclude or pass null to include all secrets | [optional] 
**include_subfolders** | **bool** | Only used if a FolderId is included and when true it will also search subfolders.  When false only secrets from the passed FolderId will be returned. | [optional] 
**start_date** | **datetime** | Include any Secrets access since this date | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


