# ConfigurationLoginTwoFactorOpenIdConnectModel

OpenID Connect Two Factor Login Configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_new_users_to_thycotic_one** | **bool** | When activated, new Secret Server users will be added automatically to Thycotic One | [optional] 
**client_id** | **str** | Client Id | [optional] 
**client_secret** | **str** | Client Secret, will only be populated for export, otherwise null | [optional] 
**client_secret_exists** | **bool** | Indicates if a Client Secret exists, since the Client Secret will only be populated for export | [optional] 
**enable** | **bool** | Enable OpenID Connect Integration | [optional] 
**logout_url** | **str** | The URL users must visit to log out of their OpenID Connect account. (Optional) | [optional] 
**server_url** | **str** | OpenID Connect Server URL | [optional] 
**use_thycotic_one_auth_as_default** | **bool** | When activated, passwords will be checked against Thycotic One instead of Secret Server. This affects the REST API, DoubleLock, and export functionality | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


