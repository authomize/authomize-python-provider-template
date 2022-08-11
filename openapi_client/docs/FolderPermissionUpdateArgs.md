# FolderPermissionUpdateArgs

Folder permission update options

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_access_role_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | Role to grant on the folder (View, Edit, Add Secret, Owner) | 
**folder_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | Folder ID | 
**id** | **bool, date, datetime, dict, float, int, list, str, none_type** | Folder permission ID. Must match ID in path | 
**break_inheritance** | **bool** | Allow updating of inherited permissions | [optional]  if omitted the server will use the default value of True
**secret_access_role_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | Role to grant on secrets in the folder (View, Edit, List, Owner, None) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


