# SecretDependencyRunScript

The RunScript details of a Dependency that directly runs a Script

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**machine_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | The machine name that the Secret Dependency runs on | [optional] 
**odbc_connection_arguments** | [**[SecretDependencyOdbcConnectionArg]**](SecretDependencyOdbcConnectionArg.md) | Connection arguments used for ODBC connections | [optional] 
**script_arguments** | [**[SecretDependencyUniversalScriptArgument]**](SecretDependencyUniversalScriptArgument.md) | Parameter script arguments used by the script | [optional] 
**script_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The Id of the script that the Secret Dependency runs. (If directly running a script) | [optional] 
**script_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | The Name of the script that the Secret Dependency runs. | [optional] 
**service_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | The service name of the Secret Dependency | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


