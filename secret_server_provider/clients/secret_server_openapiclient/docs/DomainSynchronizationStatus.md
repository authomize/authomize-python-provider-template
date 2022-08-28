# DomainSynchronizationStatus

Results of the last synchronization for this domain

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled_users** | **bool, date, datetime, dict, float, int, list, str, none_type** | Number of users that were disabled | [optional] 
**domain_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | Which domain is this status for | [optional] 
**domain_users_updated_since_last_synchronization** | **bool, date, datetime, dict, float, int, list, str, none_type** | Obsolete - Not populated. | [optional] 
**last_log_entry** | **bool, date, datetime, dict, float, int, list, str, none_type** | Log Entry used for parsing | [optional] 
**new_users_created** | **bool, date, datetime, dict, float, int, list, str, none_type** | Total new users that were created | [optional] 
**new_users_created_as_disabled** | **bool, date, datetime, dict, float, int, list, str, none_type** | Total new users that were created and then set as disabled due to either license limits or other settings | [optional] 
**users_removed_from_groups** | **bool, date, datetime, dict, float, int, list, str, none_type** | Total users removed from groups | [optional] 
**users_with_group_membership_changes** | **bool, date, datetime, dict, float, int, list, str, none_type** | Total number of users that were added or removed from any group in this domain | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


