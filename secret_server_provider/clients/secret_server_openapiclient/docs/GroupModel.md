# GroupModel

Group

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_guid** | **bool, date, datetime, dict, float, int, list, str, none_type** | Active Directory unique identifier | [optional] 
**can_edit_members** | **bool** | Whether you can edit the members of this group.  For example, Directory Services group members cannot be edited.  Populated on a single group get. | [optional] 
**created** | **bool, date, datetime, dict, float, int, list, str, none_type** | Group created date | [optional] 
**domain_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | Active Directory Domain ID | [optional] 
**domain_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | Active Directory domain name | [optional] 
**enabled** | **bool** | Whether the group is active | [optional] 
**has_group_owners** | **bool** | If true, the group is owned by specific other users/groups. If false, if it is owned by Group Administrators. | [optional] 
**id** | **bool, date, datetime, dict, float, int, list, str, none_type** | Group ID | [optional] 
**ip_address_restrictions** | [**[GroupIpAddressRestrictionSummaryModel]**](GroupIpAddressRestrictionSummaryModel.md) | Array of IP Address Restrictions for the group. | [optional] 
**is_editable** | **bool** | Whether you have permission to edit this group | [optional] 
**is_platform** | **bool** | Whether the group is a Platform Group | [optional] 
**name** | **bool, date, datetime, dict, float, int, list, str, none_type** | Group name | [optional] 
**owner_groups** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Hash of GroupIds and GroupNames that own this group. Only used if HasGroupOwners is true. | [optional] 
**owners** | [**[GroupOwner]**](GroupOwner.md) | The owners for the group, both users and groups | [optional] 
**owner_users** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Hash of GroupIds and GroupNames that own this group. Only used if HasGroupOwners is true. | [optional] 
**synchronized** | **bool** | Whether the group is synchronized with Active Directory | [optional] 
**synchronize_now** | **bool** | Active Directory Sync will only pull in members for domain groups that have this set to true. | [optional] 
**system_group** | **bool** | Whether the group is an Active Directory system group | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


