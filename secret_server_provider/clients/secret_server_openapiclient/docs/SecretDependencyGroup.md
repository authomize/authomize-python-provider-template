# SecretDependencyGroup

A Secret Dependency Group Object. A container for a logical collection of Secret Dependencies that use the same site.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The Id of the Secret Dependency Group | [optional] 
**name** | **str** | The name of the Secret Dependency Group | [optional] 
**site_id** | **int** | The Id of the Site that all dependencies in this group use | [optional] 
**site_name** | **str** | The Name of the Site that all dependencies in this group use | [optional] 
**status_failed_count** | **int** | Total Enabled Secret dependencies in this group with a Failed status | [optional] 
**status_not_run_count** | **int** | Total Enabled Secret dependencies in this group that have not yet run | [optional] 
**status_success_count** | **int** | Total Enabled Secret dependencies in this group with a Success status | [optional] 
**total_dependencies** | **int** | Total Enabled Secret dependencies in this group | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


