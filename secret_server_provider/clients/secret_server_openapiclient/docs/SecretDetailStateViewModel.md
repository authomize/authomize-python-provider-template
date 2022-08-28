# SecretDetailStateViewModel

Secret Detail State View Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**[SecretDetailActionType]**](SecretDetailActionType.md) | Allowed action for current user | [optional] 
**approval_end** | **bool, date, datetime, dict, float, int, list, str, none_type** | Date when the current approval expires, or null if there is no open approval | [optional] 
**available_actions** | [**SecretDetailStateActionsModel**](SecretDetailStateActionsModel.md) |  | [optional] 
**checked_out_user_display_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | Display Name of User that has the secret checked out | [optional] 
**checked_out_user_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | User Secret is checked out to | [optional] 
**check_out_interval_minutes** | **bool, date, datetime, dict, float, int, list, str, none_type** | Number of minutes before checkout  | [optional] 
**check_out_minutes_remaining** | **bool, date, datetime, dict, float, int, list, str, none_type** | Minutes remaining in check out | [optional] 
**folder_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | Folder Id | [optional] 
**folder_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | Folder Name | [optional] 
**id** | **bool, date, datetime, dict, float, int, list, str, none_type** | Secret Id | [optional] 
**is_active** | **bool** | Active indicator | [optional] 
**is_checked_out** | **bool** | Is the Secret checked out | [optional] 
**is_checked_out_by_current_user** | **bool** | Indicates whether the Secret is checked out by the current user | [optional] 
**password_change_pending** | **bool** | Pending Password change on secret indicator | [optional] 
**remaining_time_warning_minute_marker** | **bool, date, datetime, dict, float, int, list, str, none_type** | Minute mark to show check out warning | [optional] 
**role** | **bool, date, datetime, dict, float, int, list, str, none_type** | Role that current user has on Secret | [optional] 
**secret_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | Secret Name | [optional] 
**secret_state** | [**SecretAccessRequired**](SecretAccessRequired.md) |  | [optional] 
**warning_minutes_remaining** | **bool, date, datetime, dict, float, int, list, str, none_type** | Minutes remaining before showing check in warning | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


