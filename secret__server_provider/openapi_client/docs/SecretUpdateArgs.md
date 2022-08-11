# SecretUpdateArgs

Secret update options

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The id of the Secret to update. Must match the {id} in the path. | 
**items** | [**[RestSecretItem]**](RestSecretItem.md) | A list of secret item field values. | 
**name** | **bool, date, datetime, dict, float, int, list, str, none_type** | The name to display for the secret. | 
**access_request_workflow_map_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The id of the mapping entity that associates this secret to a specific access request workflow. | [optional] 
**active** | **bool** | Whether the secret is in an active or deleted state. | [optional] 
**auto_change_enabled** | **bool** | Whether the secret’s password is automatically rotated on a schedule. | [optional] 
**auto_change_next_password** | **bool, date, datetime, dict, float, int, list, str, none_type** | Whether the secret should be flagged for immediate password change. | [optional] 
**check_out_change_password_enabled** | **bool** | Whether the secret’s password is automatically changed when a secret is checked in. This is a security feature that prevents a use of the password retrieved from check-out after the secret is checked in. | [optional] 
**check_out_enabled** | **bool** | Whether the user must check-out the secret to view it. Checking out gives the user exclusive access to the secret for a specified period or until the secret is checked in. | [optional] 
**check_out_interval_minutes** | **bool, date, datetime, dict, float, int, list, str, none_type** | The number of minutes that a secret will remain checked out. | [optional] 
**comment** | **bool, date, datetime, dict, float, int, list, str, none_type** | If the secret requires a comment to view or requires approval to view, a reason for accessing the secret must be provided. | [optional] 
**double_lock_password** | **bool, date, datetime, dict, float, int, list, str, none_type** | If the secret is DoubleLocked, this is the DoubleLock password needed to access the secret. | [optional] 
**enable_inherit_permissions** | **bool** | Whether the secret inherits permissions from the containing folder. | [optional] 
**enable_inherit_secret_policy** | **bool** | Whether the secret policy is inherited from the containing folder. | [optional] 
**folder_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | If the secret is contained in a folder, the id of the containing folder. Set to null or -1 for secrets that are in the root folder. | [optional] 
**force_check_in** | **bool** | Force the secret to be checked in, even if checked out by someone else. The user must have the \&quot;Force Check In\&quot; permission. | [optional] 
**include_inactive** | **bool** | If the secret is deactivated, this must be set to true in order to access the secret. The user must also have the \&quot;View Deleted Secrets\&quot; permission. | [optional] 
**launcher_connect_as_secret_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | When an SSH secret is proxied, you can choose to connect as another user and then do an su to the current secret’s user. This is a common practice for connecting with a lower privileged account and then switching to the root user. | [optional] 
**new_password** | **bool, date, datetime, dict, float, int, list, str, none_type** | New secret password. | [optional] 
**no_auto_checkout** | **bool** | Don&#39;t check out the secret automatically. | [optional] 
**password_type_web_script_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The id of the password change script to use on applicable web password secrets. | [optional] 
**proxy_enabled** | **bool** | Whether sessions launched on this secret use Secret Server’s proxying or connect directly. | [optional] 
**requires_comment** | **bool** | Whether the user must enter a comment to view the secret. | [optional] 
**secret_policy_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The id of the secret policy that controls the security and other settings of the secret. Set to null to not assign a secret policy. | [optional] 
**session_recording_enabled** | **bool** | Whether session recording is enabled. | [optional] 
**site_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The id of the distributed engine site that is used by this secret for operations such as password changing. | [optional] 
**ssh_key_args** | [**SshKeyArgs**](SshKeyArgs.md) |  | [optional] 
**ticket_number** | **bool, date, datetime, dict, float, int, list, str, none_type** | If the secret requires a comment to view or requires approval and a user must provide a help desk a ticket number, this is the ticket number to the help desk request. | [optional] 
**ticket_system_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | If the secret requires a comment to view or requires approval and a user must provide a help desk a ticket number, this is the id of the help desk system configured in Secret Server that should be used to validate the ticket number. | [optional] 
**web_launcher_requires_incognito_mode** | **bool** | Whether the web launcher will require the browser to run in incognito mode. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


