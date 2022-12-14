# SecretDependencyUpdateArgs

SecretDependencyUpdateArgs

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Whether or not the Secret Dependency is active | [optional] 
**condition_dependency_id** | **int** | The Id of the dependency that will be looked at when  Condition Mode is set to &#39;DEPENDENCYPASS&#39;, &#39;DEPENDENCYFAIL&#39;. The Dependency must have a SortOrder lower than the current one. | [optional] 
**condition_mode** | **str** | Condition Mode governs if this dependency&#39;s run relies on the result of other dependencies above it. The Default is ALWAYSRUN. Other values maybe &#39;All Pass&#39;, &#39;Any Fail&#39;, &#39;DEPENDENCYPASS&#39;, &#39;DEPENDENCYFAIL&#39;. | [optional] 
**dependency_template** | [**SecretDependencyTemplate**](SecretDependencyTemplate.md) |  | [optional] 
**description** | **str** | A description for the Secret Dependency | [optional] 
**group_id** | **int** | The Id of the Dependency Group that contains the Secret Dependency. If set to 0 or a group id that does not exist on the secret, an error will be thrown. | [optional] 
**id** | **int** | The Id of the Secret Dependency | [optional] 
**machine_name** | **str** | The machine name that the Secret Dependency runs on | [optional] 
**privileged_account_secret_id** | **int** | The Id of the Privileged Secret that the Secret Dependency will use to run | [optional] 
**run_script** | [**SecretDependencyRunScript**](SecretDependencyRunScript.md) |  | [optional] 
**secret_id** | **int** | Read Only. The Id of the Secret that the Secret Dependency is assigned to. Cannot move a dependency to another secret by changing its SecretId. | [optional] 
**secret_name** | **str** | Read Only. The Name of the Secret that the Secret Dependency is assigned to | [optional] 
**service_name** | **str** | The service name of the Secret Dependency | [optional] 
**settings** | [**[SecretDependencySettingMapForDisplay]**](SecretDependencySettingMapForDisplay.md) | The Settings used by the Secret Dependency. (Ex: WaitBeforeSeconds, Database, Port, SSHKeyDigest) | [optional] 
**sort_order** | **int** | The sort order of the Secret Dependency in the group.  Determines the order of execution of the dependencies within a group. If not set (default value 0), the dependency will be added at the end of the group. If less than zero the dependency will be added as the first dependency in the group and all other dependencies in the group will be adjusted. | [optional] 
**ssh_key_secret_id** | **int** | The Id of the Secret containing the SSH key. (If dependency is tied to SSH key Secret | [optional] 
**type_id** | **int** | The Id of the type of Secret Dependency | [optional] 
**type_name** | **str** | Read Only. The name of the type of Secret Dependency | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


