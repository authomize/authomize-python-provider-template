# RestSecretItem

Secret data field item

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_description** | **str** | Longer description of the secret field. | [optional] 
**field_id** | **int** | The id of the field definition from the secret template. | [optional] 
**field_name** | **str** | The display name of the secret field. | [optional] 
**file_attachment_id** | **int** | If the field is a file attachment field, the id of the file attachment. | [optional] 
**filename** | **str** | If the field is a file attachment field, the name of the attached file. | [optional] 
**is_file** | **bool** | Whether the field is a file attachment. | [optional] 
**is_list** | **bool** | Whether or not the secret field is a list. | [optional] 
**is_notes** | **bool** | Whether the field is represented as a multi-line text box. Used for long-form text fields. | [optional] 
**is_password** | **bool** | Whether the field is a password. Password fields are hidden by default in the UI and their value is not returned in GET calls that return secrets. To retrieve a password field value, make a GET call to /api/secrets/{secretId}/fields/{slug}. | [optional] 
**item_id** | **int** | The id of the secret field item. Leave empty when creating a new secret. | [optional] 
**item_value** | **str** | The value of the secret field item. For list fields, this is a comma-delimited list of the list id guids that are assigned to this field. | [optional] 
**list_type** | [**SecretFieldListType**](SecretFieldListType.md) |  | [optional] 
**slug** | **str** | A unique name for the secret field on the template. Slugs cannot contain spaces and are used in many places to easily refer to a secret field without having to know the field id. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


