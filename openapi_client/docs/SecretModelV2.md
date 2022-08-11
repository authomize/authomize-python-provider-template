# SecretModelV2

Secret V2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_request_workflow_map_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | Access Request Workflow Map Id | [optional] 
**active** | **bool** | Whether the secret is active | [optional] 
**allow_owners_unrestricted_ssh_commands** | **bool** | Allow Owners Unrestricted SSH Commands | [optional] 
**auto_change_enabled** | **bool** | Auto Change Enabled | [optional] 
**auto_change_next_password** | **bool, date, datetime, dict, float, int, list, str, none_type** | Auto Change Next Password | [optional] 
**checked_out** | **bool** | Whether the secret is currently checked out | [optional] 
**check_out_change_password_enabled** | **bool** | Check Out Change Password Enabled | [optional] 
**check_out_enabled** | **bool** | Whether secret checkout is enabled | [optional] 
**check_out_interval_minutes** | **bool, date, datetime, dict, float, int, list, str, none_type** | Checkout interval, in minutes | [optional] 
**check_out_minutes_remaining** | **bool, date, datetime, dict, float, int, list, str, none_type** | Minutes remaining in current checkout interval | [optional] 
**check_out_user_display_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | Name of user who has checked out the secret | [optional] 
**check_out_user_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | ID of user who has checked out the secret | [optional] 
**double_lock_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | DoubleLock Id | [optional] 
**enable_inherit_permissions** | **bool** | Enable Inherit Permissions | [optional] 
**enable_inherit_secret_policy** | **bool** | Whether the secret policy is inherited from the containing folder | [optional] 
**failed_password_change_attempts** | **bool, date, datetime, dict, float, int, list, str, none_type** | Number of failed password change attempts | [optional] 
**folder_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | Containing folder ID | [optional] 
**id** | **bool, date, datetime, dict, float, int, list, str, none_type** | Secret ID | [optional] 
**is_double_lock** | **bool** | Whether double lock is enabled | [optional] 
**is_out_of_sync** | **bool** | Out of sync indicates that a Password is setup for autochange and has failed its last password change attempt or has exceeded the maximum RPC attempts | [optional] 
**is_restricted** | **bool** | Whether the secret is restricted | [optional] 
**items** | [**[RestSecretItem]**](RestSecretItem.md) | Secret data fields | [optional] 
**jumpbox_route_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | Jumpbox Route Id | [optional] 
**last_heart_beat_check** | **bool, date, datetime, dict, float, int, list, str, none_type** | Time of last heartbeat check | [optional] 
**last_heart_beat_status** | [**HeartbeatStatus**](HeartbeatStatus.md) |  | [optional] 
**last_password_change_attempt** | **bool, date, datetime, dict, float, int, list, str, none_type** | Time of most recent password change attempt | [optional] 
**launcher_connect_as_secret_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | LauncherConnectAsSecretId | [optional] 
**name** | **bool, date, datetime, dict, float, int, list, str, none_type** | Secret name | [optional] 
**out_of_sync_reason** | **bool, date, datetime, dict, float, int, list, str, none_type** | Reason message if the secret is out of sync | [optional] 
**password_type_web_script_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | Password Type Web Script Id | [optional] 
**proxy_enabled** | **bool** | Proxy Enabled | [optional] 
**requires_approval_for_access** | **bool** | Requires Approval For Access | [optional] 
**requires_comment** | **bool** | Requires Comment | [optional] 
**response_codes** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | Response Codes | [optional] 
**restrict_ssh_commands** | **bool** | Restrict SSH Commands | [optional] 
**secret_policy_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | Secret Policy Id | [optional] 
**secret_template_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | Secret template ID | [optional] 
**secret_template_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | Name of secret template | [optional] 
**session_recording_enabled** | **bool** | Whether session recording is enabled | [optional] 
**site_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | Site Id | [optional] 
**web_launcher_requires_incognito_mode** | **bool** | Web Launcher Requires Incognito Mode | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


