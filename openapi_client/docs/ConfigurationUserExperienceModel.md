# ConfigurationUserExperienceModel

Configuration User Experience

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_language** | **bool, date, datetime, dict, float, int, list, str, none_type** | The default application language for users and the language for non-user specific tasks like logging when applicable | [optional] 
**checkout_notification_threshold** | **bool, date, datetime, dict, float, int, list, str, none_type** | Percentage of secret checkout time elapsed when checkout notification will be sent | [optional] 
**default_date_format** | **bool, date, datetime, dict, float, int, list, str, none_type** | The default date format that everyone sees unless they override with a user preference | [optional] 
**default_new_user_role_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The role that should be assigned when a new user is created | [optional] 
**default_time_format** | **bool, date, datetime, dict, float, int, list, str, none_type** | The default time format that everyone sees unless they override with a user preference | [optional] 
**enable_secret_check_out_extension** | **bool** | Enables users to extend secret check out sessions. | [optional] 
**force_inactivity_timeout** | **bool** | Logout users that are inactive | [optional] 
**force_inactivity_timeout_minutes** | **bool, date, datetime, dict, float, int, list, str, none_type** | Logout users that are inactive for this many minutes | [optional] 
**require_folder_for_secret** | **bool** | Secrets must be created within a folder | [optional] 
**search_delay_ms** | **bool, date, datetime, dict, float, int, list, str, none_type** | This controls the delay, in milliseconds, until the search is executed by the global search in the header.  If set to 0, it will require the user to press enter in the search bar. | [optional] 
**secret_password_history_restriction_all** | **bool** | No duplicate passwords on a Secret | [optional] 
**secret_password_history_restriction_count** | **bool, date, datetime, dict, float, int, list, str, none_type** | How many passwords must be unique on a Secret | [optional] 
**secret_view_interval_minutes** | **bool, date, datetime, dict, float, int, list, str, none_type** | How long entering comments to view a Secret last before being required again | [optional] 
**server_time_zone_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The timezone that the server shows by default and when job scheduling runs | [optional] 
**ui_inactivity_sleep_minutes** | **bool, date, datetime, dict, float, int, list, str, none_type** | How long until the UI will go inactive and stop polling for updates | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


