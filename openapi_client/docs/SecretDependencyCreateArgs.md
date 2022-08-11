# SecretDependencyCreateArgs

The Secret Dependency Create Arguments object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Whether or not the Secret Dependency is active. | [optional] 
**condition_dependency_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The Id of the dependency that will be looked at when  Condition Mode is set to &#39;DEPENDENCYPASS&#39;, &#39;DEPENDENCYFAIL&#39;. The Dependency must have a SortOrder lower than the current one. | [optional] 
**condition_mode** | **bool, date, datetime, dict, float, int, list, str, none_type** | Condition Mode governs if this dependency&#39;s run relies on the result of other dependencies above it. The Default is ALWAYSRUN. Other values maybe &#39;All Pass&#39;, &#39;Any Fail&#39;, &#39;DEPENDENCYPASS&#39;, &#39;DEPENDENCYFAIL&#39;. | [optional] 
**dependency_template** | [**SecretDependencyTemplate**](SecretDependencyTemplate.md) |  | [optional] 
**description** | **bool, date, datetime, dict, float, int, list, str, none_type** | A description for the Secret Dependency. | [optional] 
**group_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The Id of the Dependency Group that contains the Secret Dependency. If set to default value of 0, it will be added to the first group on the secret. | [optional] 
**machine_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | The machine name that the Secret Dependency runs on. | [optional] 
**privileged_account_secret_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The Id of the Privileged Secret that the Secret Dependency will use to run. | [optional] 
**run_script** | [**SecretDependencyRunScript**](SecretDependencyRunScript.md) |  | [optional] 
**secret_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The Id of the Secret that the Secret Dependency is assigned to. | [optional] 
**secret_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | Read Only. The Name of the Secret that the Secret Dependency is assigned to. | [optional] 
**service_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | The service name of the Secret Dependency. | [optional] 
**settings** | [**[SecretDependencySettingMapForDisplay]**](SecretDependencySettingMapForDisplay.md) | The Settings used by the Secret Dependency. (Ex: WaitBeforeSeconds, Database, Port, SSHKeyDigest) | [optional] 
**sort_order** | **bool, date, datetime, dict, float, int, list, str, none_type** | The sort order of the Secret Dependency in the group.  Determines the order of execution of the dependencies within a group. If set to the default value of 0, the dependency will be added at the end of the group. If less than zero the dependency will be added as the first dependency in the group and all other dependencies in the group will be adjusted. | [optional] 
**ssh_key_secret_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The Id of the Secret containing the SSH key. (If dependency is tied to SSH key Secret) | [optional] 
**type_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The Id of the type of Secret Dependency. | [optional] 
**type_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | Read Only. The name of the type of Secret Dependency. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


