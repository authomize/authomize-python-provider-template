# FolderPermissionCreateArgs

FolderPermissionCreateArgs

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**break_inheritance** | **bool** | Allow updating of inherited permissions | [optional]  if omitted the server will use the default value of True
**folder_access_role_name** | **str** | Role to grant on the folder (View, Edit, Add Secret, Owner) | [optional] 
**folder_id** | **int** | Folder on which to grant permissions | [optional] 
**group_id** | **int** | Group to receive permissions | [optional] 
**secret_access_role_name** | **str** | Role to grant on secrets in the folder (View, Edit, List, Owner, None) | [optional] 
**user_id** | **int** | User to receive permissions | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


