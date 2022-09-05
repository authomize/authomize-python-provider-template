# SecretDetailStateViewModel

Secret Detail State View Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**[SecretDetailActionType]**](SecretDetailActionType.md) | Allowed action for current user | [optional] 
**approval_end** | **datetime** | Date when the current approval expires, or null if there is no open approval | [optional] 
**available_actions** | [**SecretDetailStateActionsModel**](SecretDetailStateActionsModel.md) |  | [optional] 
**checked_out_user_display_name** | **str** | Display Name of User that has the secret checked out | [optional] 
**checked_out_user_id** | **int** | User Secret is checked out to | [optional] 
**check_out_interval_minutes** | **int** | Number of minutes before checkout  | [optional] 
**check_out_minutes_remaining** | **int** | Minutes remaining in check out | [optional] 
**folder_id** | **int** | Folder Id | [optional] 
**folder_name** | **str** | Folder Name | [optional] 
**id** | **int** | Secret Id | [optional] 
**is_active** | **bool** | Active indicator | [optional] 
**is_checked_out** | **bool** | Is the Secret checked out | [optional] 
**is_checked_out_by_current_user** | **bool** | Indicates whether the Secret is checked out by the current user | [optional] 
**password_change_pending** | **bool** | Pending Password change on secret indicator | [optional] 
**remaining_time_warning_minute_marker** | **int** | Minute mark to show check out warning | [optional] 
**role** | **str** | Role that current user has on Secret | [optional] 
**secret_name** | **str** | Secret Name | [optional] 
**secret_state** | [**SecretAccessRequired**](SecretAccessRequired.md) |  | [optional] 
**warning_minutes_remaining** | **int** | Minutes remaining before showing check in warning | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


