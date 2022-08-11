# GroupUpdateArgs

Group update options

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **bool, date, datetime, dict, float, int, list, str, none_type** | Group ID. Must match ID in path | 
**ad_guid** | **bool, date, datetime, dict, float, int, list, str, none_type** | The Object GUID of the Active Directory Group (Hexadecimal) | [optional] 
**domain_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | Active Directory Domain ID | [optional] 
**enabled** | **bool** | Whether the group is active | [optional] 
**has_group_owners** | **bool** | If true, the group is owned by specific other users/groups. If false, if it is owned by Group Administrators. | [optional] 
**name** | **bool, date, datetime, dict, float, int, list, str, none_type** | Group name | [optional] 
**owner_group_ids** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | List of owner GroupIds. Only used if HasGroupOwners is true. | [optional] 
**owner_group_names** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | List of owner Group Names. Only used if HasGroupOwners is true. | [optional] 
**owner_user_ids** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | List of owner UserIds. Only used if HasGroupOwners is true. | [optional] 
**owner_user_names** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | List of owner Usernames. Only used if HasGroupOwners is true. | [optional] 
**synchronized** | **bool** | Whether the group is synchronized with Active Directory | [optional] 
**synchronize_now** | **bool** | Active Directory Sync will only pull in members for domain groups that have this set to true. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


