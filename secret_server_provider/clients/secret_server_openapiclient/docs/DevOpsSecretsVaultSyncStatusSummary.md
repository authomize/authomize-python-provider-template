# DevOpsSecretsVaultSyncStatusSummary

Query results

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | If the mapping is active. | [optional] 
**date_added** | **datetime** | When the Secret will be pushed next. | [optional] 
**dev_ops_secret_vault_path** | **str** | Where to push the Secret to in the Tenant. | [optional] 
**dev_ops_sync_map_id** | **int** | ID of the mapping between the Tenant and Secret. | [optional] 
**last_sync_time** | **datetime** | When the Secret was last pushed. | [optional] 
**secret_name** | **str** | Name of the Secret. | [optional] 
**status** | **str** | Status of syncing progress. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


