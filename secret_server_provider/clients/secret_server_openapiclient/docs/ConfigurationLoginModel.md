# ConfigurationLoginModel

Login Configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_auto_complete** | **bool** | Deprecated: AutoComplete is a feature provided by most web browsers to automatically remember and prefill forms for you.  This can be a great security concern since they typically do not save the data in a secure manner.  You can enable or disable web browser prefill on the Login screen by using this option. Will always return true. | [optional] 
**allow_remember_me** | **bool** | This option enables the \&quot;Remember Me\&quot; checkbox on the login screen.  When a user chooses to use \&quot;Remember Me\&quot;, an encrypted cookie will be set in their browser.  This will enable the user to revisit Secret Server without the need to log in.  This cookie will no longer be valid when the \&quot;Remember Me\&quot; period has expired and they will have to log in again | [optional] 
**cache_ad_credentials** | **bool** | Allows cached credentials to be used when Distributed Engine is unable to connect to Active Directory | [optional] 
**default_login_domain** | **str** | Default Login Domain | [optional] 
**enable_domain_selector** | **int** | Display the domain selector at login | [optional] 
**enable_login_failure_captcha** | **bool** | When this option is checked, the user will only have to complete a CAPTCHA if their login credentials are entered incorrectly a certain number of times | [optional] 
**max_concurrent_logins_per_user** | **int** | Maximum concurrent logins per user | [optional] 
**maximum_login_failures** | **int** | Set the number of login attempts allowed before a user is locked out of their account.  Once locked out, they will need a Secret Server administrator to reset their password and enable their account | [optional] 
**max_login_failures_before_captcha** | **int** | Maximum Login Failures Before CAPTCHA | [optional] 
**remember_me_time_out_minutes** | **int** | The number of minutes that you will be remembered | [optional] 
**ssh_key_integration** | [**ConfigurationLoginSshKeyIntegrationModel**](ConfigurationLoginSshKeyIntegrationModel.md) |  | [optional] 
**two_factor** | [**ConfigurationLoginTwoFactorModel**](ConfigurationLoginTwoFactorModel.md) |  | [optional] 
**user_lockout_time_minutes** | **int** | Number of minutes a User will be locked out for | [optional] 
**visual_encrypted_keyboard_enabled** | **bool** | Enable the Visual Keyboard for logins | [optional] 
**visual_encrypted_keyboard_required** | **bool** | Require the Visual Keyboard for logins | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


