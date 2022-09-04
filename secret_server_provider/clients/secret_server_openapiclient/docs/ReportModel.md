# ReportModel

Report

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **int** | The Report Category Id | [optional] 
**chart_type** | **str** | The report chart Type.  Null if no chart | [optional] 
**description** | **str** | Report Description | [optional] 
**enabled** | **bool** | Whether the Report is active | [optional] 
**enable_inherit_permissions** | **bool** | When true, permissions will be inherited from the report category in which the report resides. | [optional] 
**id** | **int** | Report ID | [optional] 
**is3_d_report** | **bool** | Whether the Report chart is displayed in 3d | [optional] 
**name** | **str** | Report name | [optional] 
**page_size** | **int** | The page size of the report | [optional] 
**report_sql** | **str** | The SQL used to generate the report | [optional] 
**system_report** | **bool** | Whether the Report is a system Report | [optional] 
**use_database_paging** | **bool** | When true paging of a report will be done in SQL server.  Not all SQL is compatible with this option. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


