# ConfigurationDatabaseModel

Database Configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_pool_identity** | **bool, date, datetime, dict, float, int, list, str, none_type** | The current application pool identity. | [optional] 
**authentication_type** | [**SqlAuthenticationType**](SqlAuthenticationType.md) |  | [optional] 
**connection_timeout** | **bool, date, datetime, dict, float, int, list, str, none_type** | The network connection timeout for connecting to SQL Server (not for query execution timeouts). | [optional] 
**database_config_file_path** | **bool, date, datetime, dict, float, int, list, str, none_type** | The database configuration file path on the current server. | [optional] 
**database_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | The database name. | [optional] 
**enable_multi_subnet_failover** | **bool** | When true Multi-Subnet Failover is configured. | [optional] 
**enable_ssl_encryption** | **bool** | When true ssl encryption will be enabled when communicating with sql server. | [optional] 
**failover_partner** | **bool, date, datetime, dict, float, int, list, str, none_type** | The current failover partner. | [optional] 
**has_disk_write_permissions** | **bool** | When true the application pool account has disk write permissions. | [optional] 
**is_tms_installed** | **bool** | When true the TMS / Privilege manager database exists. | [optional] 
**server_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | The sql server name. | [optional] 
**trust_server_certificate** | **bool** | When true the sql server ssl certificate will be trusted without validating the certificate chain. | [optional] 
**user_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | The username when using sql authentication. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


