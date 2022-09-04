# ReportExecuteArgs

Report query options

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dual_control_approval** | [**DualControlApproval**](DualControlApproval.md) |  | [optional] 
**encode_html** | **bool** | True to encode data as HTML, defaults to true if not provided | [optional] 
**end_record_number** | **int** | End Record Number when taking a specific set of records, passing this will override PageNumber and RecordsPerPage | [optional] 
**id** | **int** | The Id of the report to run. Optional: will use Name if provided | [optional] 
**is_ascending** | **bool** | Flag determining sort direction of custom sort | [optional] 
**name** | **str** | The name of the report to run. Optional: will use Id if provided | [optional] 
**order_by_field_ordinal** | **int** | Ordinal of Field for custom OrderBy of results | [optional] 
**page_number** | **int** | Page number for paging results. All records returned if null | [optional] 
**parameters** | [**[ReportParameter]**](ReportParameter.md) | The parameters of the report | [optional] 
**preview_sql** | **str** | When passed the report will be previewed with this sql | [optional] 
**records_per_page** | **int** | Number of records per page for paging results | [optional] 
**start_record_number** | **int** | Start Record Number when taking a specific set of records, passing this will override PageNumber and RecordsPerPage | [optional] 
**use_default_parameters** | **bool** | If a report contains a parameter but it is not passed the default value will be used on the server | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


