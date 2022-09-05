# DomainSynchronizationStatus

Results of the last synchronization for this domain

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled_users** | **int** | Number of users that were disabled | [optional] 
**domain_id** | **int** | Which domain is this status for | [optional] 
**domain_users_updated_since_last_synchronization** | **int** | Obsolete - Not populated. | [optional] 
**last_log_entry** | **str** | Log Entry used for parsing | [optional] 
**new_users_created** | **int** | Total new users that were created | [optional] 
**new_users_created_as_disabled** | **int** | Total new users that were created and then set as disabled due to either license limits or other settings | [optional] 
**users_removed_from_groups** | **int** | Total users removed from groups | [optional] 
**users_with_group_membership_changes** | **int** | Total number of users that were added or removed from any group in this domain | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


