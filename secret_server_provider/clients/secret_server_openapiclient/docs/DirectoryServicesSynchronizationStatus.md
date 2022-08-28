# DirectoryServicesSynchronizationStatus

Directory Synchronization Status

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_status** | [**[DomainSynchronizationStatus]**](DomainSynchronizationStatus.md) | Results from the last synchronization for each domain.  If a synchronization is currently running this will indicate the results for the last synchronization and not the current running totals. | [optional] 
**end_date_time** | **bool, date, datetime, dict, float, int, list, str, none_type** | The date and time that the last synchronization ended.  If a synchronization is currently running this will be empty. | [optional] 
**error_count** | **bool, date, datetime, dict, float, int, list, str, none_type** | The number of errors since the last synchronization start time | [optional] 
**estimated_percent_complete** | **bool, date, datetime, dict, float, int, list, str, none_type** | Based on last run time duration the percent complete assumes each run takes approximately the same amount of time | [optional] 
**next_synchronization_date_time** | **bool, date, datetime, dict, float, int, list, str, none_type** | The next time the synchronization is expected to run | [optional] 
**start_date_time** | **bool, date, datetime, dict, float, int, list, str, none_type** | The date and time that the last synchronization started.  This will be empty if a synchronization has never been run. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


