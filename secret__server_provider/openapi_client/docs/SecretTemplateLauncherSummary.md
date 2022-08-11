# SecretTemplateLauncherSummary

Summary model describing template to launcher mappings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_list_secret_field_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The ID of the list to allow | [optional] 
**connect_as_command** | **bool, date, datetime, dict, float, int, list, str, none_type** | Connect as command | [optional] 
**connect_as_command_response** | **bool, date, datetime, dict, float, int, list, str, none_type** | The expected response to get from the host on connect as | [optional] 
**connect_as_timeout_in_seconds** | **bool, date, datetime, dict, float, int, list, str, none_type** | The amount of time, in seconds, that must elapse before a timeout occurs. | [optional] 
**deny_list_secret_field_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The ID of the list to deny | [optional] 
**expected_prompt_ending** | **bool, date, datetime, dict, float, int, list, str, none_type** | The character used to mark the end of a prompt on a server, such as &#39;$&#39;, &#39;#&#39;, &#39;%&#39;, and etc | [optional] 
**fields** | [**[SecretTemplateLauncherFieldSummary]**](SecretTemplateLauncherFieldSummary.md) | Mapping of secret template fields to launch fields | [optional] 
**launcher_type_description** | **bool, date, datetime, dict, float, int, list, str, none_type** | Detailed description of this launcher | [optional] 
**launcher_type_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | ID of this launcher | [optional] 
**launcher_type_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | Name of this launcher type | [optional] 
**line_ending** | **bool, date, datetime, dict, float, int, list, str, none_type** | Connect as command line ending to be sent | [optional] 
**restrict_host_dependency_machines** | **bool** | Use dependency hosts for restrictions | [optional] 
**restrict_host_secret_field_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | Restrict user input on a launcher mapping to values in this secret field | [optional] 
**restrict_host_type** | **bool, date, datetime, dict, float, int, list, str, none_type** | Restrict host type | [optional] 
**restrict_user_input** | **bool** | User input has restrictions to allow or deny specific entries | [optional] 
**secret_type_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | Secret Template ID | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


