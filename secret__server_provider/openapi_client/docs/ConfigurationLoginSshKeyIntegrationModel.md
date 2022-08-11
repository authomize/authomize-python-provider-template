# ConfigurationLoginSshKeyIntegrationModel

Ssh Key Integration Configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_method** | **bool, date, datetime, dict, float, int, list, str, none_type** | Require password only, public key only, password or public key, password and public key | [optional] 
**enable** | **bool** | When activated, SSH key pairs can be used for authentication in SSH Terminal | [optional] 
**expiration_in_hours** | **bool, date, datetime, dict, float, int, list, str, none_type** | The number of days and hours the key will stay active | [optional] 
**key_expires** | **bool** | When activated, SSH keys will expire after a specified amount of time | [optional] 
**two_factor_bypass** | **bool** | When activated, providing a valid SSH key (and password, if required by Unix Authentication Method) will bypass any required 2FA validation | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


