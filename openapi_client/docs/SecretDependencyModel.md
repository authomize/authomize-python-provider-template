# SecretDependencyModel

The Secret Dependency model object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Whether or not the Secret Dependency is active. | [optional] 
**child_dependency_status** | **bool** | The last run status of the child Secret Dependency. | [optional] 
**condition_dependency_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The Id of the dependency that will be looked at when  Condition Mode is set to &#39;DEPENDENCYPASS&#39;, &#39;DEPENDENCYFAIL&#39;. The Dependency must have a SortOrder lower than the current one. | [optional] 
**condition_mode** | **bool, date, datetime, dict, float, int, list, str, none_type** | Condition Mode governs if this dependency&#39;s run relies on the result of other dependencies above it. The Default is ALWAYSRUN. Other values maybe &#39;All Pass&#39;, &#39;Any Fail&#39;, &#39;DEPENDENCYPASS&#39;, &#39;DEPENDENCYFAIL&#39;. | [optional] 
**dependency_template** | [**SecretDependencyTemplate**](SecretDependencyTemplate.md) |  | [optional] 
**description** | **bool, date, datetime, dict, float, int, list, str, none_type** | A description for the Secret Dependency. | [optional] 
**group_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The Id of the Dependency Group that contains the Secret Dependency. | [optional] 
**id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The Id of the Secret Dependency. | [optional] 
**log_message** | **bool, date, datetime, dict, float, int, list, str, none_type** | The last Log message for the Secret Dependency. | [optional] 
**privileged_account_secret_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The Id of the Privileged Secret that the Secret Dependency will use to run. | [optional] 
**run_script** | [**SecretDependencyRunScript**](SecretDependencyRunScript.md) |  | [optional] 
**secret_dependency_status** | **bool** | The last run status of the Secret Dependency. | [optional] 
**secret_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The Id of the Secret that the Secret Dependency is assigned to. | [optional] 
**secret_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | The Name of the Secret that the Secret Dependency is assigned to. | [optional] 
**settings** | [**[SecretDependencySettingMapForDisplay]**](SecretDependencySettingMapForDisplay.md) | The Settings used by the Secret Dependency. (Ex: WaitBeforeSeconds, Database, Port, SSHKeyDigest). If a setting exists with the same name (or intent in the case of Port and SqlPort) as a field on the Dependency template&#39;s DependencyScanItemFields collection, the value assigned to the setting takes precedence and will overwrite the corresponding DependencyScanItemField. | [optional] 
**sort_order** | **bool, date, datetime, dict, float, int, list, str, none_type** | The sort order of the Secret Dependency in the group.  Determines the order of execution of the dependencies within a group. | [optional] 
**ssh_key_secret_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The Id of the Secret containing the SSH key. (If dependency is tied to SSH key Secret | [optional] 
**ssh_key_secret_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | The Name of the Secret containing the SSH key. (If dependency is tied to SSH key Secret | [optional] 
**type_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The Id of the type of Secret Dependency. | [optional] 
**type_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | The name of the type of Secret Dependency. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


