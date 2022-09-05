# MetadataModel

A single record of metadata that is associated to one entity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contains_personal_information** | **bool** | When this is set to true, the metadata will be obfuscated during export | [optional] 
**create_date_time** | **datetime** | When was this field value entered | [optional] 
**create_user_id** | **int** | The user id of the user who entered this field value | [optional] 
**create_user_name** | **str** | Who entered this field value | [optional] 
**item_id** | **int** | The ID of the entity to which this value is associated | [optional] 
**metadata_field_id** | **int** | The metadata field ID for this value | [optional] 
**metadata_field_name** | **str** | The field name for this metadata value | [optional] 
**metadata_field_section_id** | **int** | The section ID in which this metadata value resides | [optional] 
**metadata_field_section_name** | **str** | The section name in which this metadata value resides | [optional] 
**metadata_field_type_id** | **int** | The ID for the field type in which this metadata value resides | [optional] 
**metadata_field_type_name** | **str** | The field name in which this metadata value resides | [optional] 
**metadata_item_data_id** | **int** | The sequence ID for this specific metadata value record | [optional] 
**metadata_type_name** | **str** | The type name in which this metadata value resides | [optional] 
**sort_order** | **int** | Not currently utilized, but the sort order for the metadata | [optional] 
**value_bit** | **bool** | The value when the metadata field is a boolean | [optional] 
**value_date_time** | **datetime** | The value when the metadata field is a date | [optional] 
**value_int** | **int** | The value when the metadata field is a user | [optional] 
**value_number** | **float** | The value when the metadata field is a number | [optional] 
**value_string** | **str** | The value when the metadata field is a string | [optional] 
**value_user_display_name** | **str** | The user display name when the metadata field is a user type | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


