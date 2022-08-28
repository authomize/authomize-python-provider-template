# PlatformSynchronizationStatus

Platform Synchronization Status

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date_time** | **datetime** | The date and time that the last synchronization ended.  If a synchronization is currently running this will be empty. | [optional] 
**error_count** | **int** | The number of errors since the last synchronization start time | [optional] 
**last_log_entry** | **str** | Log Entry used for parsing | [optional] 
**last_sync_groups_created** | **int** | Number of groups created during last sync | [optional] 
**last_sync_users_added_to_groups** | **int** | Number of users that were added to any platform group | [optional] 
**last_sync_users_removed_from_groups** | **int** | Number of users that were removed from any platform group | [optional] 
**next_synchronization_date_time** | **datetime** | The next time the synchronization is expected to run | [optional] 
**start_date_time** | **datetime** | The date and time that the last synchronization started.  This will be empty if a synchronization has never been run. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


