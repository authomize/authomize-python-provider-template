# DisasterRecoveryOutgoingConfigurationModel

Disaster Recovery Data Replicas

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_package_storage_path** | **bool, date, datetime, dict, float, int, list, str, none_type** | The location of where data replication files are stored temporarily on the data source. | [optional] 
**data_replicas** | [**[DisasterRecoveryDataReplicaModel]**](DisasterRecoveryDataReplicaModel.md) | The data replicas registered with this data source. | [optional] 
**data_source_key** | **bool, date, datetime, dict, float, int, list, str, none_type** | The data source key a data replica should use when enabling data replication. | [optional] 
**data_source_url** | **bool, date, datetime, dict, float, int, list, str, none_type** | The data source URL a data replica should use when enabling data replication. | [optional] 
**is_data_package_storage_path_valid** | **bool** | Whether the data package storage location is valid and ready for use. | [optional] 
**is_replica** | **bool** | Whether this instance of Secret Server is a data replica, a data source, or neither. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


