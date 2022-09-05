# GroupCreateArgs

Group create options

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether the group is active | 
**name** | **str** | Group name | 
**ad_guid** | **str** | The Object GUID of the Active Directory Group (Hexadecimal) | [optional] 
**domain_id** | **int** | Active Directory Domain ID | [optional] 
**has_group_owners** | **bool** | If true, the group is owned by specific other users/groups. If false, if it is owned by Group Administrators. | [optional] 
**is_platform** | **bool** | Whether the group is a Platform Group | [optional] 
**owner_group_ids** | **[int]** | List of owner GroupIds. Only used if HasGroupOwners is true. | [optional] 
**owner_group_names** | **[str]** | List of owner Group Names. Only used if HasGroupOwners is true. | [optional] 
**owner_user_ids** | **[int]** | List of owner UserIds. Only used if HasGroupOwners is true. | [optional] 
**owner_user_names** | **[str]** | List of owner Usernames. Only used if HasGroupOwners is true. | [optional] 
**synchronized** | **bool** | Whether the group is synchronized with Active Directory | [optional] 
**synchronize_now** | **bool** | Active Directory Sync will only pull in members for domain groups that have this set to true. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


