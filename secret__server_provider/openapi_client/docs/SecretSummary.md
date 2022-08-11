# SecretSummary

Secret summary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Whether the secret is active | [optional] 
**auto_change_enabled** | **bool** | Indicates whether or not this Secret an auto changing password | [optional] 
**checked_out** | **bool** | Whether the secret is currently checked out | [optional] 
**check_out_enabled** | **bool** | Indicates whether or not checkout is enabled for the Secret | [optional] 
**create_date** | **bool, date, datetime, dict, float, int, list, str, none_type** | When the Secret was created | [optional] 
**days_until_expiration** | **bool, date, datetime, dict, float, int, list, str, none_type** | How many days until this Secret expires | [optional] 
**double_lock_enabled** | **bool** | Indicates whether or not DoubleLock is enabled for this password | [optional] 
**extended_fields** | [**[ISecretSummaryExtendedField]**](ISecretSummaryExtendedField.md) | Any requested extended fields from a lookup request | [optional] 
**folder_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | Containing folder ID | [optional] 
**has_launcher** | **bool** | Indicates if this Secret has any launchers | [optional] 
**hide_password** | **bool** | Indicates if the launcher password is set to be hidden | [optional] 
**id** | **bool, date, datetime, dict, float, int, list, str, none_type** | Secret ID | [optional] 
**inherits_permissions** | **bool** | Indicates if this Secret inherits permissions from its folder | [optional] 
**is_out_of_sync** | **bool** | Out of sync indicates that a Password is setup for autochange and has failed its last password change attempt or has exceeded the maximum RPC attempts | [optional] 
**is_restricted** | **bool** | Whether the secret is restricted | [optional] 
**last_accessed** | **bool, date, datetime, dict, float, int, list, str, none_type** | When the Secret was last viewed, only populated when scope is Recent | [optional] 
**last_heart_beat_status** | [**HeartbeatStatus**](HeartbeatStatus.md) |  | [optional] 
**last_password_change_attempt** | **bool, date, datetime, dict, float, int, list, str, none_type** | Time of most recent password change attempt | [optional] 
**name** | **bool, date, datetime, dict, float, int, list, str, none_type** | Secret name | [optional] 
**out_of_sync_reason** | **bool, date, datetime, dict, float, int, list, str, none_type** | Reason message if the secret is out of sync | [optional] 
**requires_approval** | **bool** | Indicates if this Secret requires approval | [optional] 
**requires_comment** | **bool** | Indicates if this Secret requires comment | [optional] 
**response_codes** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | ResponseCodes | [optional] 
**secret_template_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | Secret template ID | [optional] 
**secret_template_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | Name of secret template | [optional] 
**site_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | SiteId | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


