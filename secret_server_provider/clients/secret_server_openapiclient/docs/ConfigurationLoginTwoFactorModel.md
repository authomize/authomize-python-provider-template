# ConfigurationLoginTwoFactorModel

Two Factor Login Configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_two_factor_remember_me** | **bool** | When this option is checked, the user will only have to provide their two factor authentication information once in that browser for set time. This is done by setting an encrypted cookie on the browser.  The cookie will no longer be valid when the Two Factor Remember Me Duration has expired | [optional] 
**duo** | [**ConfigurationLoginTwoFactorDuoModel**](ConfigurationLoginTwoFactorDuoModel.md) |  | [optional] 
**open_id_connect** | [**ConfigurationLoginTwoFactorOpenIdConnectModel**](ConfigurationLoginTwoFactorOpenIdConnectModel.md) |  | [optional] 
**radius** | [**ConfigurationLoginTwoFactorRadiusModel**](ConfigurationLoginTwoFactorRadiusModel.md) |  | [optional] 
**require_two_factor_for_web_login** | **bool** | Require Two Factor For Web Login | [optional] 
**require_two_factor_for_web_services** | **bool** | Require Two Factor For Web Services | [optional] 
**two_factor_remember_me_time_out_days** | **bool, date, datetime, dict, float, int, list, str, none_type** | The number of days that you will not be reprompted for 2FA | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


