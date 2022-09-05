# SecretDetailSecurityModel

Secret Detail Security

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_owners_unrestricted_ssh_commands** | **bool** | Allow Owners Unrestricted SSH Commands | [optional] 
**approval_workflow** | [**WorkflowTemplate**](WorkflowTemplate.md) |  | [optional] 
**approvers** | [**[SecretDetailUserViewModel]**](SecretDetailUserViewModel.md) | Approvers | [optional] 
**check_out_change_password_enabled** | **bool** | Check Out Change Password Enabled | [optional] 
**check_out_default_interval_display** | **str** | Check Out Default Interval Display | [optional] 
**check_out_enabled** | **bool** | Whether secret checkout is enabled | [optional] 
**check_out_interval_display** | **str** | Check Out Interval Display | [optional] 
**check_out_interval_minutes** | **int** | Checkout interval, in minutes | [optional] 
**command_restriction_type** | [**CommandRestrictionType**](CommandRestrictionType.md) |  | [optional] 
**double_lock_id** | **int** | DoubleLock Id | [optional] 
**double_lock_name** | **str** | DoubleLock Name | [optional] 
**hide_launcher_password** | **bool** | Hide Launcher Password | [optional] 
**is_double_lock** | **bool** | Whether double lock is enabled | [optional] 
**password_requirements** | [**SecretDetailSecurityPasswordRequirements**](SecretDetailSecurityPasswordRequirements.md) |  | [optional] 
**proxy_enabled** | **bool** | Proxy Enabled | [optional] 
**require_approval_type** | [**SecretDetailApprovalType**](SecretDetailApprovalType.md) |  | [optional] 
**requires_comment** | **bool** | Requires Comment | [optional] 
**restricted_ssh_command_count** | **int** | Restricted SSH Command Count | [optional] 
**restrict_ssh_commands** | **bool** | Restrict SSH Commands | [optional] 
**session_recording_enabled** | **bool** | Whether session recording is enabled | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


