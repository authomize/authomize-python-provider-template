# SecretTemplateFieldModel

Secret Template Field Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Is this field active | [optional] 
**data_type** | [**FieldDataType**](FieldDataType.md) |  | [optional] 
**description** | **str** | Description of Field | [optional] 
**dropdown_options** | [**[SecretTemplateFieldOptionModel]**](SecretTemplateFieldOptionModel.md) | These values will appear as a drop down for text fields. | [optional] 
**edit_requires_permission** | [**FieldPermissionType**](FieldPermissionType.md) |  | [optional] 
**expose_for_display** | **bool** | Is this field is exposed for display | [optional] 
**history_length** | **int** | Number of changes stored in history. If SaveAllHistory is true, this will return null. | [optional] 
**id** | **int** | Field Id | [optional] 
**name** | **str** | Name of Field | [optional] 
**password_requirement** | **int** | The Id of the Password Requirement if the data type is Password defaulting to the default Password Requirement if not set. | [optional] 
**required** | **bool** | Is this field required | [optional] 
**save_all_history** | **bool** | Indicates that all history will be saved. This will be reset if the HistoryLength is updated. | [optional] 
**searchable** | **bool** | Is this field searchable | [optional] 
**slug_name** | **str** | A unique identifier used in api calls and other interactions. The slug allows the display name to change without breaking interfaces to fields. | [optional] 
**sort_order** | **int** | Sort Order of the field used for display | [optional] 
**viewing_requires_edit** | **bool** | Is edit permission required for viewing this field | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


