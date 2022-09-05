# IFolderModel

Describes the properties of a secret folder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**child_folders** | [**[IFolderModel]**](IFolderModel.md) | List of folders within this folder | [optional] 
**folder_name** | **str** | Folder name | [optional] 
**folder_path** | **str** | Path of this folder | [optional] 
**folder_type_id** | **int** | Folder type ID | [optional] 
**id** | **int** | Folder ID | [optional] 
**inherit_permissions** | **bool** | Whether the folder inherits permissions from its parent | [optional] 
**inherit_secret_policy** | **bool** | Whether the folder inherits the secret policy | [optional] 
**parent_folder_id** | **int** | Parent folder ID | [optional] 
**secret_policy_id** | **int** | Secret policy ID | [optional] 
**secret_templates** | [**[SecretTemplateSummary]**](SecretTemplateSummary.md) | Secret templates associated with this folder | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


