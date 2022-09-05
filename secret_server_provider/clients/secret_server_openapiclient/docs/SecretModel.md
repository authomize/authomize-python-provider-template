# SecretModel

Secret

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_request_workflow_map_id** | **int** | AccessRequestWorkflowMapId | [optional] 
**active** | **bool** | Whether the secret is active | [optional] 
**allow_owners_unrestricted_ssh_commands** | **bool** | AllowOwnersUnrestrictedSshCommands | [optional] 
**auto_change_enabled** | **bool** | AutoChangeEnabled | [optional] 
**auto_change_next_password** | **str** | AutoChangeNextPassword | [optional] 
**checked_out** | **bool** | Whether the secret is currently checked out | [optional] 
**check_out_change_password_enabled** | **bool** | CheckOutChangePasswordEnabled | [optional] 
**check_out_enabled** | **bool** | Whether secret checkout is enabled | [optional] 
**check_out_interval_minutes** | **int** | Checkout interval, in minutes | [optional] 
**check_out_minutes_remaining** | **int** | Minutes remaining in current checkout interval | [optional] 
**check_out_user_display_name** | **str** | Name of user who has checked out the secret | [optional] 
**check_out_user_id** | **int** | ID of user who has checked out the secret | [optional] 
**double_lock_id** | **int** | DoubleLockId | [optional] 
**enable_inherit_permissions** | **bool** | EnableInheritPermissions | [optional] 
**enable_inherit_secret_policy** | **bool** | Whether the secret policy is inherited from the containing folder | [optional] 
**failed_password_change_attempts** | **int** | Number of failed password change attempts | [optional] 
**folder_id** | **int** | Containing folder ID | [optional] 
**id** | **int** | Secret ID | [optional] 
**is_double_lock** | **bool** | Whether double lock is enabled | [optional] 
**is_out_of_sync** | **bool** | Out of sync indicates that a Password is setup for autochange and has failed its last password change attempt or has exceeded the maximum RPC attempts | [optional] 
**is_restricted** | **bool** | Whether the secret is restricted | [optional] 
**items** | [**[RestSecretItem]**](RestSecretItem.md) | Secret data fields | [optional] 
**jumpbox_route_id** | **str** | JumpboxRouteId | [optional] 
**last_heart_beat_check** | **datetime** | Time of last heartbeat check | [optional] 
**last_heart_beat_status** | [**HeartbeatStatus**](HeartbeatStatus.md) |  | [optional] 
**last_password_change_attempt** | **datetime** | Time of most recent password change attempt | [optional] 
**launcher_connect_as_secret_id** | **int** | LauncherConnectAsSecretId | [optional] 
**name** | **str** | Secret name | [optional] 
**out_of_sync_reason** | **str** | Reason message if the secret is out of sync | [optional] 
**password_type_web_script_id** | **int** | PasswordTypeWebScriptId | [optional] 
**proxy_enabled** | **bool** | ProxyEnabled | [optional] 
**requires_approval_for_access** | **bool** | RequiresApprovalForAccess | [optional] 
**requires_comment** | **bool** | RequiresComment | [optional] 
**response_codes** | **[str]** | ResponseCodes | [optional] 
**restrict_ssh_commands** | **bool** | RestrictSshCommands | [optional] 
**secret_policy_id** | **int** | SecretPolicyId | [optional] 
**secret_template_id** | **int** | Secret template ID | [optional] 
**secret_template_name** | **str** | Name of secret template | [optional] 
**session_recording_enabled** | **bool** | Whether session recording is enabled | [optional] 
**site_id** | **int** | SiteId | [optional] 
**web_launcher_requires_incognito_mode** | **bool** | WebLauncherRequiresIncognitoMode | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


