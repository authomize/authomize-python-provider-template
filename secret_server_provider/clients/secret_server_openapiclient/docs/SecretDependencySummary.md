# SecretDependencySummary

The Summary object for a Secret Dependency

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_test** | **bool** | Whether or not this dependency can be tested | [optional] 
**enabled** | **bool** | Whether or not this dependency is enabled | [optional] 
**group_id** | **int** | The Id of the Dependency Group that contains the Secret Dependency | [optional] 
**id** | **int** | The Id of the Secret Dependency | [optional] 
**machine_name** | **str** | The machine name that the Secret Dependency runs on | [optional] 
**order** | **int** | The order for this dependency within its group | [optional] 
**run_result** | [**DependencyRunResultStatus**](DependencyRunResultStatus.md) |  | [optional] 
**secret_id** | **int** | The Id of the Secret that the Secret Dependency is assigned to | [optional] 
**service_name** | **str** | The service name of the Secret Dependency | [optional] 
**type_id** | **int** | The Id of the type of Secret Dependency | [optional] 
**type_name** | **str** | The name of the type of Secret Dependency | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


