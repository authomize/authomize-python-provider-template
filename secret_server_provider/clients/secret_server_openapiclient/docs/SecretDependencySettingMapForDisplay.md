# SecretDependencySettingMapForDisplay

Settings used by Secret Dependency Templates

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changer_setting_value** | **bool, date, datetime, dict, float, int, list, str, none_type** | The default read-only setting value on the changer that will be used if no setting value has been given. | [optional] 
**setting** | [**SecretDependencySetting**](SecretDependencySetting.md) |  | [optional] 
**setting_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The Setting Id | [optional] 
**setting_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | The Setting Name | [optional] 
**setting_value** | **bool, date, datetime, dict, float, int, list, str, none_type** | The value for the setting that will be stored in the database.  This value should be set when editing or creating a Dependency. If not set the default value will be calculated by looking at the Changer or Script. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


