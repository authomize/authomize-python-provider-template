# ReportExecuteModel

ReportExecution

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | **[str]** | Array of column names. | [optional] 
**column_types** | **[str]** | Array of column types | [optional] 
**enabled** | **bool** | Whether the Report is active | [optional] 
**id** | **int** | Report ID | [optional] 
**localized_columns** | **[str]** | Array of localized column names. | [optional] 
**name** | **str** | Report name | [optional] 
**report_preview_sql** | **str** | When passed this SQL will be used to run the report in a preview mode.  Used for testing SQL but not updating the report. | [optional] 
**rows** | **[[dict]]** | Rows of report data. | [optional] 
**system_report** | **bool** | Whether the Report is a system Report | [optional] 
**total_row_count** | **int** | Total number of rows | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


