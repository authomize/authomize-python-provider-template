# SecretDetailGeneralModel

Secret Detail General

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Whether the secret is active | [optional] 
**auto_change_password** | **bool** | Whether the password should automatically change upon expiration. | [optional] 
**can_generate_ssh_key** | **bool** | Can Generate SSH Key | [optional] 
**enable_inherit_secret_policy** | **bool** | Whether the secret policy is inherited from the containing folder | [optional] 
**expiration** | **str** | Expiration | [optional] 
**fields** | **[str]** | Secret Fields | [optional] 
**folder** | **int** | Containing folder ID | [optional] 
**heartbeat_enabled** | **bool** | Heartbeat Enabled | [optional] 
**id** | **int** | Secret Detail General Id | [optional] 
**is_favorite** | **bool** | Is Favorite | [optional] 
**is_out_of_sync** | **bool** | Whether the secret is out of sync | [optional] 
**is_totp_enabled** | **bool** | Is One Time Password Enabled | [optional] 
**last_heart_beat_check** | **datetime** | Time of last heartbeat check | [optional] 
**last_heart_beat_status** | [**SecretDetailHeartbeatStatus**](SecretDetailHeartbeatStatus.md) |  | [optional] 
**launchers** | [**[SecretDetailLauncher]**](SecretDetailLauncher.md) | Launchers | [optional] 
**name** | **str** | Secret Detail General Name | [optional] 
**out_of_sync_reason** | **str** | Reason message if the secret is out of sync | [optional] 
**secret_policy** | **int** | Secret Policy | [optional] 
**site** | **int** | Site | [optional] 
**slug_private_key** | **str** | Private Key Field Slug | [optional] 
**slug_public_key** | **str** | Public Key Field Slug | [optional] 
**template** | **int** | Secret template | [optional] 
**totp_password_slug** | **str** | One Time Password Field Slug | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


