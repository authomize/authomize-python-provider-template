# AutoExportConfigurationModel

Automatic Export Configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_auto_export** | **bool** | Whether automatic export is enabled. | [optional] 
**export_child_folders** | **bool** | Whether child folders are included in the export. | [optional] 
**export_folder_paths** | **bool** | Whether folder paths are included in the export. | [optional] 
**export_password_secret_id** | **int** | The ID of the Secret whose value is used to password protect exported data. | [optional] 
**export_path** | **str** | Where the exported file is stored if on-prem. | [optional] 
**export_totp_settings** | **bool** | Whether TOTP settings are included in the export. | [optional] 
**folder_id** | **int** | Which folder to automatically export, if none provided then all are exported. | [optional] 
**frequency_days** | **int** | How many days between each automatic export. | [optional] 
**last_exported** | **datetime** | The last time the automatic export ran. | [optional] 
**user_id** | **int** | The user the export will be run as. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


