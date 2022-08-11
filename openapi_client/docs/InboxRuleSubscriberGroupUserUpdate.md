# InboxRuleSubscriberGroupUserUpdate

The user/group to add or remove to the subscription.  Either UserId or GroupId should be set.  If both are set then GroupId will take precedence and UserId will be ignored.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The group ID representing a group or an individual user | [optional] 
**subscribe** | **bool** | When true a group or user will be subscribed to this rule.  When false a group will be removed from the list.  If the this is a user then it will be removed if it is directly subscribed or it will be explicitly unsubscribed if not currently subscribed. | [optional] 
**user_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The user ID representing a an individual user | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


