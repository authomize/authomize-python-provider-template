# SecretCreateArgs

Secret create options

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**[RestSecretItem]**](RestSecretItem.md) | An array of values for the secret fields defined in the secret template. | 
**name** | **bool, date, datetime, dict, float, int, list, str, none_type** | The name to display for the secret. | 
**secret_template_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The id of the secret template that defines the fields and properties of the secret. | 
**auto_change_enabled** | **bool** | Whether the secret’s password is automatically rotated on a schedule. | [optional] 
**check_out_change_password_enabled** | **bool** | Whether the secret’s password is automatically changed when a secret is checked in. This is a security feature that prevents a use of the password retrieved from check-out after the secret is checked in. | [optional] 
**check_out_enabled** | **bool** | Whether the user must check-out the secret to view it. Checking out gives the user exclusive access to the secret for a specified period or until the secret is checked in. | [optional] 
**check_out_interval_minutes** | **bool, date, datetime, dict, float, int, list, str, none_type** | The number of minutes that a secret will remain checked out. | [optional] 
**delay_indexing** | **bool** | Whether the search indexing should be delayed to the background process. This can speed up bulk secret creation scripts by offloading the task of indexing the new secrets to the background task at the trade-off of not having search indexes immediately available. | [optional] 
**enable_inherit_permissions** | **bool** | Whether the secret inherits permissions from the containing folder. | [optional] 
**enable_inherit_secret_policy** | **bool** | Whether the secret policy is inherited from the containing folder. | [optional] 
**folder_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | If the secret is contained in a folder, the id of the containing folder. Set to null or -1 for secrets that are in the root folder. | [optional] 
**launcher_connect_as_secret_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | When an SSH secret is proxied, you can choose to connect as another user and then do an su to the current secret’s user. This is a common practice for connecting with a lower privileged account and then switching to the root user. | [optional] 
**password_type_web_script_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The id of the password change script to use on applicable web password secrets. | [optional] 
**proxy_enabled** | **bool** | Whether sessions launched on this secret use Secret Server’s proxying or connect directly. | [optional] 
**requires_comment** | **bool** | Whether the user must enter a comment to view the secret. | [optional] 
**secret_policy_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The id of the secret policy that controls the security and other settings of the secret. Set to null to not assign a secret policy. | [optional] 
**session_recording_enabled** | **bool** | Whether session recording is enabled. | [optional] 
**site_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The id of the distributed engine site that is used by this secret for operations such as password changing. | [optional] 
**ssh_key_args** | [**SshKeyArgs**](SshKeyArgs.md) |  | [optional] 
**web_launcher_requires_incognito_mode** | **bool** | Whether the web launcher will require the browser to run in incognito mode. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


