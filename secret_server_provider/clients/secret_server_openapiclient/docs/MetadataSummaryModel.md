# MetadataSummaryModel

Query results

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contains_personal_information** | **bool** | When this is set to true, the metadata will be obfuscated during export | [optional] 
**create_date_time** | **datetime** | When the field value was created | [optional] 
**create_user_id** | **int** | The user id of who entered the field value | [optional] 
**create_user_name** | **str** | Who entered the field value | [optional] 
**item_id** | **int** | The ID of the item to which this metadata is associated | [optional] 
**metadata_field_data_type** | [**MetadataFieldDataType**](MetadataFieldDataType.md) |  | [optional] 
**metadata_field_id** | **int** | The metadata field id | [optional] 
**metadata_field_name** | **str** | The metadata field name | [optional] 
**metadata_field_section_id** | **int** | The Metadata section ID | [optional] 
**metadata_field_section_name** | **str** | The metadata section name | [optional] 
**metadata_field_type_name** | **str** | Not currently populated, see MetadataFieldDataType | [optional] 
**metadata_item_data_id** | **int** | The sequence id for this specific metadata field | [optional] 
**metadata_type** | [**MetadataType**](MetadataType.md) |  | [optional] 
**metadata_type_name** | **str** | Not currently populated, see MetadataType | [optional] 
**sort_order** | **int** | The order in which to sort the metadata fields.  This is currently not utilized. | [optional] 
**value_bit** | **bool** | When this metadata field is a boolean this will be the value | [optional] 
**value_date_time** | **datetime** | When this metadata field is a datetime this will be the value | [optional] 
**value_int** | **int** | When this metadata field is a user this will be the user id | [optional] 
**value_number** | **float** | When this metadata field is a number this will be the value | [optional] 
**value_string** | **str** | When this metadata field is a string this will be the value | [optional] 
**value_user_display_name** | **str** | When this metadata field is a user this will be the user display name | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


