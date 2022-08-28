# UserCreateArgs

User create options

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The user’s name as displayed in the user interface. | 
**password** | **str** | The password used by local accounts to log in. | 
**user_name** | **str** | The unique string identifying this user. | 
**ad_guid** | **str** | Active Directory unique identifier. | [optional] 
**domain_id** | **int** | If not null, the Active Directory domain ID. | [optional] 
**duo_two_factor** | **bool** | Whether Duo two-factor authentication is enabled. | [optional] 
**email_address** | **str** | The user&#39;s email address. Used by the system to send reports, access requests, and other notifications. | [optional] 
**enabled** | **bool** | Whether the user account is enabled. Disabled users are unable to log in and do not consume a user license. | [optional] 
**fido2_two_factor** | **bool** | Whether Duo two-factor authentication is enabled. | [optional] 
**is_application_account** | **bool** | Whether this is an application account. Application accounts are used for automation, cannot log in using the UI, and do not consume a user license. | [optional] 
**oath_two_factor** | **bool** | Whether OATH two-factor authentication is enabled. | [optional] 
**radius_two_factor** | **bool** | Whether RADIUS two-factor authentication is enabled. | [optional] 
**radius_user_name** | **str** | RADIUS username | [optional] 
**two_factor** | **bool** | Whether two-factor authentication is enabled. | [optional] 
**unix_authentication_method** | [**UnixAuthenticationMethodType**](UnixAuthenticationMethodType.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


