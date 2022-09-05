# MetadataCreateModel

Model to create a new metadata field value

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contains_personal_information** | **bool** | When this is set to true, the metadata will be obfuscated during export | [optional] 
**field_data_type** | **str** | Specify the specific data type desired.  Only required when also creating a new field.  If field MetadataFieldId is passed or a field already exists with the passed MetadataFieldName this is ignored.  Certain data types can also be inferred from which value field is set, but some require this to be explicitly set like User. | [optional] 
**metadata_field_id** | **int** | The specific field ID can be passed and in this case MetadataFieldName and MetadataFieldTypeId are ignored | [optional] 
**metadata_field_name** | **str** | When the field ID is not know this will create a field with this name.  If the field name does not already exist a new one will be created. | [optional] 
**metadata_field_section_description** | **str** | When the field section ID is not know this will create a field section with this description.  If MetadataFieldSectionId is passed or a section with the name MetadataFieldSectionName this field is ignored. | [optional] 
**metadata_field_section_id** | **int** | The specific field section ID can be passed and in this case MetadataFieldSectionName is ignored | [optional] 
**metadata_field_section_name** | **str** | When the field section ID is not know this will create a field section with this name.  If the field section name does not already exist a new one will be created.  If MetadataFieldSectionId is passed this field is ignored. | [optional] 
**metadata_field_section_requires_administer_metadata** | **bool** | When the field section ID is not know this will create a field section with this setting as to whether the Administer Metadata permission is required for edit.  If MetadataFieldSectionId is passed or a section with the name MetadataFieldSectionName, this field is ignored. | [optional] 
**metadata_field_section_requires_entity_edit** | **bool** | When the field section ID is not know this will create a field section with this setting as to whether edit permission is required for edit. Otherwise view will be required.  If MetadataFieldSectionId is passed or a section with the name MetadataFieldSectionName, this field is ignored. | [optional] 
**value_bit** | **bool** | When the field is a boolean it should assign this field on create for the value | [optional] 
**value_date_time** | **datetime** | When the field is a date it should assign this field on create for the value | [optional] 
**value_int** | **int** | When the field is a user it should assign this field on create for the value | [optional] 
**value_number** | **float** | When the field is a number it should assign this field on create for the value | [optional] 
**value_string** | **str** | When the field is a string it should assign this field on create for the value | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


