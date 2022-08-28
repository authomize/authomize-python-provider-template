# ConvertTemplateActionModel

Secret template conversion model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_mapping** | [**[ConvertTemplateFieldModel]**](ConvertTemplateFieldModel.md) | Which source fields should map to which destination fields | [optional] 
**folder_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The target folder ID | [optional] 
**is_bulk** | **bool** | Whether or not this is a bulk operation or a single secret | [optional] 
**new_secret_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | The new name for the secret | [optional] 
**secret_ids** | **[bool, date, datetime, dict, float, int, list, str, none_type]** | A list of Secret IDs that will be converted | [optional] 
**secret_template_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The new secret template ID that will be applied to all secrets | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


