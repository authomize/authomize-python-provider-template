# ConfigurationSamlModel

SAML configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enable SAML authentication | [optional] 
**enable_legacy_slo** | **bool** | Enable legacy SingleLogout | [optional] 
**identity_providers** | [**[ConfigurationSamlIdentityProviderModel]**](ConfigurationSamlIdentityProviderModel.md) | List of Identity Providers | [optional] 
**legacy_username_attribute** | **bool, date, datetime, dict, float, int, list, str, none_type** | Optional AttributeName to use for matching a Secret Server user. | [optional] 
**service_provider_certificate** | **bool, date, datetime, dict, float, int, list, str, none_type** | The Service Provider Certificate. Base64 encoded | [optional] 
**service_provider_certificate_password** | **bool, date, datetime, dict, float, int, list, str, none_type** | The password for the Service Provider Certificate | [optional] 
**service_provider_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | The name of the Service Provider | [optional] 
**use_legacy** | **bool** | Use Legacy SAML | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


