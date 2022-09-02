# SecretDetailSettingsModel

Secret Detail Settings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiration_date** | **datetime** | Expiration Date | [optional] 
**expiration_day_interval** | **int** | Expiration Day Interval | [optional] 
**expiration_template_text** | **str** | Expiration Template Text | [optional] 
**expiration_type** | [**SecretDetailExpirationType**](SecretDetailExpirationType.md) |  | [optional] 
**jumpbox_route_selection** | [**JumpboxRouteSummaryModel**](JumpboxRouteSummaryModel.md) |  | [optional] 
**one_time_password_settings** | [**OneTimePasswordSettingsModel**](OneTimePasswordSettingsModel.md) |  | [optional] 
**rdp_launcher_settings** | [**RdpLauncherSettingsModel**](RdpLauncherSettingsModel.md) |  | [optional] 
**send_email_when_changed** | **bool** | Send Email When Changed | [optional] 
**send_email_when_heartbeat_fails** | **bool** | Send Email When Heartbeat Fails | [optional] 
**send_email_when_viewed** | **bool** | Send Email When Viewed | [optional] 
**ssh_launcher_settings** | [**SshLauncherSettingsModel**](SshLauncherSettingsModel.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


