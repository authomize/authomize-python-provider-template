# ConfigurationLocalUserPasswordsModel

Configuration Section for Local User Passwords

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_users_to_reset_forgotten_passwords** | **bool** | Whether or not the local password can be reset by the user | [optional] 
**enable_local_user_password_expiration** | **bool** | Indicates whether or not local users must change their password when it is reset or expires. | [optional] 
**enable_minimum_password_age** | **bool** | Local users cannot change their password until it meets this age | [optional] 
**enable_password_history** | **bool** | Passwords cannot be reused when enabled and still in stored history | [optional] 
**local_user_password_expiration_days** | **bool, date, datetime, dict, float, int, list, str, none_type** | How many days until the password expires | [optional] 
**local_user_password_expiration_hours** | **bool, date, datetime, dict, float, int, list, str, none_type** | How many hours until the password expires | [optional] 
**local_user_password_expiration_minutes** | **bool, date, datetime, dict, float, int, list, str, none_type** | How many minutes until the password expires | [optional] 
**minimum_password_age_days** | **bool, date, datetime, dict, float, int, list, str, none_type** | How many days until password can be changed | [optional] 
**minimum_password_age_hours** | **bool, date, datetime, dict, float, int, list, str, none_type** | How many hours until password can be changed | [optional] 
**minimum_password_age_minutes** | **bool, date, datetime, dict, float, int, list, str, none_type** | How many minutes until password can be changed | [optional] 
**password_history_items** | **bool, date, datetime, dict, float, int, list, str, none_type** | How many passwords should be stored in history. | [optional] 
**password_minimum_length** | **bool, date, datetime, dict, float, int, list, str, none_type** | The minimum length required for local user passwords | [optional] 
**password_require_lowercase** | **bool** | Whether or not the local password must include a lowercase letter | [optional] 
**password_require_numbers** | **bool** | Whether or not the local password must include a number | [optional] 
**password_require_symbols** | **bool** | Whether or not the local password must include a symbol | [optional] 
**password_require_uppercase** | **bool** | Whether or not the local password must include an uppercase letter | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


