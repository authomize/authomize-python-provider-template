# DiscoveryStatusModel

DiscoveryStatusModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**[DiscoveryActionType]**](DiscoveryActionType.md) | Actions the current user can perform for Discovery | [optional] 
**discovery_computer_scan_end_date_time** | **bool, date, datetime, dict, float, int, list, str, none_type** | The date and time the Scan Computer messages completed queueing last. | [optional] 
**discovery_computer_scan_start_date_time** | **bool, date, datetime, dict, float, int, list, str, none_type** | The date and time Scan Computer messages last started. | [optional] 
**discovery_fetch_end_date_time** | **bool, date, datetime, dict, float, int, list, str, none_type** | The date and time the Host Range and Machine fetching last completed.  This will be empty if a synchronization has never been run. | [optional] 
**discovery_fetch_start_date_time** | **bool, date, datetime, dict, float, int, list, str, none_type** | The date and time the Host Range and Machine fetching was last run or started.  This will be empty if a synchronization has never been run. | [optional] 
**discovery_source_count** | **bool, date, datetime, dict, float, int, list, str, none_type** | Total number of discovery sources either active or inactive | [optional] 
**is_discovery_computer_scan_running** | **bool** | Indicates if computer scanning is actively queueing. | [optional] 
**is_discovery_enabled** | **bool** | Indicates if Discovery is currently enabled | [optional] 
**is_discovery_fetch_running** | **bool** | Indicates if the Host Range and Machine fetching is currently running. | [optional] 
**next_computer_scan_discovery_date_time** | **bool, date, datetime, dict, float, int, list, str, none_type** | The next time computer scanning is expected to run | [optional] 
**next_fetch_discovery_date_time** | **bool, date, datetime, dict, float, int, list, str, none_type** | The next time the Host Range and Machine fetching is expected to run | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


