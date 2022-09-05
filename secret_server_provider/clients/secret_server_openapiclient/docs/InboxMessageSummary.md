# InboxMessageSummary

Summary of an inbox message

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**[InboxMessageData]**](InboxMessageData.md) | All data fields for this messages | [optional] 
**details** | **str** | A common data field on all notifications | [optional] 
**expiration_date** | **datetime** | Within 24 hours of this date this message and all related history will be removed | [optional] 
**inbox_message_type_id** | **int** | The type of message id | [optional] 
**inbox_message_type_name** | **str** | The message type name | [optional] 
**is_read** | **bool** | Has the current user read this message | [optional] 
**message_created_date** | **datetime** | When was the message created | [optional] 
**message_id** | **int** | Message ID | [optional] 
**recipients** | **[str]** | Who has recieved this message | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


