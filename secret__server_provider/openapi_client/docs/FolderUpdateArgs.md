# FolderUpdateArgs

Available options for updating a secret folder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | The name of the folder | 
**folder_type_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The icon to display for the folder. Depricated in latest UI. Use 1 when setting this value. | 
**id** | **bool, date, datetime, dict, float, int, list, str, none_type** | Folder ID. Must match ID in path | 
**inherit_permissions** | **bool** | Whether the folder should inherit permissions from its parent (default: true) | [optional] 
**inherit_secret_policy** | **bool** | Whether the folder should inherit the secret policy.  Defaults to true unless creating a root folder. | [optional] 
**parent_folder_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The ID of this folder&#39;s parent folder. | [optional] 
**secret_policy_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The id of the Secret Policy that sets security and other settings on secrets contained within the folder. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


