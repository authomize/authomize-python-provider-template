# DevOpsSecretsVaultTenantSummary

Query results

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | If this Tenant should be pushed to. | [optional] 
**date_added** | **datetime** | When the Tenant was added to Secret Server. | [optional] 
**dsv_tenant_id** | **int** | Tenant ID. | [optional] 
**last_synced** | **datetime** | The last time the Sync Interval expired. | [optional] 
**secret_name** | **str** | The Secret in which to connect to DSV. | [optional] 
**sync_interval** | **int** | How often to check if secrets need to be pushed to the Tenant. | [optional] 
**tenant_name** | **str** | Tenant Name. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


