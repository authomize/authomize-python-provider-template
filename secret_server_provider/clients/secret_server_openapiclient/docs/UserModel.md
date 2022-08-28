# UserModel

User

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_account_expires** | **bool, date, datetime, dict, float, int, list, str, none_type** | Active Directory account expiration time | [optional] 
**ad_guid** | **bool, date, datetime, dict, float, int, list, str, none_type** | Active Directory unique identifier | [optional] 
**created** | **bool, date, datetime, dict, float, int, list, str, none_type** | User creation time | [optional] 
**date_option_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | DateOptionId | [optional] 
**display_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | Display name | [optional] 
**domain_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | Active Directory domain ID | [optional] 
**duo_two_factor** | **bool** | Whether Duo two-factor authentication is enabled | [optional] 
**email_address** | **bool, date, datetime, dict, float, int, list, str, none_type** | Email address | [optional] 
**enabled** | **bool** | Whether the user account is enabled | [optional] 
**external_user_source** | [**ExternalUserSourceTypes**](ExternalUserSourceTypes.md) |  | [optional] 
**fido2_two_factor** | **bool** | Whether FIDO2 two-factor authentication is enabled | [optional] 
**id** | **bool, date, datetime, dict, float, int, list, str, none_type** | User ID | [optional] 
**ip_address_restrictions** | [**[UserIpAddressRestrictionModel]**](UserIpAddressRestrictionModel.md) | Array of IP Address Restrictions for the user. | [optional] 
**is_application_account** | **bool** | IsApplicationAccount | [optional] 
**is_email_copied_from_ad** | **bool** | Whether the email address is derived from the Active Directory account | [optional] 
**is_email_verified** | **bool** | Whether the email address has been verified | [optional] 
**is_locked_out** | **bool** | Whether the user is locked out | [optional] 
**last_login** | **bool, date, datetime, dict, float, int, list, str, none_type** | Time of last login | [optional] 
**last_session_activity** | **bool, date, datetime, dict, float, int, list, str, none_type** | Time of last session activity | [optional] 
**lock_out_reason** | **bool, date, datetime, dict, float, int, list, str, none_type** | The reason for the lock out | [optional] 
**lock_out_reason_description** | **bool, date, datetime, dict, float, int, list, str, none_type** | An optional description of the reason for the lock out | [optional] 
**login_failures** | **bool, date, datetime, dict, float, int, list, str, none_type** | Number of login failures | [optional] 
**must_verify_email** | **bool** | Whether the user must verify their email address | [optional] 
**oath_two_factor** | **bool** | Whether OATH two-factor authentication is enabled | [optional] 
**oath_verified** | **bool** | Whether OATH has been verified | [optional] 
**password_last_changed** | **bool, date, datetime, dict, float, int, list, str, none_type** | Time when the password was last changed | [optional] 
**personal_group_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The personal group ID for this user.  Each user has a personal group that is a group that only contains that user. | [optional] 
**platform_integration_type** | [**PlatformIntegrationType**](PlatformIntegrationType.md) |  | [optional] 
**radius_two_factor** | **bool** | Whether RADIUS two-factor authentication is enabled | [optional] 
**radius_user_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | RADIUS username | [optional] 
**reset_session_started** | **bool, date, datetime, dict, float, int, list, str, none_type** | ResetSessionStarted | [optional] 
**slack_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | Slack ID of the user | [optional] 
**time_option_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | TimeOptionId | [optional] 
**two_factor** | **bool** | Whether two-factor authentication is enabled | [optional] 
**unix_authentication_method** | [**UnixAuthenticationMethodType**](UnixAuthenticationMethodType.md) |  | [optional] 
**user_lcid** | **bool, date, datetime, dict, float, int, list, str, none_type** | UserLcid | [optional] 
**user_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | User name | [optional] 
**verify_email_sent_date** | **bool, date, datetime, dict, float, int, list, str, none_type** | Time when the verification email was sent | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


