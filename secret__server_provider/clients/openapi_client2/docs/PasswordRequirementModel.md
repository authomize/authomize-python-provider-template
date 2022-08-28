# PasswordRequirementModel

Password Requirement Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_character_set** | [**CharacterSetSummary**](CharacterSetSummary.md) |  | [optional] 
**description** | **str** | Description | [optional] 
**example** | **str** | An example of the password | [optional] 
**is_default** | **bool** | Is Default | [optional] 
**max_password_length** | **int** | Maximum Password Length | [optional] 
**min_password_length** | **int** | Minimum Password Length | [optional] 
**name** | **str** | Name | [optional] 
**password_dictionaries** | [**[PasswordDictionarySummary]**](PasswordDictionarySummary.md) | Password Dictionaries | [optional] 
**password_requirement_id** | **int** | Password Requirement Id | [optional] 
**password_requirement_rules** | [**[PasswordRequirementRuleSummary]**](PasswordRequirementRuleSummary.md) | Password Requirement Rules | [optional] 
**prevent_dictionary_words** | **bool** | Prevent Dictionary Words | [optional] 
**prevent_sequential_pattern** | **bool** | Prevent Sequential Pattern | [optional] 
**prevent_spatial_pattern** | **bool** | Prevent Spacial Pattern | [optional] 
**prevent_username** | **bool** | Prevent Username | [optional] 
**secret_usage** | **int** | A count of secrets using the requirement | [optional] 
**type_usage** | **[str]** | A list of secret templates using the password requirement | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


