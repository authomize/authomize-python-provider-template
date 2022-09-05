# EventPipelineModel

Event Pipeline

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Active | [optional] 
**created_date** | **datetime** | Event Pipeline Created Date | [optional] 
**event_entity_type_id** | **int** | Entity Type Id | [optional] 
**event_pipeline_description** | **str** | Event Pipeline Description | [optional] 
**event_pipeline_id** | **int** | Event Pipeline Id | [optional] 
**event_pipeline_name** | **str** | Event Pipeline Name | [optional] 
**event_pipeline_policy_id** | **int** | Event Pipeline Policy Id | [optional] 
**event_pipeline_policy_map_id** | **int** | Event Pipeline Policy Map Id | [optional] 
**filter_list** | [**[EventPipelineFilterModel]**](EventPipelineFilterModel.md) | Event Pipeline Filters | [optional] 
**is_system** | **bool** | Event pipeline used by the system | [optional] 
**last_modified_date** | **datetime** | Event Pipeline Modified Date | [optional] 
**last_modified_display_name** | **str** | Event Pipeline Last Modified Date | [optional] 
**sort_order** | **int** | Sort Order | [optional] 
**task_list** | [**[EventPipelineTaskModel]**](EventPipelineTaskModel.md) | Event Pipeline Tasks | [optional] 
**triggers** | [**[EventPipelineTriggerModel]**](EventPipelineTriggerModel.md) | Event Pipeline Triggers | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


