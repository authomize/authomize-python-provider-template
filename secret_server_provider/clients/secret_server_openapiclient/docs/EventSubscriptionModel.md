# EventSubscriptionModel

An event subscription

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Is subscription active | [optional] 
**entity_actions** | [**[EventSubscriptionEntityActionModel]**](EventSubscriptionEntityActionModel.md) | A list of the entity actions that file the subscription | [optional] 
**event_severity** | **int** | The event severity | [optional] 
**event_subscription_id** | **int** | The ID of the event subscription | [optional] 
**inbox_expiration** | **int** | Nuber of days for the message to stay in the inbox | [optional] 
**subscribers** | [**[EventSubscriptionSubscriberModel]**](EventSubscriptionSubscriberModel.md) | A list of the groups subscribed to the event | [optional] 
**subscription_name** | **str** | The name of the event subscription | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


