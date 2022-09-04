# SecretDetailGeneralViewModel

Secret Detail General View Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | [**ViewFieldValueOfBoolean**](ViewFieldValueOfBoolean.md) |  | [optional] 
**auto_change_password** | [**ViewFieldValueOfBoolean**](ViewFieldValueOfBoolean.md) |  | [optional] 
**can_generate_ssh_key** | **bool** | CanGenerateSshKey | [optional] 
**enable_inherit_secret_policy** | [**ViewFieldValueOfBoolean**](ViewFieldValueOfBoolean.md) |  | [optional] 
**expiration** | [**ViewFieldValueOfString**](ViewFieldValueOfString.md) |  | [optional] 
**fields** | [**[ViewTemplateFieldOfString]**](ViewTemplateFieldOfString.md) | Fields | [optional] 
**folder** | [**ViewFieldValueOfOptionalInt32**](ViewFieldValueOfOptionalInt32.md) |  | [optional] 
**heartbeat_enabled** | [**ViewFieldValueOfBoolean**](ViewFieldValueOfBoolean.md) |  | [optional] 
**id** | **int** | Id | [optional] 
**is_favorite** | **bool** | IsFavorite | [optional] 
**is_out_of_sync** | [**ViewFieldValueOfBoolean**](ViewFieldValueOfBoolean.md) |  | [optional] 
**is_totp_enabled** | **bool** | IsTotpEnabled | [optional] 
**last_heart_beat_check** | [**ViewFieldValueOfOptionalDateTime**](ViewFieldValueOfOptionalDateTime.md) |  | [optional] 
**last_heart_beat_status** | [**ViewFieldValueOfSecretDetailHeartbeatStatus**](ViewFieldValueOfSecretDetailHeartbeatStatus.md) |  | [optional] 
**launchers** | [**[SecretDetailLauncher]**](SecretDetailLauncher.md) | Launchers | [optional] 
**name** | [**ViewFieldValueOfString**](ViewFieldValueOfString.md) |  | [optional] 
**out_of_sync_reason** | [**ViewFieldValueOfString**](ViewFieldValueOfString.md) |  | [optional] 
**secret_policy** | [**ViewFieldValueOfOptionalInt32**](ViewFieldValueOfOptionalInt32.md) |  | [optional] 
**site** | [**ViewFieldValueOfOptionalInt32**](ViewFieldValueOfOptionalInt32.md) |  | [optional] 
**slug_private_key** | **str** | SlugPrivateKey | [optional] 
**slug_public_key** | **str** | SlugPublicKey | [optional] 
**template** | [**ViewFieldValueOfOptionalInt32**](ViewFieldValueOfOptionalInt32.md) |  | [optional] 
**totp_password_slug** | **str** | TotpPasswordSlug | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


