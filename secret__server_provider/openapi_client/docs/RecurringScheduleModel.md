# RecurringScheduleModel

A recurring schedule defines an interval that can trigger tasks

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Whether or not the schedule is active | [optional] 
**duration** | **bool, date, datetime, dict, float, int, list, str, none_type** | How long is the iteration of this schedule.  A weekly schedule with an iteration of 2 would restart every other week. | [optional] 
**duration_start_date** | **bool, date, datetime, dict, float, int, list, str, none_type** | When does the schedule iteration begin | [optional] 
**entity** | [**RecurringScheduleEntityModel**](RecurringScheduleEntityModel.md) |  | [optional] 
**notes** | **bool, date, datetime, dict, float, int, list, str, none_type** | TBD | [optional] 
**recurring_schedule_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | Unique ID for this schedule | [optional] 
**recurring_schedule_type** | [**RecurringScheduleType**](RecurringScheduleType.md) |  | [optional] 
**schedule_constraints** | [**[RecurringScheduleValueModel]**](RecurringScheduleValueModel.md) | These indicate the rules for when a schedule should recur.  If all of the constraints are met then the schedule will trigger. | [optional] 
**time_zone_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | Time Zone of the times the schedule is run | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


