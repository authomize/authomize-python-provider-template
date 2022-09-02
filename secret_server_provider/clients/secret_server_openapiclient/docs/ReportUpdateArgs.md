# ReportUpdateArgs

Report update options

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the Report to update. Must match the value in the path | 
**category_id** | **int** | The Category that the report should be in | [optional] 
**chart_type** | **str** | The Chart type to use for the report | [optional] 
**description** | **str** | The description of the new report | [optional] 
**dual_control_approval** | [**DualControlApproval**](DualControlApproval.md) |  | [optional] 
**is3_d_report** | **bool** | If the report chart should be 3D or not | [optional] 
**name** | **str** | The name of the new report | [optional] 
**page_size** | **int** | The number of records that the report should return per page | [optional] 
**report_sql** | **str** | The SQL query that defines the report | [optional] 
**use_database_paging** | **bool** | If true the report will attempt to do paging in the database.  If false the paging will occur on the application server. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


