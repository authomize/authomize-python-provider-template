# SecretPolicySecurityItemsCreateModel

Secret Policy Security Item Create Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_owners_unrestricted_ssh_commands** | [**SecretPolicyDataItemOfOptionalBoolean**](SecretPolicyDataItemOfOptionalBoolean.md) |  | [optional] 
**approval_groups** | [**SecretPolicyDataItemOfUserGroupMapDataModelArray**](SecretPolicyDataItemOfUserGroupMapDataModelArray.md) |  | [optional] 
**approval_workflow** | [**SecretPolicyDataItemOfOptionalInt32**](SecretPolicyDataItemOfOptionalInt32.md) |  | [optional] 
**check_out_change_password** | [**SecretPolicyDataItemOfOptionalBoolean**](SecretPolicyDataItemOfOptionalBoolean.md) |  | [optional] 
**check_out_enabled** | [**SecretPolicyDataItemOfOptionalBoolean**](SecretPolicyDataItemOfOptionalBoolean.md) |  | [optional] 
**check_out_interval_minutes** | [**SecretPolicyDataItemOfOptionalInt32**](SecretPolicyDataItemOfOptionalInt32.md) |  | [optional] 
**enable_ssh_command_restrictions** | [**SecretPolicyDataItemOfOptionalBoolean**](SecretPolicyDataItemOfOptionalBoolean.md) |  | [optional] 
**event_pipeline_policy** | [**SecretPolicyDataItemOfOptionalInt32**](SecretPolicyDataItemOfOptionalInt32.md) |  | [optional] 
**hide_launcher_password** | [**SecretPolicyDataItemOfOptionalBoolean**](SecretPolicyDataItemOfOptionalBoolean.md) |  | [optional] 
**is_proxy_enabled** | [**SecretPolicyDataItemOfOptionalBoolean**](SecretPolicyDataItemOfOptionalBoolean.md) |  | [optional] 
**is_session_recording_enabled** | [**SecretPolicyDataItemOfOptionalBoolean**](SecretPolicyDataItemOfOptionalBoolean.md) |  | [optional] 
**require_approval_for_access** | [**SecretPolicyDataItemOfOptionalBoolean**](SecretPolicyDataItemOfOptionalBoolean.md) |  | [optional] 
**require_approval_for_access_for_editors** | [**SecretPolicyDataItemOfOptionalBoolean**](SecretPolicyDataItemOfOptionalBoolean.md) |  | [optional] 
**require_approval_for_access_for_owners_and_approvers** | [**SecretPolicyDataItemOfOptionalBoolean**](SecretPolicyDataItemOfOptionalBoolean.md) |  | [optional] 
**require_view_comment** | [**SecretPolicyDataItemOfOptionalBoolean**](SecretPolicyDataItemOfOptionalBoolean.md) |  | [optional] 
**run_launcher_using_ssh_key_secret_id** | [**SecretPolicyDataItemOfOptionalInt32**](SecretPolicyDataItemOfOptionalInt32.md) |  | [optional] 
**ssh_command_blocklist_editors** | [**SecretPolicyDataItemOfOptionalGuid**](SecretPolicyDataItemOfOptionalGuid.md) |  | [optional] 
**ssh_command_blocklist_owners** | [**SecretPolicyDataItemOfOptionalGuid**](SecretPolicyDataItemOfOptionalGuid.md) |  | [optional] 
**ssh_command_blocklist_viewers** | [**SecretPolicyDataItemOfOptionalGuid**](SecretPolicyDataItemOfOptionalGuid.md) |  | [optional] 
**ssh_command_menu_groups** | [**SecretPolicyDataItemOfSshCommandMenuGroupModelArray**](SecretPolicyDataItemOfSshCommandMenuGroupModelArray.md) |  | [optional] 
**ssh_command_restriction_type** | [**SecretPolicyDataItemOfOptionalCommandRestrictionType**](SecretPolicyDataItemOfOptionalCommandRestrictionType.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


