# DisasterRecoveryIncomingConfigurationModel

Disaster Recovery Configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_replica_name** | **str** | The data replica name given to it by the data source. | [optional] 
**data_replication_enabled** | **bool** | Whether data replication is enabled. | [optional] 
**data_replication_group_id** | **int** | The group all created secrets will be assigned to. | [optional] 
**data_source_key** | **str** | The data source key. | [optional] 
**data_source_url** | **str** | The data source URL. | [optional] 
**is_replica** | **bool** | Whether this instance of Secret Server is a data replica, a data source, or neither. | [optional] 
**is_replicating** | **bool** | Whether data replication is currently active. | [optional] 
**last_replicated** | **datetime** | The last time data replication ran. | [optional] 
**replication_interval_minutes** | **int** | How frequently data replication will take place on this data replica. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


