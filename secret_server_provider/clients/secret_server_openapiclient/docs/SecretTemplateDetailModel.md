# SecretTemplateDetailModel

Secret template detail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Is Secret Template active | [optional] 
**description** | **str** | Secret Template Description | [optional] 
**expiration_change_required_on_field_id** | **int** | Secret Template Field Id that will require change on Expiration | [optional] 
**expiration_days** | **int** | Expiration days, populated when ExpirationChangeRequiredOnFieldId is populated | [optional] 
**id** | **int** | Secret Template Id | [optional] 
**name** | **str** | Secret Template Name | [optional] 
**name_pattern** | **str** | Secret Template Name Pattern | [optional] 
**name_pattern_error_message** | **str** | Secret Template Name Pattern Error Message | [optional] 
**one_time_password_duration** | **int** | Duration in seconds that the One Time Password is valid, populated when one time password is enabled | [optional] 
**one_time_password_enabled** | **bool** | One time password enabled | [optional] 
**one_time_password_hash** | **str** | Hash to be used when generating the One Time Password, populated when one time password is enabled | [optional] 
**one_time_password_length** | **int** | Length of the generated One Time Password, populated when one time password is enabled | [optional] 
**save_all_name_history** | **bool** | Indicates that all Secret Name history will be saved. This will be reset if the SecretNameHistoryLength is updated. | [optional] 
**secret_count** | **int** | The number of Secrets that use this template | [optional] 
**secret_name_history_length** | **int** | The number of Secret Names to be saved. If SaveAllNameHistory is true, this will return null. | [optional] 
**ssh_key_format** | **str** | Format of the SSH Key, populated when the template contains a private SSH Key | [optional] 
**ssh_key_size** | **str** | Size of the SSH Key in bits, populated when the template contains a private SSH Key | [optional] 
**validate_password_requirements_on_create** | **bool** | Validate password requirements on create | [optional] 
**validate_password_requirements_on_edit** | **bool** | Validate password requirements on edit | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


