# SecretTemplateFieldUpdateArgs

Secret Template Field Update Args

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Field description | [optional] 
**display_name** | **str** | Field display name | [optional] 
**editable_permission** | **int** | Who has editing rights | [optional] 
**edit_requires** | [**EditRequiresOptions**](EditRequiresOptions.md) |  | [optional] 
**field_slug_name** | **str** | Field Slug Name | [optional] 
**generate_password_character_set** | **str** | When this is set to true, the field data will be obfuscated during export | [optional] 
**generate_password_length** | **int** | Generate password length.  Only returned if user can manage secret templates | [optional] 
**hide_on_view** | **bool** | Hide this field when viewing | [optional] 
**history_length** | **int** | History length | [optional] 
**is_expiration_field** | **bool** | Is expiration field | [optional] 
**is_file** | **bool** | Is this field a file type | [optional] 
**is_indexable** | **bool** | Is able to be indexed | [optional] 
**is_notes** | **bool** | Is this field a notes field type | [optional] 
**is_password** | **bool** | Is this field a password field type | [optional] 
**is_required** | **bool** | Is this field required | [optional] 
**is_url** | **bool** | Is this field a url field type | [optional] 
**list_type** | [**ListType**](ListType.md) |  | [optional] 
**must_encrypt** | **bool** | Must encrypt.  Only returned if user can manage secret templates | [optional] 
**name** | **str** | Field name | [optional] 
**password_requirement_id** | **int** | ID For Password Requirement assigned to field | [optional] 
**password_type_field_id** | **int** | Type of password field | [optional] 
**secret_template_field_id** | **int** | Field Id | [optional] 
**sort_order** | **int** | Sort Order for Field | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


