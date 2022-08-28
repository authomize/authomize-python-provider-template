# ConfigurationUserExperienceModel

Configuration User Experience

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_language** | **int** | The default application language for users and the language for non-user specific tasks like logging when applicable | [optional] 
**checkout_notification_threshold** | **int** | Percentage of secret checkout time elapsed when checkout notification will be sent | [optional] 
**default_date_format** | **int** | The default date format that everyone sees unless they override with a user preference | [optional] 
**default_new_user_role_id** | **int** | The role that should be assigned when a new user is created | [optional] 
**default_time_format** | **int** | The default time format that everyone sees unless they override with a user preference | [optional] 
**enable_secret_check_out_extension** | **bool** | Enables users to extend secret check out sessions. | [optional] 
**force_inactivity_timeout** | **bool** | Logout users that are inactive | [optional] 
**force_inactivity_timeout_minutes** | **int** | Logout users that are inactive for this many minutes | [optional] 
**require_folder_for_secret** | **bool** | Secrets must be created within a folder | [optional] 
**search_delay_ms** | **int** | This controls the delay, in milliseconds, until the search is executed by the global search in the header.  If set to 0, it will require the user to press enter in the search bar. | [optional] 
**secret_password_history_restriction_all** | **bool** | No duplicate passwords on a Secret | [optional] 
**secret_password_history_restriction_count** | **int** | How many passwords must be unique on a Secret | [optional] 
**secret_view_interval_minutes** | **int** | How long entering comments to view a Secret last before being required again | [optional] 
**server_time_zone_id** | **str** | The timezone that the server shows by default and when job scheduling runs | [optional] 
**ui_inactivity_sleep_minutes** | **int** | How long until the UI will go inactive and stop polling for updates | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


