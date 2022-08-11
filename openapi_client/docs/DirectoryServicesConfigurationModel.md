# DirectoryServicesConfigurationModel

Directory Services Configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days_to_keep_operational_logs** | **bool, date, datetime, dict, float, int, list, str, none_type** | How long to keep operational logs | [optional] 
**disable_inactive_users_months** | **bool, date, datetime, dict, float, int, list, str, none_type** | How long to wait before disabling inactive users | [optional] 
**enable_directory_integration** | **bool** | Whether or not any Directory Services integrations are enabled or not | [optional] 
**enable_directory_synchronization** | **bool** | Synchronize users and group membership on a time interval | [optional] 
**enable_integrated_windows_authentication** | **bool** | Integrated Windows Authentication (IWA) allows users to log into Secret Server automatically if they are logged into a workstation with their Active Directory credentials. | [optional] 
**enable_user_disabling** | **bool** | When enabled inactive users will be automatically disabled regardless of their Directory status | [optional] 
**synchronization_interval_days** | **bool, date, datetime, dict, float, int, list, str, none_type** | Synchronize days interval for users and group membership | [optional] 
**synchronization_interval_hours** | **bool, date, datetime, dict, float, int, list, str, none_type** | Synchronize hours interval for users and group membership | [optional] 
**synchronization_interval_minutes** | **bool, date, datetime, dict, float, int, list, str, none_type** | Synchronize minutes interval for users and group membership | [optional] 
**user_account_options** | [**DirectoryServicesSynchronizationUserOption**](DirectoryServicesSynchronizationUserOption.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


