# SecretPolicyDetailModelV2

Secret Policy Detail Model V2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Indicates the policy is active | [optional] 
**affected_folder_count** | **int** | The count of total folders that would be affected by changing this policy | [optional] 
**affected_inheriting_folders_count** | **int** | The count of inherited secrets that would be affected by changing this policy | [optional] 
**affected_inheriting_secrets_count** | **int** | The count of inherited secrets that would be affected by changing this policy | [optional] 
**affected_secret_count** | **int** | The count of total secrets that would be affected by changing this policy | [optional] 
**general_items** | [**SecretPolicyGeneralItemsModel**](SecretPolicyGeneralItemsModel.md) |  | [optional] 
**launcher_items** | [**SecretPolicyLauncherItemsModel**](SecretPolicyLauncherItemsModel.md) |  | [optional] 
**rpc_items** | [**SecretPolicyRpcItemsModel**](SecretPolicyRpcItemsModel.md) |  | [optional] 
**secret_policy_description** | **str** | Secret Policy Description | [optional] 
**secret_policy_id** | **int** | Secret Policy Id | [optional] 
**secret_policy_name** | **str** | Secret Policy Name | [optional] 
**security_items** | [**SecretPolicySecurityItemsModel**](SecretPolicySecurityItemsModel.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


