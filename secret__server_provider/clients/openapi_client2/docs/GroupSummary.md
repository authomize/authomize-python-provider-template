# GroupSummary

Group summary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Created Date | [optional] 
**domain_guid** | **str** | If this a synchronized group and the user requesting access has access this will be populated with the unique guid for the directory with a group search. | [optional] 
**domain_id** | **int** | Active Directory domain ID | [optional] 
**domain_name** | **str** | Active Directory domain name | [optional] 
**enabled** | **bool** | Whether the group is active | [optional] 
**id** | **int** | Group ID | [optional] 
**is_platform** | **bool** | If this is synchronized with Platform | [optional] 
**member_count** | **int** | Number of members in group | [optional] 
**name** | **str** | Group name | [optional] 
**synchronized** | **bool** | Whether the group is synchronized with Active Directory | [optional] 
**synchronize_now** | **bool** | Active Directory Sync will only pull in members for domain groups that have this set to true. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


