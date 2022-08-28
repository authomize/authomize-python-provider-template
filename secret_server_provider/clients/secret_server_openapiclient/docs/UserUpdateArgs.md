# UserUpdateArgs

User update options

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_option_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The id of the date format to use when displaying dates to this user. These options are defined in Admin &gt; Configuration. | [optional] 
**display_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | The user’s name as displayed in the user interface. | [optional] 
**duo_two_factor** | **bool** | Whether Duo two-factor authentication is enabled. | [optional] 
**email_address** | **bool, date, datetime, dict, float, int, list, str, none_type** | The user&#39;s email address. Used by the system to send reports, access requests, and other notifications. | [optional] 
**enabled** | **bool** | Whether the user account is enabled. Disabled users are unable to log in and do not consume a user license. | [optional] 
**fido2_two_factor** | **bool** | Whether FIDO2 two-factor authentication is enabled. | [optional] 
**group_owners** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | A list of group ids for the groups that can manage this user. If not set, the user is managed by all users with the ‘Administer Users’ role permission. | [optional] 
**id** | **bool, date, datetime, dict, float, int, list, str, none_type** | User ID. Must match ID in path. | [optional] 
**is_application_account** | **bool** | Whether this is an application account. Application accounts are used for automation, cannot log in using the UI, and do not consume a user license. | [optional] 
**is_group_owner_update** | **bool** | Whether the user is managed by the groups specified in GroupOwners or is managed by all users with the ‘Administer Users’ role permission. | [optional] 
**is_locked_out** | **bool** | Whether the user is locked out. A locked out user cannot log in. | [optional] 
**login_failures** | **bool, date, datetime, dict, float, int, list, str, none_type** | Number of login failures to allow before the account is locked out. Set to 0 for unlimited login attempts. | [optional] 
**oath_two_factor** | **bool** | Whether OATH two-factor authentication is enabled. | [optional] 
**password** | **bool, date, datetime, dict, float, int, list, str, none_type** | The password used by local accounts to log in. | [optional] 
**radius_two_factor** | **bool** | Whether RADIUS two-factor authentication is enabled. | [optional] 
**radius_user_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | When a user account uses RADIUS two-factor authentication, this property is the user name of the RADIUS account used to authenticate this user. | [optional] 
**time_option_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The id of the time format to use when displaying times to this user. These options are defined in Admin &gt; Configuration. | [optional] 
**two_factor** | **bool** | Whether two-factor authentication is enabled. | [optional] 
**unix_authentication_method** | [**UnixAuthenticationMethodType**](UnixAuthenticationMethodType.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


