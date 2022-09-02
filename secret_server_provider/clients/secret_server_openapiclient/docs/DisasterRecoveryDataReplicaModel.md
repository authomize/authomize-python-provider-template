# DisasterRecoveryDataReplicaModel

Disaster Recovery Data Replica

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Any error that occurred on the last data replication with this data replica. | [optional] 
**folders** | [**[FolderSimpleModel]**](FolderSimpleModel.md) | The folders to be replicated, default is all folders. | [optional] 
**id** | **str** | The data replica ID. | [optional] 
**is_replicating** | **bool** | Whether data replication is currently active for this data replica. | [optional] 
**last_replicated** | **datetime** | The last time data replication was requested by this data replica. | [optional] 
**location** | **str** | The location of the data replica. | [optional] 
**name** | **str** | The name of the data replica. | [optional] 
**status** | [**DisasterRecoveryDataReplicaStatus**](DisasterRecoveryDataReplicaStatus.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


