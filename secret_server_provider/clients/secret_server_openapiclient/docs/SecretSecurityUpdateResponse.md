# SecretSecurityUpdateResponse

Response to indicate if the Secret security settings saved properly.  If you still have access to the model the updated model will be returned.  If checkout is now enabled then model will be null.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | [**SecretDetailSecurityModel**](SecretDetailSecurityModel.md) |  | [optional] 
**success** | **bool** | Returns as true if the update was successful.  Note that any failures should throw an error | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


