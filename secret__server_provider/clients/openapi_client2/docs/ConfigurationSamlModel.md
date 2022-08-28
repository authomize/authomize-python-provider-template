# ConfigurationSamlModel

SAML configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enable SAML authentication | [optional] 
**enable_legacy_slo** | **bool** | Enable legacy SingleLogout | [optional] 
**identity_providers** | [**[ConfigurationSamlIdentityProviderModel]**](ConfigurationSamlIdentityProviderModel.md) | List of Identity Providers | [optional] 
**legacy_username_attribute** | **str** | Optional AttributeName to use for matching a Secret Server user. | [optional] 
**service_provider_certificate** | **str** | The Service Provider Certificate. Base64 encoded | [optional] 
**service_provider_certificate_expiration_date_string** | **str** | The expiration date of the Service Provider Certificate | [optional] 
**service_provider_certificate_friendly_name** | **str** | The friendly name of the Service Provider Certificate | [optional] 
**service_provider_certificate_password** | **str** | The password for the Service Provider Certificate | [optional] 
**service_provider_certificate_subject** | **str** | The subject of the Service Provider Certificate | [optional] 
**service_provider_certificate_thumbprint** | **str** | The thumbprint of the Service Provider Certificate | [optional] 
**service_provider_name** | **str** | The name of the Service Provider | [optional] 
**use_legacy** | **bool** | Use Legacy SAML | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


