# BackupConfigurationModel

Database Backup Configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_database_path** | **str** | Where to backup the database | [optional] 
**backup_failure_notification** | **bool** | Whether or not to send an email if backup fails | [optional] 
**backup_path** | **str** | Where to store the web application backup files | [optional] 
**backup_start_date_time** | **datetime** | The next time the backup will run | [optional] 
**configuration_sql_backup_timeout_minutes** | **int** | SQL Timeout when running the backup | [optional] 
**copy_only_database_backup** | **bool** | Backup type | [optional] 
**enable_database_backup** | **bool** | Whether or not the backup the database | [optional] 
**enable_scheduled_backup** | **bool** | Is the backup enabled | [optional] 
**enable_tms_backup** | **bool** | Whether or not the TMS web files are backed up | [optional] 
**enable_web_application_backup** | **bool** | Whether or not the web application is set to backup | [optional] 
**number_of_backups_to_keep** | **int** | How many backups should be kept (deletes oldest) | [optional] 
**repeat_days** | **int** | How many days between backups | [optional] 
**repeat_hours** | **int** | How many hours between backups | [optional] 
**repeat_minutes** | **int** | How many minutes between backups | [optional] 
**tms_installation_path** | **str** | Where TMS is installed | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


