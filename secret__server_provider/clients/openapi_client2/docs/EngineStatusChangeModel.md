# EngineStatusChangeModel

Change engine status

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_interval** | **int** | When activating an engine if SiteId is null this will be the default callback interval | [optional] 
**change_type** | [**EngineStatusChangeType**](EngineStatusChangeType.md) |  | [optional] 
**engine_id** | **int** | The ID of the engine to change status | [optional] 
**site_connector_id** | **int** | When activating an engine if SiteId is null this is the site connector that will be used. | [optional] 
**site_id** | **int** | When activating an engine SiteId is required | [optional] 
**site_name** | **str** | When activating an engine if SiteId is null you can pass a SiteName and it will create the site and then activate the engine | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


