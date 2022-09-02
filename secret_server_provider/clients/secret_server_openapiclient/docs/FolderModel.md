# FolderModel

Describes the properties of a secret folder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**child_folders** | [**[IFolderModel]**](IFolderModel.md) | List of folders within this folder | [optional] 
**folder_name** | **str** | The name of the folder. | [optional] 
**folder_path** | **str** | The path of all folders and subfolders beginning at the root anterminating at this folder. | [optional] 
**folder_type_id** | **int** | The icon to display for the folder. Depricated in latest UI. Use 1 when setting this value. | [optional] 
**id** | **int** | Folder ID | [optional] 
**inherit_permissions** | **bool** | Whether the folder should inherit permissions from its parent (default: true) | [optional] 
**inherit_secret_policy** | **bool** | Whether the folder should inherit the secret policy.  Defaults to true unless creating a root folder. | [optional] 
**parent_folder_id** | **int** | The ID of this folder&#39;s parent folder. | [optional] 
**secret_policy_id** | **int** | The id of the Secret Policy that sets security and other settings on secrets contained within the folder. | [optional] 
**secret_templates** | [**[SecretTemplateSummary]**](SecretTemplateSummary.md) | List of templates that may be used to create secrets in this folder | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


