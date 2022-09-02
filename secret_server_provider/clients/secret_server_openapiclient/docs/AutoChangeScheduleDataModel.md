# AutoChangeScheduleDataModel

Auto Change Schedule Data Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_only_when_expired** | **bool** | The password will only be changed when the Secret has expired | [optional] 
**change_type** | **str** | Schedule Change Type | [optional] 
**days** | **int** | Days of Recurrence if Daily ScheduleType | [optional] 
**friday** | **bool** | Occurs on Fridays when set if Weekly ScheduleType | [optional] 
**monday** | **bool** | Occurs on Mondays when set if Weekly ScheduleType | [optional] 
**monthly_day** | **str** | Day(s) used if DayOfWeekMonth and Monthly ScheduleType | [optional] 
**monthly_day_of_month** | **int** | Day of Month if DayOfMonth and Monthly ScheduleType | [optional] 
**monthly_day_order** | **str** | Day Order used if DayOfWeekMonth and Monthly ScheduleType | [optional] 
**monthly_day_order_recurrence** | **int** | Months of Recurrence if DayOfWeekMonth and Monthly ScheduleType | [optional] 
**monthly_day_recurrence** | **int** | Months of Recurrence if DayOfMonth and Monthly ScheduleType | [optional] 
**monthly_schedule_type** | **str** | Selection used if Monthly ScheduleType | [optional] 
**saturday** | **bool** | Occurs on Saturdays when set if Weekly ScheduleType | [optional] 
**starting_on** | **datetime** | Day for Schedule to start | [optional] 
**sunday** | **bool** | Occurs on Sundays when set if Weekly ScheduleType | [optional] 
**thursday** | **bool** | Occurs on Thursdays when set if Weekly ScheduleType | [optional] 
**tuesday** | **bool** | Occurs on Tuesdays when set if Weekly ScheduleType | [optional] 
**wednesday** | **bool** | Occurs on Wednesdays when set if Weekly ScheduleType | [optional] 
**weeks** | **int** | Weeks of Recurrence if Weekly ScheduleType | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


