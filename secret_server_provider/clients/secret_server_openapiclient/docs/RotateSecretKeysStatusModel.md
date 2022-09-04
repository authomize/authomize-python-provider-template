# RotateSecretKeysStatusModel

Rotate Secret Keys Status

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_request_date** | **datetime** | Date of the last time Rotate Secret Keys was requested. Null if never run. | [optional] 
**last_run_date** | **datetime** | Date of the last time Rotate Secret Keys was executed. Null if never run. | [optional] 
**last_status** | **str** | Status of the last time Rotate Secret Keys was executed. | [optional] 
**message** | **str** | Message about the last time Rotate Secret Keys was executed. | [optional] 
**progress_status** | [**RotateSecretKeysProgressModel**](RotateSecretKeysProgressModel.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


