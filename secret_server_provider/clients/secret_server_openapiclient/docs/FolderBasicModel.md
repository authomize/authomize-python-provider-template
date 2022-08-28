# FolderBasicModel

FolderBasicModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_templates** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | Allowed Templates | [optional] 
**enable_inherit_permissions** | **bool** | Should the folder inherit permissions from the parent folder | [optional] 
**enable_inherit_secret_policy** | **bool** | Should the folder inherit the secret policy from the parent folder | [optional] 
**folder_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | The dispay name for the folder | [optional] 
**has_edit** | **bool** | If the user can edit the folder | [optional] 
**has_owner** | **bool** | If the user owns the folder | [optional] 
**is_personal_folder** | **bool** | Whether or not this is a personal folder | [optional] 
**parent_folder_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The ID of the parent folder | [optional] 
**parent_folder_policy_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | Policy name on the parent folder | [optional] 
**secret_policies** | [**[SecretPolicyModel]**](SecretPolicyModel.md) | SecretPolicies | [optional] 
**secret_policy** | **bool, date, datetime, dict, float, int, list, str, none_type** | The secret policy ID that is assigned to the folder | [optional] 
**secret_templates** | [**[TemplateViewModel]**](TemplateViewModel.md) | Secret Templates | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


