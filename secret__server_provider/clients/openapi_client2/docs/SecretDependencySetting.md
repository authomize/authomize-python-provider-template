# SecretDependencySetting

Secret Dependency Settings - Mostly used internally

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Indicates the setting is active. | [optional] 
**can_edit** | **bool** | Indicates the setting details may be editted. | [optional] 
**can_edit_value** | **bool** | Indicates the setting value may be editted. | [optional] 
**child_settings** | [**[SecretDependencySetting]**](SecretDependencySetting.md) | The Child Settings that would be used  for list of options. | [optional] 
**default_value** | **str** | Default value if the setting is not given a value | [optional] 
**display_name** | **str** | Setting Display Name | [optional] 
**id** | **int** | Id of the setting | [optional] 
**is_visibile** | **bool** | Indicates the setting is visible on the UI. | [optional] 
**parent_setting_id** | **int** | Parent Setting Id used when a setting has child options. | [optional] 
**regex_validation** | **str** | Regex used to validate the input | [optional] 
**setting_name** | **str** | Name of the setting | [optional] 
**setting_section_id** | **int** | Section Id of the setting | [optional] 
**setting_type** | **int** | Type of Setting (Default (string) &#x3D; 0, Integer &#x3D; 1, String &#x3D; 2, Boolean &#x3D; 3, StringArray &#x3D; 4, DropDown &#x3D; 5,DropDownItem &#x3D; 6 | [optional] 
**sub_setting_section_id** | **int** | Subsetting Section Id | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


