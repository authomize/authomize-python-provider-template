# DiscoveryConfigurationModel

DiscoveryConfigurationModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discovery_interval_days** | **int** | Synchronize days interval for Discovery | [optional] 
**discovery_interval_hours** | **int** | Synchronize hours interval for Discovery | [optional] 
**discovery_scan_offset_hours** | **int** | Sets time offset in hours for discovery scan operations. Default value: 0 | [optional] 
**enable_discovery** | **bool** | Whether or not discovery is enabled | [optional] 
**engine_ad_discovery_batch_size** | **int** | The size of the batch for Active Directory Account engine scanning - set higher if engine takes too much time to process. Default value: 1 | [optional] 
**ignore_cluster_node_objects** | **bool** | If set to true, Discovery scans will bypass machines identified as &#39;msclustervirtualserver.&#39; Default value: False | [optional] 
**max_log_age_days** | **int** | How long to keep logs | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


